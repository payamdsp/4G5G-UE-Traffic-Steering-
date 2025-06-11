import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
import mlflow, joblib
import os

def train_ensemble(feature_path):
    df = pd.read_parquet(feature_path)
    X = df.drop(['cell_id', 'gNodeB_id', 'sNSSAI'], axis=1)
    y = (df["avg_prb_util"] > 0.8).astype(int)  # Example: 1 if overloaded
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X, y)
    iso = IsolationForest(n_estimators=50, random_state=42)
    iso.fit(X)
    joblib.dump(rf, "random_forest.pkl")
    joblib.dump(iso, "isolation_forest.pkl")
    with mlflow.start_run():
        mlflow.sklearn.log_model(rf, "random_forest")
        mlflow.sklearn.log_model(iso, "isolation_forest")

if __name__ == "__main__":
    train_ensemble("features/traffic_steering/")