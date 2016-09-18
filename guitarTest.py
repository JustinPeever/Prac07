

from guitar import Guitar

def main():
    Guitar1 = Guitar("Gibson L-5 CES", 1922, 765.40)
    Guitar2 = Guitar("Fender Stratocaster", 2014, 16035.40)

    Guitar1.get_age()
    Guitar2.get_age()

    Guitar1.is_vintage()
    Guitar2.is_vintage()
    
main()