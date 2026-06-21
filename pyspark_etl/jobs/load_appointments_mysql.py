import pandas as pd
from sqlalchemy import create_engine
import glob

csv_file = glob.glob(
    "pyspark_etl/datasets/processed/appointments/part-*.csv"
)[0]

print("Reading:", csv_file)

df = pd.read_csv(csv_file)

df = df.rename(columns={
    "AppointmentID": "appointment_id",
    "Date": "appointment_date",
    "Time": "appointment_time",
    "PatientID": "patient_id",
    "DoctorID": "doctor_id"
})

print(df.head())

engine = create_engine(
    "mysql+pymysql://smartcare:rana%402025@localhost/smartcare"
)

df.to_sql(
    "appointments",
    engine,
    if_exists="append",
    index=False
)

print("Appointments loaded successfully.")
