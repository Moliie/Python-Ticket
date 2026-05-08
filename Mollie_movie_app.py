#-----------------------------------------------------------------
# Author: Mollie Rejano
# Python Basics
# Date: May 8, 2026
# Assignment : Movie Ticket App Upgrade
#-----------------------------------------------------------------

# Movie information stored in a list of dictionaries
movies = [
{"title": "How To Train You Dragon", "genre": "Animation", "price": 20,
"available_tickets": 50},
{"title": "Sherk", "genre": "Animation", "price": 15,
"available_tickets": 50},
{"title": "Hotel For Dogs", "genre": "Action", "price": 18, "available_tickets":
25},
{"title": "The Ring", "genre": "Horror", "price": 18, "available_tickets":
35},
{"title": "Lord of the Ring", "genre": "High Fantasy & Adventure", "price": 18, "available_tickets":
60},
{"title": "Your Mine & Ours", "genre": "Romance", "price": 18, "available_tickets":
25},
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
