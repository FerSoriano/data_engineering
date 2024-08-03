import psycopg2

class DatabaseConection():
    def __init__(self, config: dict) -> None:
        self.config = config
        self.schema = self.config.get('REDSHIFT_SCHEMA')

    def get_conn(self):
        """ Connect to the Redshift database server """

        username = self.config.get('REDSHIFT_USERNAME')
        password = self.config.get('REDSHIFT_PASSWORD')
        host = self.config.get('REDSHIFT_HOST')
        port = self.config.get('REDSHIFT_PORT', '5439')
        dbname = self.config.get('REDSHIFT_DBNAME')

        try:
            # connecting to the Redshift server
            with psycopg2.connect(f"dbname={dbname} host={host} port={port} user={username} password={password}") as self.conn:
                print('Connected to the Redshift server.')
                return self.conn
        except (Exception, psycopg2.DatabaseError ) as error:
            print(error)
            print('Error: get_conn()')
            exit()

    def validate_table_exists(self, table_name) -> bool:
        with self.conn.cursor() as cursor:
            cursor.execute(f"""
                    SELECT 1 FROM information_schema.tables 
                    WHERE  table_schema = {self.schema}
                    AND    table_name   = '{table_name}';              
                """)
            table_exists = cursor.fetchone()
            if table_exists:
                return True
            else:
                return False
            
    def print_table_message(self, table_name: str, type: int) -> None:
        """ type 1: Success | type 2: Error"""
        if type == 1:
            print(f"{table_name} created successfully.")
        elif type == 2:
            print(f'Error creating: {table_name}')

    def create_stage_table_executionLog(self) -> None:
        """ Create a table in the database """
        table_name = 'stg_executionLog'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.schema}.{table_name} (
                    id INT IDENTITY(1,1),
                    last_execution DATE NOT NULL
                );
                """)
                self.conn.commit()
                self.print_table_message(table_name, 1)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.print_table_message(table_name, 2)
            self.conn.rollback()
            exit()

    def create_stage_table_medallero(self) -> None:
        """ Create stage table in the database """
        table_name = 'stg_medallero'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.schema}.{table_name} (
                    id INT IDENTITY(1,1),
                    rank INT,
                    country VARCHAR(255),
                    gold INT,
                    silver INT,
                    bronze INT,
                    total INT,
                    execution_date DATE NOT NULL
                );
                """)
                self.conn.commit()
                self.print_table_message(table_name, 1)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.print_table_message(table_name, 2)
            self.conn.rollback()
            exit()

    def create_edw_table_medallero(self) -> None:
        """ Create edw table in the database """
        table_name = 'edw_medallero'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.schema}.{table_name} (
                    id INT IDENTITY(1,1),
                    rank INT,
                    country VARCHAR(255),
                    gold INT,
                    silver INT,
                    bronze INT,
                    total INT,
                    execution_date DATE not null,
                    is_active INT not null,
                    country_id INT
                );
                """)
                self.conn.commit()
                self.print_table_message(table_name, 1)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.print_table_message(table_name, 2)
            self.conn.rollback()
            exit()

    def get_last_execution(self) -> tuple:
        """ Get the last execution """
        table_name = 'stg_executionlog'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"SELECT MAX(last_execution) FROM {self.schema}.{table_name};")
                last_execution = cursor.fetchone()
                print("get_last_execution() -> Data queried successfully")
                return last_execution[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Error: get_last_execution()')
            exit()

    def insert_to_stage_table_medallero(self, df) -> None:
        """ Insert DataFrame into Redshift table """
        table_name = 'stg_medallero'
        try:
            with self.conn.cursor() as cursor:
                for index, row in df.iterrows():
                    cursor.execute(f"""
                        INSERT INTO {self.schema}.{table_name} (rank, country, gold, silver, bronze, total, execution_date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (index, row['Country'], row['Gold'], row['Silver'], row['Bronze'], row['Total'], row['execution_date']))
                self.conn.commit()
                print(f"Data inserted successfully into {table_name}.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Error: insert_to_stage_table_medallero()')
            self.conn.rollback()
            exit()

    def truncate_stage_table_medallero(self) -> None:
        """ Truncate stage table """
        table_name = 'stg_medallero'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"TRUNCATE table {self.schema}.{table_name};")
                self.conn.commit()
                print("truncate_stage_table_medallero() -> executed successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Error: truncate_stage_table_medallero()')
            self.conn.rollback()
            exit()

    def insert_to_stage_table_executionlog(self, last_execution) -> None:
        """ Insert last execution date """
        table_name = 'stg_executionlog'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                        INSERT INTO {self.schema}.{table_name} (last_execution)
                        VALUES (%s)
                    """, (last_execution,))
                self.conn.commit()
                print("Data inserted successfully into stage.executionLog.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Error: insert_to_stage_table_executionlog()')
            self.conn.rollback()
            exit()

    def update_edw_table_medallero(self) -> None:
        """ Update Is_Active to Zero """
        table_name = 'edw_medallero'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"UPDATE {self.schema}.{table_name} SET is_active = 0 WHERE is_active = 1;")
                self.conn.commit()
                print("update_edw_table_medallero() -> executed successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Error: update_edw_table_medallero()')
            self.conn.rollback()
            exit()

    def insert_to_edw_table_medallero(self) -> None:
        """ Insert into EDW table """
        insert_table_name = 'edw_medallero'
        from_table_name = 'stg_medallero'
        left_table_name = 'edw_countries'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                    INSERT INTO {self.schema}.{insert_table_name}(
                            rank,
                            country,
                            gold,
                            silver,
                            bronze,
                            total,
                            execution_date,
                            is_active,
                            country_id
                        )
                            SELECT
                                rank, 
                                m.country,
                                gold,
                                silver,
                                bronze,
                                total,
                                execution_date,
                                1 as is_active,
                                c.id as "country_id"
                            FROM {from_table_name} m
                            LEFT JOIN {left_table_name} c 
		                        ON c.country = m.country;
                    """)
                self.conn.commit()
                print("Data inserted successfully into edw.medallero.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Error: insert_to_edw_table_medallero()')
            self.conn.rollback()
            exit()

    def create_edw_table_countries(self) -> None:
        """ Create Country table in the database """
        table_name = 'edw_Countries'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.schema}.{table_name} (
                    id INT IDENTITY(1,1),
                    country VARCHAR(255) NOT NULL
                );
                """)
                self.conn.commit()
                self.print_table_message(table_name, 1)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.print_table_message(table_name, 2)
            self.conn.rollback()
            exit()

    def insert_to_edw_table_countries(self) -> None:
        """ Insert into EDW table """
        table_name = 'edw_Countries'
        from_table_name = 'stg_medallero'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                    INSERT INTO {self.schema}.{table_name} (country)
                    SELECT DISTINCT country 
                    FROM {from_table_name} m
                    WHERE NOT EXISTS (
                        SELECT 1
                        FROM {table_name} c
                        WHERE c.country = m.country
                        )
                    ORDER BY 1 ASC;
                    """)
                self.conn.commit()
                print("Data inserted successfully into edw.countries.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Error: insert_to_edw_table_countries()')
            self.conn.rollback()
            exit()

    def create_edw_view_medallero(self) -> None:
        """ Create edw view in the database """
        view_name = 'edw_medallero_view'
        table_name = 'edw_medallero'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"""
                CREATE OR REPLACE VIEW {self.schema}.{view_name}
                AS SELECT
                    rank as "Rank"
                    ,country as "Country"
                    ,gold as "Gold"
                    ,silver as "Silver"
                    ,bronze as "Bronze"
                    ,total as "Total"
                    ,execution_date as "Last Update"
                FROM {self.schema}.{table_name}
                where is_active = 1
                order by rank ;
                """)
                self.conn.commit()
                self.print_table_message(view_name, 1)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.print_table_message(view_name, 2)
            self.conn.rollback()
            exit()