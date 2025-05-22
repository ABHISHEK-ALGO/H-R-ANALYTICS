from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
filename = "hr_anna_predictor.pkl"  # Ensure the model is in the same directory
with open(filename, "rb") as model_file:
    loaded_model = pickle.load(model_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        actual_salary = float(request.form["actual_salary"])
        promotion_last_5years = int(request.form["promotion_last_5years"])
        satisfaction_level = float(request.form["satisfaction_level"])
        last_evaluation = float(request.form["last_evaluation"])
        number_project = int(request.form["number_project"])
        average_montly_hours = int(request.form["average_montly_hours"])
        time_spend_company = int(request.form["time_spend_company"])
        Work_accident = int(request.form["Work_accident"])

        gender = request.form["gender"]
        salary_level = request.form["salary_level"]
        department = request.form["department"]

        # One-Hot Encoding for categorical features
        genders = ["Female", "Male"]
        salaries = ["high", "low", "medium"]
        departments = ["IT", "RandD", "accounting", "hr", "management",
                       "marketing", "product_mng", "sales", "support", "technical"]

        gender_encoded = [1 if gender == g else 0 for g in genders]
        salary_encoded = [1 if salary_level == s else 0 for s in salaries]
        department_encoded = [1 if department == d else 0 for d in departments]

        # Combine into final input (23 features)
        input_data = np.array([[actual_salary, promotion_last_5years, satisfaction_level,
                                last_evaluation, number_project, average_montly_hours,
                                time_spend_company, Work_accident] +
                                gender_encoded + salary_encoded + department_encoded])

        # Make Prediction
        prediction = loaded_model.predict(input_data)[0]
        prediction_prob = loaded_model.predict_proba(input_data)[:, 1][0]  # Probability of leaving

        result_text = "🔴 Likely to Leave" if prediction == 1 else "🟢 Likely to Stay"
        probability_text = f"Probability of Leaving: {prediction_prob:.2f}"

        return render_template("index.html", prediction=result_text, probability=probability_text)

    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
