import json
from io import open
Conoc = False

with open("tweet.json", "r") as read_file:
    data = json.load(read_file)
    Conoc = data['Probabilidades']


archivo = open ('tweet.txt','r')
a = archivo.read()
t = a.split()
archivo.close()

def esStream(tex, CON):
    sum = 0
    prom = 0
    l = len(tex)
    ln = len(CON)
    comparacion = []
    for i in range(l):
        for j in range (ln):
            if CON[j][0] == t[i]:
                comparacion.append(CON[j])
        for l in range(len(comparacion)):
            sum += float(comparacion[l][1])
            prom = sum / len(comparacion)
        if (prom > .55):
            return "Stream"
        else:
            return "No es stream"
print(esStream(t, Conoc))

