import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
import joblib
import numpy as np
from sklearn.model_selection import train_test_split


df = pd.read_csv(r'../../../data/vehicle-price.csv')

print("df.shape ",df.shape)
data_cleaning_pipeline = joblib.load('data_cleaning_pipeline.pkl')
cleaned_df = data_cleaning_pipeline.transform(df)
X = cleaned_df.drop(columns=['price'])
y = cleaned_df.price
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=123)
processor = joblib.load('preprocessing.pkl')
X_train_prep = processor.transform(X_train)
print('X_train_prep.shape ',X_train_prep.shape)
models = {
    'Linear':LinearRegression(),
    'Lasso':Lasso(),
    'Ridge':Ridge(),
    'RandomForest':RandomForestRegressor(),
    'DecisionTree':DecisionTreeRegressor()
}

best_model = None
best_score = -np.inf

for name,model in models.items():
    score = cross_val_score(model,X_train_prep,y_train,cv=5,scoring='r2')
    avg_score=score.mean()
    print(f"{name} R² Score: {avg_score:.4f}")
    if avg_score > best_score:
        best_score = avg_score
        best_model = model

best_model.fit(X_train_prep, y_train)
print(best_model)

joblib.dump(best_model, 'model.pkl')