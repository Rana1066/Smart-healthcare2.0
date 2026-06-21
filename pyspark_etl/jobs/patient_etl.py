from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws, split

spark = SparkSession.builder \
    .appName("SmartCare Patient ETL") \
    .master("local[*]") \
    .getOrCreate()

patients_path = "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/raw/patients.csv"

patients_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(patients_path)

patients_df.printSchema()

patients_df = patients_df.dropna()

patients_df = patients_df.withColumn(
    "full_name",
    concat_ws(" ", "firstname", "lastname")
)

patients_df = patients_df.withColumn(
    "email_domain",
    split("email", "@").getItem(1)
)

patients_df.show(10)

patients_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/processed/patients"
    )

spark.stop()
