#-----------------------------------------------------------------
# Author: Mollie Rejano
# Python Basics
# Date: May 8, 2026
# Assignment : Movie Ticket App Upgrade
#-----------------------------------------------------------------

movies_list = [
    {"key": "A", "title": "How To Train You Dragon", "genre": "Animation", "price": 20, "available_tickets": 50},
    {"key": "B", "title": "Sherk", "genre": "Animation", "price": 15, "available_tickets": 50},
    {"key": "C", "title": "Hotel For Dogs", "genre": "Action", "price": 18, "available_tickets": 25},
    {"key": "D", "title": "The Ring", "genre": "Horror", "price": 18, "available_tickets": 35},
    {"key": "E", "title": "title": "Lord of the Ring", "genre": "High Fantasy & Adventure", "price": 18, "available_tickets": 60},
    {"key": "F", "title": "Your Mine & Ours", "genre": "Romance", "price": 18, "available_tickets": 25},
  

# coupon codes - can't live without in the econamy
# 5%, 10%, 15% off
valid_coupons = {
    "SAVE5": 5,
    "POPCORN10": 10,
    "VIP15": 15,
}

# state taxes - i had to look all of these up, took forever
# some states have 0 tax which is nice
state_taxes = {
    "NJ": 0.06625,
    "NY": 0.08625,
    "PA": 0.06, 

# needed the full names too for the dropdown
state_names = {
     "NJ": "New Jersey", 
     "NY": "New York",
     "PA": "Pennsylvania", 
}

# build the dropdown list - format is like "New York (NY)"
dropdown_states = []
for code in sorted(state_names.keys()):
    dropdown_states.append(state_names[code] + " (" + code + ")")

# Welcome message and get user name
name = input("Welcome to the Movie Booker! What's your name? ")
print(f"Hello, {name}! Let's find you a movie to watch.")
# Display movie options
print("\nAvailable movies:")
for movie in movies:
print(f"- {movie['title']} ({movie['genre']}) - ${movie['price']}")
tax_rates = {
    "NY": 0.08625,
    "NJ": 0.06625,
    "PA": 0.06, 
   
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
