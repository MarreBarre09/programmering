import datetime

print("Skriv in start året")
a = input()
a = int(a)

print("Skriv in start månaden")
b = input()
b = int(b)

print("Skriv in start dagen")
c = input()
c = int(c)

print("Skriv in slut året")
d = input()
d = int(d)

print("Skriv in slut månaden")
e = input()
e = int(e)

print("Skriv in slut dagen")
f = input()
f = int(f)

print("Skriv in elmätarens startvärde")
g = input()
g = int(g)

print("Skriv in elmätarens slutvärde")
h = input()
h = int(h)
print("Skriv in dagsavgiften")
i = input()
i = float(i)

print("Skriv in kw/h priset")
j = input()
j = float(j)

date_1 = datetime.datetime(a, b, c)
date_2 = datetime.datetime(d, e, f)
date_dif = (date_2 - date_1).days

print("Dagar:", date_dif)

elmät_dif = h - g

print("Konsumerad ström:" , elmät_dif , "kw/h")

pris_med_moms = (date_dif * i + elmät_dif * j) * 1.25

print("Pris efter moms:""\033[31m", pris_med_moms ,"\033[0m""kr")