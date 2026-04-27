import pandas as pd
import numpy as np
import yaml
import logging
import os

def extract():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    os.makedirs("data/raw", exist_ok=True)
    logging.info("Gerando dados simulados")

    np.random.seed(config["data"]["seed"])
    periods = config["data"]["periods"]

    df = pd.DataFrame({
        "equipamento_id": np.random.randint(1, 6, periods),
        "data_falha": pd.date_range(start=config["data"]["start_date"], periods=periods, freq="ME"),
        "tempo_parado": np.random.randint(5, 50, periods),
        "custo_manutencao": np.random.randint(100, 1000, periods)
    })

    df.to_csv(config["paths"]["raw"], index=False)
    logging.info(f"{len(df)} registros gerados")
    return df