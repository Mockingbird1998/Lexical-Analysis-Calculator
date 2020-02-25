import sys

buffer = input('Enter phrase : ')
i = 0
while i < len(buffer):
    if buffer[i] == ' ':
        i += 1
    elif buffer[i] == '(':
        print('PAR : ', buffer[i])
        i += 1
    elif buffer[i] == ')':
        print('RPAR : ', buffer[i])
        i += 1
    elif buffer[i].isdigit():
        first = i
        while i < len(buffer) and buffer[i].isdigit():
            i += 1
            if buffer[i].isalpha():
                print('Lexical Error')
                sys.exit()
            if buffer[i] == '.':
                i += 1
                if not buffer[i].isdigit():
                    print('Lexical Error')
                    sys.exit()
                while i < len(buffer) and buffer[i].isdigit():
                    i += 1
                    if buffer[i].isalpha() or buffer[i] == '.':
                        print('Lexical Error')
                        sys.exit()
        last = i
        if '.' in buffer[first:last]:
            print('DIGIT : ', buffer[first:last])
        else:
            print('Decimal: ', buffer[first:last])
    elif buffer[i] == '+':
        print('PLUS : +')
        i += 1
        if buffer[i] == ' ':
            i += 1
        if not (buffer[i].isdigit() or buffer[i] == '(' or buffer[i] == ')'):
            print('Lexical Error')
            break
    elif buffer[i] == '-':
        print('MINUS : -')
        i += 1
        if buffer[i] == ' ':
            i += 1
        if not (buffer[i].isdigit() or buffer[i] == '(' or buffer[i] == ')'):
            print('Lexical Error')
            break
    elif buffer[i] == '*':
        print('MUL : *')
        i += 1
        if buffer[i] == ' ':
            i += 1
        if not (buffer[i].isdigit() or buffer[i] == '(' or buffer[i] == ')'):
            print('Lexical Error')
            break
    elif buffer[i] == '/':
        print('DIV : /')
        i += 1
        if buffer[i] == ' ':
            i += 1
        if not (buffer[i].isdigit() or buffer[i] == '(' or buffer[i] == ')'):
            print('Lexical Error')
            break
    elif buffer[i].isalpha():
        first = i
        i += 1
        while buffer[i].isalpha() or buffer[i].isdigit() or buffer[i] == '_':
            i = i + 1
        last = i
        print('ID : ', buffer[first:last])
    elif buffer[i] == '=':
        print('ASG : =')
        i += 1
        if buffer[i] == ' ':
            i += 1
        if not buffer[i].isalpha() or not buffer[i].isdigit():
            print('Lexical Error')
            break
