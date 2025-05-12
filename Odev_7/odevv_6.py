import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib

matplotlib.use("Agg")

def rastgeleNoktaUret(filename='static/images/plot.png', noktaSayisi=1000):

    xKoordinatlari = np.random.randint(0,1001,noktaSayisi)
    yKoordinatlari = np.random.randint(0,1001,noktaSayisi)

    df = pd.DataFrame({"x" : xKoordinatlari, "y" : yKoordinatlari})

    df.to_excel("koordinatlar.xlsx",index=False)

    df = pd.read_excel("koordinatlar.xlsx")

    print(df)

    izgaraBoyutu = 200

    plt.figure(figsize=(10, 10))

    renkler = ["red","yellow","blue","green","orange","purple","pink","brown","black","gray"]

    renkIndex = 0

    for i in range(0,1000,izgaraBoyutu):
        renkIndex = (renkIndex +1) % len(renkler)
        for j in range(0,1000,izgaraBoyutu):
            izgaraAraligi = (xKoordinatlari >= i) & (xKoordinatlari < i+izgaraBoyutu) & (yKoordinatlari >= j) & (yKoordinatlari < j+izgaraBoyutu)  
            renkIndex = (renkIndex +1) % len(renkler)
            renk = renkler[renkIndex]

            plt.scatter(xKoordinatlari[izgaraAraligi], yKoordinatlari[izgaraAraligi], s=10, c=renk)

    plt.title('Rastgele Koordinatlar') 
    plt.xlabel('X Koordinatı') 
    plt.ylabel('Y Koordinatı') 
    plt.grid(True)
    
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    plt.savefig(filename)
    plt.close()
