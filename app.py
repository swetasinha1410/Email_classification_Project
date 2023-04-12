import pickle
from flask import Flask , render_template,request,url_for
import joblib



app=Flask(__name__)
model=joblib.load(open("email_classfier_V1.0.model",'rb'))




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def prediction():
    if request.method =='GET':
        return render_template('index.html')
    elif request.method =='POST':
        message=request.form['message']
        data = [message]
        my_prediction=model.predict(data)
        print(my_prediction)
        return render_template('index.html',prediction_text=my_prediction)
    else:
        return "This method is not allowed"

    
    
   # if request.method == 'POST':
        #message=request.form['message']
       # data=[message]
        #prediction =model.predict(data)
        #print(prediction)
        #return render_template('index.html',prediction_text=prediction)

    #if request.method =='GET':
        #return render_template('index.html',)
    
    #elif request.method =="POST":
     #   sms=request.form['sms']
      #  data=['sms']
       # prediction = model.predict(data)
        #return render_template('index.html',prediction_text=prediction)
    #else:
        # Handle other request methods
       # return 'This method is not allowed'    

        ##request data
        #data_email=request.form["email_text"]
        #data=[data_email]ac
       # prediction=model.prediction(data)
    #  Get the data from POST request.
    #data=request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    #prediction=model.prediction([[data['sms']]])
    #print(prediction)
    #return render_template('index.html',prediction_text=f'Mail Predicted as -.{prediction}')



if __name__=='__main__':
    app.run(debug=True)