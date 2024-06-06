import pdf2image
import layoutparser as lp
import pytesseract
import numpy as np
import pandas as pd
import os
from utils.parsers.file_parser import FileParser
from utils.config import Config

class PdfParser(FileParser):
    """
        Parser inheriting FileParser class. Specifically designed for parsing pdf files.
    """
    def __init__(self, file, filename):
        super().__init__(file, filename)
        ### Conversting the pdf file to image format.
        self.pdf_image = pdf2image.convert_from_path(os.path.join(Config.UPLOADED_FILE_PATH.value, filename))[0]
    
    def parse_file(self):
        ### Initialzing the layout detection model.
        model = lp.Detectron2LayoutModel('lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
                                 extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5],
                                 label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"})
        ### getting the layout detection result using the pdf image.
        layout_result = model.detect(self.pdf_image)

        ### Performing OCR - Optical Character Recognition using tesseract.
        pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

        # Filter for table blocks
        table_blocks = lp.Layout([b for b in layout_result if b.type == 'Table'])
        self.parsed_text = ''
        for table_block in table_blocks:
            # Extract the table image
            table_image = self.pdf_image.crop(table_block.coordinates)
            
            # Optionally use OCR to extract text from the table image
            self.parsed_text = pytesseract.image_to_string(table_image)

        ### storing the parsed results and returning.
        super().store_parsed_text()
        return self.parsed_text
            
            