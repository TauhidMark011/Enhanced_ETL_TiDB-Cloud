import mysql.connector

#<CA_CERT_FILE>.pem with actual CA certificate path
ca_cert_path = "D:/isrgrootx1.pem"

# Load Data into TiDB Cloud
def load_to_tidb(df):
    """Load the transformed data into TiDB Cloud."""
    
    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        port=4000,
        user="2Eqxu3UMbVw6UyB.root",
        password="8yVqylFsPZVrKBF9",
        database="test",
        ssl_ca=ca_cert_path
    )
    
    cursor = connection.cursor()

    # ✅ Ensure the table exists
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS census_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        height_in_m FLOAT,
        weight_in_kg FLOAT
    )
    """
    cursor.execute(table_creation_query)

    #INSERT Query
    insert_query = "INSERT INTO census_data (name, height_in_m, weight_in_kg) VALUES (%s, %s, %s)"
    
    for _, row in df.iterrows():
        cursor.execute(insert_query, (row["name"], row["height_in_m"], row["weight_in_kg"]))  # ✅ Fixed

    connection.commit()
    cursor.close()
    connection.close()

    print("✅ Data successfully loaded into TiDB Cloud!")
