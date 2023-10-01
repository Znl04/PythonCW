# #1
# from random import randint
#
# print('Type the number around 1 and 9. You have thre turns')
# y = int(input())
# x = randint(1, 9)
#
# if x == y:
#     print(f"You won! You guess the number {y}")
# elif x != y:
#     print(f"You didn't guess the number. You have two turns")
#     y = int(input())
#     if x == y:
#         print(f"You won! You guess the number {y}")
#     elif x != y:
#         print(f"You didn't guess the number. You have one turn")
#         y = int(input())
#         if x == y:
#             print(f"You won! You guess the number {y}")
#         elif x != y:
#             print(f"You didn't guess the number. You lose. Number was {y}")
#
#
# #2
# print(" Rock-paper-scissors \n Computer picked own move \n Your turn!")
# print(" rock = 1 \n scissors = 2 \n paper = 3")
# rock = 1
# scissors = 2
# paper = 3
#
# computerMove = randint(1, 3)
# playerMove = int(input())
#
# result = ''
#
# if playerMove == rock:
#     if computerMove == scissors:
#         result = "You won computer picked scissors, You picked rock"
#     elif computerMove == paper:
#         result = "You losed computer picked paper, You picked rock"
#     elif computerMove == rock:
#         result = "Tie, computer picked rock, You picked rock"
#
# if playerMove == paper:
#     if computerMove == scissors:
#         result = "You losed computer picked paper, You picked paper"
#     elif computerMove == paper:
#         result = "Tie, computer picked rock, You picked paper"
#     elif computerMove == rock:
#         result = "You won computer picked scissors, You picked paper"
#
# if playerMove == scissors:
#     if computerMove == scissors:
#         result = "Tie, computer picked rock, You picked paper"
#     elif computerMove == paper:
#         result = "You won computer picked scissors, You picked paper"
#     elif computerMove == rock:
#         result = "You losed computer picked paper, You picked paper"
#
# print(result)

#3
def check_mobile_operator(phoneNumber):
    # phoneNumber = input()
    operators = {
        "727": "Active",
        "700": "Altel4g",
        "708": "Altel4g",
        "705": "Beeline",
        "771": "Beeline",
        "776": "Beeline",
        "777": "Beeline",
        "701": "Kcell",
        "702": "Kcell",
        "775": "Kcell",
        "778": "Kcell",
        "707": "Tele2",
        "747": "Tele2",
    }

    operator = phoneNumber[1:4]
    # check_mobile_operator()
    result = operators.get(operator, "Unknown operator")
    return(f'Your operator is {result}')
print(check_mobile_operator(input()))

#4
print('Type first and second number')
xx = int(input())
yy = int(input())
print('Type operator')
op = input()

if op == '+':
    print(xx + yy)
elif op == '-':
    print(xx - yy)
elif op == '*':
    print(xx * yy)
elif op == '/':
    print(xx / yy)
elif op == '**':
    print(xx ** yy)
elif op == '//':
    print(xx // yy)
elif op == '%':
    print(xx % yy)
