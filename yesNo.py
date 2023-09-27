import random

answerKey = ['yes', 'of course', 'maybe', 'no', 'never', 'not today', 'possibly', 'likely','unlikely']
question = ''

while(question != 'quit'):
    question = input('''Ask me a yes/no question or 'quit' to quit:  ''').lower()
    if(question.startswith('am') or question.startswith('is') or question.startswith('does')):
        print(random.choice(answerKey))
    elif(question.startswith('can') or question.startswith('are') or question.startswith('was')):
        print(random.choice(answerKey))
    elif(question.startswith('were') or question.startswith('has') or question.startswith('have')):
        print(random.choice(answerKey))
    elif(question.startswith('do') or question.startswith('did') or question.startswith('should') or question.startswith('may')):
        print(random.choice(answerKey))
    elif(question =='quit'):
        print('goodbye')
    else:
        print('''I don't understand the question.''')

