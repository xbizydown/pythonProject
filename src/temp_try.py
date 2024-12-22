# house = 1000000
# buyer = "bad credit"
#
# if buyer == "good credit":
#     print("Buyer has a good credit")
#     price_down = house * 0.9
#     print(price_down)
# else:
#     print("Buyer has a bad credit")
#     price_down = house * 0.8
#     print(price_down)

name = input("Enter your name: ")

if len(name) <= 3:
    print("Your name is too short")
elif len(name) <= 12:
    print("Your name is normal length")
else:
    print("Your name is too long")

