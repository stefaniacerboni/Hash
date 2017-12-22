import pickle
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import test


# input array pickle con una lista con due elementi
def __main__():
    m = 1000
    perc = [10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    lista = {'m': m, 'perc': perc}
    pickle.dump(lista, open("in.p", "wb"))
    lista = pickle.load(open("in.p", "rb"))
    test.run(lista)
    res = pickle.load(open("res.txt","rb"))
    y = []
    z = []
    res1 = res['Concatenata']
    res2 = res['IndirAperto']
    x = lista['perc']

    for i in range(0, len(x)):
        y.append(res1[str(x[i])+"%"][1])
        z.append(res2[str(x[i])+"%"][1])
    plt.xlabel('Percentuale')
    plt.ylabel('N Collisioni')
    plt.title('Hash Concatenato - Indirizzamento Aperto')
    plt.plot(x, y, 'b')
    plt.plot(x, z, 'g')
    plt.show()


if __name__ == __main__():
    __main__()
