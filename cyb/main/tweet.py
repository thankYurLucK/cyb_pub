import tweepy
from sentence.quote import build_Quote_Tweet_Body,searchTweets_For_Quote,getQuote


def commentWithQutoes(api:tweepy.api):
    quote=getQuote()
    tweet=searchTweets_For_Quote(quote,api)
    message=build_Quote_Tweet_Body(quote)

    api.update_status(message,in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
