class Token:
    pass


title = ['asg', 'par', 'rpar', 'plus', 'minus', 'mul', 'div']
buffer = input('Enter phrase : ')
i = 0
digit = []
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
        while buffer[i].isdigit():
            i += 1
        last = i
        print('DIGIT : ', buffer[first:last])
    elif buffer[i] == '+':
        print('PLUS : +')
        i += 1
    elif buffer[i] == '-':
        print('MINUS : -')
        i += 1
    elif buffer[i] == '*':
        print('MUL : *')
        i += 1
    elif buffer[i] == '/':
        print('DIV : /')
        i += 1
