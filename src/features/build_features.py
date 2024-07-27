import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def select_feature(df, columns_x, y):
    """
    Scales the features of the DataFrame using MinMaxScaler and 
    separates the input features (X) and the target variable (Y).
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data to be processed.
    columns_x (list): List of indices of the columns to be used as input features (X).
    y (int): Index of the column to be used as the target variable (Y).
    
    Returns:
    tuple: Returns the scaled DataFrame, the input feature matrix X, and the target vector Y.
    """
    
    # Create an instance of MinMaxScaler with a feature range of 0 to 1
    sc = MinMaxScaler(feature_range=(0, 1))
    
    # Scale the entire dataset and create a new DataFrame
    dataset_scaled = sc.fit_transform(df)
    dataset_scaled = pd.DataFrame(dataset_scaled, columns=df.columns)  # Includes the original column names
    
    # Select the input features X and the target variable Y
    X = dataset_scaled.iloc[:, columns_x].values
    Y = dataset_scaled.iloc[:, y].values
    
    return dataset_scaled, X, Y

def split_dataset(df, X, Y):
    """
    Splits the dataset into training and testing sets.

    Parameters:
    X (array-like): Matrix of input features.
    Y (array-like): Target vector.
    df (pd.DataFrame): Original DataFrame containing the data for stratification.

    Returns:
    tuple: Training and testing sets for input features (X) and target variable (Y).
    """
    
    # Split the data into training and testing sets with stratification based on the 'Outcome' column
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42, stratify=df['Outcome'])
    
    return X_train, X_test, Y_train, Y_test
