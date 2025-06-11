import uuid, time, random, json

MCC, MNC = "123", "45"  # Dummy values

def generate_ran_sample(cell_id, gnb_id):
    sample = {
        "cell_id": cell_id,
        "gNodeB_id": gnb_id,
        "MCC": MCC,
        "MNC": MNC,
        "timestamp": int(time.time()),
        "RSRP": random.uniform(-120, -70),
        "RSRQ": random.uniform(-20, -3),
        "SINR": random.uniform(-5, 30),
        "PRB_util": random.uniform(0, 1),
        "HetNet": random.choice(["macro", "small", "femto"]),
        "5QI": random.choice([1, 2, 5, 7, 8]),
        "QCI": random.choice([1, 3, 9]),
        "sNSSAI": f"slice-{random.randint(1,10)}",
        "A3_threshold": random.uniform(2, 6),
        "A5_threshold": random.uniform(2, 6),
        "PCI": random.randint(0, 503),
        "ECGI": f"ecgi-{random.randint(100000,999999)}",
        "NR_CELL_ID": f"nr-{random.randint(100000,999999)}",
        "RSI": random.randint(0, 1023)
    }
    return sample

if __name__ == "__main__":
    n_cells, n_gnb = 15000, 5000
    with open("raw_ran_data.jsonl", "w") as f:
        for cell in range(n_cells):
            gnb = f"gNB_{cell % n_gnb}"
            data = generate_ran_sample(f"cell_{cell}", gnb)
            f.write(json.dumps(data) + "\n")