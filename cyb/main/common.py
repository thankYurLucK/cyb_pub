import tweepy

def likeTweet(api,tweet):
    print(f"[+] liking tweet from {tweet.created_at}")
    api.create_favorite(tweet.id)
    

def followUser(api,user):
    print(f"[+] follow user {user.screen_name}")
    api.create_friendship(user.id)

def unfollow(api, target):
    print(f"[-] unfollowing { target.screen_name}")
    api.destroy_friendship(target.id)


def comment(api,tweet,msg):
    print(f"[+] commenting tweet from {tweet.created_at} with {msg}")
    api.update_status(msg,in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)