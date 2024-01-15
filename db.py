import os
from tokenize import String
from sqlalchemy import create_engine, text
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()

# print(f'\nCurrent version of sqlalchemy is:- {sqlalchemy.__version__}\n')

username = os.getenv('username')
host = os.getenv('host')
password = os.getenv('password')
database = os.getenv('database')

db_connect_string = f"mysql+pymysql://{username}:{password}@{host}/{database}?charset=utf8mb4" 

engine = create_engine(
    db_connect_string,
    connect_args={
        "ssl":{
             "ssl_ca": "/etc/ssl/cert.pem"
        }
    })



# ==============================================================================

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
    
#     result_dicts = []

# for row in result.all():
    
#     result_dict = {}
    
#     # Access column names directly (without using row.keys()):
#     for i in range(len(row._fields)):  # Use row._fields to get column names

#         result_dict[row._fields[i]] = row[i]  # Get column name and value
    
#     result_dicts.append(result_dict)
    
# print(result_dicts) # displaying list .

# =======================================================================================

def load_jobs_from_db():
    
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        
        jobs = []

    for row in result.all():

        result_dict = {}

    # Access column names directly (without using row.keys()):
        for i in range(len(row._fields)):  # Use row._fields to get column names

            result_dict[row._fields[i]] = row[i]  # Get column name and value

        jobs.append(result_dict)
        
    return (jobs)

    
    