from data.load_data import LoadData
from data.preprocess import ProcessData
from features.build_features import BuildFeature
from models.train_model import Train

def main():

    data = LoadData()
    df = data.get_data("data/raw/diabetes.csv")

    process = ProcessData()
    df_transformed = process.process_data(df)
    
    feature = BuildFeature()
    df_features, X, Y = feature.select_feature(df_transformed, [1,4,5,7], 8)
    X_train, X_test, Y_train, Y_test = feature.split_dataset(df_features, X, Y)
    
    model = Train()
    model.train_knn(X_train, X_test, Y_train, Y_test, 24)

if __name__ == "__main__":
    main()