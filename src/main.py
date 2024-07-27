from data.load_data import get_data

def main():
    dataset = get_data("data/raw/diabetes.csv")
    print(dataset.head())

if __name__ == "__main__":
    main()