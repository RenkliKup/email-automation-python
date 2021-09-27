import sqlite3
import logging
logger=logging.getLogger(__name__)
formatter=logging.Formatter("%(lineno)d:%(asctime)s:%(levelname)s")
fileHandler=logging.FileHandler("./log/sql.log")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
class CompanyDb:
    def __init__(self):
        
            self.con=sqlite3.connect("./sql/db/Company.db")
    def createTable(self,):
        try:  
            cursor=self.con.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Company 
                (Company_Mail text)''')
            
           # self.con.close()
            return True
        except Exception as e:
            logger.error(str(e))
    def insert(self,mail):
        try:
            cursor=self.con.cursor()
            cursor.execute(f"INSERT INTO Company(Company_Mail) VALUES('{mail}')")
            self.con.commit()
           # self.con.close()
            return True
        except Exception as e:
            print(e)
            logger.error(str(e))
    def deleteTable(self):
        try:
            
            cursor=self.con.cursor()
            cursor.execute("DELETE FROM Company")
            self.con.commit()
           # self.con.close()
            return True
        except Exception as e:
            logger.error(str(e))
            return False
    def hasCompany(self,mail):
        try:
            cursor=self.con.cursor()
            cursor.execute(f"SELECT Company_Mail FROM Company WHERE Company_Mail=='{mail}'")
            result=cursor.fetchall()
            return result

        except Exception as e:
            logger.error(str(str))
            print(e)
    def lenDb(self,):
        try:
            cursor=self.con.cursor()
            cursor.execute("SELECT Company_Mail FROM Company")
            result=cursor.fetchall()
            return result
        except Exception as e:
            logger.error(str(e))
            return False
