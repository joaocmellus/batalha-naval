import random

class Field:
	def __init__(self, ships):
		self._field = [['-' for j in range(9)] for i in range(9)]
		self._ships = ships

	def check_pos(self, pos, _type) -> bool:
		x, y = pos
		# add
		if _type == 'add':
			if self._field[x][y] == '-':
				self.add(x, y)
				return True
			else:
				return False
		# rmv
		else:
			if self._field[x][y] in ('o', '-'):
				self.remove(x, y)
				return True
			else:
				return False

	def add(self, x, y) -> None:
		'''Adiciona um barco'''
		self._field[x][y] = 'o'

	def remove(self, x, y) -> None:
		'''Remove um barco'''
		# caso acerte o barco:
		if self._field[x][y] == 'o':
			self._field[x][y] = 'x'
			self._ships -= 1
		# caso erre o barco
		else:
			self._field[x][y] = '~'
	@property	
	def show(self) -> list:
		return self._field

	@property
	def unshow(self) -> list:
		field = self._field[:]
		for y in field:
			for x in y:
				if x == 'o':
					field[y][x] = '-'
		return field

class Player:
	def __init__(self, name, ships):
		self.field = Field(ships)
		self.name = name

	def play(self):
		pass

	def pos_ship(self):
		pass

class Human(Player):
	def __init__(self, name, ships):
		super().__init__(name, ships)

	def play(self):
		print('Onde deseja atacar? (letra/número)')
		coordinate = self._check_coordinate()
		if not coordinate:
			return False
		return True

	def pos_ship(self):
		print('Onde deseja posicionar seu barco? (letra/número)')
		coordinate = self._check_coordinate()
		if not coordinate:
			print('Coordenada inválida!')
			return False
		if self.field.check_pos(coordinate, 'add'):
			print('Barco adicionado!')
			return True
		print('Coordenada inválida!')

	def _check_coordinate(self) -> tuple or None:
		'''Verifica os dados inseridos pela usuário e transforma em uma tupla'''
		value = input()
		if len(value) == 2:
			letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
			try:
				x, y = value[0].lower(), int(value[1]) - 1
			except ValueError:
				return False
			if x not in letters:
				return False
			if y < 0 or y > 8:
				return False
			x = letters.index(x)
			return (x, y)

class Computer(Player):
	def __init__(self, ships):
		super().__init__('COMPUTADOR', ships)

	def play(self) -> tuple:
		'''Retorna a tupla das coordenadas da jogada da máquina'''
		x, y = random.randint(0, 8), random.randint(0, 8)
		return (x, y)

	def pos_ship(self):
		while True:
			coordinate = self.play()
			if not self.field.check_pos(coordinate, 'add'):
				continue
			break