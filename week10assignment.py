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


    





# transaction_list = [
#     "01-Oct/Food/15.50",
#     "02-Oct/Gas/40.00",
#     "03-Oct/Food/12.25",
#     "04-Oct/Rent/800.00",
#     "05-Oct/Gas/35.00",
#     "05-Oct/Food/8.75"
# ]
# def group_expenses(transaction_list):
#     expense_dict = {}
#     for i in transaction_list:    
#         date, category, cost_str = i.split("/")
#         cost = float(cost_str)
#         if category in expense_dict:
#             expense_dict[category].append((date, cost))
#         else:
#             expense_dict[category] = [(date, cost)]
#     return expense_dict

# def summarize_budget(expense_dict):
#     for category, transactions in expense_dict.items():
#         total_cost = 0
#         for _, cost in transactions:
#             total_cost += cost
#         print(f"{category}: ${total_cost:.2f} total")

# grouped_data = group_expenses(transaction_list)
# summarize_budget(grouped_data)
                        