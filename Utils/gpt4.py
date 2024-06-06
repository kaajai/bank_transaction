import pandas as pd
from utils.config import Config
import openai
import os
import json

from utils.request import Request
class GPT4:
    """
        A singleton class representing the interaction with GPT4 API. Contains all the methods related to fetching and parsing 
        the reponses from the LLM.
    """
    def __init__(self):

        self.client = openai.Client(api_key=os.environ.get("OPENAI_API_KEY"))
        self.prompt = None
        with open(Config.PROPMPT_FILE_PATH.value, 'r') as f:
            self.prompt = f.read()


    def get_llm_response(self, request: Request)->str:
        """
            Method to fetch the response for the classification from the LLM.
            Args:
            - request: The request object containing the file and file name.
            Returns:
            - The json response from the LLM.
        """
        
        if not request.raw_parsed_content:
            return None

        if os.path.exists(os.path.join(Config.CLASSIFIED_FILE_PATH.value, request.filename.split('.')[0]+'.txt')):
            print("File exists")
            raw_string_response = open(os.path.join(Config.CLASSIFIED_FILE_PATH.value, request.filename.split('.')[0]+'.txt')).read()

        else:
            docs = [{"role": "system", "content": self.prompt + '\n' + request.raw_parsed_content}]
            response = self.client.chat.completions.create(
                            model="gpt-4",
                            messages=docs
                        )
            ### LLM response in raw string format.
            raw_string_response = response.choices[0].message.content

            ### Store the raw string
            with open(os.path.join(Config.CLASSIFIED_FILE_PATH.value, request.filename.split('.')[0]+'.txt'), 'w') as f:
                f.write(raw_string_response)

        response_dict = self._parse_llm_response(raw_string_response)

        with open(os.path.join(Config.CLASSIFIED_FILE_PATH.value, request.filename.split('.')[0]+'.json'), 'w') as file:
            json.dump(response_dict, file, indent=4)

        return response_dict


    def _parse_llm_response(self, response: str)->pd.DataFrame:
        """
            Method to parse the string response from the LLM which contains the table of contents.
            Args:
            - response: The string response fromt the LLM which contains the table of contents.
            Returns:
            - Json list containing the transaction details.
        """

        ## Extracting lines from the response from LLM.
        lines = response.strip().split("\n")
        table = [line.split('|') for line in lines]

        ## Storing records from the response table in a dataframe.
        final_table = []
        for line in table:
            new_line = []
            for ele in line:
                ele = ele.replace('-','')
                if ele :
                    new_line.append(ele.strip())
            if not new_line:
                continue
            final_table.append(new_line)
        
        ## Creating a dataframe from the parsed list.
        df = pd.DataFrame(final_table[1:],columns=final_table[0])
        return df.to_dict(orient='records')