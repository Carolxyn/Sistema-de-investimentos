def calcular_imposto_renda(valor_resgate, dias_investido):
   """
   Calcula o imposto de renda com base no número de dias investidos.

   Parâmetros:
       valor_resgate (float): O valor a ser resgatado.
       dias_investido (int): O número de dias que o valor permaneceu investido.

   Retorna:
       float: O valor do imposto de renda calculado.
   """
   # Define as alíquotas de IR com base no número de dias investidos
   if dias_investido <= 180:
       aliquota = 22.5 / 100  # 22,5%
   elif dias_investido <= 360:
       aliquota = 20 / 100  # 20%
   elif dias_investido <= 720:
       aliquota = 17.5 / 100  # 17,5%
   else:
       aliquota = 15 / 100  # 15%

   # Calcula o valor do imposto de renda
   imposto_renda = valor_resgate * aliquota
   return imposto_renda

def main():
   # Solicita ao usuário o tipo de investimento
   while True:
       try:
           tipo_investimento = int(input("Informe o tipo de investimento (1 para CDB, 2 para LCI, 3 para LCA): "))
           if tipo_investimento not in [1, 2, 3]:
               raise ValueError("Tipo de investimento inválido.")
           break
       except ValueError as e:
           print(e)

   # Solicita ao usuário o valor a ser resgatado e o número de dias investido
   while True:
       try:
           valor_resgate = float(input("Informe o valor a ser resgatado: R$ "))
           if valor_resgate <= 0:
               raise ValueError("O valor a ser resgatado deve ser positivo.")
           break
       except ValueError as e:
           print(e)

   while True:
       try:
           dias_investido = int(input("Informe o número de dias que o valor permaneceu investido: "))
           if dias_investido <= 0:
               raise ValueError("O número de dias investido deve ser positivo.")
           break
       except ValueError as e:
           print(e)

   # Verifica o tipo de investimento
   if tipo_investimento == 1:
       # Investimento CDB (Certificado de Depósito Bancário)
       imposto_renda = calcular_imposto_renda(valor_resgate, dias_investido)
       print(f"Imposto de renda a pagar sobre o resgate: R$ {imposto_renda:.2f}")
   elif tipo_investimento == 2:
       # Investimento LCI (Letra de Crédito Imobiliário) - isento de IR
       print("O investimento em LCI é isento de imposto de renda.")
   elif tipo_investimento == 3:
       # Investimento LCA (Letra de Crédito do Agronegócio) - isento de IR
       print("O investimento em LCA é isento de imposto de renda.")

 # Executa o programa 
main()