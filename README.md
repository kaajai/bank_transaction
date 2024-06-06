# 💲 Bank Transaction Extraction & Analysis 📑💳
## Project Overview

The **Bank Transaction Extraction & Analysis** project aims to extract and classify transactions from bank statements into types: credit or debit. The input statements can be in `.docx`, `.pdf`, or `.xlsx` format. The final output is a table containing metadata for each transaction, including the date, description, amount, and type.

## Features

- **Interactive UI:** Users can upload bank statement files through a Streamlit interface. The UI includes restrictions on file size and type.
- **Backend API:** A Flask API handles the backend processing, using various parsing libraries to read and extract data from different file formats.
- **Transaction Extraction & Classification:** Utilizes prompt engineering and GPT-4 for extracting and classifying transaction data.
- **Persistent Storage:** Stores extracted data for future reference.
- **Output:** Returns a JSON list containing the extracted table.

## Workflow

1. **File Upload:** Users upload a file through the Streamlit interface.
2. **API Request:** The `submit-statement` API endpoint is called with the uploaded file.
3. **File Parsing:** The file type is determined, and the appropriate parser is used to extract raw data.
4. **Data Extraction:** Raw data is processed using GPT-4 to extract and classify transactions.
5. **Result Storage:** The results are stored in a persistent storage system.
6. **Response:** The parsed table is returned to the UI as a JSON list.

## Setup

### Prerequisites

- Python 3.x
- Anaconda or virtualenv
- OpenAI API key

### Installation Steps

1. **Create a Virtual Environment:**
   ```bash
   conda create -n bank_txn_env python=3.8
   conda activate bank_txn_env
   # or using virtualenv
   python -m venv bank_txn_env
   source bank_txn_env/bin/activate

2. **Setup the virtual environment**
    ```bash
    pip install -r requirements.txt

3. **Set Environment Variable:**
    ```bash
    echo OPENAI_API_KEY=<your-key>

4. **Run Servers:**
    ```bash
    # Start the streamlit server
    streamlit run streamlit.py
    # Start the flask server
    flask run app.py


### Additional Installation(s) (if needed)
    
    $ brew install poppler

    
    $ python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

    $ pip install -U 'git+https://github.com/nikhilweee/iopath'

    $ brew install tesseract


### **Usage**

1. Navigate to the Streamlit UI in your browser.
2. Upload a bank statement file (docx, pdf, or excel).
3. View the extracted and classified transactions in the UI.

### **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request.

### **License**
This project is licensed under the MIT License. See the LICENSE file for details.

### **Acknowledgements**
- Streamlit
- Flask
- pdf2image
- layoutparser
- pytesseract
- pandas
- python-docx

### Contact
For any queries, please contact prashant.grv07@gmail.com.


    
