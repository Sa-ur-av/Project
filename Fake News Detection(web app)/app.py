from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json

pipeline = joblib.load('./pipeline.sav')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


from flask import render_template

@app.route('/api', methods=['POST'])
def get_delay():
    result = request.form
    query_title = result['title']
    query_author = result['author']
    query_text = result['maintext']
    
    query = get_all_query(query_title, query_author, query_text)
    user_input = {'query': query}
    pred = pipeline.predict(query)
    prediction = 'Real' if pred[0] == 0 else 'Fake'

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
