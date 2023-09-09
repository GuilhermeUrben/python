#  O custo ao consumidor de um carro novo é a soma do custo de fábrica com a 
# percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos sobre o 
# custo de fábrica, e depois a percentagem do distribuidor sobre o resultado). Supondo 
# que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um 
# programa que leia o custo de fábrica de um carro e informe o custo ao consumidor do 
# mesmo.

custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

imposto_custo_fabrica = custo_fabrica*0.45
custo_com_imposto_fabrica = custo_fabrica + imposto_custo_fabrica

imposto_distribuidor = custo_com_imposto_fabrica*0.28
custo_consumidor = custo_com_imposto_fabrica + imposto_distribuidor

print(f"O custo de fábrica do carro é de R$ {custo_fabrica} reais e o custo ao consumidor é de R$ {custo_consumidor} reais.")