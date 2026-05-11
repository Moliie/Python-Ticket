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
    "AL": 0.04, "AK": 0.00, "AZ": 0.056, "AR": 0.065, "CA": 0.0725,
    "CO": 0.029, "CT": 0.0635, "DE": 0.00, "FL": 0.06, "GA": 0.04,
    "HI": 0.04, "ID": 0.06, "IL": 0.0625, "IN": 0.07, "IA": 0.06,
    "KS": 0.065, "KY": 0.06, "LA": 0.0445, "ME": 0.055, "MD": 0.06,
    "MA": 0.0625, "MI": 0.06, "MN": 0.06875, "MS": 0.07, "MO": 0.04225,
    "MT": 0.00, "NE": 0.055, "NV": 0.0685, "NH": 0.00, "NJ": 0.06625,
    "NM": 0.05125, "NY": 0.08625, "NC": 0.0475, "ND": 0.05, "OH": 0.0575,
    "OK": 0.045, "OR": 0.00, "PA": 0.06, "RI": 0.07, "SC": 0.06,
    "SD": 0.045, "TN": 0.07, "TX": 0.0625, "UT": 0.0485, "VT": 0.06,
    "VA": 0.053, "WA": 0.065, "WV": 0.06, "WI": 0.05, "WY": 0.04,
}

# needed the full names too for the dropdown
state_names = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming",
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
# Display movie details and get number of tickets
print(f"\nYou chose '{chosen_movie['title']}' ({chosen_movie['genre']}) - $
{chosen_movie['price']}")
num_tickets = int(input("How many tickets would you like to purchase? "))
# Check ticket availability and calculate total price
if num_tickets <= chosen_movie["available_tickets"]:
chosen_movie["available_tickets"] -= num_tickets # Update available tickets
total_price = num_tickets * chosen_movie["price"]
print(f"\nCongratulations! You purchased {num_tickets} tickets for
'{chosen_movie['title']}' at a total of ${total_price}.")
else:
print(f"Sorry, only {chosen_movie['available_tickets']} tickets are available
for '{chosen_movie['title']}'.")
# Thank you message
print(f"\nThank you for using Movie Booker, {name}. Enjoy the movie!")
