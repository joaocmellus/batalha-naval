import os

class Interface:
    def __init__(self):
        self.title =  ' '*17 + 'BATALHA NAVAL'
        self.divider = '-'*48
        self.end_text = '  PRESSIONE ENTER'

    def top_screen(self, fields=None):
        if fields:
            field = format_map(fields)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.title)
        print(self.divider + '\n')
        if fields:
            print(field)

    def bottom_screen(self):
        print('\n' + self.divider)
        input(self.end_text)

    def render(self, func, *args, field=None):
        self.top_screen(field)
        result = func(*args)
        self.bottom_screen()
        return result

def format_map(fields) -> str:
    formated_fields = []
    for field in fields:
        formated_fields.append(format_field(field))
    if len(formated_fields) == 1:
        formated_fields[0] = list(map(lambda x: ' '*13 + x ,formated_fields[0]))
    return concatenate_fields(formated_fields)

def format_field(field:list) -> list:
    """Recebe a matriz do campo e retorna uma lista de strings do campo"""
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
    numbers = [str(i)+' ' for i in range(1,10)]
    final_field = []
    final_field.append('  ' + ' '.join(letters))
    for i, j in zip(numbers, field):
        line = i + ' '.join(j)
        final_field.append(line)
    return final_field

def concatenate_fields(fields:list) -> str:
    concat_field = ['' for i in range(0,10)]
    for i, field in enumerate(fields):
        for j, line in enumerate(field):
            if i > 0:
                line = ' '*10 + line    
            concat_field[j] += line
    text = ''
    for line in concat_field:
        text += line + '\n'
    return text