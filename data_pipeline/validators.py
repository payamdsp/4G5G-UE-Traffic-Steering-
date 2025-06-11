def validate_ran_params(params):
    # Type checks, value ranges, mandatory fields
    try:
        assert -130 < params["RSRP"] < -40
        assert -30 < params["RSRQ"] < 0
        assert -20 < params["SINR"] < 40
        assert 0 <= params["PRB_util"] <= 1
        assert params["HetNet"] in {"macro", "small", "femto"}
        assert 1 <= params["5QI"] <= 9
        assert 1 <= params["QCI"] <= 9
        assert params["A3_threshold"] > 0
        assert params["A5_threshold"] > 0
        assert 0 <= params["PCI"] <= 503
        assert 0 <= params["RSI"] <= 1023
        return True
    except Exception as e:
        # Log and reject invalid data
        print(f"Validation error: {e}")
        return False