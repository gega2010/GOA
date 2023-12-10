from turtle import *

# Number of members who have to pay
members1 = 10  # Members aged over 13 is members who have to pay
members2 = 3  # Members aged under 13 is members who doesnt have to pay

#overall 13 people

ticket = 25  # Ticket price for those who have to pay

# Printing messages based on the number of members who have to pay

if members2 > 0:
    print(f"People aged 3-10 have to pay ${ticket} for a ticket.")
else:
    print("People aged 3-10 don't have to pay for tickets at all.")

if members1 > 0:
    print(f"People aged 10-13 have to pay ${ticket} for a ticket.")
else:
    print("People aged 10-13 don't have to pay for tickets at all.")