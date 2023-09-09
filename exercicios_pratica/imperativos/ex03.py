# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus 
# Fahrenheit. A fórmula de conversão é: F=(9*C+160) / 5, sendo F a temperatura em 
# Fahrenheit e C a temperatura em Celsius.

c = float(input("Digite uma temperatura em graus Celsius para converter em Fahrenheit: "))

f = ( 9 * c + 160) / 5

print(f"\n{c}° graus Celsius equivale a {f}° Fahrenheit.\n")