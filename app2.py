from flask import Flask, request, render_template
import pickle
import numpy as np
import helper

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    q1 = request.form['question1']
    q2 = request.form['question2']
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        prediction = 'Duplicate'
    else:
        prediction = 'Not Duplicate'

    return render_template('index.html', prediction=prediction, q1=q1, q2=q2)


if __name__ == '__main__':
    app.run(debug=True)
