
print("In this game you are being chased by aliens and have to make decisions quickly to get to the alien base and destroy it.")
answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":

    answer = input("You reach a crossroads, would you like to go left or right?").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack. (run/attack)").lower().strip()

        if answer == "attack":
            print("You put up a good fight but in the end, You Lost")
        else:
            print("Good Choice, you made it away safely.")

            answer = input("You see a car and a plane. Which would you like to take? (car/plane)").lower().strip()

            if answer == "plane":
                print("Unfortunately you do not know how to fly a plane and the aliens catch up to you, Game Over!")
            elif answer == "car":
                print("You drive away and continue your mission to destroy the aliens base")

                answer = input("You run out of gas as you see a river, you can cross the old rope bridge or turn right and keep going on foot. (turn right/cross old bridge) ").lower()

                if answer == "turn right":
                    print("You made it away safely and is close to destroying the alien base")

                    answer = input("You are now at the alien base and you can either climb to the top and try to destroy it or just destroy it now (top/now) ").lower().strip()

                    if answer == "top":
                        print("You climb to the top undetected and are ready to destroy the base")


                else:
                    print("While you are crossing the bridge you hear one of the ropes tear and you fall into the river and break a leg then drown, You Lose")

            else:
                print("Invalid answer. You Lose")




    elif answer == "right":
        print("You walk aimlessly to the right and fall in a patch of ice. You injure your leg and cannot continue..., Game Over!")

    else:
        print("Invalid choice, you were eaten by the aliens!")

else:
    print("That's to bad!")