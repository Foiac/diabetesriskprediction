from data.load_data import get_data
from data.preprocess import process_data
from features.build_features import *

def main():
    df = get_data("data/raw/diabetes.csv")
    df_transformed = process_data(df)
    df_features, X, Y = select_feature(df_transformed, [1,4,5,7], 8)
    X_train, X_test, Y_train, Y_test = split_dataset(df_features, X, Y)
    print(X_train)
    print(X_test)
    print(Y_train)
    print(Y_test )

if __name__ == "__main__":
    main()