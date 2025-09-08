from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def main():
    os.makedirs("models", exist_ok=True)
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    joblib.dump(clf, "models/model.pkl")
    print("Saved model to models/model.pkl")

if __name__ == "__main__":
    main()
