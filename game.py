from interface import Interface
from player import Human, Computer 

class Game:
    def __init__(self, players, number_of_ships):
        self.players = players
        self.num = number_of_ships

    def new():
        '''Inicia uma nova partida'''
        # Definir número de barcos
        num = None
        while not num:
            num = Game.define_num_of_ships()
        # Definir jogadores
        players = []
        for i in range(2):
            result = None
            while not result:
                result = Game.define_player(i=i, num=num)
            players.append(result)
        return Game(players, num)

    @Interface.base
    def define_num_of_ships(args:dict):
        '''Pergunta o número de navios da partida'''
        print('Quantos barcos deseja para esta rodada? (máx. 10)\n')
        num = input()
        if num.isdigit():
            num = int(num)
            if num < 1 or num > 10:
                print('\nOpção inválida. Tente novamente.')
            return num
        print('\nOpção inválida. Tente novamente.')
    
    @Interface.base
    def define_player(args:dict):
        # Perguntar se o jogador será uma pessoa ou o Computador
        print(f'Selecione o jogador {args["i"]+1}:\n    1 - Jogador\n    2 - Computador')
        option = input()
        if option.isdigit():
            if int(option) == 1:
                print('Insira seu nome:')
                name = input()
                return Human(name.upper(), args['num'])
            elif int(option) == 2:
                return Computer(args['num'])
        print('\nOpção inválida. Tente novamente.')

    @Interface.base
    def pass_turn(self, args:dict):
        print('         VEZ DE {}'.format(self.players[args['player_num']].name))

    def start(self):
        # FASE 1: POSICIONAMENTO DOS BARCOS
        for player in self.players:
            for i in range(self.num):
                while True:         # Loop para o player adicionar o barco.
                    if type(player) == Computer:
                        player.pos_ship()
                        break
                    if Interface.show_field(player.field.show, player.pos_ship):
                        break

        # # FASE 2: ATAQUE
        # while True:
        #     