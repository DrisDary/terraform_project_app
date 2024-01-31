from fn_db_app import base_repository



def fetch_data(function) -> list:

    def wrapper(*args, **kwargs):

        query                      = function(*args, **kwargs)
        lst                         = base_repository.BaseRepository().fetch(query)
        
        return lst

    return wrapper


def execute_data(function):

    def wrapper(*args, **kwargs):    
        query, argument             = function(*args, **kwargs)
        output                      = base_repository.BaseRepository().execute(query, argument)
        return 
    
    return wrapper











 