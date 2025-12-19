fleet = {
    "Sedan": {"rate": 50.0, "surcharge": 25.0},
    "SUV":   {"rate": 80.0, "surcharge": 40.0}
}

drivers = {
    "D1": {"credit": 200.0, "age": 30},
    "D2": {"credit": 100.0, "age": 20}   
}

rentals = [
    ("D1", "Sedan", 3), 
    ("D2", "Sedan", 2),    
    ("D1", "Truck", 1), 
    ("D1", "Sedan", -1),   
    ("D9", "SUV", 1)       
]

def rent_vehicle(drivers_db, fleet_catalog, driver_id, model, days):
    if driver_id not in drivers_db:
        raise KeyError("Driver not found")
    if model not in fleet_catalog:
        raise KeyError("Vehicle model unavailable")
    if type(days) is not int or days < 1:
        raise ValueError("Days must be positive integer")
    daily_rate = fleet_catalog[model]["rate"]
    total_cost = daily_rate * days
    driver_age = drivers_db[driver_id]["age"]
    if driver_age < 25:
        surcharge = fleet_catalog[model]["surcharge"]
        total_cost += surcharge
    driver_credit = drivers_db[driver_id]["credit"]
    if driver_credit < total_cost:
        raise ValueError("Credit limit exceeded")
    drivers_db[driver_id]["credit"] -= total_cost
    
    return float(total_cost)

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
result = process_rentals(drivers, fleet, rentals)
print(result)
