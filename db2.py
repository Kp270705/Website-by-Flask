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
        # print(f"row._fields = {row._fields}")
        
        result_dict[row._fields[i]] = row[i]  # Get column name and value
        
        print(f"\n\n\tRow({row_no}) field ({row._fields[i]}) have value ({row[i]})")
        print(f"\t\tresult_dicts = {result_dict}")
    
    row_no += 1 # to store the value of each row.
    
    result_dicts.append(result_dict)
    print(f"\n\n")
    
    # rds = result_dicts
    # print(result_dicts)
  
#   =======================================================================================
    
# # from typing import Self
# from flask import Flask, render_template, jsonify      # there is a class "flask" inside module 'flask'
# # from flask_sqlalchemy import SQLAlchemy
# # from datetime import datetime 
# # from sqlalchemy import text

# from db import load_jobs_from_db


# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     jobs_dict = load_jobs_from_db()
#     return render_template('index.html', JOBS=jobs_dict)

# @app.route('/jobs')
# def list_jobs():
#     jobs = load_jobs_from_db()
#     return jsonify(jobs)


# if __name__ == "__main__":
#     # app.run(debug=True, port=8000)
#     app.run(host='0.0.0.0', debug=True)