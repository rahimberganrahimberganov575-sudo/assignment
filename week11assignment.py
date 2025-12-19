# -------------------------------
# Helper Function
# -------------------------------

def rent_vehicle(drivers_db, fleet_catalog, driver_id, model, days):

    # 1. Driver Check
    if driver_id not in drivers_db:
        raise KeyError("Driver not found")

    # 2. Model Check
    if model not in fleet_catalog:
        raise KeyError("Vehicle model unavailable")

    # 3. Input Validation
    if type(days) is not int or days < 1:
        raise ValueError("Days must be positive integer")

    # 4. Cost Calculation
    daily_rate = fleet_catalog[model]["rate"]
    total_cost = daily_rate * days

    # 5. Young Driver Surcharge
    driver_age = drivers_db[driver_id]["age"]
    if driver_age < 25:
        surcharge = fleet_catalog[model]["surcharge"]
        total_cost += surcharge

    # 6. Credit Check
    driver_credit = drivers_db[driver_id]["credit"]
    if driver_credit < total_cost:
        raise ValueError("Credit limit exceeded")

    # 7. Action (deduct credit)
    drivers_db[driver_id]["credit"] -= total_cost

    # 8. Return total cost
    return float(total_cost)


# -------------------------------
# Main Function
# -------------------------------

def process_rentals(drivers_db, fleet_catalog, rental_list):

    total_profit = 0.0
    rejected_requests = 0

    for driver_id, model, days in rental_list:
        try:
            cost = rent_vehicle(drivers_db, fleet_catalog, driver_id, model, days)
            total_profit += cost

        except (KeyError, ValueError, TypeError) as e:
            print(f"Rental Error for {driver_id}: {e}")
            rejected_requests += 1

    return {
        "total_profit": total_profit,
        "rejected_requests": rejected_requests
    }


# -------------------------------
# TEST DATA
# -------------------------------

fleet = {
    "Sedan": {"rate": 50.0, "surcharge": 25.0},
    "SUV":   {"rate": 80.0, "surcharge": 40.0}
}

drivers = {
    "D1": {"credit": 200.0, "age": 30},  # No surcharge
    "D2": {"credit": 100.0, "age": 20}   # Pays surcharge
}

rentals = [
    ("D1", "Sedan", 3),    # Valid → 150
    ("D2", "Sedan", 2),    # Error → Credit exceeded
    ("D1", "Truck", 1),    # Error → Model unavailable
    ("D1", "Sedan", -1),   # Error → Days invalid
    ("D9", "SUV", 1)       # Error → Driver not found
]


# -------------------------------
# RUN TEST
# -------------------------------

result = process_rentals(drivers, fleet, rentals)

print("\nFinal Result:")
print(result)
