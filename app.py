from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


app = Flask("Telecom Customer Churn Prediction")
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    if (output == 0):
        textOut = " Dos!"
    if (output == 1):
        textOut = " Normal!"
    if (output == 2):
        textOut = " Probe!"
    if (output == 3):
        textOut = " R2l!"
    if (output == 4):
        textOut = " U2r!"

    return render_template("index.html", prediction_text= "The Detected Network Intrusion is : {}".format(textOut))


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
	app.run(debug=True)