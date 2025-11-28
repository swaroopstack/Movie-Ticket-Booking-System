from config import get_connection

conn = get_connection()

if conn:
    print("✅ Database connected successfully!")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    print("Tables in movie_db:", cursor.fetchall())
    conn.close()
else:
    print("❌ Connection failed.")
