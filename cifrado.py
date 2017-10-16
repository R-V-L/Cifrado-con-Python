diccionario = {'a':'y', 'b':'p', 'c':'l', 'd':'t', 'e':'a', 'f':'v', 'g':'k', 'h':'r',
'i':'e', 'j':'z', 'k':'g', 'l':'m', 'm':'s', 'n':'h', 'o':'u', 'p':'b', 'q':'x',
'r':'n', 's':'c', 't':'d', 'u':'i', 'v':'j', 'w':'f', 'x':'q', 'y':'o', 'z':'w'}
p = dict(zip(diccionario.values(),diccionario.keys()))
s = ''

def cifrado(i):
	for l in i.lower():
		if l in diccionario:
			print(diccionario[l], end = '')
		else:
			print(l, end = '')
	else:
		print('')


def espanol(i):
	for l in i.lower():
		if l in p:
			print(p[l], end = '')
		else:
			print(l, end = '')
	else:
		print('')


while s != 'q':
	s = input("\nEscriba 'q' para quitar, 'c' para cifrar o 'd' para descifrar el mensaje: ")
	if s == 'c':
		i = input("\nEscriba la palabra a cifrar: ")
		cifrado(i)
	elif s == 'd':
		i = input("\nEscriba la palabra a descifrar: ")
		espanol(i)
	else:
		print("Comando invalido\n")