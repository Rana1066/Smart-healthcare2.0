from pyspark.sql import SparkSession
from pyspark.sql.functions import round

spark = SparkSession.builder \
    .appName("SmartCare Billing ETL") \
    .master("local[*]") \
    .getOrCreate()

billing_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/raw/billing.csv"
    )

print("Schema:")
billing_df.printSchema()

# Remove null invoice IDs
billing_df = billing_df.dropna(subset=["InvoiceID"])

# Remove duplicates
billing_df = billing_df.dropDuplicates(["InvoiceID"])

# Round amount values
billing_df = billing_df.withColumn(
    "Amount",
    round("Amount", 2)
)

billing_df.show(10)

billing_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/processed/billing"
    )

spark.stop()
