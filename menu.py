# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order = {}

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            menu_item_name = []
            menu_item_price = []
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                        menu_item_name.append(f"{key} - {key2}")
                        menu_item_price.append(value2)
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
                    menu_item_name.append(f"{key}")
                    menu_item_price.append(value)
            # 2. Ask customer to input menu item number
            selection = input("Which item would you like? Input a number: ")
            # 3. Check if the customer typed a number
            if selection.isdigit():
                # Convert the menu selection to an integer
                selection_int=int(selection)
            else: 
                while not selection.isdigit():
                    selection = input("Please enter a number: ")
                selection_int=int(selection)
                # 4. Check if the menu selection is in the menu items
                # Tell the customer they didn't select a menu option
            while selection_int < 0 or selection_int > i-1:
                selection = input(f"That's not a valid input. Please enter a value between 1 and {i-1}: ")
                if selection.isdigit():
                    selection_int=int(selection)
                else: 
                    while not selection.isdigit():
                        # Tell the customer that their input isn't valid
                        selection = input(f"Please enter a number between1 1 and {i-1}: ")
                    selection_int=int(selection)
                # Store the item name as a variable. Note: I did this above when dispalying the menu.
                # menu_item_name.append({key})
                # menu_item_price.append(value2)

                # Ask the customer for the quantity of the menu item
            order_quantity = input(f"That's {menu_item_name[selection_int-1]}. How many would you like? ")

                # Check if the quantity is a number, default to 1 if not
            if not order_quantity.isdigit():
                order_quantity = 1
                # Add the item name, price, and quantity to the order list
            print(menu_item_name[selection_int-1])
            order[menu_item_name[selection_int-1]]={
                      "Price": menu_item_price[selection_int-1],
                       "Quantity": order_quantity
            }
            print(f"Okay! Adding {order_quantity} {menu_item_name[selection_int-1]}(s) to your order!")
            # Line below for debug to see if items are added to the oder dictionary correctly.
            # print(f"Order so far order_quantity{order}.")        
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? Yes or No: ")
        valid_inputs_yes= ['y', 'yes', 'yeah', 'sure', 'okay', 'ok', 'yes, please.']
        valid_inputs_no = ['n', 'no', 'nope', 'never', 'nah', 'no, thank you.', 'no thanks']
        # 5. Check the customer's input
        while not ((keep_ordering.lower() in valid_inputs_yes) or (keep_ordering.lower() in valid_inputs_no)):
            keep_ordering = input("That wasn't a valid input. Please select: (Y)es or (N)o ")  
        # Keep ordering
        if keep_ordering.lower() in valid_inputs_yes:
            # Exit the keep ordering question loop
            break
                # Complete the order
        if keep_ordering.lower() in valid_inputs_no:
            place_order = False
            # Since the customer decided to stop ordering, thank them for
            print("Thank you for your order!")
            # Exit the keep ordering question loop
            break
            # their order

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
        
# 6. Loop through the items in the customer's order
for key, details in order.items():
    
    
    # 7. Store the dictionary items as variables
    item_name = f"{key}"
    
    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)
    # 9. Create space strings
    item_spaces = " " * num_item_spaces 
    receipt_line = item_name + item_spaces + "|"

    # 10. Print the item name, price, and quantity
    for value1, value2 in details.items():
        if value1 == "Price":
            receipt_price = {value2}
            num_item_spaces = 9 - len(str(receipt_price))
            receipt_line += f"${value2}" + " "*num_item_spaces + "| "
        elif value1 == "Quantity":
            receipt_quantity = {value2}
            receipt_line += f"{value2}"
    print(receipt_line)

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print("--------------------------|--------|----------")
order_total = sum(item["Price"]*float(item["Quantity"]) for item in order.values())    
print(" "*30 + f"Total| ${order_total}")
