import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', database='telegram', user='root', password='')
    if connection.is_connected():
        print("You're connected to database")
except Error as e:
    print("Error while connecting to MySQL", e)

def inset_wallet_info(fname, lname, uname, cid, addr, pri_key):
    try:
        query_string = "insert into user (telegram_id, first_name, last_name, user_name, address, private_key) values("
        query_string += str(cid) + ",'" + str(fname) + "', '" + str(lname) + "', '" + str(uname) + "', '" + str(addr) + "', '" + str(pri_key) + "')"
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
    except Error as e:
        print(e)

def get_wallet_address(cid):
    try:
        query_string = "select address from user where telegram_id=" + str(cid)
        cursor = connection.cursor()
        cursor.execute(query_string)
        res = cursor.fetchall()
        return [item[0] for item in res]
    except Error as e:
        print(e)