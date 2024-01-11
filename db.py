from sqlalchemy import create_engine, text
import sqlalchemy
# print(f'\nCurrent version of sqlalchemy is:- {sqlalchemy.__version__}\n')

db_connect_string = "mysql+pymysql://cmwc0oofev4bg3vqdp4p:pscale_pw_2b5cYv8A65bCDflJFGCBZYZaiJvgNkAPbs3v2pUTI6Z@aws.connect.psdb.cloud/mediahub?charset=utf8mb4" 

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
    
    row_no = 1

for row in result.all():
    # print(row)
    
    result_dict = {}
    # Access column names directly (without using row.keys()):
    for i in range(len(row._fields)):  # Use row._fields to get column names

        result_dict[row._fields[i]] = row[i]  # Get column name and value
    
    result_dicts.append(result_dict)
    
    print(result_dicts)
    print(f"\n\n")
    