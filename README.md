# Wine Quality Predictor 🍷

A web-based application that predicts the **quality of wine** based on its physicochemical properties using a **K-Nearest Neighbors (KNN) model**. Users can input feature values through a **Streamlit interface** and get real-time predictions.

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
git clone <your-repo-link>
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
https://wine-quality-knn-ew7faibofaezjhcv4egrrb.streamlit.app/
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

*(Optional: add screenshots of the Streamlit app for visual preview)*

---

## Future Improvements

* Experiment with other models like **Random Forest or XGBoost** for higher accuracy.
* Add **multi-wine type support** (red/white) for more detailed predictions.
* Deploy the app online using **Streamlit Cloud or Heroku**.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

