import gdown
import os
from sourcecode import logger
from sourcecode.model.utils.utils import create_dir
import requests
class DownloadData():
    def __init__(self):
        pass

    def download_data() ->str:
        try:
            artifacts = "../../../artifacts"
            create_dir([artifacts])
            destination_folder = "../../../artifacts/data"
            create_dir([destination_folder])
            folder_id = "1VM8xLZIIrp5IGyGzC9T2XiP-kmPS4Mg1"
            print(folder_id)  ## deleted code
            API_URL = f"https://www.googleapis.com/drive/v3/files?q='{folder_id}'+in+parents&key=AIzaSyDCdSTGDStVPzuhxlQzQlaQvoys67tlqXM"
            response = requests.get(API_URL)
            print(response) ## deleted code
            if response.status_code == 200:
                files = response.json().get('files', [])
                for file in files:
                    file_id = file['id']
                    file_name = file['name']
                    download_url = f'https://drive.google.com/uc?id={file_id}'
                    
                    # Download the file using gdown
                    print(f'Downloading {file_name}...')
                    gdown.download(download_url, os.path.join(destination_folder, file_name), quiet=False)
            else:
                print("Failed to retrieve folder content.")
                print(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            raise e
        
download = DownloadData()
DownloadData.download_data()
        
