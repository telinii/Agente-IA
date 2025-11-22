import re

# =====================================
# NL → CPC (versão melhorada)
# =====================================

def traducao_nl_para_cpc(frase: str):
    """
    Converte uma frase simples em linguagem natural para lógica proposicional.
    Suporta:
        - negações ("não ...")
        - conjunções ("e", "mas")
        - disjunções ("ou")
        - condicionais ("se ... então ...")
    """

    texto = frase.lower().strip()

    # -----------------------------------------
    # 1. Detecta condicional
    # -----------------------------------------
    cond_match = re.search(r"se (.+?) então (.+)", texto)
    if not cond_match:
        cond_match = re.search(r"se (.+?) entao (.+)", texto)

    if cond_match:
        antecedente = cond_match.group(1).strip()
        consequente = cond_match.group(2).strip()

        P, mapP = _processar_proposicoes([antecedente])
        Q, mapQ = _processar_proposicoes([consequente])

        mapping = {}
        mapping.update(mapP)
        mapping.update(mapQ)

        return f"{P} → {Q}", mapping

    # -----------------------------------------
    # 2. Divide por conectivos "e", "mas", "ou"
    # -----------------------------------------
    partes = re.split(r"\s+(e|mas|ou)\s+", texto)

    # Resultado alternado: proposição / operador / proposição / operador ...
    proposicoes = partes[0::2]
    operadores = partes[1::2]

    # -----------------------------------------
    # 3. Converte proposições em P, Q, R...
    # -----------------------------------------
    simbolos, mapping = _processar_proposicoes(proposicoes)

    # -----------------------------------------
    # 4. Junta tudo em fórmula CPC
    # -----------------------------------------
    formula = simbolos[0]
    letra_op = {"e": "∧", "mas": "∧", "ou": "∨"}

    for i, op in enumerate(operadores):
        formula += f" {letra_op[op]} {simbolos[i+1]}"

    return formula, mapping


# ===========================================================
# Função auxiliar — rotula cada proposição como P, Q, R ...
# ===========================================================
def _processar_proposicoes(lista):
    letras = "PQRSTUVWXYZABCDEFGHIJKLMNO"
    mapping = {}
    simbolos = []
    idx = 0

    for item in lista:
        negado = item.strip().startswith("não ") or item.strip().startswith("nao ")

        texto_limpo = re.sub(r"^(não|nao)\s+", "", item).strip()

        letra = letras[idx]
        idx += 1

        mapping[letra] = texto_limpo

        if negado:
            simbolos.append(f"¬{letra}")
        else:
            simbolos.append(letra)

    return simbolos if len(simbolos) > 1 else simbolos[0], mapping
