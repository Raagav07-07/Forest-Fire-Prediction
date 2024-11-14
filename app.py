from flask import Flask, request, render_template
import pickle
import numpy as np
from twilio.rest import Client

app = Flask(__name__)

# Load the model
with open('svc.pkl', 'rb') as f:
    model = pickle.load(f)

TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_PHONE_NUMBER = ''
TO_PHONE_NUMBER = ''

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    message=""
    if request.method == 'POST':
        # Get form data
        temp = float(request.form['temp'])
        ws = float(request.form['ws'])
        ffmc = float(request.form['ffmc'])
        isi = float(request.form['isi'])
        bui=float(request.form['bui'])
        fwi=float(request.form['fwi'])
        features = np.array([[temp,ws,ffmc,isi,bui,fwi]])
        prediction = model.predict(features)[0]
        prob=model.best_estimator_.predict_proba(features)[0]
        nofi = ((prob[0]) * 100).astype(int) 
        fi = ((prob[1]) * 100).astype(int)    
        if prediction == 1:
            message = f"There is a {fi}% chance of fire. Immediate action is required to prevent a forest fire."
        else:
            message = f"The forest is currently safe with a {nofi}% chance of no fire. Monitoring is recommended to ensure ongoing safety."
        print(message)


        '''client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )'''

    return render_template('index.html', prediction=prediction,message=message)

if __name__ == '__main__':
    app.run(debug=True)
