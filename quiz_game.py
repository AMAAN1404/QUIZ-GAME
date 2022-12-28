print("welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing != "yes":
    quit()
print("OKAY LETS PLAY!")
score = 0
    
answer = input("WHAT DOES A CPU STAND FOR?")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
     print("incorrect!")

answer = input("WHAT DOES A GPU STAND FOR?")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
     print("incorrect!")

answer = input("WHAT DOES A RAM STAND FOR?")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
     print("incorrect!")

answer = input("WHO IS THE TOP G?")
if answer.lower() == "andrew tate":
    print('correct!')
    score += 1
else:
     print("andrew tate")

print("you got " + str(score) + " questions correxct!")
print("you got" + str((score / 4) * 100) + "%")


