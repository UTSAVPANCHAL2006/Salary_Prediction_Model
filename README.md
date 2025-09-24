# 💼 Salary Prediction Model 

A machine learning project that predicts salaries based on employee attributes using multiple regression algorithms. The project includes an **interactive Streamlit web app** for real-time predictions.  

## ✨ Key Features  
- Predict salaries using different ML models:  
  - Linear Regression  
  - Decision Tree  
  - Random Forest  
  - Gradient Boosting  
- Interactive **Streamlit app** for live salary prediction  
- Data visualization for insights and feature analysis  
- Model saving & loading with **joblib**  

---
## 🛠️ Tech Stack  
- **Language**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Joblib, Streamlit  

---

## 📂 Project Structure 
Salary_Prediction_Model/
│

|── data/ #Dataset(s)

|── src/ # Source code for preprocessing & modeling

|── app.py # Streamlit app entry point

|── requirements.txt # Project dependencies

|── README.md # Project documentation

## ⚙️ Installation  

 
```bash
1)Clone the repository:
git clone https://github.com/UTSAVPANCHAL2006/Salary_Prediction_Model.git
cd Salary_Prediction_Model


2)Install dependencies:
pip install -r requirements.txt

3)Run the Streamlit App
streamlit run app.py
```

📊 Dataset & Preprocessing

Dataset is stored in the data/ folder

Includes cleaning, encoding categorical variables, and scaling features

Ensure dataset is available before training/running the app

🧠 Model Training

Models implemented: Linear Regression, Decision Tree, Random Forest, Gradient Boosting

Performance evaluated using metrics such as MSE ,MAE, RMSE, R²

🌐 Deployment

The app is deployed with Streamlit Cloud:

👇🏻 Live Demo

https://salarypredictionmodel-6um3ueg7f4htl2txfwcm9f.streamlit.app/
