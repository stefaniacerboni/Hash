from __future__ import division
import random
import pickle
import hash

#input array pickle con una lista con due elementi


def run(lista):

    perc = lista['perc']
    m = lista['m']
    maxtest = 20
    result = {}
    res1 = testListaConcatenata(m, perc, maxtest)
    res2 = testIndirizzAperto(m, perc, maxtest)
    result['Concatenata'] = res1
    result['IndirAperto'] = res2
    pickle.dump(result, open("res.txt", "wb"))


def testListaConcatenata(m, perc, maxtest):
    dict = {}
    for i in range(0, len(perc)): #itero per tutte le percentuali
        n = int((perc[i]/100) * m) #numero di elementi da inserire
        collision = [None] * maxtest
        for k in range(0, maxtest):  # itero per il numero massimo di test di inserimento
            chained = hash.HashLinked(m)
            for j in range(0, n):
                value = int(1 + random.random() * 100 * chained.m)
                chained.insert(value)
            collision[k] = chained.collision
            #print("Numero collisioni:", chained.collision)
        dict[str(perc[i])+"%"] = [min(collision), sum(collision)/maxtest, max(collision)]
    return dict


def testIndirizzAperto(m, perc, maxtest):
    dict = {}
    for i in range(0, len(perc)): #itero per tutte le percentuali
        n = int((perc[i]/100) * m)
        collision = [None] * maxtest
        sequence = [None] * maxtest
        for k in range(0, maxtest):  # itero per il numero massimo di test di inserimento
            openadd = hash.HashOpenAdd(m)
            for j in range(0, n):
                value = int(1 + random.random() * 100 * openadd.m)
                openadd.insert(value)
            collision[k] = openadd.collision
            sequence[k] = openadd.sequence
            # print("Numero collisioni:", openadd.collision)
        dict[str(perc[i])+"%"] = [min(collision), sum(collision)/maxtest, max(collision), min(sequence),
                                  sum(sequence)/maxtest, max(sequence)]
    return dict