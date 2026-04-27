import yaml
import logging
import os

def load(df):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    logging.info("Salvando dados")

    os.makedirs("data/processed", exist_ok=True)

    csv_path = config["paths"]["processed"].replace(".xlsx", ".csv")

    df.to_csv(csv_path, index=False)
    df.to_excel(config["paths"]["processed"], index=False)

    logging.info("Dados salvos em CSV e Excel")