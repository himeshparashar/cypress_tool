from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from superagi.tools.external_tools.cypress_tool.cypress_tool import CypressTool

class QAToolkit(BaseToolkit, ABC):
    name: str = "QA agent Toolkit"
    description: str = "QA agent toolkit contains all tools related to testing"

    def get_tools(self) -> List[BaseTool]:
        return [CypressTool()]

    # def get_env_keys(self) -> List[str]:
    #     return ["FROM"]