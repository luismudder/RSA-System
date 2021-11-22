# importacoes
#usei o Crypto apenas para  gerar numeros primos
from Crypto.Util import number
from os import mkdir
import operator

#nome da pasta que sera criada
name_dir = 'luis'#input('digite  o nome da nome pasta =>')

#Funcao do inverso muiltiplicativo modular
#peguei de um modulo, por que o que eu fiz ficou muito grande
#O nome do modulo e Sympy
def as_int(n, strict=True):
    if strict:
        try:
            if type(n) is bool:
                raise TypeError
            return operator.index(n)
        except TypeError:
            raise ValueError('%s is not an integer' % (n,))
    else:
        try:
            result = int(n)
        except TypeError:
            raise ValueError('%s is not an integer' % (n,))
        if n != result:
            raise ValueError('%s is not an integer' % (n,))
        return result
def igcdex(a, b):
    if (not a) and (not b):
        return (0, 1, 0)
    if not a:
        return (0, b//abs(b), abs(b))
    if not b:
        return (a//abs(a), 0, abs(a))
    if a < 0:
        a, x_sign = -a, -1
    else:
        x_sign = 1
    if b < 0:
        b, y_sign = -b, -1
    else:
        y_sign = 1
    x, y, r, s = 1, 0, 0, 1
    while b:
        (c, q) = (a % b, a // b)
        (a, b, r, s, x, y) = (b, c, x - q*r, y - q*s, r, s)
    return (x*x_sign, y*y_sign, a)
def mod_inverse(a, m):
    c = None
    try:
        a, m = as_int(a), as_int(m)
        if m != 1 and m != -1:
            x, y, g = igcdex(a, m)
            if g == 1:
                c = x % m
    except ValueError:
        a, m = sympify(a), sympify(m)
        if not (a.is_number and m.is_number):
            raise TypeError(filldedent('''
                Expected numbers for arguments; symbolic `mod_inverse`
                is not implemented
                but symbolic expressions can be handled with the
                similar function,
                sympy.polys.polytools.invert'''))
        big = (m > 1)
        if not (big is S.true or big is S.false):
            raise ValueError('m > 1 did not evaluate; try to simplify %s' % m)
        elif big:
            c = 1/a
    if c is None:
        raise ValueError('inverse of %s (mod %s) does not exist' % (a, m))
    return c

#gerando os numeros nessesarios para a criptografia
print('criando os numeros')
x = number.getPrime(2048)
y = number.getPrime(2048)
totient = (x-1)*(y-1)
e = number.getPrime(2048)
d = mod_inverse(e, totient)
n = y*x

#criando as pastas onde ficaram as chaves
print('criando as chaves\ncriando a chave publica')
mkdir(f'./{name_dir}')
mkdir(f'{name_dir}/chave publica')
mkdir(f'{name_dir}/chave publica/Arquivo(Um por vez)')

#pegando um modelo do meu script da chave publica
data = open('data/public.py', 'r').readlines()

#criando o arquivo da chave publica
open(f'{name_dir}/chave publica/publica.py', 'w')
publickey = open(f'{name_dir}/chave publica/publica.py', 'a')

#adicionando as variaves na chave
publickey.write(f'n = {n}\n')
publickey.write(f'e = {e}\n')

#adicionando o modelo de chave publica
for x in data:
	publickey.write(x)

publickey.close()

print('chave publica criada\ncriando a chave privada')

#criando a pasta de chave privada
mkdir(f'{name_dir}/chave privada')
mkdir(f'{name_dir}/chave privada/Arquivo(Um por vez)')

#pegando o modelo de chave privada
datap = open('data/private.py', 'r').readlines()

#criando o arquivo da chave privada
open(f'{name_dir}/chave privada/privada.py', 'w')
privatekey = open(f'{name_dir}/chave privada/privada.py', 'a')

#adicionando as variaveis na chave
privatekey.write(f'n = {n}\n')
privatekey.write(f'd = {d}\n')

#adicionando o modelo de chave privada
for x in datap:
	privatekey.write(x)
privatekey.close()

input('chave privada criada\nchaves criadas')
