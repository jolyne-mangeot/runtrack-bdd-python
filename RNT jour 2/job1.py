import mysql.connector

student_database = mysql.connector.connect(
    host="localhost",
    user="python",
    password="python123456"
)

if student_database.is_connected():
    db_infos = student_database.get_server_info()
    print(f"Connecté à MySQL, version {db_infos}")

student_database.close()