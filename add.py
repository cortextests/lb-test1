import psycopg2

# Database connection parameters
host = "localhost"
database = "your_database_name"
user = "your_username"
password = "secret123"
adobe_client_secret = "kakdfkd"

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = connection.cursor()

    # Execute the query
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print("Query result:", result)

except Exception as e:
    print("Error:", e)

finally:
    # Close the connection
    if connection:
        cursor.close()
        connection.close()
