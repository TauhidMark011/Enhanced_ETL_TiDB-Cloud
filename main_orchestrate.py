from extract_data import extract_data
from transform_data import transform_data
from load_data_tidb import load_to_tidb

transformed_csv = "transformed_data.csv"

def orchestrate_etl():
    """Main function to execute the ETL process."""
print("Extracting Data_main-orch...")
extracted_data = extract_data()
if extracted_data is None or extracted_data.empty: #Debugging to check if data is extracted before transformation.
    print("❌ Data extraction failed! No data extracted.")
    exit()
print("Data Extraction Completed.")

print("Transforming Data...")
transformed_data = transform_data(extracted_data)
print("Data Transformation Completed..")

print("Saving transformed data to CSV...")
transformed_data.to_csv(transformed_csv, index=False)  # Fixed issue
print(f"Transformed data saved as {transformed_csv}")

print("Loading data into TiDB Cloud...")
load_to_tidb(transformed_data)
print("Data successfully loaded into TiDB Cloud from main.")