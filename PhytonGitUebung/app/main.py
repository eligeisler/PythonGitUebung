import telnetlib  # unsicheres Modul (Bandit)

def check_value(x):
    unused_variable = 42  # wird nie benutzt (Linter-Warnung)
    if x > 10  # fehlender Doppelpunkt (Syntaxfehler)
        assert x != 15  # unsichere Verwendung von assert
        print("Der Wert ist größer als zehn und definitiv nicht fünfzehn, was eine unnötig lange Zeile ist, die jeden Linter garantiert stören wird, weil sie viel zu lang ist")

check_value(20)


