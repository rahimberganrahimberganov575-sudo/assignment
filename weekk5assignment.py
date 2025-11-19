def  add_product(products, prices, new_product, new_price):
    products.append(new_product)
    prices.append(new_price)

def remove_product(products, prices, product_to_remove):
    for i in range(len(products)):
        if products[i]==product_to_remove:
            products.pop(i)
            prices.pop(i)
            return True
    else:
        return False

def get_most_valuable(products, prices, count):
    copied_products = products[:]
    copied_price = prices[:]
    result = []
    for _ in range(min(count, len(copied_products))):
        index = 0
        for i in range(1,len(copied_price)):
            if copied_price[i] > copied_price[index]:
                index = i
        result.append(copied_products[index])
        copied_products.pop(index)
        copied_price.pop(index)
    return result

def manage_inventory(initial_products, initial_prices, new_product_data, product_to_remove, top_count):
    products = initial_products[:]
    prices = initial_prices[:]

    add_product(products, prices, new_product_data[0], new_product_data[1])
    remove_product(products, prices, product_to_remove)
    most_valuable_products = get_most_valuable(products, prices, top_count)
    return products,most_valuable_products



# Test Case 1
products = ["Watch", "Ring", "Bag", "Scarf", "Pen"]
prices = [5500.00, 7200.00, 3100.00, 800.00, 1200.00]
new_product = ["Statue", 6800.00]
remove_name = "Scarf"
count = 3

# When you call your function:
final_products, top_list = manage_inventory(products, prices, new_product, remove_name, count)
print('Final products: ',final_products)
print('Top list: ', top_list)
