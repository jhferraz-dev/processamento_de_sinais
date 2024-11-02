"""
Exemplo de uso da classe serial_lib.py
Desenvolvido por: Adalberto Oliveira
Fainor - Curso de Engenharia de Computação
Processamento Digital de Sinais
Outubro de 2024
"""

import time
import pygame
from serial_lib import SerialCommunication
#from processamento_lib import Processamento

#--------------------------------Comunicação Serial---------------------------------------------------

# Defining serial port info
port = "COM4"
baud_rate = 9600

serial = SerialCommunication(port=port, 
                          baud_rate=baud_rate, 
                          data_length=1, 
                          health_test=True, timeout=0.1)
serial.start()
#pds = Processamento(vin=12, tensao_base=5)

#--------------------------------Configurações do Pygame-------------------------------------------------

#inicializando o pygame
pygame.init()

#definindo configurações de tela
largura, altura = 1200, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Oscilação em tempo real")

#Plano de fundo
cor_fundo = (30,30,30)
cor_onda = (0,255,0)

#Controle de tempo e do loop
clock = pygame.time.Clock() 
executando = True

#Configurações do sinal na tela
deslocamento_x = 0

#----------------------------------Rotina Principal------------------------------------------------------
#tela.fill(cor_fundo)
tick = time.time()
while executando:
     # Verifica os eventos de saída
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    #tela.fill(cor_fundo)


    if (time.time() - tick) > 0.001:

        tick = time.time()

        # Reading serial port
        serial_data = serial.get_data()

        if serial_data:
            valor = serial_data[0]
            tensao = valor * (12/1024)
            #print(f"Amostra: {round(pds.amostra,2)} Tensao: {round(tensao,2)}",end="\r")
            print(f"Tensao: {round(tensao,2)}", end="\r")

            ajuste = int(tensao * (600/12))  #ajusta a escala de tensao para a escala de resolução da tela

            deslocamento_y = 600 - ajuste
            pygame.draw.circle(tela, cor_onda, (deslocamento_x, deslocamento_y), 2)

            #Atualiza a posição horizontal do ponto
            deslocamento_x += 1
            if deslocamento_x >= largura:
                deslocamento_x = 0
                tela.fill(cor_fundo)
                

            #Atualiza o display
            pygame.display.flip()

pygame.quit()