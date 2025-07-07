import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pickle as pl

def model():
    results = pd.read_csv('results.csv').astype(float)

    # results['weight'] = results['weight'].apply(lambda x: np.divide(40, x))
    # results['course_unit'] = results['course_unit'].apply(lambda x: np.divide(30, x))
    # results['gpa'] = results['gpa'].apply(lambda x: np.divide(4.00, x))
    # print(results.head(5))

    X = results.drop('gpa', axis=1)
    y = results['gpa']
    print("X shape: ", X.shape, "Y shape: ", y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

    # lr = LinearRegression()
    lr =  RandomForestRegressor(n_estimators=100, random_state=42)
    lr.fit(X_train, y_train)

    with open('../../api/results.pkl', 'wb') as f:
        pl.dump(lr, f)

    y_pred = lr.predict(X_test)
    # print("predict_gpa: ", y_pred)
    print("MSE: ", mean_squared_error(y_test, y_pred))
    print("MAE: ", mean_absolute_error(y_test, y_pred))

if __name__ == "__main__":
    model()