**Problem Statement**

Customer churn poses a significant challenge to subscription-based and service-oriented businesses.
Understanding the factors that influence customer retention and proactively predicting churn can save businesses revenue.
The goal of this project is to predict customer churn based on service usage patterns, contract, and account information.

**Objectives and Goals**

Integrate predictive churn models into customer relationship management (CRM) tools.
Enable early intervention strategies such as offering personalized promotions or support to at-risk customers.
Support business decision-making with data-driven insights to improve customer loyalty and satisfaction.

**Project Overview**

This project aims to predict whether a customer is likely to leave a service based on historical data and behavioral patterns.
The dataset undergoes comprehensive preprocessing and cleaning, followed by in-depth exploratory data analysis (EDA).
Feature engineering and selection steps are applied before training multiple classification models.
THe final model tested uisng hypothesis to validate assumptions influencing churn in the business.

**Insights**

- Data Processing: Handled missing values, removed redundant data, and converted categorical features to numerical format using encoding.
- EDA & Feature Engineering: Identified key drivers of churn such as contract type, monthly charges, and tenure.
                             Visualized feature correlations, churn distribution, and customer behavior trends.
- Handling Class Imbalance: Applied oversampling techniques like SMOTE to ensure balanced class representation.
- Model Training & Tuning: Evaluated multiple classifiers (Decision Tree, Random Forest and XgBoost),
                           with Random Forest delivering the best performance after achieving accuracy of 85%.
- Evaluation Metrics: Used accuracy, precision, recall, F1-score, and confusion matrix for evaluation.
- Hypothesis testing: Hypothesis testing was conducted to validate assumptions about the factors influencing churn
                      whether the retention strategy significantly reduces the churn or not.
- Deployment: Streamlined which enables business stakeholders or non-technical users to interact with the model effortlessly.


**Outcome**

- Built a robust churn prediction model with strong performance (e.g., accuracy 85%).
- Demonstrated the role of machine learning in customer analytics and business intelligence.
- This project demonstrates how predictive analytics and machine learning can enhance customer
  retention strategies and contribute to data-driven business growth.

**Tech Stack**

This project is developed using:
- Streamlit – For building an interactive web app UI
- Pandas, NumPy – For data manipulation and preprocessing
- Matplotlib, Seaborn – For data visualization
- Scikit-learn – For model building, evaluation, and tuning
- Joblib – For model serialization



