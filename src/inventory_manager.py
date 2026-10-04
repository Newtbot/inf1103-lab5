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

def add_product(new_product: dict):
    inventory_data.append(new_product)
    print("Product added sucessfully!")

def update_stock(product_item: dict):
    product_stock = int(input("New Stock Quantity: "))
    product_item["stock"] = product_stock
    print("Product updated sucessfully!")

def search_product(inventory_data: list):
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

    return product_item

def save_inventory(data_file: str, inventory_data: list):
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(inventory_data, f, indent=4)


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
        product_id = input("Product ID: ").strip().upper()
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
        
        add_product(new_product)

    elif check_user_input(user_option) == "3":
        print("Update Stock")
        product_item = search_product(inventory_data)

        if product_item:
            update_stock(product_item)
        else:
            print("Product not found.")


    elif check_user_input(user_option) == "4":
        print("Search Stock")
        product_item = search_product(inventory_data)
        if product_item:
            print(
            "--------------------------------------------------------\n"
            f"ID: {product_item['id']}\n"
            f"Name: {product_item['name']}\n"
            f"Price: ${product_item['price']}\n"
            f"Stock: {product_item['stock']}\n"
            "--------------------------------------------------------"
            )
        else: 
            print("Product not found")
    elif check_user_input(user_option) == "5":
        print("Saving inventory......")
        print("Inventory saved successfully to inventory.json.")
        save_inventory(data_file, inventory_data)

    
    elif check_user_input(user_option) == "6":
        save_inventory(data_file, inventory_data)
        print("Saving inventory before exit...")
        print(f"Inventory saved successfully.\n")
        print(
            f"Thank you for using Inventory Management System.\n"
            f"Program terminated.")
        break

    else:
        print("Please enter a valid integer. Eg. `1` ")







