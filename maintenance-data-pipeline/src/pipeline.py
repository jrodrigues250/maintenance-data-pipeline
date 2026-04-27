import logging
import os
from extract import extract
from transform import transform
from load import load
from plot import generate_plot
import yaml

def setup_logging():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    os.makedirs("data/logs", exist_ok=True)

    logging.basicConfig(
        filename=config["paths"]["log"],
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def run_pipeline():
    setup_logging()

    logging.info("Início do pipeline")

    extract()
    df = transform()
    load(df)
    generate_plot(df)

    logging.info("Pipeline finalizado com sucesso")

if __name__ == "__main__":
    run_pipeline()