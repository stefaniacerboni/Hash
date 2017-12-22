import random
import hash

def __main__():
# vari test effettuati per verificare il corretto funzionamento delle tabelle, non inerenti conl'esercizio vero e proprio
    values = [None]*1009
    lista = hash.HashLinked(1000)
    lista2 = hash.HashOpenAdd(1009)
    for i in range(0, 1009):
        values[i] = int(1 + random.random() * 1000)
        print(values[i])
        lista.insert(values[i])
        lista2.insert(values[i])
    lista.tostring()
    lista2.tostring()
    lista.delete(values[5])
    print("Collisioni Indirizzamento aperto: {0}".format(lista2.collision))
    print("Collisioni Lista Concatenata: {0}".format(lista.collision))
    print("Massima sequenza indirizzamento aperto: {0}".format(lista2.sequence))
    lista.tostring()

if __name__ == __main__():
    __main__()
