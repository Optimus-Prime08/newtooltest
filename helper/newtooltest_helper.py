import requests
import json

class NewToolTestHelper:
    def __init__(self,newtooltoken):
        """
        Initializes the NewToolTestHelper with the required tokens.

        Args:
            newtooltoken (str): Personal newtool token.
        """
        self.newtooltoken = newtooltoken

    def get_result(self,title):
        # write required functionalities
        return title