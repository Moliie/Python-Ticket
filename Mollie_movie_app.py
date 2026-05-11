#-----------------------------------------------------------------
# Author: Mollie Rejano
# Python Basics
# Date: May 8, 2026
# Assignment : Movie Ticket App Upgrade
#-----------------------------------------------------------------

# Movie information stored in a list of dictionaries
movies = [
{"title": "How To Train You Dragon", "genre": "Animation", "price": 20, "available_tickets": 50},
{"title": "Sherk", "genre": "Animation", "price": 15, "available_tickets": 50},
{"title": "Hotel For Dogs", "genre": "Action", "price": 18, "available_tickets": 25},
{"title": "The Ring", "genre": "Horror", "price": 18, "available_tickets": 35},
{"title": "Lord of the Ring", "genre": "High Fantasy & Adventure", "price": 18, "available_tickets": 60},
{"title": "Your Mine & Ours", "genre": "Romance", "price": 18, "available_tickets": 25},
]
# Welcome message and get user name
name = input("Welcome to the Movie Booker! What's your name? ")
print(f"Hello, {name}! Let's find you a movie to watch.")

# Display movie options
print("\nAvailable movies:")
for movie in movies:
print(f"- {movie['title']} ({movie['genre']}) - ${movie['price']}")

# Get user's choice and validate
while True:
chosen_movie = input("\nEnter the title of the movie you want to watch: ")
movie_found = False
for movie in movies:
if movie["title"].lower() == chosen_movie.lower():
movie_found = True

chosen_movie = movie # Store the dictionary object
break
if movie_found:
break
else:
print(f"Sorry, '{chosen_movie}' is not available. Please try again.")

# State tax rates
tax_rates = {
    "NY": 0.08625,
    "NJ": 0.06625,
    
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
