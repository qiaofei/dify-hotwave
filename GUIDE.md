# Dify 插件开发指南中文版

## 如何开发 Dify 插件

你好！看起来你已经创建了一个插件，现在让我们开始开发吧！

### 选择你要开发的插件类型

在开始之前，你需要了解一些关于插件类型的基础知识。插件支持在 Dify 中扩展以下功能：
- **工具(Tool)**: 工具提供者，如 Google 搜索、Stable Diffusion 等，可用于执行特定任务。
- **模型(Model)**: 模型提供者，如 OpenAI、Anthropic 等，你可以使用它们的模型来增强 AI 能力。
- **端点(Endpoint)**: 类似 Dify 中的服务 API 和 Kubernetes 中的 Ingress，你可以将 HTTP 服务扩展为端点，并使用自己的代码控制其逻辑。

基于你想要扩展的功能，我们将插件分为三种类型：**工具**、**模型**和**扩展**。

- **工具**: 这是一个工具提供者，但不仅限于工具，你可以在其中实现端点。例如，如果你要构建 Discord 机器人，你需要同时实现"发送消息"和"接收消息"功能，这时就需要同时使用**工具**和**端点**。
- **模型**: 仅作为模型提供者，不允许扩展其他功能。
- **扩展**: 有时你可能只需要一个简单的 HTTP 服务来扩展功能，这时**扩展**是最佳选择。

我相信你在创建插件时已经选择了合适的类型，如果没有，你可以通过修改 `manifest.yaml` 文件来更改。

### 配置文件(Manifest)

现在你可以编辑 `manifest.yaml` 文件来描述你的插件，以下是其基本结构：

- version(版本，必需)：插件版本
- type(类型，必需)：插件类型，目前仅支持 `plugin`，未来将支持 `bundle`
- author(作者，必需)：作者，这是市场中的组织名称，应该与仓库所有者相同
- label(标签，必需)：多语言名称
- created_at(创建时间，必需)：创建时间，市场要求创建时间必须小于当前时间
- icon(图标，必需)：图标路径
- resource(资源)：需要应用的资源
  - memory(内存)：最大内存使用量，主要与 SaaS 上的 serverless 资源申请相关，单位为字节
  - permission(权限)：权限申请
    - tool(工具)：反向调用工具权限
    - model(模型)：反向调用模型权限
    - node(节点)：反向调用节点权限
    - endpoint(端点)：允许注册端点权限
    - app(应用)：反向调用应用权限
    - storage(存储)：申请持久存储权限

### 安装依赖

- 首先，你需要 Python 3.11+ 环境，因为我们的 SDK 有此要求
- 然后，安装依赖：
    ```bash
    pip install -r requirements.txt
    ```
- 如果你想添加更多依赖，可以将它们添加到 `requirements.txt` 文件中。一旦你在 `manifest.yaml` 文件中将运行时设置为 python，`requirements.txt` 将自动生成并用于打包和部署。

### 实现插件

现在你可以开始实现你的插件了，通过以下示例，你可以快速理解如何实现自己的插件：

- [OpenAI](https://github.com/langgenius/dify-plugin-sdks/tree/main/python/examples/openai): 模型提供者的最佳实践
- [Google Search](https://github.com/langgenius/dify-plugin-sdks/tree/main/python/examples/google): 工具提供者的简单示例
- [Neko](https://github.com/langgenius/dify-plugin-sdks/tree/main/python/examples/neko): 端点组的有趣示例

### 测试和调试插件

你可能已经注意到插件根目录中有一个 `.env.example` 文件，只需将其复制为 `.env` 并填写相应的值。如果要在本地调试插件，你需要设置一些环境变量：

- `INSTALL_METHOD`: 设置为 `remote`，你的插件将通过网络连接到 Dify 实例
- `REMOTE_INSTALL_HOST`: Dify 实例的主机地址，可以使用我们的 SaaS 实例 `https://debug.dify.ai` 或自托管的 Dify 实例
- `REMOTE_INSTALL_PORT`: Dify 实例的端口，默认为 5003
- `REMOTE_INSTALL_KEY`: 你应该从使用的 Dify 实例获取调试密钥，在插件管理页面的右上角，你可以看到一个带有 `debug` 图标的按钮，点击它即可获取密钥

运行以下命令启动你的插件：

```bash
python -m main
```

刷新 Dify 实例页面，你应该能在列表中看到你的插件了，但它会被标记为"调试中"。你可以正常使用它，但不建议在生产环境中使用。

### 打包插件

最后，通过运行以下命令打包你的插件：

```bash
dify-plugin plugin package ./ROOT_DIRECTORY_OF_YOUR_PLUGIN
```

你将得到一个 `plugin.difypkg` 文件，就是这样，现在你可以将它提交到市场了，期待你的插件上架！

## 用户隐私政策

如果你想在市场上发布插件，请填写插件的隐私政策，详情请参考 [PRIVACY.md](PRIVACY.md)。