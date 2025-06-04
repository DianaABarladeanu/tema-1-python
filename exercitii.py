# EXERCISE 1
# Print your name
print("Diana Barladeanu")


# EXERCISE 1
print("Diana Barladeanu")


# EXERCISE 2: Creează o variabilă numar_intreg și dă-i o valoare întreagă.
numar_intreg = 42
print("Valoarea variabilei numar_intreg este:", numar_intreg)

# EXERCISE 3: Creează o variabilă numar_zecimal cu un număr float.
numar_zecimal = 3.14
print("Valoarea variabilei numar_zecimal este:", numar_zecimal)

# Stochează în mesaj orice text
mesaj = "Hello, Python!"

# Creează o variabilă activ cu valoarea True și afișeaz-o
activ = True
print(activ)

# Creează o variabilă necunoscut cu valoarea None și printeaz-o
necunoscut = None
print(necunoscut)

# Adună două numere la alegere și afișează rezultatul
x = 10
y = 7
suma = x + y
print("Suma:", suma)

# Calculează câtul și restul împărțirii dintre 17 și 4
cat = 17 // 4
rest = 17 % 4
print("Câtul:", cat)
print("Restul:", rest)

# Calculează 3 la puterea 4
putere = 3 ** 4
print("3 la puterea 4:", putere)

# Afișează dacă 5 este mai mare decât 3
comparatie = 5 > 3
print("5 este mai mare decât 3:", comparatie)

# Creează două variabile a și b
a = 15
b = 4

# Calculează (a + b) * 2 - a // b
rezultat = (a + b) * 2 - a // b
print("Rezultatul expresiei:", rezultat)

# Creează două variabile și verifică cu assert că sunt egale
x = 10
y = 5 + 5
assert x == y, "x și y ar trebui să fie egale"

# Fă assert că 10 > 2
assert 10 > 2, "10 ar trebui să fie mai mare decât 2"

# Creează un nume și folosește assert să verifici lungimea
nume = "Ana"
assert len(nume) == 3, "Numele ar trebui să aibă 3 caractere"

# Creează un text și verifică că este scris cu majuscule
text = "PYTHON"
assert text.isupper(), "Textul ar trebui să fie scris cu majuscule"

# Verifică că float(10) == 10.0
assert float(10) == 10.0, "float(10) ar trebui să fie egal cu 10.0"

# Creează o variabilă prenume cu numele tău
prenume = "Diana"

# Creează salut concatenând "Bună, " + prenume
salut = "Bună, " + prenume

# Afișează câte litere are prenume cu len()
lungime = len(prenume)
print("Lungimea prenumelui:", lungime)

# Transformă prenume în majuscule și afișează
prenume_majuscule = prenume.upper()
print("Prenumele în majuscule:", prenume_majuscule)

# Creează un mesaj complet: "Salut, " + prenume + "!", apoi afișează-l
mesaj_complet = "Salut, " + prenume + "!"
print(mesaj_complet)

# Creează două variabile și verifică suma cu assert
a = 7
b = 3
suma = a + b
assert suma == 10, "Suma ar trebui să fie 10"

# Creează un text și folosește assert pentru verificări
text = "python"
assert text.lower() == "python", "Textul în litere mici ar trebui să fie 'python'"
assert text != "PYTHON", "Textul original nu este egal cu 'PYTHON'"

# Afișează un mesaj compus din text și un număr
nivel = 5
mesaj = "Nivel: " + str(nivel)
print(mesaj)

# Creează două variabile și unește-le cu spațiu între ele
salut = "Salut"
nume = "Ioana"
mesaj_salut = salut + " " + nume
print(mesaj_salut)

# Folosește un dicționar de operatori pentru a calcula x * y
import operator

x = 2
y = 3
operatii = {
    '*': operator.mul,
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow
}

rezultat = operatii['*'](x, y)
print("Rezultatul înmulțirii:", rezultat)

# Am rezolvat exercitiile din tema 1

# Am rezolvat exercitiile din tema 1
