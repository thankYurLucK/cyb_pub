from word_src.moods import moods
from word_src.tolkienCharacterNames import tolkienCharacterNames
from word_src.descriptions import descriptions
from word_src.positivewords import positivewords
from word_src.like import like_sentence

from random import randint


def feeling():
    return "I'm feeling a little bit {} now.".format(moods[randint(0,len(moods)-1)])

def seems():
    return "That seems to be {}.".format(moods[randint(0,len(moods)-1)])

def tolkienCharacter():
    return "You act as if you were {} from Middle Earth".format(tolkienCharacterNames[randint(0,len(tolkienCharacterNames)-1)])

def charakter():
    return "You might seem {}, but you're ations are {}.".format(descriptions[randint(0,len(descriptions)-1)],descriptions[randint(0,len(descriptions)-1)])

def loveTweet():
    pos=positivewords[randint(0,len(positivewords)-1)]

    if randint(0,5) >2:
        sen=like_sentence[randint(0,len(like_sentence)-1)]
        return f"{pos}, {sen}."

    return f"{pos} :D"