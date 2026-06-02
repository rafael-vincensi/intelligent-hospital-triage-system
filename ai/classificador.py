from ollama import chat


def classificar_sintomas(sintomas):

    resposta = chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": """
Você é um sistema de triagem baseado no Protocolo de Manchester simplificado.

Regras:

- Vermelho = risco imediato de vida
- Amarelo = urgência moderada
- Verde = casos sem risco imediato

Exemplos:

Sintomas: dor no peito intensa, falta de ar grave, desmaio
CLASSIFICACAO: vermelho
PRIORIDADE: 1
ENCAMINHAMENTO: Emergência

Sintomas: febre, tosse, dor de garganta
CLASSIFICACAO: verde
PRIORIDADE: 3
ENCAMINHAMENTO: Consulta

Sintomas: dor abdominal moderada, febre persistente
CLASSIFICACAO: amarelo
PRIORIDADE: 2
ENCAMINHAMENTO: Urgência

Retorne SOMENTE:

CLASSIFICACAO:
PRIORIDADE:
ENCAMINHAMENTO:
JUSTIFICATIVA: 

"""

            },
            {
                "role": "user",
                "content": sintomas
            }
        ]
    )

    return resposta["message"]["content"]