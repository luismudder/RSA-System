from os import walk, remove
class PublicKEY:
	def __init__(self, e, n):
		self.Request_file()
		bites = str(open(f'Arquivo(Um por vez)/{self.Archive}', 'rb').read())
		number = ''
		name = ''
		for x in self.Archive:
			name += str(int(ord(x))+100)
		for x in bites[2:][:(len(bites[2:]))-1]:
			c = int(ord(x))+100
			if c-100 == 92:
				number += str(ord(chr(92))+100)
			elif c-100 != 92:
				number += str(int(ord(x))+100)
		parts = int(len(number)/1200)
		if len(number)%1200>0:
			parts += 1
		file = open('Encriptado', 'w')
		file.write(f'{pow(int(name),e,n)}\n')
		for x in range(parts):
			file.write(f'{pow(int(number[x*1200:][:1200]),e,n)}\n')
		remove(f'Arquivo(Um por vez)/{self.Archive}')
	def Request_file(self):
		for dirpath, dirname, filename in walk('Arquivo(Um por vez)/'):
			for file in filename:
				self.Archive = file
PublicKEY(e,n)