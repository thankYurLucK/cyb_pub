import tweepy

import main.answerfile as answerfile

from text.helper import checkIfInText
from main.common import comment

def searchForBotTweets(api:tweepy.API,counter=10):

    search="bot"


    for tweet in api.search(search, result_type="recent", lang="en", count=100):
        if counter== 0:
            return
        if not checkIfInText(search,tweet.text):
            # print("[*] Checking next tweet")
            continue
        
        else:
            words=str(tweet.text).split(" ")
            botWords=[]
            for x in words:
                if checkIfInText(search,x):
                    botWords.append(x)
            
            for x in botWords:
                if "@" in x:
                    continue
            counter-=1
            
            yield tweet

            yield tweet


def spam_Bot_messages(api:tweepy.API,count=10):

    for tweet in searchForBotTweets(api,count):
        msg=answerfile.randomReactionsAntiBot()
        comment(api,tweet,msg)