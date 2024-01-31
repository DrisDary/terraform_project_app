from fn_db_app.repository_helper import fetch_data, execute_data
from fn_db_app.logs import logger


class CreateTable:

    @execute_data
    def create():

        query =         f'''
                        CREATE TABLE TestTable_1    (column_1 nchar(20) NULL,\
                                                    column_2 nchar(20) NULL,\
                                                    column_3 nchar(20) NULL)
                        '''
        arguments = None
        
        return query, arguments


class PushData:

    @execute_data
    def push_items(list_of_arguments):

        query =         f'''
                        INSERT INTO dbo.TestTable_1   ("column_1",\
                                                    "column_2",\
                                                    "column_3")
                        VALUES
                                                    (?, ?, ?)
                        '''
        arguments = list_of_arguments
        
        return query, arguments


class GetData:

    @fetch_data
    def get_items():
        
        query = f"SELECT    column_1,\
                            column_2, \
                            column_3\
                FROM        dbo.TestTable_1"


        return query
        
