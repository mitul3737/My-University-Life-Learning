class buttons():
    def __init__(self,word,spaces,border):
        self.word=word
        self.spaces=spaces
        self.border=border
        print(f'{self.word} Button Specifications:')
        print(f'Button name: {self.word}')
        print(f'Number of the border characters for the top and the bottom: {1+self.spaces+len(self.word)+self.spaces+1}')
        print(f'Number of spaces between the left side border and the first character of the button name: {self.spaces}')
        print(f'Number of spaces between the right side border and the last character of the button name: {self.spaces}')
        print(f'Characters representing the borders: {self.border}')
        print("\n")
        sum_0 = ""
        sum_1=""
        sum_2=" "
        sum_3=""
        sum_0=self.border*(1+self.spaces+len(self.word)+self.spaces+1)
        print(sum_0)
        s_3=self.border+(" "*self.spaces)+self.word+(" "*self.spaces)+self.border
        print(sum_3)
        print(sum_0)


word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')