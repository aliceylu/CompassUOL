def calcular_valor_maximo(operadores, operandos) -> float:
    lista1 = list(zip(operandos, operadores))
    lista2 = list(map(lambda x: x[0][0] + x[0][1] if x[1] == "+" 
    else x[0][0] - x[0][1] if x[1] == "-" 
    else x[0][0] * x[0][1] if x[1] == "*" 
    else x[0][0] / x[0][1] if x[1] == "/" 
    else x[0][0] % x[0][1] if x[1] == "%"
    else None, lista1))
    return max(lista2)



op1 = ['+', '-', '*', '/', '+']
op2 = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
print(calcular_valor_maximo(op1, op2))
