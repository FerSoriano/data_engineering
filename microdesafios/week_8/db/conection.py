import psycopg2

class DatabaseConection():
    def __init__(self, config: dict) -> None:
        self.config = config

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

    def close_conn(self) -> None:
        """ Close connection """
        try:
            self.conn.close()
            print('Connection closed...')
        except (Exception, psycopg2.DatabaseError ) as error:
            print(error)
            print('Error: close_conn()')
            exit()