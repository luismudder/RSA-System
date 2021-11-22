# onde a variavel 'n' vai ficar 
# onde a variavel 'd' vai ficar

# importacoes
from os import remove

class PrivateKEY:
	def __init__(self, d, n):
		# abrindo o arquivo encriptografado
		code = open("Arquivo(Um por vez)/Encriptado", "r").readlines()

		# descriptografando o nome do arquivo
		name_code = str(pow(int(code[0]),d,n))

		# variavel que vai guardar o nome do arquivo
		name = ''

		# transformando o nome de int para str
		for x in range(int(len(name_code)/3)):
			name += str(chr(int(name_code[x*3:][:3])-100))

		# removendo o nome da lista ja que ele ja foi descriptografado
		code.pop(0)

		# variavel que vai guardar os bytes(em int) do arquivo
		data_code = ''

		# descriptografando os bytes do arquivo
		for x in code:
			data_code += str(pow(int(x),d,n))

		# variavel que vai guadar os bytes ja em str
		data = ''

		# transformando int em bytes
		for x in range(int(len(data_code)/3)):
			data += str(chr(int(data_code[x*3:][:3])-100))

		# criando um script que vai colocar os bytes do arquivo
		open('temp.py', 'w').write(f"def main():\n    open('{name}', 'wb').write(b'{data}')")

		# importando esse script
		from temp import main

		# iniciando o script
		main()

		# removendo o script
		remove('temp.py')

# chamando a class
PrivateKEY(d,n)
