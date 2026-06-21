import pandas as pd
from sqlalchemy import create_engine
import glob

csv_file = glob.glob(
    "pyspark_etl/datasets/processed/treatments/part-*.csv"
)[0]

print("Reading:", csv_file)

df = pd.read_csv(csv_file)

df = df.rename(columns={
    "ProcedureID": "procedure_id",
    "ProcedureName": "procedure_name",
    "AppointmentID": "appointment_id"
})

print(df.head())

engine = create_engine(
    "mysql+pymysql://smartcare:rana%402025@localhost/smartcare"
)

df.to_sql(
    "treatments",
    engine,
    if_exists="append",
    index=False
)

print("Treatments loaded successfully.")
