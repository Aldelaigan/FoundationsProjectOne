####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "C0ded Bakery" #complete me.
signature_flavors = ["orange", "latte", "nutella"] #complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print ("Our menu:")
    for x in menu:
        print ("- \"%s\" (KD %s)" % (x, menu[x]))
    # your code goes here!


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for x in original_flavors:
        print ("- \"%s\"" % (x))
    # your code goes here!


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for x in signature_flavors:
        print ("- \"%s\"" % (x)) 
    # your code goes here!


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu:
        return True
    elif order in original_flavors:
        return True
    elif order in signature_flavors:
        return True
    else:
        return False
    # your code goes here!


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    user_input = input("What's your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.\n")
    while user_input.lower() != "exit":
        if is_valid_order(user_input):
            order_list.append(user_input)
    #use while function and check if true, append
        user_input = input()
    # your code goes here!

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >= 5:
        return True
    else:
        return False
    # your code goes here!


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for user_input in order_list:
        if user_input in menu:
            total += menu[user_input]
        elif user_input in original_flavors:
            total += original_price
        elif user_input in signature_flavors:
            total += signature_price
        else:
            return False
    # your code goes here!

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    
    # your code goes here!
    for user_input in order_list:
        print("- %s" % user_input)

    total_price = get_total_price(order_list)
    print("Your total bill is: KD %s" % total_price)
    if accept_credit_card(total_price):
        print ("You can use your credit card")
    else:
        print ("We can not accept credit card")
    print("Thank you for shopping at %s" % cupcake_shop_name)
