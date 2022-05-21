def validar_cpf(cpf: str) -> bool:
    return (cpf.isnumeric() and len(cpf) == 11)


def validar_nome(nome: str) -> bool:
    nome = nome.strip()
    return (len(nome) > 0 and len(nome) <= 30)


def validar_age(age: str) -> bool:
    age_texto = str(age)
    if age_texto.isnumeric():
        return (age >= 1 and age <= 100)
    else:
        return False