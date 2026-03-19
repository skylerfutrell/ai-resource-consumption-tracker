# AI Resource Consumption Simulation

def calculate_usage(queries, energy_per_query=0.002, water_per_kwh=1.8):
    """
    Calculate energy and water usage based on AI queries.
    """
    total_energy = queries * energy_per_query
    total_water = total_energy * water_per_kwh
    return total_energy, total_water

if __name__ == "__main__":
    queries = int(input("Enter number of AI queries: "))

    energy, water = calculate_usage(queries)

    print("\nAI Resource Consumption")
    print("------------------------")
    print(f"Queries: {queries}")
    print(f"Energy Used (kWh): {energy:.4f}")
    print(f"Water Used (liters): {water:.2f}")