# import mysql.connector
# # Replace <CA_CERT_FILE>.pem with actual CA certificate path
# ca_cert_path = "D:/isrgrootx1.pem"
# # Connect to TiDB Cloud
# connection = mysql.connector.connect(
#         host ="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
#         port = 4000,
#         user = "2Eqxu3UMbVw6UyB.root",
#         password = "8yVqylFsPZVrKBF9",
#         database = "test",
#         ssl_ca = ca_cert_path #Enable TLS Security
# )
# cursor = connection.cursor()

# # Sample Data (Modify as per dataset)
# data = [
#     ("Alice", 25, "Female", "Delhi", "NY", "INDIA", 60000.00),
#     ("Bob", 30, "Male", "Chennai", "CA", "INDIA", 75000.00),
#     ("Charlie", 28, "Male", "Kolkata", "IL", "INDIA", 70000.00)
# ]

# # Insert Query (Batch Insert)
# query = """
# INSERT INTO census_data1 (name, age, gender, city, state, country, salary)
# VALUES (%s, %s, %s, %s, %s, %s, %s)
# """

# cursor.executemany(query, data)
# connection.commit()

# print("Data inserted successfully to TiDB-MySQLClient!")

# # Close the connection
# cursor.close()
# connection.close()