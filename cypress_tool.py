from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class CypressInput(BaseModel):
    greetings: str = Field(..., description="Greeting message to be sent")


class CypressTool(BaseTool):
    """
    Greetings Tool
    """
    name: str = "Greetings Tool"
    args_schema: Type[BaseModel] = CypressInput
    description: str = "Sends a Greeting Message"

    def _execute(self, greetings: str = None):
        from_name = self.get_tool_config('FROM')
        greetings_str = greetings + "\n" + from_name
        return greetings_str
