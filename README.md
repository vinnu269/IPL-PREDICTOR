# 🏏 IPL Win Probability Predictor  

This project implements an IPL (Indian Premier League) win probability predictor using a 
machine learning model. The application is built with Streamlit, providing an interactive 
user interface to predict the winning chances of batting and bowling teams during a live 
match.  

---

# ✨ Features  

- Predicts win probability for both batting and bowling teams.  
- User-friendly interface built with Streamlit.  
- Takes into account various match parameters: batting team, bowling team, host city, 
  target score, current score, overs completed, and wickets fallen.  
- Utilizes a pre-trained machine learning model for predictions.  

---

# 📂 Project Structure  

- app.py : The main Streamlit application file.  
- model.pkl : The trained machine learning model (likely a scikit-learn pipeline or similar).  
- pipe.pkl : A pipeline object, possibly containing pre-processing steps and the model.  
- team.pkl : A pickled list of IPL teams.  
- city.pkl : A pickled list of host cities.  
- requirements.txt : Lists all the Python dependencies required to run the application.  
- IPL_Win_Prob.ipynb : Jupyter Notebook for model training and analysis.  
- Practice.ipynb : Another Jupyter Notebook, possibly for practice or experimentation.  
- Data/ : Directory containing the dataset used for training the model.  
- render.yaml : Configuration file for deployment on Render (if applicable).  

---

# ⚙ Installation and Setup  

To run this application locally, follow these steps:  

1. Clone the repository  
2. Create a virtual environment (recommended)  
3. Install the required dependencies  
4. Run the Streamlit application  

---

# ▶ Usage  

Once the application is running, you can:  

1. Select the batting and bowling teams from the dropdown menus.  
2. Choose the host city.  
3. Enter the target score for the chasing team.  
4. Input the current score, overs completed, and wickets fallen.  
5. Click the *"Predict Probability"* button to see the win probabilities for both teams.  

---

# 🧠 Model Training  

The machine learning model was trained using historical IPL match data. The 
IPL_Win_Prob.ipynb notebook contains the code for data preprocessing, feature engineering, 
model selection, training, and evaluation.  

---

# 📦 Dependencies  

The project relies on the following Python libraries:  

- streamlit  
- pandas  
- numpy  
- scikit-learn  
- flask (potentially for other parts of the project or if deployed as a web service)  
- gunicorn (for production deployment of Flask apps)  

---

# 🤝 Contributing  

Contributions are welcome! Please feel free to open issues or submit pull requests.  

---
# *📬 Contact*

💡 For questions, suggestions, or collaborations, reach out:

- GitHub: https://github.com/vinnu269

- Email: vishnumangina543@gmail.com
