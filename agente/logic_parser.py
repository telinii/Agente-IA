import re

# Parser simples de fórmulas lógicas
# Este arquivo serve como utilitário, se quiser expandir as regras

OPERADORES = ["∧", "∨", "¬", "→", "↔"]

def validar_formula(formula):
    """Verifica se uma fórmula está sintaticamente correta."""
    formula = formula.replace(" ", "")
    parenteses = 0
    for c in formula:
        if c == "(":
            parenteses += 1
        elif c == ")":
            parenteses -= 1
        if parenteses < 0:
            return False
    return parenteses == 0

def extrair_proposicoes(formula):
    """Extrai letras proposicionais (P, Q, R...) de uma fórmula."""
    return sorted(set(re.findall(r"[A-Z]", formula)))
