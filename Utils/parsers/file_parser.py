import pandas as pd
from utils.config import Config
import os
class FileParser():
    """
        Parent parser class respresenting basic configuration and methods for 
        specific parsers.
    """
    def __init__(self, file, filename):
        self.file = file
        self.filename = filename
        self.parsed_text = None

    def store_parsed_text(self):
        """
            Method tostore parsed text from the input file.
        """
        
        with open(os.path.join(Config.RAW_FILE_PATH.value, self.filename), 'w') as f:
            f.write(self.parsed_text)
        


    