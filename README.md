# Cyb
Twitter Bot   
example https://twitter.com/cyb_in_www

# Setup
Intallation: `pip install tweepy`   
running: `python cyb/app.py --help`

# Customizing

## login data
+ has to be added in `main/start.py -> login`
  
+ Tutorial for getting login keys:   
 https://realpython.com/twitter-bot-python-tweepy/

## Responses to retweets
+ can be build customized especially in the file `answerfile.py`

# Project-Structure

## files
+ `app.py` mainfile
+ `import_test.py` tests import for all modules

## directories:
+ crazy Files: 
    + `antibot_hunter.py`  can search for bot messages & spam back messages
    + `word_analyzer.py` builds tweet from most used words in other tweets

+ main:  
    + `answerfile.py` contains stupid answers for special words in tweets
    + `common.py` contains useful stuff
    + `follow_handling.py` methods for handling friendships
    + `interactions_timeline_account.py` interaction with your timeline (e.g. own tweets)
    + `rate_limit.py` handles rate_limit checks -> can spawn own thread
    + `start.py` handles login and stuff
    + `tweet.py` start commenting with qutoes
+ sentence:
    + `lameSentences.py`lame but funny word builds for tweets -> random builds
    + `quote.py` handles everything with quotes
    + `special_buzz_words.py` checks for special words in tweets 
+ text:
    + `helper.py` checks if keyword in text

+ word_src:
    + `description.py` descriptions
    + `like.py` words for expressing like
    + `moods.py` moods
    + `positivewords.py` positive words (Adjectives)
    + `tolkienCharakterNames.py` names from J. R. R. Tolkien (e.g.: The Lord of the Rings)

## Useful Debugging links
+ error messages - Response code:   
https://developer.twitter.com/en/docs/basics/response-codes

# Sources

Wordlists from https://github.com/dariusk/corpora/tree/master/data/words

