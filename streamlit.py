import streamlit as st
import requests
import pandas as pd
from utils.config import Config

API_URL = 'http://127.0.0.1:5000/submit-statement'


def file_size_under_limit(file) -> bool:
    """
        The function to check the file size of the uploaded file.
        Args:
        - file: The file object containing the uploaded file.
        Returns:
        - True: If the file size is less than the maximum file size.
    """
    return file.size / (1024 * 1024) <= Config.MAX_FILE_SIZE.value

def main():
    """
        Method to for the streamlit server for testing the API to parse the bank statements.
        The fuction takes a file as input and returns a list of transactions details in the form of a table.
    """

    #Accepting file as input and restricting the type of file.
    st.title("Upload a Bank Statement to get the transaction details.")
    uploaded_file = st.file_uploader(f"Choose a file({'/'.join(Config.SUPPORTED_FILE_TYPES.value)})", type=Config.SUPPORTED_FILE_TYPES.value)
    if uploaded_file is not None:
        payload = {"filename": uploaded_file.name}
        files = {'file': uploaded_file.getvalue()}

        #Checking if the file is under the limit of the file size.
        if file_size_under_limit(uploaded_file):
            st.success("File uploaded successfully!")
        else:
            st.error(f"File size should be less than {Config.MAX_FILE_SIZE.value}MB.")

        # Make a POST request to the API URL with the file and file name as parameters
        response = requests.post(API_URL, params=payload,files=files)
        if response.status_code == 400:
            st.error("Error occured while parsing the file.")
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Check if the response is a list of JSON objects
            if isinstance(data, list):
                df = pd.DataFrame()
                for index, item in enumerate(data):
                    _df = pd.DataFrame([item])
                    df = pd.concat([df, _df], ignore_index=True)
                    
                st.table(df)
            else:
                st.error("The response is not a list of JSON objects.")
        else:
            st.error("Failed to get a valid response from the API.")

if __name__ == '__main__':
    main()
