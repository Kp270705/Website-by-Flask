
# from flask import Flask, render_template, jsonify      # there is a class "flask" inside module 'flask'
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime 


# app = Flask(__name__)


# jobs = [
#     {
#         'id':1,
#         'title': 'Data-Analyst',
#         'Location':'Delhi, India',
#         'Salary':'200000'

#     },

#     {
#         'id':2,
#         'title': 'Data-Scientist',
#         'Location':'Gurugram, India',
#         'Salary':'400000'

#     },

#     {
#         'id':3,
#         'title': 'Product-Manager',
#         'Location':'Silcher, India',
#         'Salary':'80000'

#     },
# ]

# @app.route('/')
# def hello_world():
#     return render_template('index.html', JOBS=jobs)

# @app.route('/jobs')
# def list_jobs():
#     return jsonify(jobs)


# if __name__ == "__main__":
#     app.run(debug=True, port=8000)


# ============================================================================

# from typing import Self
from flask import Flask, render_template, jsonify      # there is a class "flask" inside module 'flask'
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime 
# from sqlalchemy import text

from db import load_jobs_from_db


app = Flask(__name__)


@app.route('/')
def hello_world():
    jobs_dict = load_jobs_from_db()
    return render_template('index.html', JOBS=jobs_dict)

@app.route('/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    # app.run(debug=True, port=8000)
    app.run(host='0.0.0.0', debug=True)


