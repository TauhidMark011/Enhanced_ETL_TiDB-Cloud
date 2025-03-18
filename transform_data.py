from utils import log  # Importing log function to track transformation progress
import pandas as pd

def transform_data(df):
    """Perform data transformation like unit conversion and cleaning."""

    log("Starting data transformation...")

    # Convert height from inches to meters (only if 'height' column exists)
    if "height" in df.columns:
        log("Converting height from inches to meters...")
        df["height_in_m"] = df["height"].astype(float) * 0.0254  

    # Convert weight from pounds to kilograms (only if 'weight' column exists)
    if "weight" in df.columns:
        log("Converting weight from pounds to kilograms...")
        df["weight_in_kg"] = df["weight"].astype(float) * 0.453592  

    # Dropping original height and weight columns (if they exist)
    log("Dropping original 'height' and 'weight' columns...")
    df.drop(columns=["height", "weight"], inplace=True, errors="ignore")  

    log("✅ Data transformation completed successfully!")

    return df  # ✅ Returning transformed DataFrame properly
