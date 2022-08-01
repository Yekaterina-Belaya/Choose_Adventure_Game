name = input("Type your name: ")
print("Welcome", name, "to tis adventure!")
answer = input("You wake up on some crossroads. Before you there's a sign, \n and you have to choose whether you go left or right. What do you choose? ").lower()
if answer == "left":
    answer = input("\nYou come to a city populated by cats. They are bigger than average cats, and walk straight, just like humans.\nYou bump into a pretty cat in a pink dress. She asks you if you got lost. \nWhat will you ask her: where you can eat (type '1') or where you can stay for a night (type '2')? ")
    if answer == "1":
        print("\nThe cat tells you to go with her. You come to her house and have a dinner with her family: \na male cat in a business suit, four little kittens in differently colored dresses, and an old servant cat. \nThen the servant cat leads you to your room, you fall asleep. \nThen you wake up at home.")
    elif answer == "2":
        print("\nThe cat tells you to go with her. She leads you to your room. \nYou regret not having asked her if you could have someting to eat \nwhen you hear the cat family having dinner downstairs. You feel hungry. \nYou fall asleep. Then you wake up at home, still hungry.")
    else:
        print("\nWrong choice. We're afraid, you've lost it. Try again!")
elif answer == "right":
    answer = input("\nYou come to a city populated by ants. They are a way bigger than average ants. \nIt seems that they are building something. One ant comes to you and gives you a cat-sized rock. \nWill you take it and follow the ants (type '1'), or will you dismiss it (type '2')? ")
    if answer == "1":
        print("\nYou bring the rock to a huge pyramid. Then the bell rings - that means the shift is over. \nYou follow the ants. It's dinner time. You get a big juicy raspberry. \nYou wake up at home, willing to buy some raspberry today.")
    elif answer == "2":
        print("\nThe ants got angry at you. You run away from them, but they are faster so they catch you. \nYou wake up at home, scared.")
    else:
        print("\nWrong choice. We're afraid, you've lost it. Try again!")
else:
    print("\nWrong choice. We're afraid, you've lost it. Try again!")
