import requests
import json

from typing import Type, Optional
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from helper.newtooltest_helper import NewToolTestHelper

#tool args schema
class NewToolTestSchema(BaseTool):
    # args for the tool
    title: str = Field(
        ...,
        description= "title for the test tool",
    )

class NewToolTest(BaseTool):
    """
        NewToolTest tool
        
        Attributes:
            name : The name.
            description : The description.
            args_schema : The args schema.
    """
    name= "NewToolTest"
    # describes the tool
    description = (
        "A tool for testing"
    )
    args_schema: Type[NewToolTestSchema]=NewToolTestSchema

    def _execute(self,title: str):
        """
            Execute  the NewToolTest tool.

            Args:
                title: The title of the test tool
            
            Returns:
                Tested Succesfully or failed to test.
        """

        try:
            # write code for tool functionality
            tool_token=self.get_tool_config("NEWTOOLTOKEN")
            newtooltest_helper=NewToolTestHelper(tool_token)
            result=newtooltest_helper.get_result(title)
            return "Tested Succesfully"
        except:
            return "failed to test"
