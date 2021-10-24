from data import question_data
from question_model import Question

from quiz_brain import QuizBrain
question_bank = []
count = 0
for i in question_data:
    que = i["text"]
    ans = i["answer"]
    new_que = Question(que,ans)
    question_bank.append(new_que)
    count += 1
#print(question_bank[1].question)
#print(count)
#point = 0
#jcount = 5
next = QuizBrain(question_bank)
next.next_question()

