# 1

kms = int(input("Km: "))
print("Miles:", round(0.6214 * kms, 2))

# 2

import dollar as dl
dram = int(input("Dram: "))
print(f"Dollar value of your dram: {round(dl.dollar * dram, 2)}$")

# 3

height = int(input("Insert your height: "))
print("Ideal weight for you heigh is:", (height - 100) - (height - 150) / 2)

# 4

food_bool = int(input("Send 1 if you want to order pizza (500 dram), Send 2 if you want to order kebab (700 dram) \n")) - 1

sauce_bool = int(input("Send 1 if you want ketchup (100 dram), send 2 if you want mayonez (120 dram) \n")) - 1

overal_price = 500 * bool(food_bool - 1) + 700 * bool(food_bool) + 100 * bool(sauce_bool - 1) + 120 * bool(sauce_bool)

print("You have ordered pizza with Mayonez and your price is 620 =>", "True" * bool((int(bool(620 - overal_price)) - 1)) + "False" * (int(bool(620 - overal_price))))
print("You have ordered pizza with Ketchup and your price is 600 =>", "True" * bool((int(bool(600 - overal_price)) - 1)) + "False" * (int(bool(600 - overal_price))))
print("You have ordered kebab with Ketchup and your price is 800 =>", "True" * bool((int(bool(800 - overal_price)) - 1)) + "False" * (int(bool(800 - overal_price))))
print("You have ordered kebab with Mayonez and your price is 820 =>", "True" * bool((int(bool(820 - overal_price)) - 1)) + "False" * (int(bool(820 - overal_price))))

# 4th with better solution1

import time
print("Welcome to food court")

time.sleep(2)

food_bool = int(input("Send 1 if you want to order pizza (500 dram), send 2 if you want to order kebab (700 dram) or send 0 for nothing \n")) - 1
food_name = "pizza" * bool(food_bool - 1) + "kebab" * bool(food_bool)
food_check = food_name * int(bool(food_bool + 1)) + "no food" * bool(int(bool(food_bool + 1)) - 1)
print("Sending order to chief-cook...")

time.sleep(2)

sauce_bool = int(input("Send 1 if you want ketchup (100 dram), send 2 if you want mayonez (120 dram), or send 0 for nothing \n")) - 1
sauce_name = "ketchup" * bool(sauce_bool - 1) + "mayonez" * bool(sauce_bool)
sauce_check = sauce_name * int(bool(sauce_bool + 1)) + "no sauce" * bool(int(bool(sauce_bool + 1)) - 1)
overal_price = (500 * bool(food_bool - 1) + 700 * bool(food_bool))* bool(int(bool(food_bool + 1))) + (100 * bool(sauce_bool - 1) + 120 * bool(sauce_bool)) * bool(int(bool(sauce_bool + 1)))
print("Processing...")

time.sleep(1)

print(f"You have ordered {food_check} with {sauce_check} and your bill is {overal_price}" )