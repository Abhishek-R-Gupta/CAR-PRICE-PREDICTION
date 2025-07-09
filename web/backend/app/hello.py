import pandas as pd
from preprocessing_pipeline import CarDataPreprocessor

df = pd.read_csv(r'../../../data/cleaned-data.csv')
print(df.info())
print(df.shape)
pipeline = CarDataPreprocessor()
pipeline.fit(df)
X_trans = pipeline.transform(df)
print(X_trans.shape)
