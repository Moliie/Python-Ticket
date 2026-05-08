# State tax rates
tax_rates = {
    "NY": 0.08625,
    "NJ": 0.06625,
    "CA": 0.0725,
    "FL": 0.06
}

TICKET_PRICE = 12.00

print("Welcome to the Movie Ticket App!")
print("----------------------------------")

# Display movie menu
print("\nAvailable Movies:")
for key, info in movies.items():
    print(f"{key}) {info['title']} - Seats Left: {info['seats']}")

# Movie selection
choice = input("\nSelect a movie (A-F): ").upper()

if choice not in movies:
    print("Invalid selection.")
    exit()

movie = movies[choice]
print(f"\nYou selected: {movie['title']}")
print(f"Seats available: {movie['seats']}")

# Ticket quantity
tickets = int(input("How many tickets would you like: "))

if tickets <= 0:
    print("Invalid number of tickets.")
    exit()

if tickets > movie["seats"]:
    print(f"Sorry, only {movie['seats']} seats are left.")
    exit()

# Update inventory
movie["seats"] -= tickets

# Coupon
coupon_code = input("Enter coupon code (or press Enter to skip): ").upper()
discount_rate = coupons.get(coupon_code, 0)

# State tax
state = input("Enter your state abbreviation (NY, NJ, CA, FL): ").upper()
tax_rate = tax_rates.get(state, 0)

# Price calculations
subtotal = tickets * TICKET_PRICE
discount_amount = subtotal * discount_rate
subtotal_after_discount = subtotal - discount_amount
tax_amount = subtotal_after_discount * tax_rate
total = subtotal_after_discount + tax_amount

# Final summary
print("\n----- ORDER SUMMARY -----")
print(f"Movie: {movie['title']}")
print(f"Tickets: {tickets}")
print(f"Price before discount: ${subtotal:.2f}")
print(f"Discount applied: -${discount_amount:.2f}")
print(f"Tax ({state}): +${tax_amount:.2f}")
print(f"TOTAL: ${total:.2f}")
print("--------------------------")
print("Thank you for your purchase!")
