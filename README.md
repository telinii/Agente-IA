# Agente-IA


# 🧠 Tradutor de Fórmulas Proposicionais para Linguagem Natural

Este projeto implementa um agente capaz de **traduzir fórmulas da Lógica Proposicional (CPC)** para **linguagem natural**, permitindo que proposições como `¬P → (Q ∧ R)` sejam convertidas para frases claras e compreensíveis para humanos.

O sistema foi implementado em **Python + Streamlit**, com regras bem definidas e um mecanismo simples e eficiente de tradução.



---

## 📌 1. Arquitetura do Sistema (1 ponto)

A arquitetura é composta por três elementos principais: **Interface**, **Mecanismo de Tradução** e **Dicionário de Significados**.

+-------------------------------------------------------+
| Interface (UI) |
| Streamlit App |
| - Recebe fórmula CPC |
| - Recebe dicionário de significados |
| - Exibe tradução final |
+-----------------------------|-------------------------+
|
v
+-------------------------------------------------------+
| Motor de Tradução (traduzir_formula) |
| - Remove espaços |
| - Separa símbolos e conectivos |
| - Aplica regras de negação |
| - Mapeia conectivos: ∧ ∨ → ↔ |
| - Reescreve condicionais com "Se..., então..." |
+-----------------------------|-------------------------+
|
v
+-------------------------------------------------------+
| Dicionário de Significados |
| Ex.: { "P": "chove", "Q": "faço café" } |
| - Mantém maiúsculas/minúsculas |
| - Permite personalização pelo usuário |
+-------------------------------------------------------+


### 🔍 Fluxo de Funcionamento

1. Usuário insere fórmula proposicional (ex.: `¬P → Q`).
2. Usuário define significados de cada proposição.
3. A função `traduzir_formula()` processa:
   - Reconhece negação
   - Substitui conectivos
   - Constrói frase lógica
   - Ajusta condicionais
4. A interface exibe o texto traduzido.

---

## 📌 2. Estratégia de Tradução (1 ponto)

A tradução foi construída usando **apenas regras determinísticas**, sem LLM no processamento principal (mas pode ser estendido).

### ✔️ Regras implementadas

#### **1. Remoção de espaços**
Facilita o parsing.

#### **2. Identificação de negação**
- Detecta `¬P`, `¬Q`, etc.
- Aplica regra:

| Caso | Entrada | Resultado |
|------|---------|-----------|
| Palavra inicia com maiúscula | "Chove" | "Não Chove" |
| Palavra inicia com minúscula | "chove" | "não chove" |

#### **3. Mapeamento de conectivos**
Tabela implementada:

| Símbolo | Frase |
|---------|--------|
| ∧ | e |
| ∨ | ou |
| → | então |
| ↔ | se e somente se |

#### **4. Reescrita de condicionais**
Frase com "então" vira:

`Se X, então Y`

Isso melhora a fluência da linguagem natural.

---

### ✔️ Exemplos com análise

#### 🔸 Exemplo 1
Input:

Formula: ¬P → Q
Significados: P=Chove, Q=Levo guarda-chuva


Output:

Se Não Chove, então Levo guarda-chuva


**Acerto:** Capitalização preservada, estrutura condicional ok.  
**Limitação:** "Não Chove" pode soar estranho; ideal seria "não chove" (ver melhorias).

---

#### 🔸 Exemplo 2
Input:

(P ∧ Q) ∨ ¬R


Output:

(P e Q) ou não R


**Acerto:** Regras de conectivo funcionando.  
**Limitação:** Sistema ainda não remove parênteses excedentes na frase final.

---

#### 🔸 Exemplo 3
Input:

P ↔ Q

Output:

P se e somente se Q



**Acerto:** Tradução fiel à lógica.  
**Limitação:** Frase não é muito "natural".

---

## 📌 3. Limitações e Possibilidades de Melhoria (1 ponto)

### ❗ Limitações atuais

- 🚫 O sistema não transforma expressões complexas em frases totalmente naturais.
- 🚫 Não reorganiza frases com muitos parênteses.
- 🚫 Não interpreta precedência lógica mais complexa.
- 🚫 Não utiliza Árvores Sintáticas (AST), o que limitaria fórmulas longas.
- 🚫 Não possui LLM para gerar frases mais naturais.

---

### ⭐ Melhorias possíveis

1. **Implementar parser sintático formal (como Shunting Yard)**  
   → Permite montar uma árvore lógica adequada.

2. **Transformar a árvore lógica em texto natural usando templates linguísticos**  
   → Frases gramaticalmente mais próximas da língua real.

3. **Adicionar um pós-processador com LLM**  
   → Reescreve a frase para deixá-la mais clara e fluida.

4. **Melhor modularização da tradução**  
   → Fácil adicionar mais conectivos.

5. **Exportar resultado em texto / PDF direto no app**.

6. **Salvar dicionário de proposições para reuso pelo usuário**.

---

## 📌 4. Vídeo de Demonstração (1 ponto)

📽️ **Link do vídeo:**  
👉 https://www.youtube.com/watch?v=UFowiCiSscU

---

## ✔️ Estado Final do Projeto

- Interface funcional em Streamlit  
- Tradução fiel e determinística  
- Arquitetura simples e clara  
- Código limpo e reaproveitável  

---





