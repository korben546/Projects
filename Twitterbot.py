#borrowed is the urllib2 and had to make it python3

#17 05 22 Notes
#this only runs on windows and requires twarc
#its pretty simple it just gets the latest tweets replys commants and retweets in order to play rock paper scissors
#it looks really messy but was made a while ago
from os import environ as e
from twython import Twython
from datetime import datetime
import json, os, time, random, urllib.request, re

rps = []
result = []
rock = 0
paper = 0
scissors = 0
round = 0

#Gets number of replies by running cmd version of twarc if twarc missing use pip
def tweetreplynum(id):
    os.system('cmd /c "twarc replies ' + str(id) + " > tweets.jsonl --profile WitterRock & twarc dehydrate tweets.jsonl > tweet-ids.txt")
    #os.system('cmd /k '"twarc dehydrate tweets.jsonl > tweet-ids.txt")

    #open file get number of lines
    # Opening a file 
    try:
        file = open("tweet-ids.txt","r") 
        tweetreplynum.commentcount = 0
        
        # Reading from file 
        Content = file.read() 
        split = Content.split("\n") 
        
        for x in split: 
            if x: 
                tweetreplynum.commentcount += 1
                
        print(tweetreplynum.commentcount) 
        file.close()
        os.remove("tweet-ids.txt")
        os.remove("tweet-ids.jsonl")
    except:
        tweetreplynum.commentcount = 0

#get number of retweets of latest tweet from account
def getretweetnum(id):
    os.system("cmd /c twarc retweets " + str(id) + " > retweets.jsonl & twarc dehydrate retweets.jsonl > retweets.txt")
    print(id)
    #try:
    file = open("retweets.txt","r") 
    getretweetnum.retweetcount = 0
    
     # Reading from file 
    Content = file.read() 
    split = Content.split("\n") 
        
    for x in split: 
        if x: 
            getretweetnum.retweetcount += 1
    print(getretweetnum.retweetcount) 
    file.close()

# start main instance open developer credentials and verify connection

print("rock paper scissors starting")

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
twitter.verify_credentials()
# rock is retweet like is paper comment is scissors
while True:
    draw = False
    rps = []
    result = []
    round = round + 1
    dt = datetime.now()
    twitter.update_status(status= str(dt) +'\n Rock Paper Scissors round ' + str(round) + ' will finish 3 minutes after this tweet \n to vote \U0001F9F1 retweet\n to vote \U0001F4C4 like\n to vote \U00002702 comment on this tweet \n rock has won ' + str(rock) + ' times paper has won ' + str(paper) + ' times and scissors has won ' + str(scissors) + ' times')
    #change to 180 for 3 mins 30 secs is for debugging
    time.sleep(180)
    os.system('cmd /c "twarc search from:WitterRock > latest.jsonl & twarc dehydrate latest.jsonl > latest-ids.txt"')
    latest = open("latest-ids.txt", "r").readlines()
    latelen = len(latest)
    id = latest[0]
    os.remove("latest-ids.txt")
    os.remove("latest.jsonl")
    status = twitter.show_status(id = int(id))
    print(status)
    #remove the newline
    ids = int(id)
    print(id)
 
#run twarc from command line
    likes = status['favorite_count']
    command = "cmd /c twarc retweets " + str(id) + " > retweets.jsonl & twarc dehydrate retweets.jsonl > retweets.txt"
    getretweetnum(id)
    tweetreplynum(id)
    
    #append to temporary array for sorting cos makes life easier
    rps.append(likes)
    print(likes)
    rps.append(getretweetnum.retweetcount)
    rps.append(tweetreplynum.commentcount)
    rps = sorted(rps)

    #handle if a draw and randomising to deal with draws
    dt = datetime.now()
    if rps[0] == rps[1]:
        if rps[1] == rps[2]:
            twitter.update_status(status = str(dt) +'\n its a draw \U0001F643 \n rock got ' + str(getretweetnum.retweetcount) + ' paper got ' + str(likes) + ' scissors got ' + str(tweetreplynum.commentcount))
            draw = True
        else:
            if rps [2] == likes:
                # TODO impliment ransomisation DONE
                ran = random.randint(1,2)
                if ran == 1:
                    getretweetnum.retweetcount = getretweetnum.retweetcount + 1.5
                else:
                    tweetreplynum.commentcount = tweetreplynum.commentcount + 1.5
            elif rps[2] == getretweetnum.retweetcount:
                ran = random.randint(1,2)
                if ran == 1:
                    likes = likes + 1
                else:
                    tweetreplynum.commentcount = tweetreplynum.commentcount + 1.5
            elif rps[2] == tweetreplynum.commentcount:
                ran = random.randint(1,2)
                if ran == 1:
                    getretweetnum.retweetcount = getretweetnum.retweetcount + 1.5
                else:
                    likes = likes + 1
            rps = []
            rps.append(likes)
            rps.append(getretweetnum.retweetcount)
            rps.append(tweetreplynum.commentcount)
            rps = sorted(rps)
    elif rps[1] == rps[2]:
        ran = random.randint(1,2)
        if rps[1] == likes:
            if rps [2] == getretweetnum.retweetcount:
                if ran == 1:
                    likes = likes + 1
                else:
                    getretweetnum.retweetcount = getretweetnum.retweetcount + 1.5
            elif rps [2] == tweetreplynum.commentcount:
                if ran == 1:
                    likes = likes + 1
                else:
                    tweetreplynum.commentcount = tweetreplynum.commentcount + 1.5
        if rps[1] == getretweetnum.retweetcount:
            if rps [2] == likes:
                if ran == 1:
                    likes = likes + 1
                else:
                    getretweetnum.retweetcount = getretweetnum.retweetcount + 1.5
            elif rps [2] == tweetreplynum.commentcount:
                if ran == 1:
                    getretweetnum.retweetcount = getretweetnum.retweetcount + 1.5
                else:
                    tweetreplynum.commentcount = tweetreplynum.commentcount + 1.5
        if rps[1] == tweetreplynum.commentcount:
            if rps [2] == getretweetnum.retweetcount:
                if ran == 1:
                    tweetreplynum.commentcount = tweetreplynum.commentcount + 1.5
                else:
                    getretweetnum.retweetcount = getretweetnum.retweetcount + 1.5
            elif rps [2] == likes:
                if ran == 1:
                    likes = likes + 1
                else:
                    tweetreplynum.commentcount = tweetreplynum.commentcount + 1.5
        rps = []
        rps.append(likes)
        rps.append(getretweetnum.retweetcount)
        rps.append(tweetreplynum.commentcount)
        rps = sorted(rps)
                
#turn into string so easier later

    for x in rps:
        if x == likes:
            result.append("likes")
        elif x == getretweetnum.retweetcount:
            result.append("retweet")
        elif x == tweetreplynum.commentcount:
            result.append("comment")
    if result[0] == result[1] and draw == False:
        if result[1] == result[2]:
            twitter.update_status(status = str(dt) +'\n its a draw \U0001F643 \n rock got ' + str(getretweetnum.retweetcount) + ' paper got ' + str(likes) + ' scissors got ' + str(tweetreplynum.commentcount))
            draw = True

#game logic \ is for emojis

    print(draw)
    print(result)
    if draw == False:
        try:
            if result[1] == "likes":
                if result[2] == "retweet":
                    paper = paper + 1
                    twitter.update_status(status= str(dt) +'\nlets see who won this round of rock paper scissors \n \U0001F9F1 vs \U0001F4C4 \n \U0001F4C4 wins \n rock got ' + str(getretweetnum.retweetcount) + " votes and paper got " + str(likes) + " votes" )
                elif result[2] == "comment":
                    scissors = scissors + 1
                    twitter.update_status(status= str(dt) +'\nlets see who won this round of rock paper scissors \n \U00002702 vs \U0001F4C4 \n \U00002702 wins \n scissors got ' + str(tweetreplynum.commentcount) + " votes and paper got " + str(likes) + " votes")
            if result[1] == "retweet":
                if result[2] == "likes":
                    paper = paper + 1
                    twitter.update_status(status= str(dt) +'\nlets see who won this round of rock paper scissors \n  \U0001F4C4 vs \U0001F9F1 \n \U0001F4C4 wins \n paper got ' + str(likes) + " votes and rock got " + str(getretweetnum.retweetcount) + " votes")
                elif result[2] == "comment":
                    rock = rock + 1
                    twitter.update_status(status= str(dt) +'\nlets see who won this round of rock paper scissors \n \U00002702 vs \U0001F9F1 \n \U0001F9F1 wins \n scissors got ' + str(tweetreplynum.commentcount) + " votes and rock got " + str(getretweetnum.retweetcount) + " votes")
            if result[1] == "comment":
                if result[2] == "retweet":
                    rock = rock + 1
                    twitter.update_status(status= str(dt) +'\nlets see who won this round of rock paper scissors \n \U0001F9F1 vs \U00002702 \n \U0001F9F1 wins \n rock got ' + str(getretweetnum.retweetcount) + " votes and scissors got " + str(tweetreplynum.commentcount) + " votes")
                elif result[2] == "likes":
                    scissors = scissors + 1
                    twitter.update_status(status= str(dt) +'\nlets see who won this round of rock paper scissors \n \U0001F4C4 vs \U00002702 \n \U00002702 wins \n paper got ' + str(likes) + " votes and scissors got " + str(tweetreplynum.commentcount) + " votes")
        except:
            print("stuff hasnt gone to plan failiure at gamelogic for who won")
            twitter.update_status(status='whoops something went wrong at game logic @korben5461 \n line 239 to 260 Fix Me \n \U0001F9F1 \U0001F4C4	\U00002702 \n ' + str(rps) + str(result) + str(id) + str(dt))



