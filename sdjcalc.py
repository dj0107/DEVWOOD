
def Def(base):

    global diction

    base2 = base[3:].strip(' ')
    point = base2.index('=')
    rightside = base2[point + 1 :].strip(' ')

    if base2.count('=') != 1:
        print('오류: 등호가 없거나 2개 이상입니다')
        return

    if ' ' in rightside:
        print('오류: 숫자 사이에 빈칸이 있습니다')
        return
    elif '.' in rightside:
        print('오류: 정수가 아닙니다')
        return
    elif rightside.isdigit() == False:
        print('오류: 숫자로만 이루어져있지 않습니다')
        return

    leftside = base2[0 : point - 1].strip(' ')

    if '=' in leftside or '+' in leftside or '-' in leftside \
        or '*' in leftside or '/' in leftside:
        print('오류: 변수 이름에 =, +, -, *, / 는 있어선 안 됩니다.')
        return

    if leftside.isdigit() == True:
        print('오류: 변수가 숫자로만 이루어져있습니다.')
        return


    diction[leftside] = int(rightside)
    return

def Calc(base,diction):

    base2 = base[4:].strip(' ')
    if base.count('+') == 1:
        operator = '+'
    if base.count('-') == 1:
        operator = '-'
    if base.count('*') == 1:
        operator = '*'
    if base.count('/') == 1:
        operator = '/'

    if base.count('+') + base.count('-') + base.count('*') + base.count('/') != 1:
        print('오류: 식에 +,-,*,/ 중 하나가 한 번만 등장해야 합니다.')
        return

    point = base2.index(operator)
    leftside = base2[0:point - 1].strip(' ')
    rightside = base2[point + 1 :].strip(' ')

    if leftside in diction.keys():
        left = diction[leftside]
    else:
        if leftside.isdigit():
            left = int(leftside)
        else:
            print('오류:', leftside, '는 선언하지 않은 변수입니다.')
            return

    if rightside in diction.keys():
        right = diction[rightside]
    else:
        if rightside.isdigit():
            right = int(rightside)
        else:
            print('오류:', rightside, '는 선언하지 않은 변수입니다.')
            return

    if operator == '+':
        print(left + right)
        return
    elif operator == '-':
        print(left - right)
        return
    elif operator == '*':
        print(left * right)
        return
    else:
        try:
            print(left / right)
            return
        except ZeroDivisionError:
            print('오류: 0으로 나눌 수는 없습니다.')
            return


diction = {}
stop = False

while not stop:
    base = input()

    # quit
    if base.lower()[0:4] == 'quit' and len(base) == 4:
        print('quit')
        stop = True

    # define
    elif base[0:4] == 'def ':
        Def(base)

    # calculate
    elif base[0:5] == 'calc ':
        Calc(base,diction)

    # see
    elif base.strip(' ') == 'see':
        print('-' * 26)
        for i in diction.keys():
            print(i , ':' , diction[i])
        print('-' * 26)

    # undefined
    else:
        print('undefined')