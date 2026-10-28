import json
import os
import mysql.connector
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME", "pzb4me.mock")

url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}"
engine = create_engine(url)

def read_data(filename):
    """read file"""
    return pd.read_csv(filename)
def clean_data(data):
    """clean data"""
    return data.dropna()
def load_data(data,table="mock"):
    """load the data"""
    df.to_sql("mock", con=engine, if_exists="replace", index=False)
    engine.dispose()
if __name__=="__main__": 
    def main():
        read_data()
        clean_data()
        load_data()
