
# function that trata os valores 0
def process_data(df):

    # Column list to replace "0" values with NaN values
    columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    # Replace 0 with np.nan in the specified columns
    df[columns] = df[columns].replace(0, np.nan)
    # Loop through each column and fill missing values with the mean of the column
    df.fillna({col: df[col].mean() for col in columns}, inplace=True)

    return df