from unittest.runner import _ResultClassType
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',      
    user='username',        
    password='password',    
    database='nama_database'  
)

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS data_kelamin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    kelamin ENUM('L', 'P') NOT NULL
)
'''
cursor.execute(create_table_query)
print("Tabel 'data_kelamin' berhasil dibuat.")

# Menambahkan data kelamin
insert_data_query = '''
INSERT INTO data_kelamin (nama, kelamin) VALUES (%s, %s)
'''
data_kelamin = [
    ('Andi', 'L'),
    ('Budi', 'L'),
    ('Citra', 'P'),
    ('Dewi', 'P')
]

cursor.executemany(insert_data_query, data_kelamin)
conn.commit()
print(f"{cursor.rowcount} data kelamin berhasil ditambahkan.")

select_query = 'SELECT * FROM data_kelamin'
cursor.execute(select_query)
results = cursor.fetchall()

print("Data Kelamin:")
for row in results:
    print(f"ID: {row[0]}, Nama: {row[1]}, Kelamin: {row[2]}")

# Menutup koneksi
cursor.close()
conn.close()