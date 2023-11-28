R1= input("Você quer fazer uma operação matemática? [s] ou [n]:")

A2=[]
S2=[]
M2=[]
D2=[]

while R1 == 's':
    A3= int(input("Digite A:"))
    B= int(input("Digite B:"))
    O= input("Digite a operação:")
    if O == '+':
        def A(A3, B):
            return A3 + B
        R2= A(A3, B)
        A2.append(R2)
        print(f"{A3} + {B} = {R2}")
    elif O == '-':
        def S(A3, B):
            return A3 - B
        R2= S(A3, B)
        S2.append(R2)
        print(f"{A3} - {B} = {R2}")
    elif O == '*':
        def M(A3, B):
            return A3 * B
        R2= M(A3, B)
        M2.append(R2)
        print(f"{A3} * {B} = {R2}")
    elif O == '/':
        def D(A3, B):
            if B != 0:
                return A3 / B
            else:
                return "Divisão recusada :/."
        R2= D(A3, B)
        D2.append(R2)
        print(f"{A3} / {B} = {R2}")
    else:
        print("Operação recusada :/")
    R3 = input("Você quer fazer uma operação matemática? [s] ou [n]:")
    if R1 or R3 == 'n':
        print("Calculadora desligada :/")

print("Histórico de resultados:")
print(f"Adições efetuadas: {A2}")
print(f"Subtrações efetuadas: {S2}")
print(f"Multiplicações efetuadas: {M2}")
print(f"Divisões efetuadas: {D2}")