from nl2cpc import traducao_nl_para_cpc
from cpc2nl import traducao_cpc_para_nl

# Teste 1: NL → CPC
frase = "Se chover, então a grama ficará molhada."
formula, mapa = traducao_nl_para_cpc(frase)
print("Frase:", frase)
print("Fórmula:", formula)
print("Mapeamento:", mapa)

# Teste 2: CPC → NL
formula2 = "(P ∧ Q) → R"
mapeamento = {"P": "chover", "Q": "fizer frio", "R": "a aula será cancelada"}
texto = traducao_cpc_para_nl(formula2, mapeamento)
print("\nFórmula:", formula2)
print("Texto:", texto)
