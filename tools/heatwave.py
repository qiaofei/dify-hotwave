from collections.abc import Generator
from typing import Any
import requests
from bs4 import BeautifulSoup
import json
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class HeatwaveTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """获取今日热榜聚合数据"""
        try:
            results = self._get_tophub_hot()
            markdown_text = "# 今日热榜聚合\n\n"
            
            for platform, items in results.items():
                if items:  # 确保该平台有数据
                    markdown_text += f"## {platform}\n\n"
                    for index, item in enumerate(items, 1):
                        # 获取原始标题
                        title = item.get("title", "")
                        link = item.get("link", "")
                        
                        # 处理标题格式
                        # 1. 移除换行符
                        title = title.replace('\n', ' ')
                        # 2. 如果以数字开头，尝试移除序号
                        if title and title[0].isdigit():
                            parts = title.split(' ', 1)
                            if len(parts) > 1:
                                title = parts[1]
                        # 3. 移除多余空格
                        title = ' '.join(title.split())
                        
                        markdown_text += f"{index}. [{title}]({link})\n"
                    markdown_text += "\n"
                    
            yield self.create_text_message(markdown_text)
            
        except Exception as e:
            yield self.create_text_message(str(e))

    def _get_tophub_hot(self):
        """获取今日热榜数据"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get('https://tophub.today', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = {}
        
        # 获取所有热榜板块
        sections = soup.select('.cc-cd')
        
        for section in sections:
            # 获取板块标题
            title_elem = section.select_one('.cc-cd-lb')
            if not title_elem:
                continue
            
            platform_title = title_elem.text.strip()
            # 只保留指定的四个平台
            if platform_title not in ['知乎', '百度', '抖音', '微博']:
                continue
            items = []
            
            # 获取该板块下的所有热门条目
            entries = section.select('.cc-cd-cb-l a')
            for entry in entries[:10]:  # 每个板块取前10条
                title = entry.text.strip()
                link = entry.get('href', '')
                if title and link:
                    items.append({
                        "title": title,
                        "link": link
                    })
                    
            if items:  # 只添加有内容的板块
                results[platform_title] = items
                
        return results
