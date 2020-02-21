import tweepy
from time import sleep
from threading import Timer

class MainResources(object):
    def __init__(self, name, subs: dict):
        self.name = name
        self.SubResources = subs


class SubResource(object):
    def __init__(self, name, limit, reset):
        self.name = name
        self.limit = limit
        self.reset = reset


class RateLimitStatus(object):
    def __init__(self, api: tweepy.API):
        self.api = api
        self.json = api.rate_limit_status()
        self.resources = dict()

    def printRaw(self):
        print(self.json)

    def parse(self):
        if not self.json:
            return

        for key, value in self.json["resources"].items():
            subs = dict()
            for k, v in value.items():
                sub = SubResource(k, v["limit"], v["reset"])
                subs[k] = sub

            main = MainResources(key, subs)

            self.resources[key] = main

    def getList(self):
        return self.resources.values()

    def update(self):
        self.json = self.api.rate_limit_status()

        new_resources = dict()

        for key, value in self.json["resources"].items():
            subs = dict()
            for k, v in value.items():
                sub = SubResource(k, v["limit"], v["reset"])
                subs[k] = sub

            main = MainResources(key, subs)

            new_resources[key] = main

        self.compareDictToSelf(new_resources)

    def compareDictToSelf(self, new_resources: dict):

        for key_main in self.resources.keys():
            for sub_key in self.resources[key_main].SubResources.keys():

                old = self.resources[key_main].SubResources[sub_key].limit
                new = new_resources[key_main].SubResources[sub_key].limit
                if old != new:

                    print(
                        f"Found diff in {key_main} // {sub_key} : limit changed from {old} to {new}")

                # else:
                #     print(f"{old} == {new}")


class RateLimitStatusTimer(object):

    def __init__(self,api:tweepy.API,timeDiff=5):


        self.x=RateLimitStatus(api)
        self.x.parse()
        self.timeDiff=timeDiff

    def timeR(self):
        self.x.update()
        self.setTimer()

    def setTimer(self):
        w=Timer(self.timeDiff,self.timeR)
        w.setDaemon(True)
        w.start()

    def start(self):
        self.setTimer()