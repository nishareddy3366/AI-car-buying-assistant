import random
import pandas as pd
from vector_store.retriever import populate_chromadb

# Expanded base patterns based on California Car Online inventory :contentReference[oaicite:4]{index=4}
base_data = [
    {"make": "Toyota",   "model": "RAV4",       "condition": "Used",     "body_style": "SUV",    "fuel_type": "Gasoline"},
    {"make": "Honda",    "model": "Civic",      "condition": "Certified","body_style": "Sedan",  "fuel_type": "Gasoline"},
    {"make": "Ford",     "model": "F-150",      "condition": "Used",     "body_style": "Truck",  "fuel_type": "Gasoline"},
    {"make": "Chevrolet","model": "Equinox",    "condition": "Used",     "body_style": "SUV",    "fuel_type": "Gasoline"},
    {"make": "BMW",      "model": "X3",         "condition": "Certified","body_style": "SUV",    "fuel_type": "Gasoline"},
    {"make": "Tesla",    "model": "Model Y",    "condition": "New",      "body_style": "SUV",    "fuel_type": "Electric"},
    {"make": "Toyota",   "model": "Corolla",    "condition": "Certified","body_style": "Sedan",  "fuel_type": "Hybrid"},
    {"make": "Hyundai",  "model": "Santa Fe",   "condition": "Used",     "body_style": "SUV",    "fuel_type": "Gasoline"},
    {"make": "Mazda",    "model": "CX-5",       "condition": "Used",     "body_style": "SUV",    "fuel_type": "Gasoline"},
    {"make": "Nissan",   "model": "Altima",     "condition": "Used",     "body_style": "Sedan",  "fuel_type": "Gasoline"},
    {"make": "Ford",     "model": "Mustang",    "condition": "Used",     "body_style": "Coupe",  "fuel_type": "Gasoline"},
    {"make": "Audi",     "model": "Q5",         "condition": "Certified","body_style": "SUV",    "fuel_type": "Gasoline"},
    {"make": "Kia",      "model": "Sorento",    "condition": "Used",     "body_style": "SUV",    "fuel_type": "Gasoline"},
    {"make": "Lexus",    "model": "RX 350",     "condition": "Used",     "body_style": "SUV",    "fuel_type": "Gasoline"},
]

def generate_description(base, year, price, msrp, mileage):
    cond = base["condition"].lower()
    return (f"A {year} {base['make']} {base['model']} ({cond}), "
            f"{base['body_style']} with {mileage} miles, "
            f"priced at ${price} (MSRP: ${msrp}).")

synthetic = []
for _ in range(350):
    base = random.choice(base_data)
    year = random.randint(2018, 2025)
    price = random.randint(20000, 50000)
    mileage = 0 if base["condition"] == "New" else random.randint(5000, 80000)
    msrp = price + random.randint(2000, 8000) if base["condition"] != "New" else price + random.randint(0, 5000)
    certified = (base["condition"] == "Certified")
    desc = generate_description(base, year, price, msrp, mileage)
    synthetic.append({
        "make": base["make"],
        "model": base["model"],
        "year": year,
        "price": price,
        "msrp": msrp,
        "discount": round((msrp - price) / msrp * 100, 1),
        "condition": base["condition"],
        "body_style": base["body_style"],
        "fuel_type": base["fuel_type"],
        "mileage": mileage,
        "certified_preowned": certified,
        "description": desc
    })

df = pd.DataFrame(synthetic)
df.to_csv(r"C:\Users\Nikhil\Documents\ai-car-assistant\data\car_inventory.csv", index=False)
populate_chromadb()
print("✅ Saved enhanced dataset with 350 listings to 'data/enhanced_car_inventory.csv'")
