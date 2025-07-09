# import joblib
# import pandas as pd
#
data = {
    'make': 'Mercedes-Benz',
    'model': 'Sprinter 2500',
    'year' : 2023,
    'engine': '16V DDI DOHC Turbo Diesel',
    'cylinders': 4,
    'fuel': 'diesel',
    'body': 'cargo-van',
    'drivetrain': 'all-wheel-drive'
}
#
# # df = pd.read_csv('../../../data/vehicle-price.csv')
# #
# df = pd.DataFrame([data])
# print(df)
# cleaning_pipeline = joblib.load('data_cleaning_pipeline.pkl')
# prep_pipeline = joblib.load('preprocessing.pkl')
#
# cleaned_df = cleaning_pipeline.transform(df)
# # X = df.drop(columns=['price'])
# X_prep = prep_pipeline.transform(cleaned_df)
# print('X_prep.shape ',X_prep.shape)
# model = joblib.load('model.pkl')
# prediction = model.predict(X_prep)
# print('prediction.shape ',prediction.shape)
# print('prediction ',prediction)