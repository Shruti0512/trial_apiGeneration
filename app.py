# from flask import Flask,request,jsonify

# app= Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello World"

# #ab hum api create krne ke liye pehle api ko path denge run krane ke liye , and api works on two type of methods get and post
# @app.route('/predict',methods=['POST'])
# def predict():
#     #user abhi hume 3 input dega cgpa,iq,result
#     cgpa=request.form.get('cgpa')
#     iq=request.form.get('iq')
#     profile_score=request.form.get('profile_score')

#     #dictionarry
#     result={'cgpa':cgpa,'iq':iq,'profile_score':profile_score}

#     #function ko json me convert krna pdega py h isiliye to jsonify ke object me bhejna pdega
#     ##postman
#     #create collection->POST->paste url->provide path after url "http://--:5000/predict" and provide key and value as per the code dictionary and send

#     return jsonify(result)




# if __name__=='__main__':
#     #run file it will give url on our local machine and now we have to convert this model into api and test on postman
#     app.run(debug=True)

from flask import Flask,request,jsonify
import numpy as np
# now making prediction through model
import pickle
model=pickle.load(open('model.pkl','rb'))


app= Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

#ab hum api create krne ke liye pehle api ko path denge run krane ke liye , and api works on two type of methods get and post
@app.route('/predict',methods=['POST'])
def predict():
    #user abhi hume 3 input dega cgpa,iq,result
    cgpa=request.form.get('cgpa')
    iq=request.form.get('iq')
    profile_score=request.form.get('profile_score')

    input_query=np.array([[cgpa,iq,profile_score]]) 

# 0 index pr uska result hoga
    result=model.predict(input_query)[0]

# always return a dictionary
    return jsonify({'placement':str(result)})




if __name__=='__main__':
    #run file it will give url on our local machine and now we have to convert this model into api and test on postman
    app.run(debug=True)

## here is a one problem that this url/api is on our local machine and android studio will not identify it
## so make it universal deploy on heroku