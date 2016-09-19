

from guitar import Guitar


def main():
    guitars=[]

    name = "Start"
    finish = True
    print('My guitars!')
    # while finish == True:
    #
    #     name = input("Name: ")
    #     if name!="":
    #         year = int(input("Year: "))
    #         cost = float(input("Cost: "))
    #         Guitar(name, year, cost)
    #         #Gtar.append([name, year, cost])
    #         #Guitar(name, year, cost).__str__()
    #         print(Guitar)
    #     else:
    #         finish = False

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print('These are my guitars:')
    i = 0
    for guitar in guitars:
        if guitar.is_vintage():
            vintage = "(vintage)"
        else:
            vintage=""
        i= i+1
        print("Guitar {}: {} ({}), worth $ {} {}".format(i,guitar.name,guitar.year,guitar.cost, vintage))


    #Guitar1 = Guitar("Gibson L-5 CES", 1922, 765.40)
    #Guitar2 = Guitar("Fender Stratocaster", 2014, 16035.40)


main()