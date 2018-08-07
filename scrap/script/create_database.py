import MySQLdb
from configparser import ConfigParser




def create_db():
    
    conf = ConfigParser()    
    conf.read("../setup.ini")
    host = conf['mysql']["host"]
#    port = conf['mysql']["port"]
    user = conf['mysql']["username"]
    passwd = conf['mysql']["password"]
    database = conf['mysql']["database"]
    
    mysql = MySQLdb
    db = mysql.connect(host=host,  user=user, passwd=passwd)
    cursor = db.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS {}".format(database)
    cursor.execute(sql)       
    db.close()


create_db()

        
    


    
