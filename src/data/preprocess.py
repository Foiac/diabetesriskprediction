import numpy as np

class ProcessData:
    
    def process_data(self, df):
        """
        Processes a DataFrame to handle zero values in specific columns by replacing them with NaN,
        followed by filling these missing values with the column mean.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the data to be processed.

        Returns:
        pd.DataFrame: The processed DataFrame with zero values replaced by NaN and missing values
                      filled with the column mean.
        """
        # List of columns to replace "0" values with NaN
        columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

        # Replace 0 with np.nan in the specified columns
        df[columns] = df[columns].replace(0, np.nan)

        # Iterate through each column and fill missing values with the column mean
        df.fillna({col: df[col].mean() for col in columns}, inplace=True)

        return df
