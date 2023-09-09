velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade > RADAR_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_passou_radar_1 and velocidade_carro_passou_radar_1:
    print('carro multado em radar 1')
print('FIM')