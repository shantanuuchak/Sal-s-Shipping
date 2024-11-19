# Sal's Shipping
# Get the price for each parcel based on weight
# And also calculate the cheapest option
weight = 3

# Price Variables
price_gs = None
price_gp = 125.00
price_dr = None

# Ground Shipping
if weight <= 2:
  price_gs = (weight * 1.5) + 20
elif weight > 2 and weight <= 6:
  price_gs = (weight * 3) + 20
elif weight > 6 and weight <= 10:
  price_gs = (weight * 4) + 20
else:
  price_gs = (weight * 4.75) + 20

# Drone Shipping
if weight <= 2:
  price_dr = (weight * 4.5)
elif weight > 2 and weight <= 6:
  price_dr = (weight * 9)
elif weight > 6 and weight <= 10:
  price_dr = (weight * 12)
else:
  price_dr = (weight * 14.25)

# Print statements
print(f"The weight is {weight}")
print(f"The price for ground shipping: ${price_gs}")
print(f"The price for ground premium: ${price_gp}")
print(f"The price for drone shipping: ${price_dr}")

cheapest = {
  "name": None,
  "price": None
}

# Cheapest Option
if price_gs < price_gp and price_gs < price_dr:
  cheapest["name"] = "Ground Shipping"
  cheapest["price"] = price_gs
elif price_gp < price_gs and price_gp < price_dr:
  cheapest["name"] = "Ground Premium"
  cheapest["price"] = price_gp
else:
  cheapest["name"] = "Drone Shipping"
  cheapest["price"] = price_dr


print(f'The cheapest option is {cheapest["name"]} and the price is ${cheapest["price"]}')