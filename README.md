# Wine Quality Predictor 🍷

A web-based application that predicts the **quality of wine** based on its physicochemical properties using a **K-Nearest Neighbors (KNN) model**. Users can input feature values through a **Streamlit interface** and get real-time predictions.

---
## 🔗 Live Demo

https://wine-quality-knn-ew7faibofaezjhcv4egrrb.streamlit.app/

---
## Features

* Predict wine quality based on user-defined chemical features.
* Interactive sidebar to adjust input features and see predictions instantly.
* Standardizes input data for accurate predictions using **scikit-learn’s StandardScaler**.
* Demonstrates practical use of **KNN classification** for regression-like prediction.

---

## Tech Stack

* **Python 3**
* **scikit-learn** – KNN model, preprocessing, and train-test split
* **Pandas** – Dataset manipulation
* **Streamlit** – Interactive web interface

---

## Dataset

The project uses the `WineQT.csv` dataset containing physicochemical properties of wine and corresponding quality scores.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/pyscar/wine-quality-knn.git
cd <your-repo-folder>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure `WineQT.csv` is in the project directory.

---

## Usage

1. Run the Streamlit app:

```bash
streamlit run wine_knn_app.py
```

2. Open the link provided by Streamlit in your browser.

3. Use the **sidebar sliders** to adjust wine features (e.g., acidity, sugar, pH).

4. View the predicted wine quality in real-time under the **Prediction** section.

---

## Model

* **Algorithm:** K-Nearest Neighbors (KNN)
* **K:** 5 neighbors
* **Preprocessing:** Features standardized using StandardScaler
* **Train/Test Split:** 80/20

---

## Screenshots
<img width="1848" height="896" alt="image" src="https://github.com/user-attachments/assets/57615001-c6fd-4e5d-b75a-62a39e0a64ed" />

<img width="1917" height="967" alt="image" src="https://github.com/user-attachments/assets/58ee7898-0ebf-4b8f-b006-5c95efb5d250" />

* Distribution of wine quality
  <img width="1013" height="597" alt="image" src="https://github.com/user-attachments/assets/a64a6b31-4c17-4532-8d34-e2a0a16532b1" />
* Histogram of all features
  <img width="1413" height="665" alt="image" src="https://github.com/user-attachments/assets/97b0640d-f57c-4161-991d-b3252a2c3e87" />
* Confusion Matrix
  <img width="993" height="827" alt="image" src="https://github.com/user-attachments/assets/492b7a43-5ae4-4557-9d3f-a66bcf858788" />
* Scatter plot
  <img width="732" height="480" alt="image" src="https://github.com/user-attachments/assets/cf7d0bd8-19b4-4c71-af44-285da0fd27f1" />
* Normal distribution
  <img width="631" height="441" alt="image" src="https://github.com/user-attachments/assets/de5da221-84f4-40fb-b3a0-4b624a4da7c1" />
* Acid base quality
  <img width="681" height="496" alt="image" src="https://github.com/user-attachments/assets/9b4f1617-1e7c-404b-b484-08ef14cfea78" />
---

## Future Improvements

* Experiment with other models like **Random Forest or XGBoost** for higher accuracy.
* Add **multi-wine type support** (red/white) for more detailed predictions.
* Deploy the app online using **Streamlit Cloud or Heroku**.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

