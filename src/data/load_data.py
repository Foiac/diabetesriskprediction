import pandas as pd

class LoadData:

    def get_data(self, path):
        """
        Reads data from a CSV file and returns a DataFrame.

        Parameters:
        path (str): The path to the CSV file containing the data.

        Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
        """
        # Reads the data from the CSV file specified in 'path'
        df = pd.read_csv(path)

        # Returns the DataFrame containing the read data
        return df