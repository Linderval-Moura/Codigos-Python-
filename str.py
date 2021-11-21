Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Imprimindo uma string.
s = "Olá, mundo!"
print(s)

# Tipo de uma string.
type(s)

# Tamanho de uma string.
len(s)

# Concatenação
print("Meu Brasil " + "brasileiro")

# Substitui uma substring por alguma outra coisa.
s1 = s.replace("mundo", "meu abacate")

print(s1)

# A string s começa com "Olá"?
print(s.startswith("Olá"))

# A string s termina com "mundo"?
print(s.endswith("mundo"))

# Quantas ocorrências da palavra "abacate" a string s1 possui?
print(s1.count("abacate"))