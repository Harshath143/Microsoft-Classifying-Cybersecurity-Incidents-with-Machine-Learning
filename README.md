# Microsoft-Classifying-Cybersecurity-Incidents-with-Machine-Learning

## Project Overview
This project utilizes machine learning to classify cybersecurity incidents, aiming to improve the efficiency of Security Operation Centers (SOCs). The model is trained to categorize incidents into triage grades: True Positive (TP), Benign Positive (BP), and False Positive (FP). By accurately classifying incidents, the model enables SOC teams to prioritize responses, reducing the time spent on low-priority issues.

## Business Use Cases
- **SOCs**: Improves response prioritization, allowing analysts to focus on critical threats.
- **Incident Response Automation**: Suggests appropriate actions for different types of incidents.
- **Threat Intelligence**: Enhances threat detection by incorporating historical data.
- **Enterprise Security Management**: Reduces false positives and ensures timely response to true threats.

## Skills Developed
- Data Preprocessing and Feature Engineering
- Machine Learning Classification Techniques
- Model Evaluation Metrics (Macro-F1 Score, Precision, Recall)
- Cybersecurity Frameworks (MITRE ATT&CK)
- Handling Imbalanced Datasets

## Project Workflow

### 1. Data Exploration
Conducted an initial inspection of the dataset to understand features, distributions, and target classes.

### 2. Data Preprocessing
- **Handling Missing Data**: Addressed missing values by imputation and transformation.
- **Feature Engineering**: Created new features from existing ones and encoded categorical variables.

### 3. Data Splitting
Split the dataset into training and validation sets using stratified sampling to ensure balanced class distributions.

### 4. Model Selection
The Random Forest model was selected for its robustness and interpretability. Baseline models like Logistic Regression and Decision Trees,... were used for comparison.

### 5. Model Evaluation
The model was evaluated using metrics like macro-F1 score, precision, and recall to ensure balanced performance across classes.

### 6. Final Testing
After tuning, the model was evaluated on the test set to assess its generalizability and final performance.

### 7. Documentation
The entire process was documented, covering data handling, modeling, evaluation, and recommendations for future improvements.

## Project Directory Structure
```plaintext
Classifying-Cybersecurity-Incidents/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── newtrain.csv
├── notebooks/
│   └── eda_notebook.ipynb
├── models/
│   └── best_rf_model.pkl
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── utils.py
├── README.md
└── requirements.txt
