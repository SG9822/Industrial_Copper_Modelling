# Industrial_Copper_Modelling
To predict the Status and price of the copper

# Industrial Copper Modeling

## Introduction

Enhance your proficiency in data analysis and machine learning with our "Industrial Copper Modeling" project. In the copper industry, dealing with complex sales and pricing data can be challenging. Our solution employs advanced machine learning techniques to address these challenges, offering regression models for precise pricing predictions and lead classification for better customer targeting. You'll also gain experience in data preprocessing, feature engineering, and web application development using Streamlit, equipping you to solve real-world problems in manufacturing.

## Table of Contents

- [Key Technologies and Skills](#key-technologies-and-skills)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Key Technologies and Skills

- Python
- Numpy
- Pandas
- Scikit-Learn
- XGBoost
- Matplotlib
- Seaborn
- Pickle
- Streamlit

## Installation

To run this project, you need to install the following packages:

pip install -r requirements.txt

## Usage

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/gopiashokan/Industrial-Copper-Modeling.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`
4. Access the app in your browser at [http://localhost:8501](http://localhost:8501)

## Features

### Data Preprocessing:

- **Data Understanding**: Identify variable types and distributions, handle unwanted values.
- **Handling Null Values**: Address missing values using appropriate imputation methods.
- **Encoding and Data Type Conversion**: Prepare categorical features for modeling.
- **Skewness - Feature Scaling**: Address skewness in continuous variables using transformations.
- **Outliers Handling**: Detect and handle outliers using the Interquartile Range (IQR) method.
- **Wrong Date Handling**: Resolve discrepancies in dates to maintain data integrity.

### Exploratory Data Analysis (EDA) and Feature Engineering:

- **Skewness Visualization**: Visualize and correct skewness in continuous variables.
- **Outlier Visualization**: Identify and rectify outliers using Seaborn's Boxplot.
- **Feature Improvement**: Create new features to gain deeper insights and improve dataset efficiency.

### Classification:

- **Success and Failure Classification**: Define and classify leads as 'Won' or 'Lost'.
- **Handling Data Imbalance**: Implement oversampling methods to address data imbalance.
- **Algorithm Assessment**: Evaluate various algorithms and select the most suitable one.
- **Algorithm Selection**: Choose the Random Forest Classifier for robust performance.
- **Hyperparameter Tuning with GridSearchCV and Cross-Validation**: To fine-tune our model and mitigate overfitting, we employ GridSearchCV with cross-validation for hyperparameter tuning.
  This function allows us to systematically explore multiple parameter values and return the optimal set of parameters. {'max_depth': 20, 'max_features': 'sqrt', 'min_samples_leaf': 1, 'min_samples_split': 2}
- **Model Accuracy and Metrics**: With the optimized parameters, our Random Forest Classifier achieves an impressive 96% accuracy, ensuring robust predictions for unseen data. To further evaluate our model, we leverage key metrics such as the confusion matrix, precision, recall, F1-score, AUC, and ROC curve, providing a comprehensive view of its performance.
- **Model Persistence**: We conclude this phase by saving our well-trained model to a pickle file. This enables us to effortlessly load the model and make predictions on the status whenever needed, streamlining future applications.

### Regression:

- **Algorithm Assessment**: Evaluate various algorithms and select the most suitable one.
- **Algorithm Selection**: After thorough evaluation, two contenders, the Extra Trees Regressor and Random Forest Regressor, demonstrate commendable testing accuracy. Upon checking for any overfitting issues in both training and testing, both models exhibit strong performance without overfitting concerns. I choose the Random Forest Regressor for its ability to strike a balance between interpretability and accuracy, ensuring robust performance on unseen data.
- **Hyperparameter Tuning with GridSearchCV and Cross-Validation**: To fine-tune our model and mitigate overfitting, we employ GridSearchCV with cross-validation for hyperparameter tuning. This function allows us to systematically explore multiple parameter values and return the optimal set of parameters. {'max_depth': 20, 'max_features': None, 'min_samples_leaf': 1, 'min_samples_split': 2}.
- **Model Accuracy and Metrics**:  With the optimized parameters, our Random Forest Regressor achieves an impressive 95.6% accuracy. This level of accuracy ensures robust predictions for unseen data. We further evaluate our model using essential metrics such as mean absolute error, mean squared error, root mean squared error, and the coefficient of determination (R-squared). These metrics provide a comprehensive assessment of our model's performance.

## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or feedback, please contact [Shanmugagouthaman] at [shanmugagouthaman46@gmail.com].


