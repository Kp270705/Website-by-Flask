from sqlalchemy import create_engine, text
import sqlalchemy
# print(f'\nCurrent version of sqlalchemy is:- {sqlalchemy.__version__}\n')

db_connect_string = "mysql+pymysql://krssmmr3xe4apura5i1m:pscale_pw_KZGskPQ6Vvjy741U33TPITs85EizC2szBbt3sXdfnZ1@aws.connect.psdb.cloud/mediahub?charset=utf8mb4" 

engine = create_engine(
    db_connect_string,
    connect_args={
        "ssl":{
             "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(f"\n\t Type of result:- {type(result)}\n")
    result_all = result.all()
    
    # print(f"\n\tType of result_all:- {type(result_all)}\n")
    # print(f"\n\tType of result_all 1:- {type(result_all[0])}\n")
    # print(f"First result_all:- {result_all[0]}\n")
    # print(f"\n\tType of result_all 2:- {type(result_all[1])}\n")
    # print(f"Second result_all:- {result_all[1]}\n")
    
    #converting rows into dict:- 
    first_row_result_dict = dict(result_all[0])
    second_row_result_dict = dict(result_all[1])
    
    print(f"type of (first_row_result_dic) is:-{type(first_row_result_dict)}")
    print(f"type of (second_row_result_dic) is:-{type(second_row_result_dict)}")
    
    print(f"Here (first_row_result_dict) is:- \n{first_row_result_dict}")
    print(f"Here (second_row_result_dict) is:- \n{second_row_result_dict}")
    