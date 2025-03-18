import pandas as pd 
import json
import os 
import xml.etree.ElementTree as ET 
from utils import log  # Ensure 'utils.py' has the log function

# Set the source directory where the data files are located
source_dir = r"E:\\source"
# Destination file for transformed data
transformed_csv = "transformed_data.csv"

def extract_data():
    """Extract data from multiple files in the source directory."""
    all_data = []

    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
         
        #Function to extract CSV Files 
        if file.endswith(".csv"):
            log(f"Extracting .csv file: {file}")
            df = pd.read_csv(file_path)
            all_data.append(df)

            #Function to extract JSON Files
        elif file.endswith(".json"):
            log(f"Extracting json file: {file}")
            with open(file_path, 'r') as f:
                #Uses json.loads(line) to read each line separately.
                #Converts multiple JSON objects into a DataFrame correctly.
                #Prevents "Extra data" error from json.load().
                data = [json.loads(line) for line in f] #Load each line as a JSON object |  
            df = pd.DataFrame(data) # Convert list of dictionaries to DataFrame
            all_data.append(df)

        #Function to extract XML Files
        elif file.endswith(".xml"):
            log(f"Extracting .xml file: {file}")
            tree = ET.parse(file_path)  # Parsing the XML file
            root = tree.getroot() # Getting the root element of the XML
            data = [] # Empty list to hold parsed data

            # Loop through XML elements and extract relevant data
            for item in root.findall(".//record"):  # Adjust tag if needed
                record = {child.tag: child.text for child in item}
                data.append(record)

            if data:  # Only append if data exists
                df = pd.DataFrame(data)
                all_data.append(df)

    # Ensure there's data before concatenating
    if all_data:
        return pd.concat(all_data, ignore_index=True)
    else:
        log("No valid data files found in the source directory.")
        return None
