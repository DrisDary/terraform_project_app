import os
import pyodbc
from fn_db_app.logs import logger

class BaseRepository():


    def __init__(self):
        pass


    def __open_connection__(self):

        try:
            cs = os.environ['DB_CONNECTION_STRING']
            self.conn = pyodbc.connect(cs+'Authentication=ActiveDirectoryMsi')
            self.cursor         = self.conn.cursor()
    
        except Exception as e:
            logger.error(e)


    
    def __close_connection__(self):

        try:
            self.conn.close()

        except Exception as e:
            logger.error(e)
        

    def fetch(self, query : str) -> list:



        self.__open_connection__()

        try:
            self.cursor.execute(query)
            records     = self.cursor.fetchall()
            

            return records

        except Exception as e:
            logger.error(e)

        finally:
            self.__close_connection__()

   

    def execute(self, query : str , args):


        self.__open_connection__()

        try:
            if args != None:
                self.cursor.fast_executemany = True
                self.cursor.executemany(query, args)
                
            else:
                self.cursor.execute(query)

        except Exception as e:
            logger.error(e)

        finally:
            self.conn.commit()
            self.__close_connection__()
            





