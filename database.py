import mysql.connector as sql

mydb = sql.connect(
    host='localhost',
    user='root',
    passwd='Arun@123456',
    database='user_database'
)

cursor=mydb.cursor()

def create_table():
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS user
                   (username VARCHAR(30) NOT NULL,
                   email VARCHAR(30) NOT NULL,
                   Phone INTEGER NOT NULL,
                   password VARCHAR(30) NOT NULL,
                   balance INTEGER NOT NULL,
                   deposit INTEGER NOT NULL,
                   withdraw INTEGER NOT NULL)
                   ''')
    

mydb.commit()

