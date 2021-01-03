p1 = [(4, 3), (8, 1), (3, 0)] # P1 Polinomu 3x^0 + 8x^1 + 4x^3
p2 = [(4, 3),(2, 1), (8, 7), (6, 0), (8, 9), (2, 31)] # P2 Polinomu 6x^0 + 2x^1 + 4x^3 + 8x^7 + 8x^9 + 2x^31


# Fark Fonksiyonu
def diffPoly(PolyOne, PolyTwo):
    result = []  # sonuc Listesi
    tempPolyOne = [] # P1 Polinomunun gecici listesi
    tempPolyTwo = [] # P2 Polinomunun gecici listesi

    ''' 
        Eger tempPolyOne lsitesi ilk defa doldurulacaksa
        parametre olarak polyOne icerigini bu listeye tek tek atiyoruz
    '''
    if len(tempPolyOne) == 0:
        for i in range(len(PolyOne)):
            tempPolyOne.append(PolyOne[i])

    ''' 
        Eger tempPolyTwo lsitesi ilk defa doldurulacaksa 
        parametre olarak polyTwo icerigini bu listeye tek tek atiyoruz
    '''
    if len(tempPolyTwo) == 0:
        for i in range(len(PolyTwo)):
            tempPolyTwo.append(PolyTwo[i])

    ''' 
        Elimizde iki tane liste var ve bizim bu listeleri gezmemiz gerekiyor, bunun icin de 
        PolyOne ve PolyTwo'nun uzunlugu kadar listeleri geziyoruz. Listeleri (carpan, us)olarak duzenlersek;
        usleri esitise carpanlari cikararak bunu result listesine ekliyoruz ve cikardigimiz iki degeri
        hem tempPolyOne hem de tempPolyTwo'dan siliyoruz.
    '''
    for i in range(len(PolyOne)):
        for j in range(len(PolyTwo)):
            if PolyOne[i][1] == PolyTwo[j][1]:
                equalResult = PolyOne[i][0] - PolyTwo[j][0]
                result.append((equalResult, PolyOne[i][1]))
                tempPolyOne.remove((PolyOne[i][0], PolyOne[i][1]))
                tempPolyTwo.remove((PolyTwo[j][0], PolyTwo[j][1]))
                
    ''' 
        Eger tempPolyOne gecici listede usleri esit olmayan deger varsa
        Bu degeri gidip result listesine ekliyoruz
    '''
    if len(tempPolyOne) != 0:
        for i in range(len(tempPolyOne)):
            result.append(tempPolyOne[i])

    ''' 
        Eger tempPolyTwo gecici listede usleri esit olmayan deger varsa
        Bu degeri gidip result listesine ekliyoruz
    '''
    if len(tempPolyTwo) != 0:
        for i in range(len(tempPolyTwo)):
            result.append(tempPolyTwo[i])
    ''' 
        sonucu dondururken de result listesini usse gore siralayarak geriye donduruyoruz.
    '''
    return sorted(result, key=lambda x: x[1],reverse=True)


# Toplama Fonksiyonu
def addPoly(PolyOne, PolyTwo):
    result = []  # sonuc Listesi
    tempPolyOne = [] # P1 Polinomunun gecici listesi
    tempPolyTwo = [] # P2 Polinomunun gecici listesi

    ''' 
        Eger tempPolyOne lsitesi ilk defa doldurulacaksa  
        parametre olarak polyOne icerigini bu listeye tek tek atiyoruz
    '''
    if len(tempPolyOne) == 0:
        for i in range(len(PolyOne)):
            tempPolyOne.append(PolyOne[i])

    ''' 
        Eger tempPolyTwo lsitesi ilk defa doldurulacaksa 
        parametre olarak polyTwo icerigini bu listeye tek tek atiyoruz
    '''
    if len(tempPolyTwo) == 0:
        for i in range(len(PolyTwo)):
            tempPolyTwo.append(PolyTwo[i])

    ''' 
        Elimizde iki tane liste var ve bizim bu listeleri gezmemiz gerekiyor bunun icin de 
        PolyOne ve PolyTwo uzunlugu kadar listeleri geziyoruz. Listeleri (carpan, us) olarak duzenlersek;
        usleri esitise carpanlari toplayarak bunu result listesine ekliyoruz ve topladigimiz iki degeri
        hem tempPolyOne hem de tempPolyTwo'dan siliyoruz.
    '''
    for i in range(len(PolyOne)):
        for j in range(len(PolyTwo)):
            if PolyOne[i][1] == PolyTwo[j][1]:
                equalResult = PolyOne[i][0] + PolyTwo[j][0]
                tempPolyOne.remove((PolyOne[i][0], PolyOne[i][1]))
                tempPolyTwo.remove((PolyTwo[j][0], PolyTwo[j][1]))
                result.append((equalResult, PolyOne[i][1]))

    ''' 
        Eger tempPolyOne gecici listede usleri esit olmayan deger varsa
        Bu degeri gidip result listesine ekliyoruz.
    '''
    if len(tempPolyOne) != 0:
        for i in range(len(tempPolyOne)):
            result.append(tempPolyOne[i])

    ''' 
        Eger tempPolyTwo gecici listede usleri esit olmayan deger varsa
        Bu degeri gidip result listesine ekliyoruz.
    '''
    if len(tempPolyTwo) != 0:
        for i in range(len(tempPolyTwo)):
            result.append(tempPolyTwo[i])

    ''' 
        sonucu dondururken de result listesini usse gore siralayarak geriye donduryoruz.
    '''
    return sorted(result, key=lambda x: x[1],reverse=True)

print(diffPoly(p1, p2))
print(addPoly(p1, p2))
