import inquirer
import random 
from termcolor import colored

greeks = {
    'delta': {
        'european': {
            'call': '+',
            'put': '-'
        },
        'american': {
            'call': '+',
            'put': '-'
        }
    },
    'gamma': {
        'european': {
            'call': '+',
            'put': '+',
            'equal': True,
        },
        'american': {
            'call': '+',
            'put': '+',
        }
    },
    'vega': {
        'european': {
            'call': '+',
            'put': '+',
            'equal': True,
        },
        'american': {
            'call': '+',
            'put': '+',
        }
    },
    'theta': {
        'european': {
            'call': '?',
            'put': '?',
        },
        'american': {
            'call': '-',
            'put': '-',
        }
    },
    'rho': {
        'european': {
            'call': '+',
            'put': '-'
        },
        'american': {
            'call': '+',
            'put': '-'
        }
    },
    'psi': {
        'european': {
            'call': '-',
            'put': '+'
        },
        'american': {
            'call': '-',
            'put': '+'
        }
    },
}


def quizGreeks():
    
    questionNr = 0

    def newQuestion():

        nonlocal questionNr
        questionNr += 1

        # Pick a random greek 
        greek = random.choice(list(greeks.keys()))
        
        
        bothTypes = random.choice([True, False])
        positiveCheck = random.choice([True, False])
        checkOptionsCallsOrPuts = random.choice(['options', 'call', 'put'])
        selectType = None if bothTypes else random.choice(['european', 'american'])

        # 10% chance for equality check
        checkEquality = random.random() <= 0.10


        isTrue = None

        # Determine isTrue based on a selection of greeks
        greekData = greeks[greek]
        if bothTypes:
            if checkEquality: 
                isTrue = False # Greeks of American options are never equal
            else:
                if positiveCheck:
                    if checkOptionsCallsOrPuts == 'options':
                        isTrue = greekData['european']['call'] == '+' and greekData['american']['call'] == '+' and greekData['european']['put'] == '+' and greekData['american']['put'] == '+'
                    elif checkOptionsCallsOrPuts == 'call':
                        isTrue = greekData['european']['call'] == '+' and greekData['american']['call'] == '+'
                    elif checkOptionsCallsOrPuts == 'put':
                        isTrue = greekData['european']['put'] == '+' and greekData['american']['put'] == '+'
                else:
                    if checkOptionsCallsOrPuts == 'options':
                        isTrue = greekData['european']['call'] == '-' and greekData['american']['call'] == '-' and greekData['european']['put'] == '-' and greekData['american']['put'] == '-'
                    elif checkOptionsCallsOrPuts == 'call':
                        isTrue = greekData['european']['call'] == '-' and greekData['american']['call'] == '-'
                    elif checkOptionsCallsOrPuts == 'put':
                        isTrue = greekData['european']['put'] == '-' and greekData['american']['put'] == '-'
        else:
            if checkEquality: 
                if selectType == 'american':
                    isTrue = False # Greeks of American options are never equal
                else: 
                    isTrue = 'equal' in greekData['european'] and greekData['european']['equal'] == True
            else: 
                if positiveCheck:
                    if checkOptionsCallsOrPuts == 'options':
                        isTrue = greekData[selectType]['call'] == '+' and greekData[selectType]['put'] == '+'
                    elif checkOptionsCallsOrPuts == 'call':
                        isTrue = greekData[selectType]['call'] == '+'
                    elif checkOptionsCallsOrPuts == 'put':
                        isTrue = greekData[selectType]['put'] == '+'
                else:
                    if checkOptionsCallsOrPuts == 'options':
                        isTrue = greekData[selectType]['call'] == '-' and greekData[selectType]['put'] == '-'
                    elif checkOptionsCallsOrPuts == 'call':
                        isTrue = greekData[selectType]['call'] == '-'
                    elif checkOptionsCallsOrPuts == 'put':
                        isTrue = greekData[selectType]['put'] == '-'


        # Uppercase first letter in greek
        greekName = greek.title()
        optionWording = 'options' if checkOptionsCallsOrPuts == 'options' else 'calls' if checkOptionsCallsOrPuts == 'call' else 'puts'

        questionWording = greekName + " is "

        if checkEquality:
            questionWording += "equal"
            optionWording = "options"
        else:
            if positiveCheck:
                positiveWord = random.choice(['Positive', 'Non-negative'])
                questionWording += positiveWord
            else:
                negativeWord = random.choice(['Negative', 'Non-positive'])
                questionWording += negativeWord

        questionWording += " for "
        if bothTypes: 
            questionWording += "both European and American " + optionWording
        else :
            questionWording += selectType.title() + " " + optionWording
        pass

        print("Question " + str(questionNr))
        questions = [
        inquirer.List('answer',
                        message=questionWording,
                        choices=['True', 'False'],
                    ),
        ]
        answer = inquirer.prompt(questions)
        if answer['answer'] == 'True':
            if isTrue:
                print(colored('Correct!', 'green'))
            else:
                print(colored('Wrong!', 'red'))
        else:
            if isTrue:
                print(colored('Wrong!', 'red'))
            else:
                print(colored('Correct!', 'green'))
        print('\n')


    exitApp = False
    while not exitApp:
        newQuestion()


    pass

print("Welcome to trainer")
quizGreeks()