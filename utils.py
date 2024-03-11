import mysql.connector.pooling

# Create a connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="my_pool",
    pool_size=30,
    host="localhost",
    user="ne",
    password="xxxvideo102TAN@#$",
    database="ProxyDB",
)

# connection_pool = mysql.connector.pooling.MySQLConnectionPool(
#     pool_name="my_pool",
#     pool_size=30,
#     host="localhost",
#     user="root",
#     password="123",
#     database="ProxyDB",
# )


# Function to get a connection from the pool
def get_connection_from_pool():
    try:
        connection = connection_pool.get_connection()
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        print(f"Error getting connection from pool: {e}")
    return None