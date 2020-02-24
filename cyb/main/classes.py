class Task(object):
    def __init__(self,task,*args):
        self.task=task
        self.args=args

    def run(self):
        self.task(*self.args)