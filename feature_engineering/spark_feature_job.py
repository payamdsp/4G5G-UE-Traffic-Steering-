from pyspark.sql import SparkSession, functions as F

def main():
    spark = SparkSession.builder.appName("TrafficSteeringFeatureEng").getOrCreate()
    df = spark.read.json("raw_ran_data.jsonl")
    features = df.groupBy("cell_id", "gNodeB_id", "sNSSAI").agg(
        F.avg("RSRP").alias("avg_rsrp"),
        F.avg("RSRQ").alias("avg_rsrq"),
        F.avg("SINR").alias("avg_sinr"),
        F.avg("PRB_util").alias("avg_prb_util"),
        F.max("A3_threshold").alias("max_a3"),
        F.max("A5_threshold").alias("max_a5"),
        F.countDistinct("PCI").alias("pci_variance"),
        F.first("HetNet").alias("hetnet"),
        F.first("5QI").alias("5qi"),
        F.first("QCI").alias("qci"),
        F.first("MCC").alias("mcc"),
        F.first("MNC").alias("mnc"),
        F.first("ECGI").alias("ecgi"),
        F.first("NR_CELL_ID").alias("nr_cell_id"),
        F.first("RSI").alias("rsi")
    )
    features.write.parquet("features/traffic_steering/", mode="overwrite")
    spark.stop()
if __name__ == "__main__":
    main()