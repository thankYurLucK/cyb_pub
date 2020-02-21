import tweepy
from text.helper import checkIfInText



def build_Quote_Tweet_Body(quote:dict)->str:
    """
    builds complet tweet-body with random quote,

    if no quote is provided, it will use getQuote()
    """

    if quote:
        req=quote["quote"]

        body = """
                \"{}\" \nby {}
        """.format(req["body"], req["author"])

        return body


def getQuote():
    """
    loads random quote from http://favqs.com

    returns body
    """
    import requests
    r = requests.get("https://favqs.com/api/qotd")
    try:
        body = r.json()
    except:
        body = None
        print("[-] ", r)
    return body


def searchTweets_For_Quote(quote:dict,api:tweepy.API)->tweepy.Status:
    """
    search tweets for a quote, based on tags from quote

    can be used with getQuote:  
    searchTweets_For_Quote(getQuote(),...)

    """


    if not quote:
        print("[--] error")
        return

    qt=quote["quote"]

    search=" ".join(qt["tags"]) # search parameter

    for tweet in api.search(search, result_type="recent", lang="en", count=10):
        all_keywords_in_tweet=True

        for Should_Have_Keyword in qt["tags"]:
            if not checkIfInText(Should_Have_Keyword,tweet.text):
                print("[*] Checking next tweet")
                all_keywords_in_tweet=False
        if not all_keywords_in_tweet:
            continue 

        return tweet 


        # print("[+] Commenting on {}".format(tweet.text))
        # api.update_status("\"{}\" by {}".format(qt["body"],qt["author"]),in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)


