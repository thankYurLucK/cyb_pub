import tweepy

from main.common import likeTweet, followUser, unfollow, comment
from random import randint
from sentence.lameSentences import loveTweet



def getAllFriends(api):
    for friend in tweepy.Cursor(api.friends).items():
        yield friend


def getFriendship(api, friend, target):
    friend_ship = api.show_friendship(friend.id, target_id=target.id)[0]
    return friend_ship


def getAllFriendList(api):
    friends = getAllFriends(api)

    out = list()
    [out.append(f) for f in friends]

    return out


def killFriendships(api, count=10):
    friends = getAllFriendList(api)
    me = api.me()

    for friend in reversed(friends):
        friend_ship = getFriendship(api, friend, me)

        if not friend_ship.following:
            print(
                f"[~] user found, who does not like me :( -> {friend.screen_name}")
            unfollow(api, friend)

            count -= 1

            if count == 0:
                return


def createRandomSearchString(length=3):
    search = ""
    for i in range(length):
        search += chr(randint(65, 90))

    print(f"[+] created search: {search}")
    return search


def getLastTweet(api, user):
    tweet = None
    try:
        tweet = api.user_timeline(user.id, count=1)[0]
        print(
            f"[+] last found for {user.screen_name} tweet from {tweet.created_at}")

    except Exception as error:
        print(error)
    return tweet


def createFriendships(api, new_count=4):

    search = createRandomSearchString(4)

    for user in api.search_users(search):

        count = user.followers_count

        if count > 2 and count < 200:
            print(f"[*] choose user {user.screen_name} with {count} friends")

            last_tweet = getLastTweet(api, user)
            if not last_tweet:
                continue

            #liking
            likeTweet(api,last_tweet)

            #comment
            msg = loveTweet()
            comment(api, last_tweet, msg)

            #follow
            followUser(api,user)

            new_count -= 1
            if new_count == 0:
                return

