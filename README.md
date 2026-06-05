# 🍷 Wine Quality Prediction App

A machine learning web app that predicts whether a red wine is **Good** or **Bad** quality based on its chemical properties. Built with **Streamlit** for the frontend and a trained **scikit-learn** model saved using `joblib`.

---

## 📁 Project Structure

```
new_project_wine/
│
├── app.py                    # Streamlit web app — prediction interface
├── wine_quality.ipynb        # Jupyter Notebook — data analysis, model training & evaluation
├── winequality-red.csv       # Dataset — red wine chemical properties & quality scores
└── wine_quality_model.pkl    # Trained ML model (generate by running the notebook)
```

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install streamlit numpy joblib scikit-learn pandas
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wine-quality-prediction.git
   cd wine-quality-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model first (generates `wine_quality_model.pkl`):
   - Open and run all cells in `wine_quality.ipynb`

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501`

---

## 🔍 How It Works

1. The dataset (`winequality-red.csv`) contains 11 chemical features and a quality score (0–10).
2. The notebook trains a classification model, converting quality scores into **Good (1)** or **Bad (0)** labels.
3. The trained model is saved as `wine_quality_model.pkl`.
4. The Streamlit app lets users input chemical properties and get an instant prediction.

---

## 🧪 Input Features

| Feature | Description |
|---|---|
| Fixed Acidity | Tartaric acid content |
| Volatile Acidity | Acetic acid — too high causes vinegar taste |
| Citric Acid | Adds freshness and flavor |
| Residual Sugar | Sugar remaining after fermentation |
| Chlorides | Salt content |
| Free Sulfur Dioxide | Prevents microbial growth |
| Total Sulfur Dioxide | Total SO₂ in wine |
| Density | Density of the wine |
| pH | Acidity level |
| Sulphates | Additive contributing to SO₂ |
| Alcohol | Alcohol percentage |

---

## 📊 Output

- 🍷 **Good Quality Wine** — predicted quality is high
- ⚠️ **Bad Quality Wine** — predicted quality is low

---

## 📝 Dataset

- Source: [UCI Machine Learning Repository — Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- 1,599 red wine samples with 11 chemical features

---

## 🙋 Author

**Jai Jadhav**
