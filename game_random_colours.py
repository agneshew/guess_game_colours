
import random

print ("Welcome im my guess game. About what colour I'm thinking?, ")

colours = ["white", "yellow", "orange", "red", "pink", "blue", "green", "black"]

print (colours)

while True:
    
    myColour = random.choice(colours)
    userColour = input ("Give me a colour. ")
    
    if myColour == userColour.lower():
        print ("Congrats you guess")
        contPlay = input ("Do you want play one more time? yes or no ")
        
        if contPlay.lower() == "yes":
            continue
        else:
            break
    else:
        print ("Sorry, a Was thinking about", myColour)
        contPlay = input ("Do you want play one more time? yes or no ")
        
        if contPlay.lower() == "yes":
            continue
        else:
            break
        
print ("Thank you for playing")

