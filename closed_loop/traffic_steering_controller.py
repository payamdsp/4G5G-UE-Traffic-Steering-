import joblib, pandas as pd
from datetime import datetime

def decide_steering_action(rf_pred, iso_score, prb_util, sinr, thresholds):
    if rf_pred == 1 or iso_score < -0.1 or prb_util > thresholds["prb_util_high"]:
        return "STEER_AWAY"
    elif sinr < thresholds["sinr_low"]:
        return "STEER_TO_BETTER_SINR"
    else:
        return "NO_ACTION"

def act_on_cell(cell_id, action):
    # Placeholder: Secure API call to RAN controller or O-RAN SMO
    print(f"{datetime.now()}: Cell {cell_id} action: {action}")

def closed_loop_steering(feature_file, thresholds):
    rf = joblib.load("random_forest.pkl")
    iso = joblib.load("isolation_forest.pkl")
    df = pd.read_parquet(feature_file)
    for idx, row in df.iterrows():
        features = row.drop(['cell_id', 'gNodeB_id', 'sNSSAI']).values.reshape(1, -1)
        rf_pred = rf.predict(features)[0]
        iso_score = iso.decision_function(features)[0]
        action = decide_steering_action(
            rf_pred, iso_score, row["avg_prb_util"], row["avg_sinr"], thresholds
        )
        act_on_cell(row["cell_id"], action)

if __name__ == "__main__":
    thresholds = {"prb_util_high": 0.85, "sinr_low": 5}
    closed_loop_steering("features/traffic_steering/", thresholds)