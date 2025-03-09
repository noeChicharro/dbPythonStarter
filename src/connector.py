import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Wuschtel5!',
    database='expenditure'
)

if connection.is_connected():
    print('Connected to MySQL database')
else:
    print('Connection failed')  

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS valueYear')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS valueYear (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year VARCHAR(30) NOT NULL,
    value VARCHAR(30) NOT NULL
)
'''

cursor.execute(create_value_tabel)
print('Table created')

connection.commit()
cursor.close()

connection.close()