import tweepy
from time import sleep
from main.answerfile import check_for_keywords_and_react_to_it


def get_Retweets_self_done(api:tweepy.api):
    for tweet in tweepy.Cursor(api.retweets_of_me,count=10).items():
        yield tweet


def get_Mentions(api:tweepy.api,id_time=None):
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=id_time,count=10).items():
        print(f"[*] found tweet for answer {tweet.text}")
        yield tweet




def getLastRetweet_Self_done(api):

    tweet = api.user_timeline( count = 1)[0]
    print(f"[+] last found tweet from {tweet.created_at}")
    return tweet


def commentLastestRetweets(api):
    last_tweet=getLastRetweet_Self_done(api)

    id_last=last_tweet.id

    for tweet in get_Mentions(api,id_time=id_last):

        # liking
        api.create_favorite(tweet.id)

        msg=check_for_keywords_and_react_to_it(tweet.text)
        if not msg:
            print("[-] no msg to answer")
            return
        print(f"[+] commenting {msg} under tweet from {tweet.created_at}")
        api.update_status(msg,in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)



