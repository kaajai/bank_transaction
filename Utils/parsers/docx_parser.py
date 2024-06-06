from utils.parsers.file_parser import FileParser
import docx
class DocxParser(FileParser):
    def __init__(self, file, filename):
        """
        Parser inheriting FileParser class. Specifically designed for parsing docx files.
        """
        super().__init__(file, filename)

    def parse_file(self):
        """
            Parsing method for docx file.
            Args:
            - None
            Returns:
            - Parsed text from the docx file
        """
        doc = docx.Document(self.file)
        self.parsed_text = ""
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    self.parsed_text+= cell.text
        super().store_parsed_text()
        return self.parsed_text

            