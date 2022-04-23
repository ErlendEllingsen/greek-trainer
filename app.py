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
        checkEquality = random.random() <= 0.175


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
print("""

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&@@@@@@@@@@@&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&@@&@&&@@&&&&&&&&&&&&@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#########BBB##BBBBB##BB###&@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&###BP5YJJJ??JYY5YYYYYYJJJJYYYPB#&@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGY?7!~~^^^^~!!!~~~~~~~^~~~!!7?J5B#&@@&&@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##GJ!!!!!~^^^^^^^^^^^^^^^~~~~!!!777?YGB#&@&&@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BP7!!!!!~~~~~~~~~~~~~~!!!777777??????5GBB&&#&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BP7!!!!!~~~~~~~~~~~~~~~~!77777??J????J5PGBB&&&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GY7!!!~~~^^^^^^^~~^^^^^^^~~!!7???JJJJY5PGGB#&&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PJ77!!~^^^^^~~~~~~~~~~~~~!!!!77??JJJJY5GGGGG&&&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5?77!7777?777~~~~~~~!7?JYY5YJJJ???JJYYYPGGPG#&&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&Y777JJJJ??!!!!~~~!!777777???JYYYJ??JYYYYPGGPB&&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GY??YY????JJJJ??!!7JYJJ?JJJ????JJY5G5JPGPPGGPB&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5?J!!777?J5P5J?75J5PGJ7?JY?YPP55YJJYBYJ5GB##BB#&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5JY?~~JJ?Y5Y?77P!~!5P?7?7??JJJYJJ?JPJJJYYGBBBBPG#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B?J?!~~!!!!777?5!:^~?PPJJ???7??????YJ7?JJJ5GP5YY55&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B7?7777777?????!^::~!?YYJJJJJJ???77777?JYY5PYYJY5Y#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J7!~~^^^~~~~~~^^:^~!!7???77!!!!!!77??JYYY55PYJJ5P@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B!!!~~~~~~~~^~~~!7??7!!JYJ777!777???JJYYYYY55YJP&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J!!!~~^~~!!~?7!7?JY5JJJJ??!!777???JJYYYYYYY5Y5&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G!!~~~~~~~~~!!!!777????777!!77???JJJYYYYYJJYY&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&7!!~~~~~~~~~!!777???7777?777????JJJYYYYYJJY#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G?!!!~~~!7?????JYYY5555J??????JJJJYYYY55G&@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G!!!!!!?YJ??7???JJY555Y?7???JJJJJYY5555#@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5!!!!!!!!!!!7????JJJJ??????JJJJY555555B@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5!!!!!!!!!!7777??JJJJJ??JJJYY55555555#@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G?7777!!!!!77?JJJJJJJJJYYY55PP5555555P@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&Y777!!!!77??????JJYYY555PPPP55555Y!^J&@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P??7777??????JJY555PPPPPP55555J7~~!JB#&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@57????JJJJJYY55PPPPPP55555YJ7!!!7Y####&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B?77????JJYY55555555555YJ?!!77!?G#&#####&@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&57?7777??JJYYYYYYYYYYYJ?77777775#&######BB#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G7?55?777??JJJJJJJJJJ?777777777JG##########BB#&&@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&?!J55PJ777??JJJJJ??77!77?77777?5#&##########B##BBBB#&@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G!~?Y55P5???JJJJ?77!!77?7777777JG###########&&&#BBBBBBBBB#&@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#J^~77JY5GGJ??JJ?7??!7??7777777?5#&&&######&@@&#####BBBBBBBGGBB#&@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#BBBGJ!~~77JY5GG5?777777??77777!!77JG&&##&&###############BBBBBBBBBGGGB
@@@@@@@@@@@@@@@@@@@@@@@&#BBGGBBBBJ7JJ7~~7JYGP5Y77?77777?7!!!!!75#&#&&#################BBBBBBBBBBBBBB
@@@@@@@@@@@@@@@@@@@&#BGGGGBBBBBBBY7??Y?~!!7Y5YY777777777??!!!?G&&################&&##BBBBBBBBBBBBBBB
""")
quizGreeks()
