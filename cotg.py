import math

regex = [0,180,360]

uhel = float(input(': '))
inp = input("chcete znat cotg hodnotu/uhel (c/u): ")
if inp == 'c':
    x = round(1/(math.tan(math.radians(int(uhel)))),3)
    if uhel in regex:
        print('wrong num, cotg nema 0,180,360, spust znovu')
    print("cotg({}) je {}".format(uhel, x))

if inp == 'u':
    x = round(math.acos(uhel/math.sqrt(1+uhel**2)),3)
    print(round(math.degrees(x),1), ' or ', round(360-(180-math.degrees(x)),1))