from random import choice as c
from random import randint as r
import time


def Countdown():
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

def Add_Cards(card_list):
    sum = 0
    for i in card_list:
        sum += value_dict[i]

    return sum

def Result():
    if(Add_Cards(player_cards) > Add_Cards(computer_cards)):
        print(f"Congratulations you won!!")
    elif(Add_Cards(computer_cards) > Add_Cards(player_cards)):
        print(f"OOPS You Lost!!")
    elif(Add_Cards(player_cards) == Add_Cards(computer_cards)):
        print("Its a Tie!!")

while True:
    Question = input("Do want to play Black-Jack? (yes/no): ")
    if(Question == 'yes'):
        print("___________________________________________________________________________________________")
        print("\t\t\tRULES")
        print("1 to 10 represents there value only")
        print('"J", "Q", "K" represents 10 & "A" represents 11')
        print("You and the computer will get 2 cards")
        print("You can see one of the 2 cards of the computer") 
        print("And decide whether to take one more card or to bid all the closest to 21 will win the game")
        print("__________________________________________________________________________________________\n\n ")

        input("Click 'ENTER' to start: ")
        print("Starting!!")
        Countdown()

        box = [1,2,3,4,5,6,7,8,9,10,'Q','K','J','A']
        value_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'Q': 10, 'K': 10, 'J': 10, 'A': 11}
        player_cards = [c(box),c(box)]
        computer_cards = [c(box),c(box)]
        print(f"Your cards are {player_cards}")
        print(f"One of computer's card is {computer_cards[0]}")

        while True:
            player_question = input("Do you want to take one more card? (yes/no): ")
            if(player_question == 'yes'):
                new_player_card = c(box)
                player_cards.append(new_player_card)
                if(Add_Cards(player_cards)>21):
                            print(f"Your new card was {new_player_card}")
                            print("You went above 21 you lost!!")
                            break
                elif(Add_Cards(player_cards)<= 21):
                    print(f"Now your cards are {player_cards}")

                    if(Add_Cards(computer_cards) < 21):
                        random_num = r(0,1)
                        if(random_num == 1):
                            new_computer_card = c(box)
                            computer_cards.append(new_computer_card)

                        if(Add_Cards(computer_cards) > 21):
                            print("Computer also took one card and it went above 21\nYou won!!")
                            break

                        elif(Add_Cards(computer_cards)<=21):
                                imp_question = input("Bid or take one more card? (bid/take): ")
                                if(imp_question == "bid"):
                                    print(f"Your cards are {player_cards}")
                                    print(Add_Cards(player_cards))
                                    print(f"Computer cards are {computer_cards}")
                                    print(Add_Cards(computer_cards))
                                    Result()
                                    break
                            

            elif(player_question == 'no'):
                print(f"Your cards are {player_cards}")
                print(Add_Cards(player_cards))
                print(f"Computer's cards are {computer_cards}")
                print(Add_Cards(computer_cards))
                Result()
                break


    elif(Question == 'no'):
        print("Exiting Game")
        Countdown()
        break
    else:
        print("!!ERROR!!")