# model_loader.py
import pickle
import pandas as pd

class ModelLoader:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        try:
            with open(self.model_path, 'rb') as file:
                model = pickle.load(file)
            print("Model loaded successfully.")
            return model
        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def predict(self, input_data):
        if self.model:
            try:
                # Ensure input_data is in the correct format for prediction
                if not isinstance(input_data, pd.DataFrame):
                    input_df = pd.DataFrame(input_data)
                else:
                    input_df = input_data

                print("Input data shape:", input_df.shape)

                # Call the model's predict method
                prediction = self.model.predict(input_df)
                return prediction
            except Exception as e:
                print(f"Prediction error: {e}")
                return None
        else:
            print("Model not loaded.")
            return None
