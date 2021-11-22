# onde a variavel 'n' vai ficar
# onde a variavel 'e' vai ficar

# importacoes
from os import walk, remove

class PublicKEY:
	def __init__(self, e, n):
		# funcao que acha o arquivo que sera criptografado
		self.Request_file()

		# abrindo o arquivo que sera criptografado
		bites = str(open(f'Arquivo(Um por vez)/{self.Archive}', 'rb').read())

		# variaveis onde sao guardados os bytes que sao transformados em int
		number = ''
		name = ''

		# transformando o nome em int
		for x in self.Archive:
			# sao adicionados 100 na numero int para deixar eles com o mesmo tamanho
			# ex: 1,10,100 esses numeros tem tamanhos diferentes, mas adicionando 100
			# eles ficam com o mesmo tamanho => 101,110,200, isso facilita na hora de descriptografar
			name += str(int(ord(x))+100)

		# transformando os bytes do arquivo em int
		for x in bites[2:][:(len(bites[2:]))-1]:
			c = int(ord(x))+100

			# caso tenha '\', fiz isso por que dava bug
			if c-100 == 92:
				number += str(ord(chr(92))+100)

			# caso normal
			elif c-100 != 92:
				number += str(int(ord(x))+100)

		# a criptografia RSA so consegue criptografar numeros menores que a variavel 'n'
		# dividindo os int para conseguir criptografar
		# variavel que define em quantas pantes o int sera dividido
		parts = int(len(number)/1200)
		if len(number)%1200>0:
			parts += 1

		# criando o arquivo Encriptado
		file = open('Encriptado', 'w')

		# adicionando o nome criptografado
		file.write(f'{pow(int(name),e,n)}\n')

		# criptografando cada parte do int que foi dividido
		for x in range(parts):
			file.write(f'{pow(int(number[x*1200:][:1200]),e,n)}\n')

		# removendo o seu arquivo
		remove(f'Arquivo(Um por vez)/{self.Archive}')

	# funcao que acha seu arquivo
	def Request_file(self):
		for dirpath, dirname, filename in walk('Arquivo(Um por vez)/'):
			for file in filename:
				# varivel que guarda o nome do seu arquivo
				self.Archive = file

# chamando a class
PublicKEY(e,n)
