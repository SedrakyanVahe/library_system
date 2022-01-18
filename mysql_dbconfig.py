import mysql.connector as cn

#################################################################################
# connect to MySql
#################################################################################
try:
    db = cn.connect(
        host="localhost",
        port="3306",
        user="vahe",
        password="1234",
        database="library_system",
    )
except:
    print("errror")
