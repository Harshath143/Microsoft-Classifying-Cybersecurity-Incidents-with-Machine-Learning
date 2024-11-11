# main.py
from flask import Flask, request, jsonify
import pandas as pd
from model_loader import ModelLoader

# Initialize Flask app
app = Flask(__name__)

# Load the model using ModelLoader
model_loader = ModelLoader('C:\Projects\Microsoft-project\Adv_random_forest_model.pkl')

@app.route('/')
def home():
    return "Welcome to the Prediction API! Use the /predict endpoint to make predictions.", 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Print input data for debugging
        print("Received data:", data)

        # Convert input to DataFrame
        input_df = pd.DataFrame([data])

        # Debug input DataFrame shape and content
        print("Input DataFrame:", input_df)

        # Get prediction
        prediction = model_loader.predict(input_df)
        
        if prediction is not None:
            return jsonify({"prediction": prediction.tolist()}), 200
        else:
            return jsonify({"error": "Prediction failed"}), 500

    except Exception as e:
        print("Error during prediction:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
