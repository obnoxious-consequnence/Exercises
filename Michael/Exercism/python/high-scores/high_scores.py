class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
    def latest(self):
        return self.scores[-1]
    def personal_best(self):
        return max(self.scores)
    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]
    def report(self):
        if self.latest() >= self.personal_best():
            return "Your latest score was %d. That's your personal best!" % self.latest()
        else:
            return "Your latest score was %d. That's %d short of your personal best!" % (self.latest(), self.personal_best() - self.latest())