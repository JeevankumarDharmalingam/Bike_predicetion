# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:03:55 2020

@author: Jeev
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Regressor.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Owner=int(request.form['Owner'])
        
        df = pd.DataFrame([[Year,Owner,Kms_Driven,Present_Price]],columns=['year','owner','km_driven','ex_showroom_price'])
        prediction=model.predict(df)
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Bike at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run()