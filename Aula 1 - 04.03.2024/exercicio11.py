# (FORBELLONE, 2023) Determine os resultados obtidos na avaliação das expressões lógicas seguintes, sabendo que A, B, C contêm, respectivamente 2, 7, 3,5, e que existe um variável lógica L cujo valor é falsidade (F).

a = 2
b = 7
c = 3.5
l = False

# a. B = A * C e (L ou V)

op1 = b == a * c
print(op1)

# b. B > A ou B = pot(A, A)

op2 = b > a or b == a**a
print(op2)

# c. L e B div A >= C ou não A <= C


# d. não L ou V e rad(A + B) >= C


# e. B/A = C ou B/A <> C


# f. L ou pot(B, A) <= C * 10 + A * B

