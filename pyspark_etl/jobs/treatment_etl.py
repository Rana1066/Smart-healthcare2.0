from pyspark.sql import SparkSession
from pyspark.sql.functions import upper

spark = SparkSession.builder \
    .appName("SmartCare Treatments ETL") \
    .master("local[*]") \
    .getOrCreate()

treatments_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/raw/treatments.csv"
    )

print("Schema:")
treatments_df.printSchema()

# Remove null ProcedureID
treatments_df = treatments_df.dropna(
    subset=["ProcedureID"]
)

# Remove duplicates
treatments_df = treatments_df.dropDuplicates(
    ["ProcedureID"]
)

# Convert procedure names to uppercase
treatments_df = treatments_df.withColumn(
    "ProcedureName",
    upper("ProcedureName")
)

treatments_df.show(10)

treatments_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/processed/treatments"
    )

spark.stop()
