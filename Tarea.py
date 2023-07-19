option=0
n=0
pila=n
option=input("Ingrese una opcion para la pila")
if option == 1:
	def init(pila):
		pila.items = [n]

else:

	if option == 2:
		def isEmpty(pila):
			return pila.items == [n]

		print(pila)
	else:

		if option == 3:
			def push(pila, item):
				n=input("Ingrese un valor a sacar de la Pila")
			pila.items.append(n)
		print(pila)

	Else

	if option == 4:
				def pop(pila):
					n=input("Ingrese un valor a sacar de la Pila")
					return pila.items.pop(n)
				print(pila)
	Else

	if option == 5:
				def top(pila):
					return pila.items[len(pila.items)-1]
				print(pila)

	def size(pila):
		return len(pila.items)
	print(pila)