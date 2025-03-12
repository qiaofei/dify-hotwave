# Heatwave 插件项目结构说明

## 项目概述
Heatwave 是一个 Dify 平台的插件，主要用于获取国内热点新闻。

## 目录结构 
heatwave/
├── assets/ # 资源文件目录
│ └── icon.svg # 插件图标
├── provider/ # 提供者目录
│ ├── heatwave.py # 提供者实现代码
│ └── heatwave.yaml # 提供者配置文件
├── tools/ # 工具目录
│ ├── heatwave.py # 工具实现代码
│ └── heatwave.yaml # 工具配置文件
├── .env.example # 环境变量示例文件
├── .gitignore # Git 忽略文件配置
├── .difyignore # Dify 忽略文件配置
├── GUIDE.md # 插件开发指南
├── PRIVACY.md # 隐私政策文件
├── README.md # 项目说明文件
├── main.py # 插件入口文件
├── manifest.yaml # 插件清单文件
└── requirements.txt # Python 依赖文件

## 核心文件说明

### 1. manifest.yaml
- 插件的主配置文件
- 定义了插件的基本信息、版本、作者、支持的语言等
- 配置了插件的资源限制和权限要求
- 指定了运行环境要求（Python 3.12）

### 2. provider/heatwave.py
- 实现了 ToolProvider 类
- 负责处理凭证验证等基础功能

### 3. tools/heatwave.py
- 实现了具体的工具功能
- 继承自 Tool 类
- 包含实际的新闻获取逻辑

### 4. tools/heatwave.yaml
- 定义了工具的参数配置
- 支持多语言标签
- 指定了查询参数的要求

### 5. main.py
- 插件的入口文件
- 初始化插件实例
- 设置最大请求超时时间为 120 秒

### 6. requirements.txt
- 指定了项目依赖
- 主要依赖 dify_plugin 包（版本 0.0.1b67）

### 7. 配置文件
- `.env.example`: 环境变量配置示例
- `.gitignore`: Git 版本控制忽略文件配置
- `.difyignore`: Dify 特定的忽略文件配置

### 8. 文档文件
- `GUIDE.md`: 详细的插件开发指南
- `PRIVACY.md`: 插件隐私政策
- `README.md`: 项目基本信息

## 技术特点
1. 支持多语言（中文、英文、日文、葡萄牙文）
2. 采用 Python 3.12 作为运行环境
3. 支持 AMD64 和 ARM64 架构
4. 内存限制为 256MB
5. 提供了存储功能，限制为 1MB

## 开发注意事项
1. 需要 Python 3.11+ 环境
2. 开发时需要配置 .env 文件进行本地调试
3. 可以使用 Dify 的调试功能进行在线测试
4. 打包时使用 dify-plugin 命令生成 .difypkg 文件