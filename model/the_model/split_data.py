import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataframe(df: pd.DataFrame, train_ratio=0.7):
    train_df, test_df = train_test_split(df, train_size=train_ratio, random_state=42)
    return train_df, test_df

