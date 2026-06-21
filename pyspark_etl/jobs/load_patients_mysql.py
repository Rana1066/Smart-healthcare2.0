import pandas as pd
from sqlalchemy import create_engine
import glob

csv_file = glob.glob(
    "pyspark_etl/datasets/processed/patients/part-*.csv"
)[0]

print("Reading:", csv_file)

df = pd.read_csv(csv_file)

# Rename columns to match MariaDB table
df = df.rename(columns={
    "PatientID": "patient_id"
})

# Remove duplicate patient IDs
df = df.drop_duplicates(subset=["patient_id"])

print("Total rows:", len(df))
print("Unique IDs:", df["patient_id"].nunique())

print(df.head())

engine = create_engine(
    "mysql+pymysql://smartcare:rana%402025@localhost/smartcare"
)

df.to_sql(
    "patients",
    engine,
    if_exists="append",
    index=False
)

print("Patients loaded successfully.")