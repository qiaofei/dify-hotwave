from typing import Any
import requests
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class HeatwaveProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        """验证凭据
        这个热点新闻工具不需要特殊的凭据验证
        """
        pass
