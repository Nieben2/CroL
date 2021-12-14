class skills():
    def __init__(self):
        self.exp = 0
        self.return_string = ""

    def gathering(self, skill_level):
        import random
        self.success = random.randint(0,100)
        if self.success <= skill_level:
            self.return_string = "You gather a branch"
        else:
            self.return_string = "You didnt find anything"
        return self.return_string