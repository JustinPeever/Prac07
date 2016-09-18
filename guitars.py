

from guitar import Guitar


def main():
    Gtar=[]

    name = "Start"
    finish = True
    print('My guitars!')
    while finish == True:

        name = input("Name: ")
        if name!="":
            year = int(input("Year: "))
            cost = float(input("Cost: "))

            Gtar.append([name, year, cost])
            Guitar(name, year, cost).__str__()
        else:
            finish = False
    print('These are my guitars:')
    i = 0
    for line in Gtar:

        name, year, cost = line[0], line[1], line[2]
        if (2016-year)>=50:
            age="(vintage)"
        else:
            age=""
        i= i+1
        print("Guitar {}: {} ({}), worth $ {} {}".format(i,name,year,cost, age))


    #Guitar1 = Guitar("Gibson L-5 CES", 1922, 765.40)
    #Guitar2 = Guitar("Fender Stratocaster", 2014, 16035.40)


main()