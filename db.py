from sqlalchemy import create_engine, text
import sqlalchemy
# print(f'\nCurrent version of sqlalchemy is:- {sqlalchemy.__version__}\n')

username = "a1xyz68xar0rnkz6qs28"
hostid = "aws.connect.psdb.cloud"
password = "pscale_pw_QUYkpeTJum4OgNBQUfyDbGbZypHSLrPRFZFEqnYZUVD"
database = "mediahub"

db_connect_string = f"mysql+pymysql://{username}:{password}@{hostid}/{database}?charset=utf8mb4" 

engine = create_engine(
    db_connect_string,
    connect_args={
        "ssl":{
             "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
    result_dicts = []
    rds = []

for row in result.all():
    
    result_dict = {}
    
    # Access column names directly (without using row.keys()):
    for i in range(len(row._fields)):  # Use row._fields to get column names

        result_dict[row._fields[i]] = row[i]  # Get column name and value
    
    result_dicts.append(result_dict)
    
print(result_dicts) # displaying list .
    