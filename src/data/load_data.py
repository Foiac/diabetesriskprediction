import pandas as pd

# function that reads the data
def get_data(path):
    df = pd.read_csv(path)

    return df