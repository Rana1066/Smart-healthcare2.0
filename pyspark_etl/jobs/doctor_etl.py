from pyspark.sql import SparkSession
from pyspark.sql.functions import upper

spark = SparkSession.builder \
    .appName("SmartCare Doctors ETL") \
    .master("local[*]") \
    .getOrCreate()

doctors_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/raw/doctors.csv"
    )

print("Schema:")
doctors_df.printSchema()

# Remove null DoctorID rows
doctors_df = doctors_df.dropna(subset=["DoctorID"])

# Remove duplicate doctors
doctors_df = doctors_df.dropDuplicates(["DoctorID"])

# Convert specialization to uppercase
doctors_df = doctors_df.withColumn(
    "Specialization",
    upper("Specialization")
)

doctors_df.show(10)

doctors_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/processed/doctors"
    )

spark.stop()
