from abc import ABC
from typing import List

from superagi.tools.base_tool import BaseToolkit, BaseTool
# tools import statements
from newtool_test import NewToolTest

class NewToolkit(BaseToolkit,ABC):
    #name for the toolkit
    name: str = "NewTool Toolkit"
    #description for the toolkit
    description: str = "Toolkit containing tools for performing test operations"
    def get_tools(self)->List[BaseTool]:
        #return all tools in the toolkit
        return [NewToolTest]
    def get_env_keys(self) -> List[str]:
        # return required keys and tokens
        return ["NEWTOOLTOKEN"]