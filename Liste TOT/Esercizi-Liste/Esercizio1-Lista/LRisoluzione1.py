#es. 1
lista = [1, 2, 3, 4, 5]
print(f"Il terzo elemento della lista é: {lista[2]}") #stampa 3° elemento

#es. 2
lista.append(60) # aggiunge il n° 60 alla lista
del(lista[1]) # rimozione secondo elemento 

print(lista)

#es. 3
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
nuova = [i for i in lista2 if i %2 == 0] # crea nuova lista contente solo i numeri pari di lista2
print(nuova)

#es. 4
numeri1 = [1, 2, 3]
numeri2 = [4, 5, 6]

combinazione = numeri1 + numeri2 # concatena due liste numeri1 e numeri2
print(combinazione)