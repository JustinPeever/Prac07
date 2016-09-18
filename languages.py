

from programminglanguage import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    ruby._str_()
    python._str_()
    vb._str_()

    looplist = [ruby, python, vb]

    for obj in looplist:
        if obj.typing == "Dynamic":
            print(obj.name)

main()