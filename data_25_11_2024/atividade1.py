# Solicita os dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros (exemplo: 1.75): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Determina a classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso normal"
elif 25 <= imc <= 29.9:
    classificacao = "Acima do peso"
elif 30 <= imc <= 39.9:
    classificacao = "Obesidade Grau I ou II"
else:
    classificacao = "Obesidade Grau III (mórbida)"

# Exibe o resultado
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}.")
