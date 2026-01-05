# 🔌 AI-Powered Energy Consumption Optimization System

A production-style AI system that **predicts energy consumption, evaluates efficiency, and generates actionable optimization recommendations** to reduce energy waste.

## 🌍 Live Demo

👉 **Try it here:**
[https://pranav25187-ai-energy-optimization-system-appapp-ecpstl.streamlit.app/](https://pranav25187-ai-energy-optimization-system-appapp-ecpstl.streamlit.app/)


---

<img width="1919" height="922" alt="Screenshot 2026-01-05 225347" src="https://github.com/user-attachments/assets/fef59649-7e53-4a11-ac11-a70c01eb5ebb" />


## 📌 Problem Statement

Residential and commercial buildings typically waste **15–30% of energy** due to:
- Poor load scheduling
- Inefficient appliance usage
- High reactive power losses

Most solutions only **predict energy usage**.  
This project goes further by **optimizing energy consumption with explainable recommendations**.

---

## 🎯 What This System Does

✔ Predicts **next-hour energy consumption**  
✔ Calculates a custom **Energy Efficiency Score (0–100)**  
✔ Detects inefficiencies such as peak-hour overuse and reactive power waste  
✔ Generates **human-readable optimization recommendations**  
✔ Estimates **realistic energy savings (%)**

---

## 🧠 System Architecture

```

Raw Energy Logs (.txt)
↓
Data Cleaning & Feature Engineering
↓
ML Model (Random Forest Regression)
↓
Efficiency Scoring
↓
Rule-Based Optimization Engine
↓
Streamlit Dashboard (Decision Support)

```

---

## 🛠️ Tech Stack (100% Free)

- **Python**
- **Pandas, NumPy** – data processing
- **Scikit-learn** – ML modeling
- **Random Forest Regressor** – energy prediction
- **Streamlit** – interactive dashboard
- **Joblib** – model serialization

No paid APIs. No cloud credits. Fully free.

---

## 📂 Project Structure

```

ai-energy-optimization-system/
│
├── data/
│   ├── raw/            # Original energy dataset (.txt)
│   └── processed/      # Cleaned & feature-engineered data
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│
├── src/
│   ├── **init**.py
│   └── optimizer.py    # Optimization & recommendation logic
│
├── app/
│   └── app.py          # Streamlit dashboard
│
├── models/
│   └── energy_model.pkl
│
├── requirements.txt
└── README.md

````

---

## 📊 Dataset

- **Source:** UCI Machine Learning Repository  
- **Type:** Smart meter household energy logs  
- **Format:** Raw `.txt` file (semicolon separated)  
- **Features include:**
  - Global active power
  - Global reactive power
  - Voltage & intensity
  - Appliance-level sub-metering (kitchen, laundry, HVAC)

This dataset reflects **real-world smart meter data**, not curated CSV files.

---

## 🤖 Machine Learning Approach

- **Task:** Time-aware regression (next-hour energy prediction)
- **Model Used:** Random Forest Regressor
- **Why Random Forest?**
  - Handles non-linear energy patterns
  - Robust to noisy sensor data
  - Requires minimal tuning
  - Stable for production use

### Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## ⚙️ Optimization Logic (Key Differentiator)

Instead of using ML for recommendations, the system uses **explainable rule-based logic**:

- Peak-hour load shifting detection
- Reactive power inefficiency detection
- Appliance-level optimization (laundry, HVAC)
- Overall efficiency assessment

📌 This mirrors how **real energy management systems** operate.

---

## 📈 Example Output

- **Predicted Consumption:** 5.3 kW  
- **Efficiency Score:** 58 / 100  
- **Estimated Savings:** 22%  

**Recommendations:**
- Shift heavy appliance usage to off-peak hours  
- Optimize HVAC usage and thermostat settings  

---

## ▶️ How to Run Locally

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app/app.py
````

---


---

## 📌 Why This Project Stands Out

* Uses **raw energy logs**, not cleaned Kaggle CSVs
* Separates **prediction** and **optimization**
* Fully explainable (no black-box recommendations)
* Realistic savings estimates (no fake claims)
* Industry-style project structure

---

## 🎯 Future Improvements

* Real-time IoT sensor integration
* User-specific appliance profiling
* Historical optimization tracking
* Multi-building energy comparison

---

## 🧑‍💻 Author

**Pranav**
Final Year Computer Engineering Student
Focused on building **industry-grade, explainable AI systems**

---

⭐ If you found this project useful, feel free to star the repository!
