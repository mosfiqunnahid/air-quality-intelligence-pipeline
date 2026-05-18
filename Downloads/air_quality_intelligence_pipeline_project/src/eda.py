import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/processed/air_quality_data.csv"
FIGURE_DIR = "reports/figures"


def run_eda():
    os.makedirs(FIGURE_DIR, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)
    print("\nColumns:", df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDescriptive statistics:")
    print(df["value"].describe())

    pollutant_avg = (
        df.groupby("parameter")["value"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))
    pollutant_avg.plot(kind="bar")
    plt.title("Average Pollution Value by Pollutant")
    plt.xlabel("Pollutant")
    plt.ylabel("Average Value")
    plt.tight_layout()

    plt.savefig(
        f"{FIGURE_DIR}/average_pollution_by_pollutant.png"
    )

    plt.show()

    count_by_pollutant = df["parameter"].value_counts()

    plt.figure(figsize=(8, 5))
    count_by_pollutant.plot(kind="bar")
    plt.title("Number of Measurements by Pollutant")
    plt.xlabel("Pollutant")
    plt.ylabel("Count")
    plt.tight_layout()

    plt.savefig(
        f"{FIGURE_DIR}/measurement_count_by_pollutant.png"
    )

    plt.show()


if __name__ == "__main__":
    run_eda()