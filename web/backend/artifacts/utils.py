import pandas as pd


def clean_df(df):
    # List of columns that are optional and can be safely dropped if present
    drop_cols = ['name', 'description', 'exterior_color', 'interior_color',
                 'trim', 'transmission', 'doors', 'mileage']

    # Drop optional columns if they exist
    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

    # Lowercase all column names
    df = df.rename(columns=str.lower)

    # Define required columns for filtering NA rows
    required_cols = ['make', 'model', 'price', 'fuel', 'body', 'engine']
    available_required_cols = [col for col in required_cols if col in df.columns]

    # Drop rows with NA in required columns (only if those columns exist)
    if available_required_cols:
        df = df.dropna(subset=available_required_cols)

    # Handle missing 'cylinders' only if it exists
    if 'cylinders' in df.columns:
        df['cylinders'] = df['cylinders'].fillna(0)

    return df


def clean_df_wrapper(X):
    return clean_df(X)


def clean_make(df,col="make"):
    df = df.copy()
    df[col] =  df[col].astype(str).str.strip().str.lower().replace(r'\s+','-',regex=True)
    luxury_brands = ['bmw','mercedes-benz','audi','lexus','porsche','jaguar','infiniti',
            'cadilac','tesla','volvo','land-rover','acura','lincoln','genesis']
    df[col] = df[col].apply(
        lambda x: 'luxury' if any(luxury in x for luxury in luxury_brands) else x
    )
    value_count = df[col].value_counts()
    frequent_values = set(value_count[value_count>50].index)
    df[col] = df[col].apply(lambda x: x if x in frequent_values else 'other_make')
    return df
def clean_make_wrapper(df):
    return clean_make(df, 'make')

def model_cleaner(df,col='model'):
    df=df.copy()
    df[col] = df[col].astype(str).str.strip().str.lower().str.replace(r'\s+','-',regex=True)
    count = df[col].value_counts()
    frequent_values = set(count[count>=30].index)
    df[col] = df[col].apply(lambda x:x if x in frequent_values else 'other-model')
    return df
def model_cleaner_wrapper(df):
    return model_cleaner(df, 'model')

def year_pipe_wrapper(x):
    return x.astype(str)

def engine_extractor(df,col="engine"):
    df = df.copy()
    df[col] = df[col].astype(str).str.strip().str.lower()
    df['has_turbo'] = df[col].astype(str).str.contains('turbo').astype(int)
    df['engine_liter'] = df[col].astype(str).str.extract(r'(\d.\d+)l',expand=False)
    df['engine_liter'] = pd.to_numeric(df['engine_liter'],errors='coerce')
    df['engine_liter'] = df['engine_liter'].fillna(0)
    df['valves'] = df[col].str.extract(r'(\d{2})v', expand=False)
    df['valves'] = pd.to_numeric(df['valves'],errors='coerce')
    df['valves'] = df['valves'].fillna(0)
    df = df.drop(columns=['engine'])
    return df
def engine_extractor_wrapper(df):
    return engine_extractor(df, 'engine')


def fuel_cleaner(df,col='fuel'):
    df = df.copy()
    df[col] = df[col].astype(str).str.strip().str.lower().replace(r'\s+','-',regex=True)
    def simplify_fuel(value):
        if 'hybrid' in value:
            return 'hybrid'
        elif 'diesel' in value:
            return 'diesel'
        else:
            return value
    df[col] = df[col].apply(simplify_fuel)
    return df
def fuel_cleaner_wrapper(df):
    return fuel_cleaner(df, 'fuel')

def body_cleaning(df,col='body'):
    df = df.copy()
    df[col] = df[col].astype(str).str.strip().str.lower().str.replace(r'\s+','-',regex=True)
    return df
def body_cleaning_wrapper(df):
    return body_cleaning(df, 'body')

def drivetrain_cleaning(df,col='drivetrain'):
    df = df.copy()
    df[col] = df[col].astype(str).str.strip().str.lower().replace(r'\s+','-',regex=True)

    def simplify_drive(value):
        if 'all' in value or 'four' in value:
            return 'all'
        else:
            return value.split('-')[0]
    df[col] = df[col].apply(simplify_drive)
    return df
def drivetrain_cleaning_wrapper(df):
    return drivetrain_cleaning(df, 'drivetrain')