import random

print("------------------------")
print("---Snakes and Ladders---")
print("------------------------")

dict={15:5,43:10,98:23,52:20,62:30, 0:0 ,10:10,35:8,91:2,24:40,80:20}
player1=0
player2=0

name1 = str(input("Enter first player name: "))
name2 = str(input("Enter second player name: "))


while player1<=100 and player2<=100:
    # logic
    input("Press enter ")
    dice1=random.randint(1,6)
    print("Dice 1   : ",dice1)
    player1= player1 + dice1
    print("Player 1 :",player1)
    input("Press enter ")
    dice2=random.randint(1,6)
    print("Dice 2   : ",dice2)
    player2= player2 + dice2
    print("Player 2 :",player2)
    

    #conditions for winner and looser....................
    if player1 >= 100:
        print("----------------")
        print(name1,"has Won")
        print("----------------")
        print(name2,"has lost")
        # break
    elif player2 >= 100:
        print("----------------")
        print(name2,"has Won")
        print("----------------")
        print(name1,"has lost")
        # break

    # conditions for snakes ..........................    
    elif player1 ==15:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player1 = player1-dict[15]
        print("Now Player 1 :",player1)

    elif player2 ==15:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player2 = player2-dict[15] 
        print("Now Player 2 :",player2)

    elif player1 ==43:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player1 = player1-dict[43]
        print("Now Player 1 :",player1)

    elif player2 ==43:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player2 = player2-dict[43]
        print("Now Player 2 :",player2) 

    elif player1 ==98:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player1 = player1-dict[98]
        print("Now Player 1 :",player1)

    elif player2 ==98:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player2 = player2-dict[15] 
        print("Now Player 2 :",player2)    

    elif player1 ==52:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player1 = player1-dict[52]
        print("Now Player 1 :",player1)

    elif player2 ==52:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player2 = player2-dict[52] 
        print("Now Player 2 :",player2)

    elif player1 ==62:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player1 = player1-dict[62]
        print("Now Player 1 :",player1)

    elif player2 ==62:
        print("--------------")
        print("It's a Snake ")
        print("--------------")
        player2 = player2-dict[62] 
        print("Now Player 2 :",player2)

    #conditions for ladders.................................
    elif player1 ==10:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player1 = player1+dict[10]
        print("Now Player 1 :",player1)

    elif player2 ==10:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player2 = player2+dict[10]  
        print("Now Player 2 :",player2)

    elif player1 ==35:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player1 = player1+dict[35]
        print("Now Player 1 :",player1)   

    elif player2 ==35:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player2 = player2+dict[35]
        print("Now Player 2 :",player2)     


    elif player1 ==80:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player1 = player1+dict[80]
        print("Now Player 1 :",player1)

    elif player2 ==80:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player2 = player2+dict[80]  
        print("Now Player 2 :",player2)


    elif player1 ==24:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player1 = player1+dict[24]
        print("Now Player 1 :",player1)

    elif player2 ==24:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player2 = player2+dict[24]  
        print("Now Player 2 :",player2)


    elif player1 ==91:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player1 = player1+dict[91]
        print("Now Player 1 :",player1)

    elif player2 ==91:
        print("--------------")
        print("It's a Ladder ")
        print("--------------")
        player2 = player2+dict[91]  
        print("Now Player 2 :",player2)



    