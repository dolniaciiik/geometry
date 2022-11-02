#kalkulacka - objem a obsah hexapyramid
def hexapyramid():
    h = float(input('výška objektu?'))
    s = float(input('délka strany?'))

    while  h < 0:
        print('cislo nesmi byt mensi jak nula')
        h = float(input('výška objektu?'))

    while s < 0:
        print('cislo nesmi byt mensi jak nula')
        s = float(input('délka strany?'))

    #obsah objektu

    V = (math.sqrt(3) / 2) * s  ** 2 * h

    while V < 0:
        print('Error')
        h = float(input('výška objektu?'))
        s = float(input('délka strany?'))

    #objem objektu

    P = (3 * math.sqrt(3) / 2) * (s ** 2)

    N = ((3 * s) * math.sqrt((h ** 2) + (3 * (s ** 2) / 4)))

    S = P + N 

    while S < 0:
        print('Error')
        h = float(input('výška objektu?'))
        s = float(input('délka strany?'))

    print('objem objektu je',S)
    print('obsah objektu je',V)