import pymysql as mysql
def connection():
    db=mysql.connect(host="localhost",user="root",password="8520",port=3306,db="nemesisdata")
    cmd=db.cursor()
    return db,cmd