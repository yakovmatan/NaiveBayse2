
# Naive Bayes Classification Project

This Python project implements a complete Naive Bayes classification system, including data loading, preprocessing, model training, evaluation, REST APIs, and interactive Streamlit apps for prediction and visualization.

---

## 📦 Project Structure

```
.
|--└── data/
    └── buy_computer_data.csv  
├── the_model/
│   ├── data_loader.py          # Load CSV, Excel, JSON data files
│   ├── cleaner.py              # Data cleaning (currently a placeholder)
│   ├── builder.py              # Naive Bayes model implementation with smoothing
│   ├── split_data.py           # Train/test split function
│   └── valitator.py            # Model evaluation: accuracy, confusion matrix
├── manager.py                  # Workflow manager: data → clean → split → train → eval
├── main.py                     # Main API (port 8000) exposing model stats
├── classifeir/
│   ├── prediction.py           # Predict single samples
│   └── info_model.py           # Load trained model info for prediction API
├── main_prediction.py          # Prediction API (port 8001)
├── app_streamlit.py            # Streamlit app for interactive prediction UI
├── dashboard_streamlit.py      # Streamlit dashboard for model evaluation visualization
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Dockerfile for main API
├── Dockerfile_prediction       # Dockerfile for prediction API
 # Sample dataset
```

---

## ✨ Features

- Load datasets in CSV, Excel, or JSON formats  
- Basic data cleaning placeholder for future enhancements  
- Split datasets into training and testing sets  
- Train a Naive Bayes classifier with Laplace smoothing  
- Evaluate model performance: accuracy and confusion matrix  
- RESTful APIs exposing model stats and prediction endpoints  
- Two separate APIs: one for stats (port 8000) and one for prediction (port 8001)  
- Interactive Streamlit apps for easy prediction and visual evaluation  
- Docker support for containerized deployment  

---

## 🛠️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the main API (statistics & model info)

```bash
docker build -t naive-bayes-api -f Dockerfile .
docker run -p 8000:8000 naive-bayes-api
```

The API will be available at: `http://localhost:8000`

### 3. Run the prediction API

```bash
docker build -t naive-bayes-prediction -f Dockerfile_prediction .
docker run -p 8001:8001 naive-bayes-prediction
```

The API will be available at: `http://localhost:8001`

### 4. Run the Streamlit app for prediction UI

```bash
streamlit run app_streamlit.py
```

### 5. Run the Streamlit dashboard for model evaluation

```bash
streamlit run dashboard_streamlit.py
```

---

## 📚 How It Works

1. Load data using `DataLoader`.  
2. Clean data using `Cleaner` (currently no changes, designed for future).  
3. Split data into train/test sets with `split_dataframe`.  
4. Train the Naive Bayes model (`NaiveBayes.fit()`).  
5. Evaluate the model using `Evaluation` class (accuracy, confusion matrix).  
6. Use `NaiveBayesManager` to orchestrate all these steps and serve data via API.  
7. Use main API to get model statistics and metadata.  
8. Use prediction API for single-sample prediction requests.  
9. Streamlit apps consume these APIs for interactive usage.

---

## ⚠️ Notes

- There is a minor typo in the code: `get_confusion_metrix` should be `get_confusion_matrix`.  
- Enhance `Cleaner` to perform real data preprocessing.  
- Run both APIs simultaneously to enable full Streamlit functionality.  
- Update API URLs and ports in the Streamlit apps as needed.

---

## 📦 Dependencies

- pandas  
- scikit-learn  
- fastapi  
- uvicorn  
- requests  
- streamlit  
- seaborn  
- matplotlib  

---

## 📝 Author

Yakov Matan  
GitHub: [https://github.com/yakovmatan](https://github.com/yakovmatan)

---

## 📜 License

This project is provided for educational purposes. Feel free to use, modify, or extend it.

---

If you have any questions or need further assistance, feel free to ask!
