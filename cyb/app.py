import argparse,tweepy
from main.start import login,followFollower

from main.interactions_timeline_account import commentLastestRetweets

from main.tweet import commentWithQutoes

from main.follower_handling import killFriendships,createFriendships

from main.rate_limit import RateLimitStatusTimer

from crazy.antibot_hunter import spam_Bot_messages

from main.classes import Task


parser = argparse.ArgumentParser(description='Running a bot')

parser.add_argument( '-r','--resp',
                    help='Responding', action="store_true", dest="respond")

# parser.add_argument( '-t','--tweet',
#                     help='tweeting qoutes', dest="tweetquotes",type=int)

parser.add_argument( "-tw",'--tweetquotes', dest="tweet_count",help="number of tweets to create with quotes"
                    )        

parser.add_argument( '-f','--foll',
                    help='following follower', action="store_true", dest="follow")

parser.add_argument( '-c','--crf',
                    help='create follower', dest="create_friends_count")

parser.add_argument( '-d','--dsf',
                    help='destroy friendhsips', dest="destroy_friends_count")

parser.add_argument( '-t','--tim',
                    help='setup Timer to check Rate limit in seconds', dest="check_rate")

parser.add_argument( '-s','--spam',
                    help='spam antiBot messages', dest="message_count")


args = parser.parse_args()

print (args)

api=login()

tasks=[]

if args.respond:
    tasks.append(Task(commentLastestRetweets,api))

if args.follow:
    tasks.append(Task(followFollower,api))


if args.tweet_count:
    count=int(args.tweet_count)

    [tasks.append(Task(commentWithQutoes,api)) for x in range(count)]

    

if args.create_friends_count:
    count=int(args.create_friends_count)
    # createFriendships
    tasks.append(Task(createFriendships,api,count))    


if args.destroy_friends_count:
    count=int(args.destroy_friends_count)

    # killFriendships
    tasks.append(Task(killFriendships,api,count))    


if args.check_rate:
    
    tim=int(args.check_rate)
    x=RateLimitStatusTimer(api,tim)
    x.start()

if args.message_count:
    
    count=int(args.message_count)
    
    # spam messages
    tasks.append(Task(spam_Bot_messages,api,count))    

for t in tasks:
    try:
        t.run()
    except Exception as ex:
        print(f"[-] error with task {t.task}")
        print(f"Excepiton {ex}")
