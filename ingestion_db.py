import pandas as pd
import os
from sqlalchemy import create_engine
os.makedirs('logs', exist_ok=True)
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)
# Connect to SQLite database
engine = create_engine('sqlite:///ingestion.db')

def ingest_db(df,table_name,engine):
    """ this will ingest dataframe into databse table"""
    df.to_sql(table_name,con = engine, if_exists = 'replace',index= False)

def load_raw_data():
    start=time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df=pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df,file[:-4],engine)
    end=time.time()
    total_time= (end-start)/60
    logging.info('---Ingestion Complete---')

    logging.info(f'\nTotal Time taken: {total_time} minutes')
if __name__ == '__main__':
    load_raw_data()
    
