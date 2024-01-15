
from pathlib import Path

from flask import Flask, render_template, jsonify      # there is a class "flask" inside module 'flask'
from db import load_jobs_from_db


app = Flask(__name__)


@app.route('/')
def hello_world():
    jobs_dict = load_jobs_from_db()
    return render_template('index.html', JOBS=jobs_dict)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    
    app.run(debug=True, port=8000)
    # app.run(host='0.0.0.0', debug=True)


