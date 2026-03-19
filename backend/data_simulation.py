import pandas as pd
import random
from datetime import datetime, timedelta

def simulate_data(days=30):
    """
    Simulate AI queries and resource consumption over a number of days.
    """
    data = []
    start_date = datetime.now() - timedelta(days=days)

    for i in range(days):
        date = start_date + timedelta(days=i)
        queries = random.randint(500, 5000)  # daily AI queries
        energy_per_query = 0.002            # kWh
        water_per_kwh = 1.8                  # liters

        energy = queries * energy_per_query
        water = energy * water_per_kwh

        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "queries": queries,
            "energy_kwh": round(energy, 4),
            "water_liters": round(water, 2)
        })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = simulate_data(30)  # simulate 30 days
    print(df.head())

    # Save to CSV for later use in SQL or visualization
    df.to_csv("data/ai_usage.csv", index=False)
    print("\nCSV saved to data/ai_usage.csv")