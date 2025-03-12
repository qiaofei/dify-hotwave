# 热浪插件

**作者:** qiaofei  
**版本:** 0.0.2  
**类型:** tool

## 描述
热浪是一个强大的 Dify 趋势话题聚合插件，用于收集和展示来自中国主要社交媒体和内容平台的实时热门话题。目前支持微博、知乎、微信、抖音和百度。

## 特点
- 实时趋势话题聚合
- 多平台支持（微博、知乎、微信、抖音、百度）
- 结构化的 markdown 格式数据输出
- 可自定义平台选择
- 清晰友好的显示格式

## 安装
```bash
# 安装所需依赖
pip install -r requirements.txt
```

## 使用方法
- 下载.difypkg文件前往dify平台安装即可
- 下载源码自行打包

## 配置
无需额外配置。插件可以直接使用默认设置。

## API 访问限制
- 建议保持合理的请求间隔
- 遵循各平台的 API 使用规范
- 默认缓存时间：5分钟

## 输出格式
插件以 markdown 格式返回数据：
```markdown
# 今日热门话题

## 平台名称
1. [话题标题](话题链接)
2. [话题标题](话题链接)
...
```

## 依赖
- Python 3.12+
- requests
- beautifulsoup4

## 隐私与安全
- 仅收集公开可用数据
- 不收集或存储用户数据
- 遵守平台服务条款
- 详细隐私信息请参见 [PRIVACY.md](PRIVACY.md)

## 贡献指南
请阅读 [DEVELOPER_GUIDELINES.md](DEVELOPER_GUIDELINES.md) 了解我们的行为准则和提交拉取请求的流程。

## 许可证
MIT 许可证

## 联系方式
- 邮箱: qiaofei9@foxmail.com
- 问题反馈: 请通过 GitHub Issues 提交
- 技术爱好者加v联系:felixw1229



