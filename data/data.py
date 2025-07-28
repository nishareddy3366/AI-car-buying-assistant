import pandas as pd

data = [
    {"make": "Toyota", "model": "Camry", "year": 2020, "price": 22000, "condition": "Used", "body_style": "Sedan", "mileage": 30000},
    {"make": "Honda", "model": "Civic", "year": 2019, "price": 19000, "condition": "Used", "body_style": "Sedan", "mileage": 40000},
    {"make": "Ford", "model": "Escape", "year": 2021, "price": 27000, "condition": "New", "body_style": "SUV", "mileage": 0},
    {"make": "Tesla", "model": "Model 3", "year": 2022, "price": 35000, "condition": "New", "body_style": "Sedan", "mileage": 0},
    {"make": "Hyundai", "model": "Elantra", "year": 2018, "price": 15000, "condition": "Used", "body_style": "Sedan", "mileage": 50000},
]

df = pd.DataFrame(data)
df.to_csv(r"C:\Users\Nikhil\Documents\ai-car-assistant\car_inventory.csv", index=False)