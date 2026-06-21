from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws

spark = SparkSession.builder \
    .appName("SmartCare Appointments ETL") \
    .master("local[*]") \
    .getOrCreate()

appointments_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/raw/appointments.csv"
    )

print("Schema:")
appointments_df.printSchema()

# Remove null IDs
appointments_df = appointments_df.dropna(
    subset=["AppointmentID", "PatientID", "DoctorID"]
)

# Remove duplicate appointments
appointments_df = appointments_df.dropDuplicates(["AppointmentID"])

# Create appointment datetime column
appointments_df = appointments_df.withColumn(
    "appointment_datetime",
    concat_ws(" ", "Date", "Time")
)

appointments_df.show(10)

appointments_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(
        "/mnt/f/Learning/Smart-healthcare2.0/pyspark_etl/datasets/processed/appointments"
    )

spark.stop()
