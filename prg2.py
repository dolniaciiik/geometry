# Zkompletoval Martin Dolniak, 2022

# imports
import math

msg = '''
Vitej v kalkulacce, @Prg    
vyber teleso:
        1 krychle
        2 kvadr
        3 ctyrboky jehlan
        4 kuzel
        5 koule
        6 komoly jehlan
        7 valec
        8 komoly kuzel
        9 trojboky jehlan
        10 sin
        11 cos
        12 tan
        13 cot
        14 to co ma flora
'''

#krychle
# Suchopar, 2022, CC BY-SA
def krychle():
    print ("Vítej v programu na výpočet objemu a obsahu krychle")
    while True:
        a = int(input("Zadej stranu a v cm "))
        if a > 0:
            break 
        else: 
            print ("Neplatná hodnota")
    S = (6*a*a)
    print ("Obsah je", S)
    V = (a*a*a)
    print ("Objem je", V)

#kvadr
# Dlubal, 2022, CC BY-SA
def kvadr():
    print("Vítej v programu na výpočet obsahu a objemu kvádru " ) 
    while True:
        a = int(input("Zadej délku strany a v cm " ))
        if a >0:
            break
        else:
            print("Neplatná hodnota")
    while True:
        b = int(input("Zadej délku strany b v cm " ))
        if b >0:
            break
        else:
            print("Neplatná hodnota " )
    while True:
        c = (input("Napiš zda chceš S nebo V " ))
        if c == "S" or c == "V":
            break
        else:
            print("Neplatná hodnota " )
    while True:
        if c == "V":
            break
        else:
            S = (a*2+a*b*4)
            print("Obsah kvádru je:", S)
            break

    V = (a*a*b)
    print("Objem kvádru je:", V)
    print("gg by Dubaj")

#ctyrboky jehlan
# Vurma, 2022, CC BY-SA
def ctryb_jehlan():
    print("Vítej v programu na vypočítání obsahu a objemu")
    while True:
        A = int(input("Zadej stranu A u čtverce v cm:"))
        if A > 0:
            break
        else:
            print("Špatná hodnota demente!")
    Sp = (A*A)
    print("Obsah podstavy je:", Sp)
    while True:
        B = int(input("Zadej délku výšky pro vypočítání objemu v cm:"))
        if B > 0:
            break
        else:
            print("Špatná hodnota demente!")
    V = (B)
    VH = (Sp*V/3)
    print("Objem hranolu je:", VH)

#kalkulacka - kuzel
# Luu, 2022, CC BY-SA
def kuzel():
    print("Výpočet objem a obsah kužele")
    while True:
        r=int(input("Zadej poloměr kužele v cm: "))
        if 0<r:
            break
        else:
            print("Zadej kladné číslo")
    while True:
        v=int(input("Zadej výšku kužele v cm: "))
        if 0<v:
            break
        else:
            print("Zadej kladné číslo")
    V=(math.pi*r**2*v)/3
    print("Objem kužele je",V)

    while True:
        s=int(input("Zadej stranu pláště kužele v cm: "))
        if 0<s:
            break
        else:
            print("Zadej kladné číslo")
    S=math.pi*r*(r+s)
    print ("Obsah kužele je",S) 

#koule
# Špičák, 2022, CC BY-SA
def koule():
    print ("Výtej v programu pro výpočet objemu a povrchu koule v centimetrech krychlových a čtverečních")
    while True:
        r = int (input("zadej r:"))
        if r > 0:
            break
        else:
            print ("zadal jsi nepravdivou hodnotu, r nemůže být menší než nula")
    print ("Povrch koule je:", 4 * 3.1416 * r * r, "cm2" "   Objem koule je", 4/3 * 3.1416 * r * r * r, "cm3" )

#komoly jehlan
# Kusý, 2022, CC BY-SA
def k_jehlan():
    while True:
        s1 = int(input("zadejte vrchní stranu s1 :"))
        if s1 > 0 :
            break
        else:
            print("zadal jsi číslo menší jak nula")
    while True:
    
        s2 = int(input("stranu podstavy s2 :"))
        if s2 > 0 :
            break
        else:
            print("zadal jsi číslo menší jak nula")
    while True:
        v = int(input("výšku v :"))
        if v > 0 :
            break
        else:
            print("zadal jsi číslo menší jak nula")
    S= (s1+s2*v)
    print("povrch komolého jehlanu je: ", str(V), "cm3 ")

    while True:
        s1 = int(input("zadejte vrchní stranu s1 :"))
        if s1 > 0 :
            break
        else:
            print("zadal jsi číslo menší jak nula")
    while True:
    
        s2 = int(input("stranu podstavy s2 :"))
        if s2 > 0 :
            break
        else:
            print("zadal jsi číslo menší jak nula")
    while True:
        v = int(input("výšku v :"))
        if v > 0 :
            break
        else:
            print("zadal jsi číslo menší jak nula")
    V= 0.33*(s1+s2+ math.sqrt(s1+s2))
    print("objem komolého jehlanu je: ", str(V), "cm3 ")

#valec
# Slavík, 2022, CC BY-SA
def valec():
    print ("Výpočet objemu válce")
    while True:
            r = int(input("zadej poloměr válce v cm:")) #poloměr
            if r > 0:
                break
            else:
                print("hodnota nesmí být záporná")
    while True:
            v = int(input("zadej výšku válce v cm:")) #výška
            if v > 0 :
                break
            else:
                print ("hodnota nesmí být záporná")
    π = (math.pi) #pí
    V = (π*r*r*v)
    print ("objem válce je:", V ,"cm³")

    print("Výpočet obsahu válce")
    while True:
            r = int(input("zadej poloměr válce v cm:"))
            if r > 0:
                break
            else:
                print("hodnota nesmí být záporná")
    while True:
            v = int(input("zadej výšku válce v cm:"))
            if v > 0:
                break
            else:
                print("hodnota nesmí být záporná")
    π = (math.pi)
    Sp = (π*r*r)
    Spl = (2*π*r*v)
    S = (2*Sp+Spl)
    print ("obsah válce je:", S ,"cm²")

#komoly kuzel
# Paďourek, 2022, CC BY-SA
def komoly_kuzel():
    print("vytej v programu kde se pocita objem a obsah")
    print("vytvoril matej padourek v roce 2022")
    
    while True:
        hodnotar1= int(input("zadej hodnotu ktera ma byt dosazena za podstavu 1 :"))
        if hodnotar1 > 0:
            break
        else:
            print("zadana hodnota je nespravna")
        
    while True:        
        hodnotav= int(input("zadej hodnotu ktera ma byt dosazena za v :"))
        if hodnotav > 0:
            break
        else:
            print("zadana hodnota je nespravna")
        
    while True:        
        hodnotar2= int(input("zadej hodnotu ktera ma byt dosazena za podstavu2 :"))
        if hodnotar2 > 0:
            break
        else:
            print("zadana hodnota je nespavna")

    pi = math.pi

    V=pi* hodnotav/3*(hodnotar1**2 + hodnotar1*hodnotar2 + hodnotar2**2)

    S= pi * hodnotar1**2 + pi * hodnotar2**2 + pi*(hodnotar1+hodnotar2)*math.sqrt(hodnotav**2+(hodnotar1-hodnotar2)**2)
    print("Objem  " , round(V,2))
    print("Povrch " , round(S,2))

#trojboky jehlan
# Jedinák, 2022, CC BY-SA
def troj_jehl():
    print("vytej v programu na vypocet povrchu a objemu rovnostraneho trojstraneho jehlanu")
    rozhodnuti = int(input("napis 1 pokud chces pocitat obsah napis 2 pokud chces pocitat objem"))
    if (rozhodnuti == 1):
        while True:
            strana = int(input("zadej velikost hrany v cm"))
            if (strana > 0):
                break
            else:
                print("zadal jsi neplatnou hodnotu")  
        while True:
            vyska = int(input("zadej vysku trojuhelniku"))
            if (vyska > 0):
                break
            else:
                print("zadal jsi neplatnou hodnotu")
        celypovrch1 = strana * vyska
        celypovrch2 = celypovrch1 / 2
        vysledekpovrchu = celypovrch2 * 4
        print(vysledekpovrchu)
    elif (rozhodnuti == 2):
        while True:
            strana = int(input("zadej velikost hrany v cm"))
            if (strana > 0):
                break
            else:
                print("zadal jsi neplatnou hodnotu")
        while True:
            vyska = int(input("zadej vysku trojuhelniku"))
            if (strana > 0):
                break
            else:
                print("zadal jsi neplatnou hodnotu")
        necelyobsahpodstavy = strana * vyska
        obsahpodstavy = necelyobsahpodstavy / 2
        obsahpodstavy1 = obsahpodstavy / 3
        necelyobjem = obsahpodstavy1 * vyska
        print(necelyobjem)
    else:
        print("zadal jsi spatnou hodnotu")
            
#sinus
def sinus():
    print("Vítejte v programu na výpočet Sinus.")
    print("Vytvořil Ondra Šejstal")

    while True:
        sin1 = input("Buť zadejte S pokud chcete zadávat ve stupních, nebo zadejte R pokud chcete zadávat v radiánech: ")
        if sin1=="S" or sin1=="R":
            if sin1=="S":
                try:
                    x = float(input("Zadejte hodnotu x: "))
                    print("Výseldek je: ",round(math.sin(math.radians(x)),3))
                    break
                except ValueError:
                    print("zadejte číselnou hodnotu")  
            else:
                try:
                    x = float(input("Zadejte hodnotu x: "))
                    print("Výseldek je: ",math.sin(x))
                    break
                except ValueError:
                    print("zadejte číselnou hodnotu")

#kalkulacka - kosinus
# Hasilik, 2022, CC BY-SA
def cosinus():
    while True:
        var1 = input("Buť zadejte D pokud chcete zadávat ve stupních, nebo zadejte R pokud chcete zadávat v radiánech: ")
        if var1 == "D":
            try:
                x = int(input("Zadejte hodnotu x: "))
                print("Výseldek je: ",round(math.cos(math.radians(x)),3))
                break
            except ValueError:
                print("zadejte číselnou hodnotu")    
        elif var1 == "R":
            try:
                x = int(input("Zadejte hodnotu x: "))
                print("Výseldek je: ",round(math.cos(x),2))
                break
            except ValueError:
                print("zadejte číselnou hodnotu") 
        else:
            print("Zadejte D/R!")

#tangens
# Pokorný, 2022, CC BY-SA
def tangens():
    import math

    print("Výtejte v programu na výpočet Tangensu")
    print("Vytvořil Vít Pokorný 2022")

    while True:
        A = input("Zadejte Deg pokud chcete zadávat ve stupních, zadejt Rad pokud chcete zadávat v radiánech ")
        if A == "Deg" or A == "Rad":
            break
        else:
            print("Neplatná hodnota")
    while True:
        X = int(input("Zadejte vstupní hodnotu: "))
        if A == "Deg":
            try:
                print("Výsledek je: ", round(math.tan(math.radians(X)), 3))
                break
            except ValueError or ZeroDivisionError:
                print("neplatná hodnota")
        else:
            try:
                print("Výsledek je: ", round(math.tan(X), 3))
                break
            except ValueError or ZeroDivisionError:
                print("neplatná hodnota")
    print("Konec")

#kalkulacka - kotangens
# Dolniak, 2022, CC BY-SA
def calc_cotg():
    regex = [0,180,360]
    inp = input("chcete znat cotg hodnotu/uhel (c/u): ")
    uhel = float(input(': '))

    while uhel in regex:
        print('uhel nesmi byt 0,180,360. AGAIN')
        uhel = float(input(":"))

    if inp == 'c':
        x = round(1/(math.tan(math.radians(int(uhel)))),3)
        print("cotg({}) je {}".format(uhel, x))

    elif inp == 'u':
        x = round(math.acos(uhel/math.sqrt(1+uhel**2)),3)
        print(round(math.degrees(x),1), ' or ', round(360-(180-math.degrees(x)),1))

    else:
        print('neco se rozbilo, nesnaz se to opravit')


    while True:
        var1 = input("Buť zadejte D pokud chcete zadávat ve stupních, nebo zadejte R pokud chcete zadávat v radiánech: ")
        if var1 == "D":
            try:
                x = int(input("Zadejte hodnotu x: "))
                print("Výseldek je: ",round(math.cos(math.radians(x)),3))
                break
            except ValueError:
                print("zadejte číselnou hodnotu")    
        elif var1 == "R":
            try:
                x = int(input("Zadejte hodnotu x: "))
                print("Výseldek je: ",round(math.cos(x),2))
                break
            except ValueError:
                print("zadejte číselnou hodnotu") 
        else:
            print("Zadejte D/R!")

#kalkulacka - objem a obsah hexapyramid
# Stembera, 2022, CC BY-SA
def hexapyramid():
    h = float(input('výška objektu?'))
    s = float(input('délka strany?'))

    while  h <= 0:
        print('cislo nesmi byt mensi jak nula')
        h = float(input('výška objektu?'))

    while s <= 0:
        print('cislo nesmi byt mensi jak nula')
        s = float(input('délka strany?'))

    #obsah objektu

    V = (math.sqrt(3)/2)* s**2 *h

    while V <= 0:
        print('Error')
        h = float(input('výška objektu?'))
        s = float(input('délka strany?'))

    #objem objektu

    P = (3*math.sqrt(3)/2)*(s**2)

    N = ((3*s)*math.sqrt((h**2)+(3*(s**2)/4)))

    S = P+N 

    while S < 0:
        print('Error')
        h = float(input('výška objektu?'))
        s = float(input('délka strany?'))

    print('obsah objektu je {}'.format(S))
    print('objem objektu je {}'.format(V))

print(msg)
a = input("vyber: ")
match a:
    case "1":
        krychle()
    case "2":
        kvadr()
    case "3":
        ctryb_jehlan()
    case "4":
        kuzel()
    case "5":
        koule()
    case "6":
        pass
    case "7":
        valec()
    case "8":
        komoly_kuzel()
    case "9":
        troj_jehl()
    case '10':
        sinus()
    case '11':
        cosinus()
    case '12':
        tangens()
    case '13':
        calc_cotg()
    case '14':
        hexapyramid()
    case other:
        print("ups, neumim")