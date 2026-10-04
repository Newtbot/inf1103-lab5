from pathlib import Path
import os
import json

# The store manager needs a system that remembers inventory levels even after the
# program closes. Furthermore, they need to store a history of all transaction amounts,
# not just the running total

# 1. Data Representation:
# Represent inventory items using dictionaries and store at least three products in a
# list.

# 2. Data Manipulation:
# Maintain your functional design. Create add_product(), update_stock(),
# search_product() and display_all() fuctions in inventory dictionary.

# 3. Data Persistence:
# Check whether inventory.json exists. Create load_inventory() to load
# inventory.json if it exists. Otherwise, begin with an empty inventory. Create
# save_inventory() and save data to inventory.json.

# 4. Build a Menu System:
# Create menu options for Display, Add, Update, Search, Save and Exit


data_file = "src/model/inventory.json"


# Persistence: At the start of the program, read the information previously saved
# in the inventory file. If the inventory file does not exist, start with an empty
# inventory and continue running without producing an error.
def check_file(data_file: str) -> bool:
    path = Path(data_file)
    # Check that it exists, is an actual file (not a folder), and ends with .json
    return path.is_file() and path.suffix.lower() == ".json"

def check_user_input(user_input):
    #check if its digit. and if its digit return the number
    if user_input.isdigit():
        return user_input
    else:
        return "NaN"

def load_inventory():
    #check if checkfile is true if true read file or "load file"
    if check_file(data_file):
        with open(data_file, "r", encoding="utf-8") as file:
            content = file.read()
            return True
    else:
        #create file if check file is false
        with open(data_file, "w", encoding="utf-8") as f:
            pass

def display_all():
    if check_file(data_file):
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    else:
        return "Error: Missing File"

# def save_inventory(valid_transaction):
#     next_id = 1001

#     # 1. Read existing file to find the highest current ID
#     if os.path.exists(file):
#         with open(file, "r", encoding="utf-8") as f:
#             existing_ids = []
#             for line in f:
#                 parts = line.strip().split(",")
#                 first_item = parts[0].strip()
#                 if first_item.isdigit():
#                     existing_ids.append(int(first_item))
                
#             if existing_ids:
#                 next_id = max(existing_ids) + 1
#     with open(file, "a", encoding="utf-8") as f:
#         for transaction in valid_transaction:
#             product_name , quantity = transaction
#             f.write(f"{next_id}, {product_name}, {quantity}\n")
            
#     with open(file, "r", encoding="utf-8") as f:
#         content = f.read()
#         lines = [line.strip() for line in content.splitlines() if line.strip()]
#         last_order = lines[-1] if lines else "No orders found"

#         return f"{content}\n\nNew Order Added:\n{last_order}\n\nOrder successfully saved to order.txt"

inventory_data = display_all()

while True:
    #if true run the program
    if load_inventory(): 
        print(
            "========================================================\n"
            "INVENTORY MANAGEMENT SYSTEM\n"
            "========================================================\n\n"
            "inventory.json found.\n"
            "Inventory loaded successfully\n\n"
            "----------- MENU -----------\n"
            "1. Display All Products\n"
            "2. Add Product\n"
            "3. Update Stock\n"
            "4. Search Product\n"
            "5. Save Inventory\n"
            "6. Exit\n"
            "----------------------------\n"
            )
    #the list will host product dict
    #option 1 will read the json file and represent it as a dict
    #option 2 will append the user input to a dict
    #option 3 will update the product based on dict keys and dict values
    #option 4 will get values by dict key 
    #option 5 will save the list to json file
    #option 6 will save the data and exit 

    user_option = input("Enter Option: ")
    if check_user_input(user_option) == "1":
        
        print(
            "--------------------------------------------------------\n"
            "Current Inventory\n"
            "--------------------------------------------------------"
            )
        if not inventory_data:
            print("Inventory Not found") 
        else:
            for item in inventory_data:
                print(
                        f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
                    )
    elif check_user_input(user_option) == "2":
        print("\nAdd New Product\n")
        product_id = input("Product ID: ").strip()
        product_name = input("Product Name: ").strip()

        # Convert price to float and stock to int
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        new_product = {
            "id": product_id,
            "name": product_name,
            "price": price,
            "stock": stock,
        }

        inventory_data.append(new_product)
        print("Product added sucessfully!")

    elif check_user_input(user_option) == "3":
        print("Update Stock")
        product_id = input("Enter Product ID: ").upper()
        product_item = None
        for item in inventory_data:
            # Safely read the id, returns None if "id" is missing
            if item.get("id") == product_id:
                product_item = item
                print("Product Found")
                print(
                    f"Name: {item['name']}\n"
                    f"Stock: {item['stock']}\n"   
                )

                if product_item: 
                    product_stock = int(input("New Stock Quantity: "))
                    product_item["stock"] = product_stock
                    print("Product updated sucessfully!")
        # if found_item:
        #     # Update the value using standard assignment
        #     found_item["stock"] = 25
        #     found_item["price"] = 1199.99
        #     print(f"Updated {found_item.get('name')}")
        # else:
        #     print("Item not found.")

        # if found_item:
        # # .update() modifies multiple fields at once
        # found_item.update({
        #     "price": 1050.00,
        #     "stock": 30
        # })



    # if check_user_input(user_input) == "quit":
    #     # 3. Write-Back: When the user types quit, save the final total and the transaction
    #     # history list to inventory.txt.
    #     print(save_inventory(valid_transaction))

    #     total_inventory , errors = generate_report(current_total, errors)
    #     break

    # #logic of my operations
    # elif (check_user_input(user_input)):
    #     stock_value = int(user_input)

    #     #append values to array for file writing operations
    #     valid_transaction.append((product_input, stock_value))

    #     #pass user input to process delivery for logic oprs
    #     current_total = process_delivery(current_total, stock_value)


    else:
        print("Please enter a valid integer. Eg. `1` ")







