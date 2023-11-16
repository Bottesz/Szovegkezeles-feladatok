def elsofeladat():
    szoveg = str("Indul a kutya és atyúk aludni - árvíztűrő tükörfúrógép")
    i = 0
    szamlalo= 0
    hossz = len(szoveg)
    while i < hossz:
        if szoveg [i] == ' ':
            szamlalo+=1 
        i += 1
    print("A szövegben lévő szóközök száma:",{szamlalo} )

def masodikfeladat():
    szoveg = ("Indul a kutya és a tyúk aludni-árvíztűrő tükörfúrógép")
    nincsszokoz = ''
    i = 0
    while i < len(szoveg):
        if szoveg [i] != ' ':
            nincsszokoz += szoveg[i]
        i += 1
    print("Szöveg szóközök nélkül",{nincsszokoz})

#def harmadikfeladat():

