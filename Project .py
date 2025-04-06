from flask import Flask,render_template,request
import pandas as pd
import numpy as np 
import pickle
app=Flask(__name__)
car=pd.read_csv('CarPriceCSV.csv')
model_path = r"C:\Users\praja\Desktop\RKP\Python\PROJECT\CCC\CarPricePredictor2.pkl"



with open("DATA.pkl","rb") as file:
    model_pkl=pickle.load(file)
  





@app.route('/')
def index():
    companies=sorted(car['company'].unique())
    car_model=sorted(car['name'].unique())
    year=sorted(car['year'].unique())
    fuel_type=car['fuel_type'].unique()
    return render_template('index.html', companies=companies, car_model=car_model, year=year, fuel_type=fuel_type)

@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get('car_model')
    year_str = request.form.get('year')
    if not year_str or not year_str.isdigit():
      return "Error: Year is missing or invalid", 400  # HTTP 400: Bad Request
    year = int(year_str)
    fuel_type=request.form.get('fuel_type')\
    
    kilo_driven=int(request.form.get('Km_driven'))
    df = pd.DataFrame([[car_model, company, year, kilo_driven, fuel_type]],
                  columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    prediction = model_pkl.predict(df)

  

    return str(prediction.astype(np.int16))
if __name__=="__main__": 
    app.run(debug=True)



