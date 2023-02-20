from field import Field

class Player:
    def __init__(self, name):
        self.name = name
        self.field = Field()

    def play(self):
        pass

    def pos_ship(self):
        pass

    def attack(self, target):
        pass

    def defend(self, coordinate):
        if self.field.check_pos(coordinate, 'remove'):
            ships = self.field.ships
            self.field.remove(coordinate)
            if self.field.ships < ships:
                print('VOCÊ DESTRUIU UM BARCO') # teste
            if self.field.ships == 0:
                print('VOCÊ GANHOU') # teste
            return True
        else:
            return False

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self, text) -> tuple or None:
        """
        Recebe e valida os dados de coordenadas inseridos pelo 
        usuário e então os retorna como tupla.
        
        :param text: str texto a ser exibido
        :return: tuple(x, y) ou None caso seja uma coordenada inválida
        """
        # Receber dados
        print(text)
        value = input()

        # Validar dados
        if len(value) == 2:
            letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
            try:
                x, y = value[0].lower(), int(value[1]) - 1
            except ValueError:
                return
            if x not in letters:
                return
            if y < 0 or y > 8:
                return
            x = letters.index(x)
            return (x, y)

    def pos_ship(self):
        coordinate = self.play('Onde deseja posicionar seu barco? (letra/número)')
        if not coordinate:
            print('Coordenada inválida!')
            return False
        if self.field.check_pos(coordinate, 'add'):
            self.field.add(coordinate)
            print('Barco adicionado!')
            return True
        print('Coordenada inválida!')

    def attack(self, target):
        coordinate = self.play('Onde deseja atacar? (letra/número)')
        if not coordinate:
            print('Coordenada inválida!')
            return False
        # Realiza o ataque
        if target.defend(coordinate):
            return True
        print('Coordenada inválida!')
        
class Computer(Player):
    def __init__(self):
        super().__init__('COMPUTADOR')

    def play(self) -> tuple:
        '''Retorna a tupla das coordenadas da jogada da máquina'''
        x, y = random.randint(0, 8), random.randint(0, 8)
        return (x, y)

    def pos_ship(self):
        is_valid = False
        while not is_valid:
            coordinate = self.play()
            if self.field.check_pos(coordinate, 'add'):
                is_valid = True

    def attack(self, target):
        is_valid = False
        while not is_valid:
            coordinate = self.play()
            if target.defend(coordinate):
                is_valid = True