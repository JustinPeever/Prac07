

from programminglanguage import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby, python, vb)
    languages = [ruby, python, vb]

    for language in languages:
        if language.is_dynamic():
            print(language)

main()