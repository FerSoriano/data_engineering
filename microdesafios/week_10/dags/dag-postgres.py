from datetime import datetime, timedelta
from email.policy import default
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args={
    'owner': 'FerSoriano',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='dag_con_conexion_postgres',
    description= 'Nuestro primer dag usando python Operator',
    start_date=datetime(2024,8,26),
    schedule_interval='0 0 * * *',
    tags=['postgres','microdesafio_10']
    ) as dag:
    

    create_schema = PostgresOperator(
        task_id='crear_schema_postgres',
        postgres_conn_id = 'postgres_localhost',
        sql="""
            CREATE SCHEMA IF NOT EXISTS airflow AUTHORIZATION airflow;
        """
    )

    create_table= PostgresOperator(
        task_id='crear_tabla_postgres',
        postgres_conn_id= 'postgres_localhost',
        sql="""
            create table if not exists fin_mundo_fs(
                dt date,
                pais varchar(30)
            )
        """
    )

    insert_data =PostgresOperator(
        task_id='insertar_en_tabla',
        postgres_conn_id= 'postgres_localhost',
        sql="""
            insert into fin_mundo_fs (dt,pais) values ('12-12-2025','Colombia');
            insert into fin_mundo_fs (dt,pais) values ('11-08-2035','Brasil');
            insert into fin_mundo_fs (dt,pais) values ('8-09-2030','Argentina');
            insert into fin_mundo_fs (dt,pais) values ('3-07-2045','Chile');
            insert into fin_mundo_fs (dt,pais) values ('7-11-2028','Ecuador');
            insert into fin_mundo_fs (dt,pais) values ('9-03-2032','Peru');
            insert into fin_mundo_fs (dt,pais) values ('8-08-2026','Uruguay');
            insert into fin_mundo_fs (dt,pais) values ('2-05-2037','Paraguay');
            insert into fin_mundo_fs (dt,pais) values ('12-12-2080','Venezuela');
            insert into fin_mundo_fs (dt,pais) values ('11-12-2071','Mexico');
        """
    )

    create_schema >> create_table >> insert_data