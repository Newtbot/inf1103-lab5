from pathlib import Path
import csv
import re
import os

# Persistence: At the start of the program, read the information previously saved
# in the inventory file. If the inventory file does not exist, start with an empty
# inventory and continue running without producing an error.
def check_file(file_path: str) -> bool:
    path = Path(file_path)
    # Check that it exists, is an actual file (not a folder), and ends with .txt
    return path.is_file() and path.suffix.lower() == ".txt"


def load_inventory():
    file = "src/model/inventory.txt"
    #check if checkfile is true if true read file or "load file"
    if check_file(file):
        with open(file, "r", encoding="utf-8") as file:
            content = file.read()
    else:
        #create file if check file is false
        with open(file, "w", encoding="utf-8") as f:
            f.write("Current Orders:\n\n")
            pass

def save_inventory(valid_transaction):
    file = "src/model/inventory.txt"
    next_id = 1001

    # 1. Read existing file to find the highest current ID
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            existing_ids = []
            for line in f:
                parts = line.strip().split(",")
                first_item = parts[0].strip()
                if first_item.isdigit():
                    existing_ids.append(int(first_item))
                
            if existing_ids:
                next_id = max(existing_ids) + 1
    with open(file, "a", encoding="utf-8") as f:
        for transaction in valid_transaction:
            product_name , quantity = transaction
            f.write(f"{next_id}, {product_name}, {quantity}\n")
            
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        last_order = lines[-1] if lines else "No orders found"

        return f"{content}\n\nNew Order Added:\n{last_order}\n\nOrder successfully saved to order.txt"


current_total = 0 # stock handle 
errors = 0 # errors 
delivery_cost = 0 # delivery cost

# 2. History Tracking: Use a Python list (array) to store every valid transaction
# amount entered.
valid_transaction = []

# 1. get_valid_input(): Handles the prompt, handles input validation, and
# returns a valid integer or a "quit" signal.
# check if stock is integer and negative value
def check_user_input(user_input):
    # isdigit only returns True for digits
    # returns false for negative
    # we should check for whether its digit or negative value
    if user_input.isdigit():
        return user_input.strip().isdigit()
    elif (user_input).lower().strip() == "quit":
        return "quit"


# 2. process_delivery(current_total, new_value): Calculates the new total and
# returns it.
def process_delivery(current_total, new_value):
    current_total+= new_value
    return current_total  # total inventory / total process stock since we always start stock at 0


# 3. calculate_tax(amount): A new requirement! This function takes a delivery
# amount and returns the tax (10% of that specific delivery).
def calculate_tax(amount):
    return round(amount * 0.1, 2)  # get 10 percent of the value and round it to 2 d.p


# 4. generate_report(total_units, failed_attempts): A dedicated function to print
# the final summary.
def generate_report(current_total, errors):
    return current_total, errors


while True:
    load_inventory()
    # 1. Initialize the inventory to zero in the start
    product_input = input("Enter Product Name: ")
    if product_input.lower() == "quit":
        print(save_inventory(valid_transaction))

        break
    user_input = input("Enter Quantity: ") #quantity value

    if check_user_input(user_input) == "quit":
        # 3. Write-Back: When the user types quit, save the final total and the transaction
        # history list to inventory.txt.
        print(save_inventory(valid_transaction))

        total_inventory , errors = generate_report(current_total, errors)
        break

    #logic of my operations
    elif (check_user_input(user_input)):
        stock_value = int(user_input)

        #append values to array for file writing operations
        valid_transaction.append((product_input, stock_value))

        #pass user input to process delivery for logic oprs
        current_total = process_delivery(current_total, stock_value)

        # print("Total inventory:" , current_total )

        #tax calculation
        # tax = calculate_tax(stock_value)
        # print("Total Tax for this Delivery:"  , tax)

        # 7. Trigger Overstock Alert: If the total inventory exceeds 500 units, print an
        # alert and break the loop immediately. (keep in mind of the conditional flow we
        # discussed this week: if, elif and else)
        if (current_total > 500):
            print("My total inventory has exceeded capacity!!!")
            break

    else:
        print("Please enter a valid integer. Eg. `1` ")
        errors+=1