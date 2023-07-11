from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Fuel_Type = request.form['Fuel_Type']
        Seller_Type = request.form['Seller_Type']
        Transmission = request.form['Transmission']
        Owner = int(request.form['Owner'])
        age_of_the_car = request.form['age_of_the_car']
        prediction = model.predict([[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, age_of_the_car]])
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text="You can sell your car at {} lakhs".format(output))

if __name__ == "__main__":
    app.run(debug=True)
