from os import remove
class PrivateKEY:
	def __init__(self, d, n):
		code = open("Arquivo(Um por vez)/Encriptado", "r").readlines()
		name_code = str(pow(int(code[0]),d,n))
		name = ''
		for x in range(int(len(name_code)/3)):
			name += str(chr(int(name_code[x*3:][:3])-100))
		code.pop(0)
		data_code = ''
		for x in code:
			data_code += str(pow(int(x),d,n))
		data = ''
		for x in range(int(len(data_code)/3)):
			print()
			data += str(chr(int(data_code[x*3:][:3])-100))
		open('temp.py', 'w').write(f"def main():\n    open('{name}', 'wb').write(b'{data}')")
		from temp import main
		main()
		remove('temp.py')
PrivateKEY(d,n)