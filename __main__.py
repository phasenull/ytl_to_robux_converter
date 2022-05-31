import RatesAPI as api
devex_rate = 350
def ConvertToRobux(tl:float):
    dolarPrice = api.GetRate("usd")
    x = 100000/(devex_rate*float(dolarPrice))
    print(x * tl)
    return (x * tl)
while True:
    tl = input("TL Değeri Gir: ")
    try:
        print("{} TL = {} R$".format(tl,ConvertToRobux(float(tl))//0.01/100))
    except:
        print("""Bu gün de "{}" 'in sayı olduğunu öğrendik 🤣""".format(tl))