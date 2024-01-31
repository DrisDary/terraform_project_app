from fn_db_app.logs import logger
import azure.functions as func
from fn_db_app import data_repository as repo

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        repo.CreateTable.create()

        data_to_be_inserted = [('Cat', 'Dog"', 'Mouse')]
        repo.PushData.push_items(data_to_be_inserted)

        get_all_data_from_database = repo.GetData.get_items()

        view_data = []

        for item in get_all_data_from_database:
            view_data.append(item)

        return func.HttpResponse(f"The data in the database is: \n {view_data}")
    
    except Exception as e:
        logger.error(e)







