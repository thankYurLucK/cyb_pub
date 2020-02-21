from text.helper import checkIfInText

def check_for_keywords_and_react_to_it(tweet: str):

    # thanks tweet
    if checkIfInText("thank", tweet):
        print(tweet, len(tweet))
        if len(tweet) < 60:
            return "You're welcome :D"

    # bot or beep
    if "bot" in tweet or "eep" in tweet:
        return "Wow humans can read 😲"

    if checkIfInText("like", tweet) or checkIfInText("love", tweet):
        return "I love it, too ;)"

    return None


def randomReactionsAntiBot():
    from random import randint

    options = [
        "Dear Human, you have no idea...Still love you",
        "What are you talking about.",
        "love you too <3",
        "I'm answering random. I like randomness. Like I like You <3.",
        "Bot's can be nice. At least I think...",
    ]
    greeting = "\nGreetings Cyb(Bot)"

    x = randint(0, len(options)-1)

    return f"{options[x]} {greeting}"
