drink_type_dict = {
    'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
    'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 3},
    'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 40},
    'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 0},
    'CC': {'description': 'Coca cola', 'price': 1.3, 'quantity': 50},
    '1P': {'description': '100 Plus', 'price': 1.3, 'quantity': 50}}


def add_drink_type(drink_Newid, des_drink, price, quantity):
    drink = {'description': des_drink, 'price': price, 'quantity': quantity}
    drink_type_dict[drink_Newid] = drink


def replenish_drink(drink_Newid, quantity):
    drink = drink_type_dict.get(drink_Newid)
    drink['quantity'] += int(quantity)
    print(drink["description"], "has been topped up!")


def displayVM():
    for d in drink_type_dict:
        drink = drink_type_dict.get(d)
        print("DrinkID: %s desc: %s price: %0.1f quantity:%d" % (d, drink['description'],
               drink['price'], drink['quantity']))



drinks_dict = {
    "IM": {'item': 'IM', 'drink': 'Iced Milo', 'cost': float(1.50), 'Number': 0},
    "HM": {'item': 'HM', 'drink': 'Hot Milo', 'cost': float(1.20), 'Number': 0},
    "IC": {'item': 'IC', 'drink': 'Iced Coffee', 'cost': float(1.50), 'Number': 0},
    "HC": {'item': 'HC', 'drink': 'Hot Coffee', 'cost': float(1.20), 'Number': 0},
    "1P": {'item': '1P', 'drink': '100 Plus', 'cost': float(1.10), 'Number': 0},
    "CC": {'item': 'CC', 'drink': 'Coca Cola', 'cost': float(1.30), 'Number': 0}}

selectNumber = 0
cost = 0
answer = input("Are you a vendor (Y/N)? ")
answer = answer.upper()
newdrink = {}
if answer == "N":
    for key, value in drink_type_dict.items():
            if drink_type_dict[key]['quantity'] != 0:
                print(f"{key}. {value['description']} (${str(value['price'])}) Qty: {str(value['quantity'])}")
            else:
                print(f"{key}. {value['description']} (${str(value['price'])}) *out of stock*")
    total = 0
    while True:
        choice = str(input('Enter choice: ')).upper()
        if choice in drink_type_dict:
            if drink_type_dict[choice]['quantity'] > 0:
                selectNumber += 1
                total += drink_type_dict.get(choice)['price']
                drink_type_dict[choice]['quantity'] -= 1
                print(f"Number of drinks selected = {selectNumber}")
            else:
                print(drink_type_dict[choice]['description'], "is out of stock.")

        if choice == '0':
            selectNumber = 0
            print("Please pay:$%.2f" %(total))
            print("Indicate your payment:")
            while True:
                dollar10 = int(input('Enter no. of $10 notes: '))
                amountPaid = dollar10*10
                if amountPaid > total:
                    print("change:$%.2f" % (amountPaid-total))
                    amountPaid = 0
                    total = 0
                    print("Drinks paid. Thank you.")
                    break
                else:
                    dollar5 = int(input('Enter no. of $5 notes: '))
                    amountPaid += dollar5 * 5
                    if amountPaid > total:
                        print("change:$%.2f"% (amountPaid-total))
                        amountPaid= 0
                        total = 0
                        print("Drinks paid. Thank you.")
                        break
                    else:
                        dollar2 = int(input('Enter no. of $2 notes: '))
                        amountPaid += dollar2 * 2
                        if amountPaid > total:
                            print("change:$%.2f" % (amountPaid-total))
                            print("Drinks paid. Thank you.")
                            amountPaid= 0
                            total = 0
                            break
                        else:
                            print("Not enough to pay your drinks.")
                            print("Please take back your cash.")
                            cancel = str(input('Do you want to cancel your payment? Y/N:'))
                            cancel=cancel.upper()
                            if cancel == "Y":
                                print("Purchase is cancelled. Thank you.")
                                break
                            elif cancel == "N":
                                continue
            break

elif answer == "Y":
    while True:
        print("Welcome to ABC Vending Machine.")
        print("Select from following choices to continue:")
        print("1. Add Drink Type")
        print("2. Replenish Drink")
        print("0. Exit")
        vendor_choice = input("Enter choice: ")

        if vendor_choice == '1':
            while True:
                drink_id = str(input("Enter drink id:")).upper()
                if drink_id in drink_type_dict:
                    print("Drink id exists")
                elif drink_id != drink_type_dict:
                    drink_desc = input("Enter drink description:")
                    drink_cost = float(input("Enter price:$"))
                    drink_quantity = int(input("Enter quantity:"))
                    print("Drinks added")
                    add_drink_type(drink_id, drink_desc, drink_cost, drink_quantity)
                    print("After adding")
                    displayVM()
                    break
        elif vendor_choice == '2':
            displayVM()
            print("0. Exit / Payment")
            while True:
                drink_id = str(input("Enter drink id:")).upper()
                if drink_id not in drink_type_dict:
                    print("No drink with this drink id. Try again.")
                else:
                    if drink_id in drink_type_dict:
                        if drink_type_dict[drink_id]['quantity'] < 5:
                            drink_quantity = input("Enter quantity to replenish: ")
                            replenish_drink(drink_id, drink_quantity)
                            print("After replenish")
                            displayVM()
                            break
                        else:
                            print("No need to replenish. Quantity is greater than 5.")