from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from cypress_tool import GreetingsTool


class QAToolkit(BaseToolkit, ABC):
    name: str = "QA Toolkit"
    description: str = "AQ Tool kit contains all tools related to Testing"

    def get_tools(self) -> List[BaseTool]:
        return [GreetingsTool()]

    def get_env_keys(self) -> List[str]:
        return ["FROM"]