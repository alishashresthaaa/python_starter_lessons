# Given a list of dictionaries representing products,
# each with a name (string) and price (float),
# write a Python function filter_expensive_products(products, threshold)
# that returns a new list containing only the products whose
# price is greater than or equal to a given threshold. For example:
# python
#
# Copy code
# products = [
#     {"name": "Laptop", "price": 1200.50},
#     {"name": "Mouse", "price": 35.99},
#     {"name": "Monitor", "price": 150.45}
# ]
# threshold = 100.00
# The function should return a list containing the "Laptop" and "Monitor" dictionaries.

def filter_expensive_products(user_products_list,threshold):
    '''
    Returns the expensive product list more than the given threshold
    :param products_threshold:
    :return:
    '''
    filtered_products = []
    for product in user_products_list:
        if(product["price"]) >= threshold:
            filtered_products.append(product)
    return filtered_products


products = [
    {"name": "Laptop", "price": 1200.50},
    {"name": "Mouse", "price": 35.99},
    {"name": "Monitor", "price": 150.45}
]
threshold = 100.00

output_list = filter_expensive_products(products,threshold)
print(output_list)

