def conta_vogais(texto: str) -> int:
    resultado = list(filter(lambda x: x in "AEIOUaeiou", texto))
    return len(resultado)