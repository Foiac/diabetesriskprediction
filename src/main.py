from data.load_data import get_data
from data.preprocess import process_data
from features.build_features import *
from models.train_model import train_knn

def main():

    df = get_data("diabetesriskprediction/data/raw/diabetes.csv")
    df_transformed = process_data(df)
    df_features, X, Y = select_feature(df_transformed, [1,4,5,7], 8)
    X_train, X_test, Y_train, Y_test = split_dataset(df_features, X, Y)
    train_knn(X_train, X_test, Y_train, Y_test, 24)

if __name__ == "__main__":
    main()