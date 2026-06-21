import pandas as pd
from sqlalchemy import create_engine
import glob

csv_file = glob.glob(
    "pyspark_etl/datasets/processed/doctors/part-*.csv"
)[0]

print("Reading:", csv_file)

df = pd.read_csv(csv_file)

df = df.rename(columns={
    "DoctorID": "doctor_id",
    "DoctorName": "doctor_name",
    "Specialization": "specialization",
    "DoctorContact": "doctor_contact"
})

print(df.head())

engine = create_engine(
    "mysql+pymysql://smartcare:rana%402025@localhost/smartcare"
)

df.to_sql(
    "doctors",
    engine,
    if_exists="append",
    index=False
)

print("Doctors loaded successfully.")
