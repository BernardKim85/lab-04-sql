import os
import pandas as pd
from sqlalchemy import create_engine

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}"
engine = create_engine(url)

def read_data(filename):
    """read and return file"""
    return pd.read_csv(filename)
def clean_data(data):
    """clean data"""
    return data.dropna()
def load_data(data,table="mock"):
    """load the data"""
    data.to_sql(table, con=engine, if_exists="replace", index=False)
    engine.dispose()
def main():
    data = read_data("MOCK_DATA.csv")
    data = clean_data(data)
    load_data(data)
if __name__=="__main__": 
    main()