import mysql.connector as cn

#################################################################################
# connect to MySql
#################################################################################
try:
    db = cn.connect(
        host="localhost",
        port="3306",
        user="yourUserName",
        password="yourPassword",
        database="library_system",
    )
except:
    print("error")
