# import mysql.connector
# # Replace <CA_CERT_FILE>.pem with actual CA certificate path
# ca_cert_path = "D:/isrgrootx1.pem"
# # try: 
# connection = mysql.connector.connect(
#         host ="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
#         port = 4000,
#         user = "2Eqxu3UMbVw6UyB.root",
#         password = "8yVqylFsPZVrKBF9",
#         database = "test",
#         ssl_ca = ca_cert_path #Enable TLS Security
# )
# print("Connected to TiDB Cloud successfully!")

# cursor = connection.cursor()
#     # Run a simple query to check connection
#     # cursor.execute("SHOW TABLES;")
# cursor.execute("SELECT DATABASE();")
# db_name = cursor.fetchone()
# print(f"✅ Connected to TiDB Cloud! current database = {db_name[0]}")

# cursor.close()
# connection.close()
# print("Connection closed..")
    # for table in cursor.fetchall():
    #     print(table)

# except mysql.connector.Error as e:
#     print("Error Counting:", e)

# finally :
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("Connection closed..")
