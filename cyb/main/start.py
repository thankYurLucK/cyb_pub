import tweepy

##  Config

def login()->tweepy.API:
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    if checkLogin(api):
        return api

    return None


##  Check Login
def checkLogin(api)->bool:
    try:
        api.verify_credentials()
        print("Authentication OK")
        return True
    except Exception as ex:
        print("Error during authentication({})".format(ex))
    return False


##  Follow follower
def followFollower(api:tweepy.API):
    for follower in tweepy.Cursor(api.followers).items():
        print("[+] following follower")
        follower.follow()