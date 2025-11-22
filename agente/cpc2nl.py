import re

def traduzir_formula(formula: str, significados: dict) -> str:
    """
    Traduz fórmulas proposicionais (CPC) para linguagem natural.
    Considera negação, conectivos e mantém maiúsculas/minúsculas.
    """

    # Remove espaços
    f = formula.replace(" ", "")

    # Função para traduzir símbolos simples como P, Q, ¬P etc.
    def traduz_simbolo(simbolo):
        negado = False

        # Detecta negação
        if simbolo.startswith("¬"):
            negado = True
            simbolo = simbolo[1:]

        # Sem significado
        if simbolo not in significados:
            return simbolo

        texto = significados[simbolo]

        # Mantém capitalização original
        if negado:
            return f"não {texto}" if texto[0].islower() else f"Não {texto}"

        return texto

    # Coloca espaços nos conectivos
    f = (f.replace("→", " → ")
           .replace("∧", " ∧ ")
           .replace("∨", " ∨ ")
           .replace("↔", " ↔ ")
           .replace("¬", " ¬"))

    partes = f.split()

    conectivos = {
        "→": "então",
        "∧": "e",
        "∨": "ou",
        "↔": "se e somente se"
    }

    resultado = []

    for item in partes:
        if item in conectivos:
            resultado.append(conectivos[item])
        else:
            resultado.append(traduz_simbolo(item))

    frase = " ".join(resultado).strip()

    # Se for condicional → reorganiza para "Se X, então Y"
    if "então" in frase:
        antes, depois = frase.split("então", 1)
        antes = antes.strip()
        depois = depois.strip()
        return f"Se {antes}, então {depois}"

    return frase
