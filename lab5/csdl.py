from ensurepip import version
from turtle import pu
import  pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-VON6VIQ;DATABASE=QLMonAn;UID=sa;PWD=123;ENCRYPT=no')
cursor = conn.cursor()
cursor.execute("SELECT @@version")
conn.close()
db_version = cursor.fetchone()
print('bạn đang dùng hệ quản trị CSDL SQL Server phiên bản ',db_version)