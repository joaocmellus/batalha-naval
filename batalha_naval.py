import os
import time
import random

# SÍMBOLOS
# -		território inexplorado
# o 	barco aliado
# ~		local vazio (após o tiro)
# x		barco destruído

class Jogador:
	def __init__(self, nome, tipo, barcos):
		self.nome = nome
		self.tipo = tipo
		self.barcos = barcos
		self.campo = [['-' for j in range(9)] for i in range(9)]
		self.campo_visivel = [['-' for j in range(9)] for i in range(9)]

	def verificar(self, coordenada, tipo) -> bool:
		'''Verifica se é possível efetuar a ação na coordenada'''
		x, y = coordenada
		if tipo == 'add':
			if self.campo[x][y] == '-':
				return True
			else:
				return False
		elif tipo == 'rmv':
			if self.campo[x][y] in ('o', '-'):
				return True
			else:
				return False

	def adicionar(self, coordenada) -> None:
		'''Adiciona um barco'''
		x, y = coordenada
		self.campo[x][y] = 'o'

	def remover(self, coordenada) -> None:
		'''Remove um barco'''
		x, y = coordenada
		if self.campo[x][y] == 'o':
			self.campo[x][y] = 'x'
			self.campo_visivel[x][y] = 'x'
			self.barcos -= 1
		else:
			self.campo[x][y] = '~'
			self.campo_visivel[x][y] = '~'

class Partida:
	def __init__(self, jogadores, num):
		self.jogadores = jogadores
		self.barcos = num

	def nova():
		'''Inicia uma nova partida'''
		# Inserir número de barcos
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			print('               BATALHA NAVAL                \n')
			print('Quantos barcos deseja para esta rodada? (máx. 10)\n')
			num = input('> ')
			if num.isdigit():
				num = int(num)
				if num > 0 and num < 11:
					break
			print('Opção inválida. Tente novamente.')
			time.sleep(2)			

		# Perguntar se o jogador será uma pessoa
		jogadores = []
		for i in range(2):
			while True:
				os.system('cls' if os.name == 'nt' else 'clear')
				print('               BATALHA NAVAL                \n')
				print(f'Selecione o jogador {i+1}:\n\t 1 - Jogador\n\t 2 - Computador')
				tipo = input('> ')
				if tipo.isdigit():
					if int(tipo) == 1:
						print('\nInsira seu nome:')
						nome = input('> ')
						jogadores.append(Jogador(nome, 'jogador', num))
						break
					elif int(tipo) == 2:
						jogadores.append(Jogador('Computador', 'computador', num))
						break
				print('Opção inválida. Tente novamente.')
				time.sleep(2)

		return Partida(jogadores, num)

	def adicionar_barcos(self):
		'''Inicia a fase de adição dos barcos'''
		for i, jogador in enumerate(self.jogadores):
			if jogador.tipo == 'jogador':
				for j in range(self.barcos):
					while True:
						os.system('cls' if os.name == 'nt' else 'clear')
						print('               BATALHA NAVAL                \n')
						print(f'JOGADOR {i+1}:', jogador.nome)
						print('Onde deseja posicionar seu barco? (letra/número)')
						coordenada = self.inserir_coordenada()
						print(coordenada)
						if not coordenada:
							print('Opção inválida. Tente novamente.')
							time.sleep(2)
							continue
						print(jogador.verificar(coordenada, 'add'))
						if jogador.verificar(coordenada, 'add'):
							jogador.adicionar(coordenada)
							print('Barco adicionado!')
							break
						print('Opção inválida. Tente novamente.')
						time.sleep(2)
			else:
				for j in range(self.barcos):
					while True:
						coordenada = self.sortear_coordenada()
						if jogador.verificar(coordenada, 'add'):
							jogador.adicionar(coordenada)
							break

	def mostrar_campo(self, num) -> None:
		'''Recebe o número do jogador, formata o campo e exibe na tela'''
		letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
		os.system('cls' if os.name == 'nt' else 'clear')
		print('               BATALHA NAVAL                \n')
		j1, j2 = self.jogadores
		# Vez do jogador 1
		if num == 0:
			# Verfica se o jogador 1 é uma maquina
			if j1.tipo == 'jogador':
				campo1 = j1.campo
				campo2 = j2.campo_visivel
			else:
				campo1 = j1.campo_visivel
				if j2.tipo == 'jogador':
					campo2 = j2.campo
				else:
					campo2 = j2.campo_visivel
		else:
			if j2.tipo == 'jogador':
				campo2 = j2.campo
				campo1 = j1.campo_visivel
			else:
				campo2 = j2.campo_visivel
				if j1.tipo == 'jogador':
					campo1 = j1.campo
				else:
					campo1 = j1.campo_visivel

		for i, j, k in zip(letras, campo1, campo2):
			linha = i + ' ' + ' '.join(j) + '\t\t' + ' '.join(k)
			print(linha)
		print()

	def inserir_coordenada(self) -> tuple or bool:
		'''Verifica os dados inseridos pela usuário e transforma em uma tupla'''
		valor = input('> ')
		if len(valor) == 2:
			letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
			try:
				x, y = valor[0].lower(), int(valor[1]) - 1
			except ValueError:
				return False
			if x not in letras:
				return False
			if y < 0 or y > 8:
				return False
			x = letras.index(x)
			return (x, y)
		return False

	def sortear_coordenada(self) -> tuple:
		'''Retorna a tupla das coordenadas da jogada da máquina'''
		x, y = random.randint(0, 8), random.randint(0, 8)
		return (x, y)

	def turno(self, num) -> str:
		'''Executa a ação do jogador e retorna o tipo do sucesso ou falha'''
		if num == 0:
			atacante, inimigo = self.jogadores
		else:
			inimigo, atacante = self.jogadores

		if atacante.tipo == 'jogador':
			print('Onde deseja atacar? (letra/número)\n')
			coordenada = self.inserir_coordenada()
			if not coordenada:
				return 'c'
		else:
			coordenada = self.sortear_coordenada()
		if not inimigo.verificar(coordenada, 'rmv'):
			return 'a'
		barcos = inimigo.barcos
		inimigo.remover(coordenada)
		if inimigo.barcos == 0:
			return 'v'
		if barcos > inimigo.barcos:
			return 'o'
		return '-'

	def passar_vez(self, num):
		os.system('cls' if os.name == 'nt' else 'clear')
		print('               BATALHA NAVAL                \n')
		print('VEZ DO JOGADOR', num+1)
		input('> ')

def main():
	while True:
		partida = Partida.nova()
		partida.adicionar_barcos()
		vitoria = False
		x = 0
		for i in partida.jogadores:
			if i.tipo == 'jogador':
				x += 1
		# Batalha
		while vitoria == False:
			for i, jogador in enumerate(partida.jogadores):
				if vitoria == True:
					break
				partida.passar_vez(i)
				if jogador.tipo == 'jogador':
					while True:
						partida.mostrar_campo(i)
						resultado = partida.turno(i)
						if resultado == 'c':
							print('Coordenada inválida! Tente novamente.')
							continue
						elif resultado == 'a':
							print('Você já atacou esta coordenada! Ataque outra.')
							continue
						partida.mostrar_campo(i)
						if resultado == 'o':
							print('Você destruiu um barco inimigo!')
						else:
							print('Você errou...')
						if resultado == 'v':
							print(f'Parabéns {jogador.nome}, você venceu!')
							vitoria = True
						break
				else:
					while True:
						partida.mostrar_campo(i)
						resultado = partida.turno(i)
						if resultado == 'a':
							continue
						partida.mostrar_campo(i)
						if resultado == 'o':
							print('O jogador', i+1, 'destruiu um barco!')
						else:
							print('O jogador', i+1, 'errou.')
						if resultado == 'v':
							print(f'Jogador{i+1} venceu!')
						break
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			print('               BATALHA NAVAL                \n')
			if x == 1:
				print('Obrigado por jogar! Deseja jogar novamente? (s/n)')
			elif x == 2:
				print('Obrigado por jogarem! Desejam jogar novamente? (s/n)')
			else:
				print('Obrigado por ver o computador jogar :(. Deseja jogar novamente? (s/n)')
				pass
			op = input('> ').lower()
			if op not in ('s', 'n', 'sim', 'não', 'nao'):
				print('Opção inválida. Tente novamente.')
				time.sleep(2)
				continue
			else:
				break
		if op in ('n', 'não', 'nao'):
			break
		else:
			continue

main()