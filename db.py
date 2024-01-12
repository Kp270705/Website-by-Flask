from sqlalchemy import create_engine, text
import sqlalchemy
# print(f'\nCurrent version of sqlalchemy is:- {sqlalchemy.__version__}\n')

username = "1hkyiig3tsjf4jxidw75"
host = "aws.connect.psdb.cloud"
password = "pscale_pw_nvOwSxbsu2w7IrstYYnIUy0R9qJE5RMExKulLV67JAP"
database = "mediahub"

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
    
    # print(jobs)
        
    
# if __name__  ==  "__main__":
#     ldb =load_jobs_from_db()
    
    