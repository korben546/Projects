#This is the nea task 3
#This is All my own code :)
#the debug command is nice
#The references to connect and sync are for a W.I.P multiplayer.
#now it has a less dull way of playing thanks to me spending 10 mins of my life repeating the same commands
#until i got bored and made this



import random
import sys
done = 0
user1 = "placeholder"
#game loop start
while done == 0:
    #define variables which get reset after game restarts
    gamestate = True
    first = False
    play = False
    auto = False
    more = True
    second = False
    debug_auto = False
    j = -1
    deck1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    deck = []
    deck2 = []
    colour = ["Red","Yellow","Black"]
    user = []
    passw = []

    def Debug():
        #guess what this does
        print("printing all availiable variables and perhaps other stuff")
        print(command)
        print(done)
        print(gamestate)
        print(first)
        print(play)
        print(auto)
        print(debug_auto)
        print(more)
        print(mor)
        print(second)
        print(j)
        print(dlen)
        print(usern)
        print(passwo)
        for x in user:
            print(x)
        for x in passw:
            print(x)
        for x in deck1:
            print(x)
        for x in deck:
            print(x)
        for x in deck2:
            print(x)
        for x in colour:
            print(x)
        print("All done CONGRATURATIONS You are great debugger!")
        

    #start game
    while more == True:
        user.append(input("please enter username"))
        passw.append(input("please enter password"))
        mor = input("do you want to add another user keep in mind there needs to be two")
        if mor == "n" and len(passw) != 1:
            more = False
            print("done")
            login = True
            
    ready = input("are both players ready y or n ")
    if ready == "Y" or ready == "y":
        random.shuffle(deck1)
    else:
        break

        
    #put authentication here
    print("May you please login")
    while login == True:
        usern = input("Enter username")
        passwo = input("Enter password")
        j = -1
        for x in user:
            j = j + 1
            if x == usern:
                if passw[j] == passwo:
                    print ("logged on")
                    if second == True:
                        login = False
                else:
                    print("failed")
                    gamestate = False
                    done = 1
        if second == False:
            print("log into the second user please")
            second = True
            j = -1

        #after auth start gameloop
    while gamestate == True:
        if len(deck1) == 0:
            print ("the main deck is empty play to find out who wins")
            play = True
        if auto == False:
            command = input("Please type your command if you need help type Help ")
        dlen = len(deck1) - 1
        if command == "Help":
            print("Draw 1 - player 1 draws a card from the top")
            print ("Draw 2 - Must come after draw 1 player 2 draws card and if you have winning colour or number you win")
            print("Play - use after draw 2 or when deck is empty")
            print("Auto - executes all above commands")
            print("Quit - quit the game")
            print("Replay - starts a new game")
            #print("Connection - checks with other players computer to check they are still connected")

        #draw 1 draws player 1 card removes from main deck andassignes random colour from list
        #will not run if first = False and play = True or deck empty
            
        elif command == "Draw 1" and len(deck1) != 0 or command == "draw 1" and len(deck1) != 0 or command == "Auto" and len(deck1) != 0 or command == "auto" and len(deck1) != 0:
            if first != True and play == False:
                print("Drawing a random card")
                first = True
                card1 = deck1[random.randint(0,dlen)]
                colour1 = colour[random.randint(0,2)]
                deck1.remove(card1)
                deck.append(card1)
                print("You got card number " + str(card1) + " with the colour " + colour1)
                if command == "Auto" or command == "auto":
                    auto = True
                    command = "Draw 2"
                    print("automatic mode")
            else:
                print("whoops player 2 has to draw first")

        #same as draw 2
                
        elif command == "Draw 2" and len(deck1) != 0 or command == "draw 2" and len(deck1) != 0:
            if first == True and play == False:
                print("Drawing a random card")
                first = False
                card2 = deck1[random.randint(0,dlen)]
                colour2 = colour[random.randint(0,2)]
                deck1.remove(card2)
                deck2.append(card2)
                print("You got card number " + str(card2) + " with the colour " + colour2)
                play = True
                if auto == True:
                    command = "play"
                    print("continuing auto")
            else:
                print("whoops player 1 has to draw first")

        #play checks who takes the cards and if main deck is empty decides who wins
                
        elif command == "Play" and play == True or command == "play" and play == True:
            if len(deck1) == 0:
                    print("The deck is empty lets find out who won")
                    if len(deck) < len(deck2):
                        print("player 2 wins")
                        break
                    elif len(deck) > len(deck2):
                        print("player 1 wins")
                        break
                    elif len(deck) == len(deck2):
                        print("its a draw")
                        break
                    else:
                        print("Whoops something did an oopsie")
                        Debug()
            if colour1 == colour2:
                #print(colour1 + colour2)
                if card1 < card2:
                    print("player 2 takes both cards")
                    deck2.append(card1)
                    deck.remove(card1)
                elif card1 > card2:
                    print("Player 1 takes both cards")
                else:
                    print("Whoops there appears to have been an error")
                    print("Tell korben he has made a terrible mistake")
                    print("Actually tell him all this")
                    #call error debugger function
                    Debug()
            if colour1 != colour2:
                if colour1 == "Red":
                    if colour2 == "Black":
                        print("Player 1 takes both cards")
                        deck2.remove(card2)
                        deck.append(card2)
                    else:
                        print("Player 2 takes both cards")
                        deck.remove(card1)
                        deck2.append(card1)
                elif colour1 == "Yellow":
                    if colour2 == "Red":
                        print("Player 1 takes both cards")
                        deck2.remove(card2)
                        deck.append(card2)
                    else:
                        print("Player 2 takes both cards")
                        deck.remove(card1)
                        deck2.append(card1)
                elif colour1 == "Black":
                    if colour2 == "Yellow":
                        print("Player 1 takes both cards")
                        deck2.remove(card2)
                        deck.append(card2)
                    else:
                        print("player 2 takes both cards")
                        deck.remove(card1)
                        deck2.append(card1)
                        #reset variables
            if auto == True and debug_auto == False:
                auto = False
            elif auto == True and debug_auto == True:
                auto = True
                command = "auto"
            play = False
            first = False
        elif command == "Replay" or command == "replay":
            gamestate = False
            print("Bye Bye")

#this is the debugger this is used to fix stuff may break the sync between games as such the sync command is included to make p 2 variables the same as
            #p1 debugger version
            #debug for stuff

        elif command == "Debug":
            print("hey has something gone wrong")
            print("anyhow how did you find this")
            Debug()
            loop = True
            while loop == True:
                debug = input("Please enter debug commands here before returning to normal game to return type return")
                if debug == "clear1":
                    for x in deck1:
                        deck1.remove(x)
                    print("removed" + str(x))
                elif debug == "clear 2":
                    for x in deck2:
                        deck2.remove(x)
                        print("deck 2 cleared")
                elif debug == "clear":
                    for x in deck:
                        deck.remove(x)
                        print("removed " + str(x))
                elif debug == "sync":
                    #sync all variabes with p2 copy multiplayer only
                    print("sync complete")
                elif debug == "debug":
                    Debug()
                #dauto makes auto run forever to speed up testing.
                elif debug == "debug_auto":
                    print ("infinite auto on")
                    debug_auto = True
                elif debug == "return":
                    loop = False
                
else:
    done = 0


