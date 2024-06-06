from utils.parsers.file_parser import FileParser
import pandas as pd
class ExcelParser(FileParser):
    """
        Parser inheriting FileParser class. Specifically designed for parsing Excel files.
    """
    def __init__(self, file, filename):
        ### Stroing the filename and file using the super keyword.
        super().__init__(file, filename)

    def parse_file(self):
        """
            Method to parse the file and store the parsed text in self.parsed_text.
            Args:
            - None
            Returns:
            - Parsed text from the excel file
        """
        
        self.parsed_text = pd.read_excel(self.file).fillna('').to_string(index=False)
        super().store_parsed_text()
        return self.parsed_text