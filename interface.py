import os
from player import Human

class Interface:
    def base(func):
        def interface(**kwargs):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('         BATALHA NAVAL')
            print('-------------------------------\n')
            result = func(kwargs)
            print('\n-------------------------------')
            input('Pressionado ENTER...') 
            return result
    
        return interface

    @base
    def show_map(players, turn, func):
        '''Recebe o número do jogador, formata o campo e exibe na tela'''
        letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
        p1, p2 = players
        # Vez do jogador 1
        if turn == 0:
            # Verfica se o jogador 1 é humano
            if type(p1) == Human:
                field1 = p1.field.show
                field2 = p2.field.unshow
            else:
                field1 = p1.field.unshow
                if type(p2) == Human:
                    field2 = p2.field.show
                else:
                    field2 = p2.field.unshow
        else:
            if type(p2) == Human:
                field2 = p2.field.show
                field1 = p1.field.unshow
            else:
                field2 = p2.field.unshow
                if type(p1) == Human:
                    field1 = p1.field.show
                else:
                    field1 = p1.field.unshow

        
        for i, j in zip(letters, zip(field1, field2)):
            line = i + ' '.join(j[0]) + (' ' * 8) + ' '.join(j[1])
            print(line)
        print()

        return func()

    @base
    def show_field(player, func):
        '''Exibe o campo na tela'''
        letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
        field = player.field.show
        for i, j in zip(letters, field):
            line = i + ' ' + ' '.join(j)
            print(line)
        print()

        return func()