import matplotlib.pyplot as plt
import yaml
import logging
import os

def generate_plot(df):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    logging.info("Gerando gráfico")

    os.makedirs("data/plots", exist_ok=True)

    df["mes"] = df["mes"].astype(str)

    plt.figure()
    plt.plot(df["mes"], df["tempo_parado"])
    plt.xticks(rotation=45)
    plt.title("Tempo parado por mês")
    plt.xlabel("Mês")
    plt.ylabel("Tempo parado")

    plt.tight_layout()
    plt.savefig(config["paths"]["plot"])

    logging.info("Gráfico gerado")