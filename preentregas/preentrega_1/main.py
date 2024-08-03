import os
from datetime import datetime
from dotenv import load_dotenv

from db.connect import DatabaseConection
from etl.olympics_medals import Medals

load_dotenv()

CREATE_TABLES = True
CREATE_VIEWS = True
RUN_ETL = True

def main(create_tables: bool, create_views: bool, run_etl: bool) -> None:

    config = {
        "REDSHIFT_USERNAME" : os.getenv('REDSHIFT_USERNAME'),
        "REDSHIFT_PASSWORD" : os.getenv('REDSHIFT_PASSWORD'),
        "REDSHIFT_HOST" : os.getenv('REDSHIFT_HOST'),
        "REDSHIFT_PORT" : os.getenv('REDSHIFT_PORT', '5439'),
        "REDSHIFT_DBNAME" : os.getenv('REDSHIFT_DBNAME')
        }

    db = DatabaseConection(config=config)
    db.get_conn()

    try:
        if create_tables:
            db.create_stage_table_executionLog()
            db.create_stage_table_medallero()
            db.create_edw_table_countries()
            db.create_edw_table_medallero()
        
        if create_views:
            db.create_edw_view_medallero()

        last_execution = db.get_last_execution()
        today = datetime.now().strftime("%Y-%m-%d")

        if today == str(last_execution):
            print('Execution completed, the process has already been executed today. Data not added.')
            exit()

        if run_etl:
            medals = Medals()
            medals.get_response()
            df = medals.get_medals()

            # Truncar Stage
            db.truncate_stage_table_medallero()
            # Insertar Stage
            db.insert_to_stage_table_medallero(df=df)
            # Insertar Execution Log
            db.insert_to_stage_table_executionlog(today)
            # Insertar Stage
            db.insert_to_edw_table_countries()
            # Actualizar Is_Active a 0
            db.update_edw_table_medallero()
            # Insertar en EDW
            db.insert_to_edw_table_medallero()
            
            print('ETL process completed successfully...')
    
    except Exception as error:
            print(error)
            exit()

if __name__ == "__main__":
    main(create_tables=CREATE_TABLES, create_views=CREATE_VIEWS, run_etl=RUN_ETL)