from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('savemodel.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    pregnancies = request.form['pregnancies']
    glucose	 = request.form['glucose']
    bp = request.form['bp']
    skinthickness = request.form['skinthickness']
    insulin= request.form['insulin']
    bmi= float(request.form['bmi'])
    dpf=float(request.form['dpf'])
    age=request.form['age']
    result = int(model.predict([[pregnancies, glucose,bp, skinthickness,insulin,bmi,dpf,age]]))
    if result==1:
        r='The Person Have Diabetes'
    else:
        r='The Person Does Not Have Diabetes'
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)