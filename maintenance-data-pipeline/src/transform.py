import pandas as pd
import yaml
import logging
import os

def transform():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    logging.info("Transformando dados")

    df = pd.read_csv(config["paths"]["raw"])
    df["data_falha"] = pd.to_datetime(df["data_falha"])

    df["mes"] = df["data_falha"].dt.to_period("M")

    kpi = df.groupby("mes").agg({
        "tempo_parado": "sum",
        "custo_manutencao": "sum"
    }).reset_index()

    os.makedirs("data/processed", exist_ok=True)
    return kpi