import joblib
import pandas as pd
from app.schemas import CarInput
# from app.utils import clean_df_wrapper,clean_make_wrapper,model_cleaner_wrapper,year_pipe_wrapper,engine_extractor_wrapper,fuel_cleaner_wrapper,body_cleaning_wrapper,drivetrain_cleaning_wrapper
from app.preprocessing_pipeline import CarDataPreprocessor

# print('libraries loaded')


pipeline = CarDataPreprocessor()
df = pd.read_csv(r'app/cleaned-data.csv')
pipeline.fit(df)
print('pipeline transformed')
print('preprocessor loaded')


model = joblib.load(r'app/model.pkl')
print("model loaded")

def predict_price(data: CarInput):
    # Convert input to Dataframe
    input_df = pd.DataFrame([data.dict()])
    print('input_df ',input_df)

    # Apply preprocessing to input DataFrame
    X_transformed = pipeline.transform(input_df)
    print('X_transformed ',X_transformed)

    # predict the output from model
    price = model.predict(X_transformed)[0]
    print('price ',price)
    return round(price,2)

