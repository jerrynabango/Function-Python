def apply_discount(original_price, discount_percent):
    if discount_percent >= 20:
        discounted_price = original_price - (original_price * discount_percent / 100)
        return discounted_price
    else:
        return original_price

initial_price = float(input("Please input the initial price of the item: "))
discount_rate = float(input("Please enter the discount rate: "))

final_price = apply_discount(initial_price, discount_rate)

if final_price != initial_price:
    print(f"The discounted final price is: ${final_price:.2f}")
else:
    print("No discount applied. The original price remains: ksh{:.2f}".format(initial_price))
