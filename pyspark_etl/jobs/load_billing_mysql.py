import pandas as pd
from sqlalchemy import create_engine
import glob

csv_file = glob.glob(
    "pyspark_etl/datasets/processed/billing/part-*.csv"
)[0]

print("Reading:", csv_file)

df = pd.read_csv(csv_file)

df = df.rename(columns={
    "InvoiceID": "invoice_id",
    "PatientID": "patient_id",
    "Items": "items",
    "Amount": "amount"
})

print(df.head())

engine = create_engine(
    "mysql+pymysql://smartcare:rana%402025@localhost/smartcare"
)

df.to_sql(
    "billing",
    engine,
    if_exists="append",
    index=False
)

print("Billing loaded successfully.")
