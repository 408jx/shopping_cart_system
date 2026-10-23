import datetime
products = ["chips", "soda", "candy", "cookies", "water", "sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00 ]

shopping_cart = []
user_choice = 0 

def display_items(products, prices):
    print("========== AVAILABLE PRODUCTS ==========")

    for i in  range(len(products)):
        print(f"{i + 1}. {products[i]}   ${prices[i]}")

    print()

def add_item(products, shopping_cart):
    print("which produce would you like to add?")
    print("1.chips")
    print("2.Soda")
    print("3.Candy")
    print("4.Cookies")
    print("5.Water")
    print("6.Sandwich")

    print()

    product_num = int(input("Enter product number: "))
    shopping_cart.append(products[product_num - 1])
    print(f"{products[product_num - 1]} was added to the cart!")

#the fuction makes it remove the items in the users cart
def remove_product(shopping_cart):
    print("========== YOUR SHOPPING CART ==========")
    if len(shopping_cart) == 0:
       print("your cart is empty son")
       return
    for i in range(len(shopping_cart)):
        print(f" {i + 1 }. {shopping_cart[i]}")

    print("which item would you like to remove? ")
    remove_item = int(input("Enter item number: ")) 
    if 1 <= remove_item <= len(shopping_cart):
        removed_item = shopping_cart.pop(remove_item - 1)
        print(f"{remove_item} was removed from your cart ")
    else:
        print("Not a vaild product number. try again ")

def cart_items(shopping_cart):
    print("========== YOUR SHOPPING CART ==========")
    if len(shopping_cart) == 0:
        print("you have no items! ")   
    else:
        for i in range(len(shopping_cart)):
            print(f" {i + 1}. {shopping_cart[i]}")
    print(f"total items {len(shopping_cart)}")



def calc_price_total(shopping_cart):
    print("========== CURRENT TOTAL ==========")
    total = 0 
    if len(shopping_cart) == 0:
        print("your cart is empty")
        return total
    for item in shopping_cart:
        index = products.index(item)
        price = prices[index]
        print(f"{item}    ${price:2f}")
        total += price

    print(f"subtotal: $ {total:2f}")
    return total


def checkout(total):
    print("========== RECEIPT ==========")
    print(f"Date: {datetime.date.today()}")
    print(f" subtotal:     ${total:.2f}")
    for item in  shopping_cart:
        index = products.index(item)
        price = price[index]
        print(f"{item}   ${price:.2f}")
    if total >= 40:
        print("discount: 15%")
        saved = total * 0.15
        print(f"saved amount:  {saved:.2f}")
        final_total = total - saved 
    elif total >= 20:
        print("discount:  10%")
        saved = total * 0.10 
        print(f"saved amount:   {saved:.2f}")
        final_total = total - saved
    elif total >= 10:
        print("discount:  5%")
        saved = total * 0.05
        print(f"saved amount:    {saved:.2f}")
        final_total = total - saved
    else:
        print("discount:  what discount? ")
        print("amount saved: nun ")
        final_total = total

    print(f"Final Total: {final_total:.2f}")
    print("thank for shopping here son!:) ")
    return final_total

while user_choice != 6:
    print("========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print()

    user_choice = int(input("what would you like to do?: "))

    if user_choice == 1:
        display_items(products, prices)
    
    elif user_choice == 2:
        add_item(products, shopping_cart)
    
    elif user_choice == 3:
        remove_product(shopping_cart)
    
    elif user_choice == 4:
        cart_items(shopping_cart)
    
    elif user_choice == 5:
        calc_price_total(shopping_cart)
    
    elif user_choice == 6:
        total = calc_price_total(shopping_cart)
        checkout(total)
        break

 


    


    

