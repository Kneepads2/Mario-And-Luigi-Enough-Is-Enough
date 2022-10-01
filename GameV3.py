import time #used for the textTimer 
import random #random used for dice mechanic


class GameV3:
     titleText = "\nMARIO AND LUIGI: ENOUGH IS ENOUGH\nA game made by Dylan Tran" #title of the game and credits
     divider = "\n------------------------------------------" #a divider to make the terminal look more organized
     
     introText1 = "\nWelcome to Mario and Luigi: Enough is Enough!!!!!!!!" #a summary of the Mario games story
     introText2 = "I'm sure you're well aware of the classic Mario story, but in case you don't, here you go."
     introText3 = "One day, Mario visits Princess Peach but then she is suddenly kidnapped by Bowser, a giant turtle monster."
     introText4 = "Mario then travels the world to get to Bowser's castle where he defeats Bowser and saves the Princess!"
     introText5 = "This story is then repeated in each new Mario game."
     introText6 = "In this world, Mario has done this adventure more times than he can count and he is sick of it."
     introText7 = "Once again, Princess Peach is kidnapped. Mario decides to consult Luigi about this.\n\n"
     introTexter = [divider,introText1,introText2,introText3,introText4,introText5,introText6,introText7] #list containg the introTexts
     introLength = len(introTexter) - 1 #introTexter length
     

     mario = "Mario: " #used for intro dialogue
     luigi = "Luigi: " #used for intro dialogue
     kong = "Donkey Kong: " #donkey kong dialogue
     bowser = "Bowser: " #Bowser dialogue
     peach = "Princess Peach: "#Peach dialogue
     wario = "Wario: "#Wario dialogue

   #the intro dialogue between Mario and Luigi that leads up to the 'Choose a role' part
     introDialogue1 = (mario+"Luigi, my brother, How you been?")
     introDialogue2 = (luigi+"Tired, there's so much work to do around here and half the time I'm doing work you should be doing.")
     introDialogue3 = (luigi+"You're always traveling the world to save Peach but how many times has this happened? Are you orchestrating this kidnapping plot to get out of work?")
     introDialogue4 = (mario+"Well Luigi, that's what I came here to talk about.")
     introDialogue5 = (luigi+"So you admit it?")
     introDialogue6 = (mario+"No of course not. I wanted to talk about stopping this kidnapping plot once and for all.")
     introDialogue7 = (luigi+"Hmm, well we could just kill Bowser but you've defeated him so many times now that I feel like he should be dead by now.")
     introDialogue8 = (mario+"I know. I've tossed him into lava. I've crushed him with the Crushers. I've barraged him with hundreds of fireballs and still nothing. AND you've even sucked up his ghost tons of times now")
     introDialogue9 = (luigi+"You think Bowser's immortal?")
     introDialogue10 = (mario+"At this point, yea.")
     introDialogue11 = (luigi+"Hmmm. Mario, I once heard that Donkey Kong had a magical treasure called \"the Banana Gun\". It's said that it could kill anyone no matter what.")
     introDialogue12 = (mario+"How do you know this?")
     introDialogue13 = (luigi+"I had some drinks with Donkey Kong before and he briefly mentioned it.")
     introDialogue14 = (mario+"His Jungle is far. Do you think he'd be willing to give it to me?")
     introDialogue15 = (luigi+"Of course. I'm sure he'd symphathize with you.")
     introDialogue16 = (mario+"Alright then, I'll head there right now.")
     introDialogue17 = (luigi+"Wait, I'll go for you. You've done enough. I'll do it.")
     introDialogue18 = (mario+"No, I'll do it. It's just one more run.")
     dialogueTexter = [introDialogue1,introDialogue2,introDialogue3,introDialogue4,introDialogue5,introDialogue6,introDialogue7,introDialogue8,introDialogue9,introDialogue10,introDialogue11,introDialogue12,introDialogue13,introDialogue14,introDialogue15,introDialogue16,introDialogue17,introDialogue18]
     dialogueLength = len(dialogueTexter) - 1
     
     # a function that will print a list from left to right while having a delay between each print
     # I know i didnt use it that much and I should've used it more but it is what it is
     def textTimer(a,listEnd,var,waiting):
        while (a<=listEnd):
             print(var[a])
             time.sleep(waiting)
             a += 1
             if (a>listEnd):
                break
     loadingScreen = divider+"\nLoading............"+divider # Loading screen, its here to make the terminal look more organized
     
     #Game tutorial
     tutorialText1 = "\n\nGame tutorial time!!!"
     tutorialText2 = "When you are presented with a challenge, we will prompt you to roll the dice."
     tutorialText3 = "We'll say something like 'Roll the dice.' and then you'll enter 'roll' into the terminal. Simple?"
     tutorialText4 = "Well, good luck slaying Bowser!!!!!\n\n"
     tutorialTexter = [tutorialText1,tutorialText2,tutorialText3,tutorialText4] # tutorial list
     tutorialLength = len(tutorialTexter) - 1 #tutorial length
     
     magicalDice1 = 0 #these 3 magicDie variables are used to get the function paramters running
     magicalDice2 = 0
     magicDieTotal = 0
     roll = "" #used as function parameter 
     yourChance = 0 #used as function parameter
     
     #the 'dice based gameplay'
     #result is the input, man is the character used for dialogue, dice 1 2 and 3 are magicalDice 1 2 and Total, winChallenge is the dialogue for winning
     #loseChallenge is the dialogue used for losing, attribute is the attribute used for the challenge, attributeAndDice is where yourChance comes in
     #baseChance is the base chance the player has to win without rolling
     #winCondition is the number required to win the challenge
     def rollTheDice(result,man,dice1,dice2,dice3,perform,winChallenge,loseChallenge,attribute,attributeAndDice,baseChance,winCondition):
         result = str(input("Roll the dice (type 'roll'). "))
         if (result == "roll" or result == "gamble" or result == "roll the dice"):
            print(man+" rolls the magical die.")
            time.sleep(2)
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dice3 = dice1 +dice2
            print("Dice 1 rolls a "+str(dice1)+".")
            print("Dice 2 rolls a "+str(dice2)+".")
            time.sleep(2)
            print("The total is "+str(dice3)+".")
            print(perform)
            attributeAndDice = dice3*attribute + baseChance
            if (attributeAndDice>winCondition):
               print(winChallenge)
            else:
               print(loseChallenge)
               print("\nGAME OVER!") # you lose
               quit()
         else: # the else is for people who decide to write anything other than what is needed
            while (result != "roll" or result != "gamble" or result != "roll the dice"):#itll keep looping as long as you keep inputting random stuff
               result = str(input("Roll the Dice (type 'roll'). ")) 
               if (result == "roll" or result == "gamble" or result == "roll the dice"):
                print(man+" rolls the magical die.")
                time.sleep(2)
                dice1 = random.randint(1,6)
                dice2 = random.randint(1,6)
                dice3 = dice1 +dice2
                attributeAndDice = dice3*attribute + baseChance
                print("Dice 1 rolls a "+str(dice1))
                print("Dice 2 rolls a "+str(dice2))
                time.sleep(2)
                print("The total is "+str(dice3))
                print(perform)
                time.sleep(2)
                if (attributeAndDice>winCondition):
                  print(winChallenge)
                  
                else:
                  print(loseChallenge)
                  print("\nGAME OVER!")
                  quit()
                break #to break out of the while loop
                  
               
            
