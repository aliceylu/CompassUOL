from functools import reduce

def calcula_saldo(lancamentos) -> float:
    extrato = list(map(lambda x: x[0] if x[1] == "C" else -x[0], lancamentos))
    saldo = reduce(lambda a, b: a + b, extrato)
    return saldo