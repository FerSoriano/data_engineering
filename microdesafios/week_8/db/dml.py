# DML = Data Manipulation Language

import psycopg2
from db import DatabaseConection

class DataManipulation(DatabaseConection):
    def __init__(self, config: dict) -> None:
        super().__init__(config)
        self.schema = self.config.get('REDSHIFT_SCHEMA')
        self.table_name = 'POLITICAS_2050_FS'

    def create_table_Politicas_2050(self) -> None:
        """ Create table """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.schema}.{self.table_name} (
                    id INT IDENTITY(1,1),
                    pais VARCHAR(100),
                    comisionado VARCHAR(250),
                    reduccion_CO2 VARCHAR(2),
                    incrmento_P VARCHAR(2),
                    inversion_arboles VARCHAR(2),
                    fecha DATE,
                    telefono INT
                );
                """)
                self.conn.commit()
                print(f'The table {self.table_name} was created...')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.conn.rollback()
            exit()


    def truncate_table_Politicas_2050(self) -> None:
        """ Truncate table """
        try:
            with self.conn.cursor() as cursor:
                    cursor.execute(f'TRUNCATE TABLE {self.schema}.{self.table_name};')
                    self.conn.commit()
                    print('Table truncated')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.conn.rollback()
            exit()

    def insert_data(self, df) -> None:
        """ Insert DataFrame into Redshift table """
        try:
            with self.conn.cursor() as cursor:
                for index, row in df.iterrows():
                    cursor.execute(f"""
                        INSERT INTO {self.schema}.{self.table_name} (pais, comisionado, reduccion_CO2, Incrmento_P, Inversion_arboles, Fecha, Telefono)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (row['Pais'], row['Fake_Comisionado'], row['Reduccion_CO2'], row['Incrmento_P'], row['Inversion_arboles'], row['Fake_Fecha'], row['Fake_Telefono']))
                self.conn.commit()
                print(f"Data inserted successfully into {self.table_name}.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Error: insert_data()')
            self.conn.rollback()
            exit()

