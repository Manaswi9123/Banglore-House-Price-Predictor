from flask import Flask, render_template,request
import  pandas as pd
import numpy as np
import sklearn
import pickle

app=Flask(__name__)
df=pd.read_csv('cleaned_data.csv')
pipe=pickle.load(open('ridgeModel.pkl','rb'))
@app.route('/')
def index():
    locations=sorted(df['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict',methods=['POST'])
def predict():
    location=request.form.get('location')
    bhk=float(request.form.get('bhk'))
    bath=float(request.form.get('bath'))
    sft=float(request.form.get('total_sft'))
    print(location,bhk,bath,sft)
    input=pd.DataFrame([[location,sft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction=(pipe.predict(input)[0] )* 1e5
    return str(np.round(prediction,2))

if __name__=='__main__':
    app.run(debug=True,port=5001)