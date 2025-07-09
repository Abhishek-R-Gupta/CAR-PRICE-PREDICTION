import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import re
from utils import clean_df_wrapper,clean_make_wrapper,model_cleaner_wrapper,year_pipe_wrapper,engine_extractor_wrapper,fuel_cleaner_wrapper,body_cleaning_wrapper,drivetrain_cleaning_wrapper






make_pipe = Pipeline([
    ('clean', FunctionTransformer(clean_make_wrapper, validate=False)),
    ('ohe', OneHotEncoder(handle_unknown='ignore'))

])




model_pipe = Pipeline([
    ('clean', FunctionTransformer(model_cleaner_wrapper, validate=False)),
    ('ohe', OneHotEncoder(handle_unknown="ignore"))
])





year_pipe = Pipeline([
    ('to_str', FunctionTransformer(year_pipe_wrapper)),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])



engine_pipe = Pipeline([
    ('extract', FunctionTransformer(engine_extractor_wrapper, validate=False)),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])



fuel_pipe = Pipeline([
    ('cleaning', FunctionTransformer(fuel_cleaner_wrapper, validate=False)),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])




body_pipe = Pipeline([
    ('cleaning', FunctionTransformer(body_cleaning_wrapper, validate=False)),
    ('encoder', OneHotEncoder(handle_unknown="ignore"))
])




drivetrain_pipe = Pipeline([
    ('clean', FunctionTransformer(drivetrain_cleaning_wrapper, validate=False)),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessing_pipeline = ColumnTransformer(transformers=[
    ('make', make_pipe, ['make']),
    ('model', model_pipe, ['model']),
    ('year', year_pipe, ['year']),
    ('engine', engine_pipe, ['engine']),
    ('fuel', fuel_pipe, ['fuel']),
    ('body', body_pipe, ['body']),
    ('drivetrain', drivetrain_pipe, ['drivetrain'])
])

full_preprocessing_pipeline = Pipeline([
    ('features', preprocessing_pipeline)
])

df = pd.read_csv('../../../data/vehicle-price.csv')





data_cleaning_step = Pipeline([
    ('clean_df', FunctionTransformer(clean_df_wrapper, validate=False))
])
print(df.shape)
data_cleaning_step.fit(df)
clean_df = data_cleaning_step.transform(df)
path = r'/data/cleaned-data.csv'
clean_df.to_csv(path)
print(clean_df.shape)

# joblib.dump(data_cleaning_step, 'data_cleaning_pipeline.pkl')

X = clean_df.drop(columns=['price'])
full_preprocessing_pipeline.fit(X)
print(full_preprocessing_pipeline.transform(X).shape)
# joblib.dump(full_preprocessing_pipeline, 'preprocessing.pkl')