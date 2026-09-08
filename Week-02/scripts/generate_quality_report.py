from pathlib import Path
import pandas as pd

RAW = Path("../data/raw/des_normal_estimates_major_crops.csv")
OUT = Path("../outputs/quality_reports/des_quality_report.csv")

df = pd.read_csv(RAW)

report = pd.DataFrame({
    "check": [
        "row_count",
        "column_count",
        "missing_cells",
        "duplicate_rows",
        "negative_area",
        "negative_production",
        "negative_yield",
        "unique_crops",
        "unique_periods"
    ],
    "value": [
        len(df),
        df.shape[1],
        int(df.isna().sum().sum()),
        int(df.duplicated().sum()),
        int((df["area_mha"] < 0).sum()),
        int((df["production_mt"] < 0).sum()),
        int((df["yield_kg_ha"] < 0).sum()),
        int(df["crop"].nunique()),
        int(df["period"].nunique())
    ]
})

OUT.parent.mkdir(parents=True, exist_ok=True)
report.to_csv(OUT, index=False)
print(report)
