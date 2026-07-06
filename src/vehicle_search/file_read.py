from pathlib import Path

import pandas as pd


def read_vehicle_sales(make: str, model: str, sale_year: int,
                       file_path: str | Path):

    vehicle_sales = pd.read_csv(file_path)

    vehicle_sales["saledate_clean"] = (
        vehicle_sales["saledate"]
        .str.replace(r"\s+\([A-Z]+\)$", "", regex=True)
)
    vehicle_sales["saledate_clean"] = pd.to_datetime(vehicle_sales["saledate_clean"],
                                               errors="coerce", utc=True)
    vehicle_sales["sale_year"] = vehicle_sales["saledate_clean"].dt.year

    print(f"{make}, {model}, {sale_year}")

    selected_sales = vehicle_sales[
        (vehicle_sales["make"].str.strip().str.lower() == make.strip().lower()) &
        (vehicle_sales["model"].str.strip().str.lower() == model.strip().lower()) &
        (vehicle_sales["sale_year"] == int(sale_year))
    ]

    data_frame = selected_sales.head()
    print(data_frame)

    print(f"Vehicles sold {selected_sales.shape[0]}")
