import os
from dotenv import load_dotenv

from db import DataManipulation
from modules import encrypt_data

load_dotenv()

def main() -> None:

    config = {
        "REDSHIFT_USERNAME" : os.getenv('REDSHIFT_USERNAME'),
        "REDSHIFT_PASSWORD" : os.getenv('REDSHIFT_PASSWORD'),
        "REDSHIFT_HOST" : os.getenv('REDSHIFT_HOST'),
        "REDSHIFT_PORT" : os.getenv('REDSHIFT_PORT', '5439'),
        "REDSHIFT_DBNAME" : os.getenv('REDSHIFT_DBNAME'),
        "REDSHIFT_SCHEMA" : os.getenv('REDSHIFT_SCHEMA'), 
        }

    db = DataManipulation(config=config)
    db.get_conn()

    db.create_table_Politicas_2050()
    db.truncate_table_Politicas_2050()

    data = encrypt_data()
    db.insert_data(df=data)

    db.close_conn()

    print('Done!')


if __name__ == '__main__':
    main()
