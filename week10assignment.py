shipment_list = [
    "New York|Box101|50",
    "Chicago|Box102|20",
    "New York|Box103|30",
    "Miami|Box104|15",
    "Chicago|Box105|45",
    "New York|Box106|10"]

def group_packages(shipment_list):
    shipping_dict = {}
    for i in shipment_list:    
        city, packageip, kg_str = i.split("|")
        kg = int(kg_str)
        if city in shipping_dict:
            shipping_dict[city].append((packageip, kg))
        else:
            shipping_dict[city] = [(packageip, kg)]
    return shipping_dict

def calculate_truck_loads(shipping_dict):
    for citys, data in shipping_dict.items():
        total_kg = 0
        for _, kgs in data:
            total_kg += kgs
        print(f"{citys}: {total_kg} kg total")

nimas = group_packages(shipment_list)
calculate_truck_loads(nimas)

