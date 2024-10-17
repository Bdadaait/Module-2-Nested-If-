#Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place== "cave":
    print("You find a hidden treasure!")


#Task 2: Setting the Scene

place = input("Choose a place: forest or cave? ")


if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place==  "cave":
    light= input("do you want light a torch or proceed in the dark ? : ")
    if light== "light a torch":
      print("You find a hidden treasure whithin 15 minutes!")
    
    else:
      print("You find a hidden treasure whithin 30 minutes!")
