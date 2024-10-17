# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = ("large hall" if attendees > 100  else "conference room")
print(venue)

# Task 2: Venue Selection

attendees = int(input("Enter number of attendees: ")) 
venue = "large hall" if attendees > 100 else "conference room" 
recommended_thing = " " 

if attendees > 130: 
    recommended_thing = "projector" 
elif attendees > 70: 
    recommended_thing = "audio system" 
    
print(f"Venue: {venue}") 
if recommended_thing: 
    print(f"Recommended equipment: {recommended_thing}")

# Task 3: Catering Choices

attendees = int(input("Enter number of attendees: ")) 
venue = "large hall" if attendees > 100 else "conference room" 
recommended_thing = " " 

if attendees > 130: 
    recommended_thing = "projector" 
elif attendees > 70: 
    recommended_thing = "audio system" 
    

vegetarian = input(' do you want vegetarian food (yes/no): ')
Meal= "Veggie Delight Caterees" or "Gourmet Meals Cateres"

if vegetarian =="yes " :
    Meal = "Veggie Delight Caterees "
else:
    Meal = "Gourmet Meals Cateres"

print(f"Venue: {venue}") 
if recommended_thing: 
    print(f"Recommended equipment: {recommended_thing}")
print(f"Recomendeed meal: {Meal}")