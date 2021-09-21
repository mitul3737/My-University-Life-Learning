 
class QuizBrain:
    def __init__(self,qlist):
        self.questionnumber = 0
        self.questionlist = qlist
        self.currentque = ""
    def next_question(self):
        self.choice = input()
    def __str__(self):
        self.currentque = self.questionlist[self.questionnumber]
        return f"Q{self.questionnumber}: {self.currentque} (True/False): "
