from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load model using pickle
model_path = "HR_Analytics_predictor.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Define keys for input order
        feature_keys = [
            'actual_salary', 'promotion_last_5years', 'satisfaction_level',
            'last_evaluation', 'number_project', 'average_montly_hours',
            'time_spend_company', 'work_accident', 'salary_category',
            'gender_male', 'department_randd', 'department_accounting',
            'department_hr', 'department_management', 'department_marketing',
            'department_product_mng', 'department_sales', 'department_support',
            'department_technical'
        ]

        # Extract and format input
        features = [float(request.form[key]) for key in feature_keys]
        final_input = np.array(features).reshape(1, -1)

        # Predict
        prediction = model.predict(final_input)
        result = 'Will Leave' if prediction[0] == 1 else 'Will Stay'

        return render_template('index.html', prediction_text=f'Employee {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
