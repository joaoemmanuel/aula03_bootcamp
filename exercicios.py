### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# try:
#     preco = int(input("Insira o valor: "))
#     qtd   = int(input("Insira a quantidade: "))
#     if preco > 0 and qtd > 0:
#         print("Dados válidos")
#     else:
#         print("Dados inválidos") 
# except ValueError:
#     print("O valor informado não foi um número inteiro.")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
# try:
#     temp = float(input("Informe a temperatura: "))
#     if temp < 18:
#         print(f"A temperatura de {temp}°C é considerada baixa.")
#     elif temp >= 18 and temp <= 26:
#         print(f"A temperatura de {temp}°C é considerada normal.")
#     else:
#         print(f"A temperatura de {temp}°C é considerada alta.")
# except ValueError:
#     print("O valor informado não é válido.")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if  log['level'] == "ERROR":
#     print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# try:
#     idade = int(input("Informe sua idade: "))
#     email = str(input("Informe seu email: "))
#     if not 18 <= idade <= 65:
#         print("Idade fora do permitido.")
#     elif "@" not in email or "." not in email:
#         print("Email inválido.")
#     else:
#         print ("Dados válidos.")
# except ValueError:
#     print("Insira um valor número para a idade.")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao = {"valor": 12000, 'hora': 20}
# if transacao['valor'] > 10000 or not 9 <= transacao['hora'] <= 18:
#     print("Transação suspeita.")
# else:
#     print("Transação bem sucedida")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# texto = str(input("Digite o texto: "))
# palavras = texto.split()
# contagem = {}

# for palavra in palavras:
#     if palavra in contagem:
#         contagem[palavra] += 1
#     else:
#         contagem[palavra] = 1

# print(contagem)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# num = [10, 20, 30, 40, 50]
# minimo = min(num)
# maximo = max(num)
# normalizados = [(x - minimo) / (maximo - minimo) for x in num]

# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# usuarios = [
#     {'nome': "Joao", 'email': "joao@gmail.com"},
#     {'nome': "Stefany", 'email': "stefany@gmail.com"},
#     {'nome': "Carlos", 'email': "carlos@gmail.com"},
# ]
# dados_validos = [usuario for usuario in usuarios if usuario['nome']]

# print(dados_validos)
        

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# num = range(1, 15)
# # pares = []
# # for x in num:
# #     if x % 2 == 0:
# #         pares.append(x)
# # ou
# pares = [x for x in num if x % 2 == 0]
# print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]
# agregado = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in agregado:
#         agregado[categoria] += valor
#     else:
#         agregado[categoria] = valor

# print(agregado)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# entrada = ""
# while entrada.lower() != "sair":
#     entrada = str(input("Informe a instrução (digite 'sair' para terminar):"))

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# num = int(input("Digite um número de 1 a 10: "))
# while num < 1 or num > 10:
#     print("Número fora do intervalo da instrução!")
#     num = int(input("Digite um número de 1 a 10: "))
# print("Número válido!")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# pag_atual = 1
# pag_total = 10

# while pag_atual <= pag_total:
#     if (pag_total-pag_atual) > 1:
#         print(f"Página {pag_atual} lida! Faltam {pag_total-pag_atual} páginas até o fim do arquivo!")
#         pag_atual += 1
#     elif (pag_total-pag_atual) == 1:
#         print(f"Página {pag_atual} lida! Falta {pag_total-pag_atual} página até o fim do arquivo!")
#         pag_atual += 1
#     else:
#         print(f"Página {pag_atual} lida!")
#         print("Não há mais páginas!")
#         pag_atual += 1
# print("Fim do processamento!")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# conectado = ""
# max_tentativas = 5
# tentativas = 0
# while tentativas <= max_tentativas:
#     conectado = str(input("Conexão bem sucedida?"))
#     if conectado.lower().strip() == "sim":
#         print("Servidor Conectado")
#         break
#     elif conectado.lower().strip() == "nao":
#         print("Servidor Desconectado. Tentando conectar novamente")
#         tentativas += 1
#     else:
#         print("Entrada inválida!")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
lista = [1, 2, "teste", "parar", 5]
i = 0
while i < len(lista):
    if lista[i] == "parar":
        print("Valor de parada detectado.")
        break
    print(f"Valor processado: {lista[i]}")
    i += 1
