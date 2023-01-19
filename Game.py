from pygame import mixer
import pygame
from time import sleep

# ************************************************ #
mixer.init()
mixer.music.load('ratsasan.mp3')
mixer.music.play(-1)
# ************************************************ #

print("Welcome to the HAUNTED MANSION!")
print("There is a distant family billionaire who has just passed way, leaving this mansion and gifting this mansion to "
      "you for $140 million.")
print("As the newfound owner, you decided to pay a visit to the mansion.")
print("The house is dated, creaky, and falling apart. You walking in the front door.")
print("You are 24+ years. You are a boy! \n ")
print("*****************************GAME-STARTED***************************** \n ")

print("Do you want to enter the dining room or living room or the bathroom?? ")

roomChoice = input("> ").lower()

if roomChoice == "dining room":
    print("You chose to go into the dining room.")
    print("There are again 2 different ways. \n 1. Kitchen \n 2. Washing area.")
    print("Where would you prefer to go : Kitchen OR Washing area?? ")

    kitchenORWashingArea = input("> ").lower()

    if kitchenORWashingArea == "kitchen":
        print("You choose to move to kitchen")
        print("You herd a scary noice saying GO FROM THIS HOUSE!!")
        mixer.music.stop()
        mixer.music.load('scary.mp3')
        pygame.image.load('scr.jpg')
        mixer.music.play()
        sleep(4)
        mixer.music.load('ratsasan.mp3')
        mixer.music.play(-1)
        print("Would you like to run away?? ")

        runAWAY = input("> ")

        if runAWAY == "yes":
            print("You choose to RUN!")
            print("Again, when you reach to the door scary voice came and said YOU LOOSER RUN AWAY! You said I will"
                  "call police and kill you.")
            print("You flourishing-ly ran away from the house...")

        elif runAWAY == "no":
            mixer.music.stop()
            mixer.music.load('scary.mp3')
            pygame.image.load('scr.jpg')
            mixer.music.play()
            sleep(4)
            mixer.music.load('ratsasan.mp3')
            mixer.music.play(-1)
            print("You are brave and choose to not run away!")
            print("You ignored the scary sound and move forward.")
            print("Suddenly...You got unconscious and teleported to the bathroom.")
            print("You tried to open the door but it was locked...")
            print("A sign was written that BATH INTO THE TUB and you compulsively agreed!")
            print("You unclothe your selves and sit in the bathtub.")
            print("You saw an entrance to the ground floor")
            print("Would you like to go in the entrance???")

            goInENTRANCE = input("> ")

            if goInENTRANCE == "yes":
                print("You said to go in entrance!!")
                print("You went in the entrance. You are now whole without clothes.")
                print("Do you want to find clothes??")

                findClothes = input("> ")

                if findClothes == "yes":
                    print("You want clothes.")
                    print("You find clothes and wore it and found that they were MILITARY Clothes and were ARMOURED"
                          "and you thought now I will be a little safe of this DEMON!! You found some guns and"
                          "equiped all the guns and now can fight from the monster/DEMON..")
                    print("You came back up and with the help of gun you break the door. You found that the demon is"
                          "in front.")
                    print("DO YOU WANT TO FIGHT FROM THE DEMONN??")

                    fightDEMON = input("> ")

                    if fightDEMON == "yes":
                        print("You tried to fight with demon but DIED beause demon is more strond than youuu!!!")
                        print("YOU ARE DEAD!!")
                        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        mixer.music.stop()
                        mixer.music.load('scary.mp3')
                        pygame.image.load('scr.jpg')
                        mixer.music.play()
                        sleep(4)
                        mixer.music.load('ratsasan.mp3')
                        mixer.music.play(-1)

                    elif fightDEMON == "no":
                        print("You tried to run away from demon but it catched you and kill you!!")
                        print("YOU ARE DEAD!!")

                    else:
                        print("INVALID INPUT!!")

                elif findClothes == "no":
                    print("You don't want clothes.")
                    print("You are at least romaing around here there for 5 hrs and now because of cold temprature"
                          "you got died!!")
                    mixer.music.stop()
                    mixer.music.load('scary.mp3')
                    pygame.image.load('scr.jpg')
                    mixer.music.play()
                    sleep(4)
                    mixer.music.load('ratsasan.mp3')
                    mixer.music.play(-1)

                else:
                    print("INVALID INPUT!!")

            elif goInENTRANCE == "no":
                print("You disagree the DEMON rule and now you are trapped in here forever.")
                print("OH! I remembered that I have phone.")
                print("Do you want to open your phone???")
                mixer.music.stop()
                mixer.music.load('scary.mp3')
                pygame.image.load('scr.jpg')
                mixer.music.play()
                sleep(4)
                mixer.music.load('ratsasan.mp3')
                mixer.music.play(-1)

                openPHONE = input("> ")

                if openPHONE == "yes":
                    print("You tried to open phone but DEMON switched it off.")
                    print("You woke up and it was all a bad dream!!!!!!!!!")
                    mixer.music.stop()
                    mixer.music.load('scary.mp3')
                    pygame.image.load('scr.jpg')
                    mixer.music.play()
                    sleep(4)
                    mixer.music.load('ratsasan.mp3')
                    mixer.music.play(-1)

                elif openPHONE == "no":
                    print("You will not open phone and trapped here forever! ")
                    print("AFTER FEW HRS! \n ")
                    print("DEMON CAME AND KILLED YOUUUUUUUUU!")
                    mixer.music.stop()
                    mixer.music.load('scary.mp3')
                    pygame.image.load('scr.jpg')
                    mixer.music.play()
                    sleep(4)
                    mixer.music.load('ratsasan.mp3')
                    mixer.music.play(-1)

                else:
                    print("INVALID INPUT!!")

            else:
                print("INVALID INPUT!!")


        else:
            print("INVALID INPUT!!")

    elif kitchenORWashingArea == "washing area":
        print("You choose to go in WASHING AREA!")
        print("You saw a way from washing machine!")
        print("Do you want to go inside the washing machine??")

        wantWASHINGMACHHINEinside = input("> ")

        if wantWASHINGMACHHINEinside == "yes":
            print("You choose that want to go in washing machine and explore the enterence!!")
            print("As you steped inside the machine a strange sound came and said HEY! RUN AWAYYYY!!")
            mixer.music.stop()
            mixer.music.load('scary.mp3')
            pygame.image.load('scr.jpg')
            mixer.music.play()
            sleep(4)
            mixer.music.load('ratsasan.mp3')
            mixer.music.play(-1)

            runAWAY2 = input("> ")

            if runAWAY2 == "yes":
                print("You accepeted the DEMON order and want to RUN!")
                print("You sucessfully reach the gate and DEMON REPILIED : HAHAHAHA! LOSER YOU ARE LOSERRR!!")
                print("DO you want to say loser to the DEMON??")

                sayLOSER = input("> ")

                if sayLOSER == "yes":
                    print("You said DEMON loser!")
                    mixer.music.stop()
                    mixer.music.load('scary.mp3')
                    pygame.image.load('scr.jpg')
                    mixer.music.play()
                    sleep(4)
                    mixer.music.load('ratsasan.mp3')
                    mixer.music.play(-1)
                    print("DEMON CAME AND KILLED YOUU!!")

                elif sayLOSER == "no":
                    print("You IGNORED HIM and RAN AWAY!")

                else:
                    print("INVALID INPUT!!")

            elif runAWAY2 == "no":
                pass

            else:
                print("INVALID INPUT!!")

        elif wantWASHINGMACHHINEinside == "no":
            pass
        else:
            print("INVALID INPUT!!")

    else:
        print("INVALID INPUT!!")

elif roomChoice == "living room":
    print("You enter the living room!")
    print()

elif roomChoice == "bathroom":
    print("You enter the Bathroom.")
    print()

else:
    print("Sorry! We can't understand your input.")
