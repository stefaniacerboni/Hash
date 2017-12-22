from LinkedList import LinkedList
from LinkedList import Node

class _Hash:
    # aggiungo underscore, per convenzione un nome preceduto da underscore
    # dovrebbe essere trattato come una parte non pubblica dall'API

    def __init__(self, m):
        self.m = m
        self.list = [None] * m
        self.collision = 0
        # print "La dimensione utilizzata sara': ", m

    # definisco la funzione hashing: metodo delle divisioni:

    def hashing(self, key, i=None):
        if i is None:
            return key % self.m
        else:
            return (i + key) % self.m


class HashLinked(_Hash):

    def __init__(self, m):
        if isprime(m):
            _Hash.__init__(self, m)
            for i in range(0, self.m):
                self.list[i] = LinkedList()
        else:
            while not isprime(m):
                m = m-1
            self.__init__(m)

    def insert(self, x):
        index = self.hashing(x)
        if not self.list[index].is_empty():
            self.collision += 1
        self.list[index].add(x)

    def search(self, x):
        index = self.hashing(x)
        if self.list[index].size() != 0:
            found = self.list[index].search(x)
            if found:
                print("Elemento {0} trovato all'indice {1}".format(x,index))
                return index
            else:
                print("Elemento con chiave {0} non presente".format(x))

    def delete(self, x):
        index = self.hashing(x)
        if self.list[index].size() != 0:
            found = self.list[index].remove(x)
            if found:
                print("Elemento {0} trovato all'indice {1} ed eliminato".format(x, index))
                return index
            else:
                print("Elemento con chiave {0} non presente".format(x))

    def tostring(self):
        print("Hash Table _ Concatenamento")
        for i in range(0, self.m):
            print("{0}| Chiavi: {1}".format(i, self.list[i].printL()))


class HashOpenAdd(_Hash):
    def __init__(self, m):
        if isprime(m):
            _Hash.__init__(self, m)
            self.sequence = 0
        else:
            while not isprime(m):
                m = m+1
            self.__init__(m)

    def insert(self, x):
        i = 0
        while i != self.m:
            index = self.hashing(x, i)
            if self.list[index] is None:
                self.list[index] = x
                self.sequence = max(i, self.sequence)
                return index
            else:
                i += 1
                if i == 1:
                    self.collision += 1
        print("Lista piena, impossibile inserire ", x)

    def delete(self, x):
        index = self.hashing(x)
        i = 0
        while self.list[index] is not None and i != self.m:
            index = self.hashing(x,i)
            if self.list[index] == x:
                print("Elemento {0} trovato all'indice {1} ed eliminato".format(x, index))
                self.list[index] = "DELETED"
                return index
            i = i+1
        print("Elemento con chiave {0} non presente".format(x))

    def search(self, x):
        index = self.hashing(x)
        i = 0
        while self.list[index] is not None and i != self.m:
            index = self.hashing(x, i)
            if self.list[index] == x:
                print("Elemento {0} trovato all'indice {1}".format(x, index))
                return index
            i = i+1
        print("Elemento con chiave {0} non presente".format(x))

    def tostring(self):
        print("Hash Table _ Indirizzamento Aperto")
        for i in range(0, self.m):
            if self.list[i] is not None:
                print("{0}| Chiave: {1}".format(i, self.list[i]))
            else:
                print("{0}| NIL".format(i, self.list[i]))


def isprime(m):
    if m <= 1:
        return False
    elif m <= 3:
        return True
    elif m % 2 == 0 or m % 3 == 0:
        return False
    i = 5
    while i * i <= m:
        if m % i == 0 or m % (i+2) == 0:
            return False
        i = i + 6
    return True

