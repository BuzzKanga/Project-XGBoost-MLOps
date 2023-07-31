# pip install --upgrade xgboost

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import mlflow
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# from xgboost import XGBClassifier
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from hyperopt.pyll import scope
from prefect import flow, task


# warnings.filterwarnings("ignore")

@task(retries=3, retry_delay_seconds=2)
def read_data(filename):
    """Read data into DataFrame"""
    df = pd.read_csv(filename)
    return df

@task
def prep_data(churn):
    churn = churn.drop("Phone", axis=1)
    churn["Area Code"] = churn["Area Code"].astype(object)
    churn = churn.drop(["Day Charge", "Eve Charge", "Night Charge", "Intl Charge"], axis=1)
    
    X, y = churn.drop('Churn?', axis=1), churn[['Churn?']]

    cats = X.select_dtypes(exclude=np.number).columns.tolist()

    # Convert to Pandas category
    for col in cats:
        X[col] = X[col].astype('category')

    y['Churn?'] = y['Churn?'].replace({'True.': 1, 'False.': 0})
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    dtrain = xgb.DMatrix(X_train, label=y_train, enable_categorical=True)
    dtest = xgb.DMatrix(X_test, label=y_test, enable_categorical=True)

    return dtrain, dtest, y_test
    

# def train_model():
#     model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss',tree_method="hist",enable_categorical=True)
#     model.fit(X_train, y_train)

#     return model

# def pred_model():
#     y_pred = model.predict(X_test)

#     accuracy = accuracy_score(y_test, y_pred)
#     accuracy

#     return model

@task(log_prints=True)
def train_xgb_model(dtrain, dtest):

    with mlflow.start_run():

        best_params = {
            'learning_rate'	: 0.2611886716276454,
            'max_depth' : 39,
            'min_child_weight' : 4.490391995734931,
            'objective' : 'binary:logistic',
            'reg_alpha' : 0.044567672488398144,
            'reg_lambda' : 0.11968534468462336,
            'seed' : 42
        }

        mlflow.log_params(best_params)

        booster = xgb.train(
            params=best_params,
            dtrain=dtrain,
            num_boost_round=1000,
            evals=[(dtest,"test")],
            early_stopping_rounds=50
        )      

    return booster

@task
def pred_xgb_model(booster, dtest, y_test):

    with mlflow.start_run():

        y_pred_prob = booster.predict(dtest)
        y_pred = (y_pred_prob >= 0.5).astype(int)
        accuracy = accuracy_score(y_test, y_pred)
        loss = -accuracy
            
        mlflow.log_metric("accuracy", accuracy)

        mlflow.xgboost.log_model(booster, artifact_path='models_mlflow')

    return y_pred

@flow
def main_flow():
    """The main training pipeline"""
    print("starting...")

    # MLflow settings
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("xgboost-experiment")

    # Load
    filename = "../data/churn.txt"
    churn_raw_data = read_data(filename)

    # Transform
    xgb_dtrain, xgb_dtest, y_test = prep_data(churn_raw_data)
    print("prep_data complete")

    # Train
    xgb_model = train_xgb_model(xgb_dtrain, xgb_dtest)

    # Predict
    xgb_pred = pred_xgb_model(xgb_model, xgb_dtest, y_test)

    # Save model

    print(xgb_pred)

    print("finished successfully")

if __name__ == "__main__":
    main_flow()