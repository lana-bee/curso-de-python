# Iportando a biblioteca pygame
from random import randint
from sys import exit
import pygame
from pygame.locals import *


#=============================
#-----1. Criando a janela-----
#=============================

pygame.init() # 1. Inicializa o pygame

# Configura as dimensões da janela e cria a tela
LARGURA = 600
ALTURA  = 400
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Jogo da Cobrinha") # 1. Define o título do jogo

# 1. Cria o relógio para controlar os FPS
relógio = pygame.time.Clock()

#=====================================================
#---11. Carregando e tocando a musica de fundo ----
#====================================================

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(0.3) 
pygame.mixer.music.play(-1)

#=====================================================
#---11. Carregando e tocando o Som da comida ----
#====================================================
som_comida = pygame.mixer.Sound("som_comida.wav")

#=====================================================
#----2. Definindo o tamanho dos Bolcos e Fundo----
#=====================================================
TAMANHO_GRAMADO = 20 # Largura x Altura em pixels

COR_FUNDO = (170,215,81) # (R,G,B)
COR_GRAMADO = (162,209,73)

#=====================================================
#----4. Carregando a imagem da maçã----
#=====================================================

maca = pygame.image.load("maca.png").convert_alpha()
maca = pygame.transform.scale(maca, (30,30))






#=====================================================
#----4. A Estrutura e o Estado Inicial da Cobra----
#=====================================================

inicio = [
    pygame.Rect(x, 200,TAMANHO_GRAMADO, TAMANHO_GRAMADO)
    for x in (80,60,40)

]

cobra = inicio.copy()

#=====================================================
#----5. Movimento Automático da Cobra----
#=====================================================

velocidade_x = (TAMANHO_GRAMADO) 
velocidade_y = (0)

#=====================================================
#----7. A Comida da Cobra----
#=====================================================

comida_x = randint(0,(LARGURA-TAMANHO_GRAMADO)// TAMANHO_GRAMADO) * TAMANHO_GRAMADO
comida_y = randint (0,(ALTURA-TAMANHO_GRAMADO)// TAMANHO_GRAMADO) * TAMANHO_GRAMADO
comida = pygame.Rect(comida_x,comida_y, TAMANHO_GRAMADO, TAMANHO_GRAMADO)
# Carregando a imagem da moeda
#imagem_moeda = pygame.image.load("moeda.png").convert_alpha()
#imagem_moeda = pygame.transform.scale(imagem_moeda, (20, 20))

#=====================================================
#----9. Inicio da pontuação e a font----
#=====================================================

pontos = 0

fonte = pygame.font.SysFont("Press Start 2P",35,bold=True)



# 1. Looping que mantém a janela aberta
rodando = True
while rodando:
   for event in pygame.event.get():
      if event.type == QUIT:
         rodando = False
            
    #=====================================================
    #----6. Controles do Teclado (Setas)----
    #=====================================================

      elif event.type ==KEYDOWN: 
         if event.key == K_LEFT and velocidade_x == 0:
            velocidade_x = -TAMANHO_GRAMADO
            velocidade_y = 0

         elif  event.key == K_RIGHT and velocidade_x == 0:
            velocidade_x = TAMANHO_GRAMADO
            velocidade_y = 0

         elif  event.key == K_UP and velocidade_y == 0:
            velocidade_x = 0
            velocidade_y = -TAMANHO_GRAMADO

         elif  event.key == K_DOWN and velocidade_y == 0:
            velocidade_x = 0
            velocidade_y = TAMANHO_GRAMADO

    #=====================================================
    #----5. Atualizando a Posição da Cobra----
    #=====================================================

   cabeca = pygame.Rect(
       cobra[0].x + velocidade_x,
       cobra[0].y + velocidade_y,
       TAMANHO_GRAMADO,
       TAMANHO_GRAMADO 
       )
    

   cobra.insert(0,cabeca)

#=====================================================
#----5. Colisão da cobra com a Maçã----
#=====================================================

   if cobra[0].colliderect(comida):
    comida.x = randint(0,(LARGURA-TAMANHO_GRAMADO)// TAMANHO_GRAMADO) * TAMANHO_GRAMADO
    comida.y = randint (0,(ALTURA-TAMANHO_GRAMADO)// TAMANHO_GRAMADO) * TAMANHO_GRAMADO
    pontos += 1 # 9. Soma dos Pontos
    som_comida.play()

   else:
         cobra.pop() #remove o ultimo item da lista copy

   if (
      cobra [0].x < 0 or
      cobra [0].x >= LARGURA or
      cobra [0].y < 0 or
      cobra [0].y >= ALTURA or
      any(cobra[0].colliderect(parte) for parte in cobra[1:])

   ):
      cobra= inicio.copy()

      velocidade_x = (TAMANHO_GRAMADO)
      velocidade_y = (0)

      pontos = 0 # 9. Zera os pontos

      comida.x = randint(0,(LARGURA-TAMANHO_GRAMADO)// TAMANHO_GRAMADO) * TAMANHO_GRAMADO
      comida.y = randint (0,(ALTURA-TAMANHO_GRAMADO)// TAMANHO_GRAMADO) * TAMANHO_GRAMADO

   # 2. Pintando toda a tela de fundo
   tela.fill (COR_FUNDO)

    #=====================================================
    #----3. Desenhando o fundo Quadriculado (Grama)----
    #=====================================================

   for x in range (0, LARGURA,TAMANHO_GRAMADO):
      for y in range(x % 40, ALTURA, 40):
         pygame.draw.rect(tela, COR_GRAMADO, (x,y,TAMANHO_GRAMADO, TAMANHO_GRAMADO))

#=====================================================
#----7. Desenhando a comida na tela----
#=====================================================
   tela.blit(maca, (comida.x, comida.y))



    #=====================================================
    #----4. A Estrutura Inicial da Cobrinha----
    #=====================================================
    
   # Desenhando a cobra
   for parte in cobra:
    # Corpo laranja
    pygame.draw.rect(tela, (255, 140, 0), parte)

    # Contorno preto em todos os quadradinhos
    pygame.draw.rect(tela, (0, 0, 0), parte, 2)

    # Desenhando os olhos na cabeça
   cabeca = cobra[0]

   pygame.draw.circle(
    tela, (0, 0, 0),
    (cabeca.x + 6, cabeca.y + 6), 3
   )

   pygame.draw.circle(
    tela, (0, 0, 0),
    (cabeca.x + 14, cabeca.y + 6), 3
   )

    #=====================================================
    #----9. Redenrizando e Exibindo o placar----
    #=====================================================

   mensagem_placar = f"Pontos:{pontos}"
   texto_formatado = fonte.render(mensagem_placar, True, (50, 50, 50))
   tela.blit(texto_formatado, (10, 10))

    
   # 1. Atualiza oque aparece na tela
   pygame.display.flip()

   # 1. Manter a taxa de 10 quadros por segundo
   relógio.tick(10)


# 1. Encerra o pygame corretamente
pygame.quit()
exit()



