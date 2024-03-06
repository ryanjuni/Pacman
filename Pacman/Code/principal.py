import pygame
import constantes
import os

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):    
        self.toda_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self): 
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS) 
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        self.toda_as_sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(constantes.PRETO)         
        self.toda_as_sprites.draw(self.tela)
        pygame.display.flip()

    def carregar_arquivos(self): 
        diretorio_Imagens = os.path.join(os.getcwd(), 'Imagens')
        self.diretorio_Audios = os.path.join(os.getcwd(), 'Audios')
        self.spritessheet = os.path.join(os.getcwd(), constantes.SPRITESSHEET)
        self.pacman_start_logo = os.path.join(diretorio_Imagens, constantes.PACMAN_START_LOGO)
        self.pacman_start_logo_img = pygame.image.load(self.pacman_start_logo).convert()

    def mostrar_texto(self, texto, tamanho, cor, x, y):    
        fonte = pygame.font.Font(self.fonte, tamanho)  
        texto_surface = fonte.render(texto, True, cor)
        texto_rect = texto_surface.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto_surface, texto_rect)

    def mostrar_start_logo(self, x, y):
        start_logo_rect = self.pacman_start_logo_img.get_rect()
        start_logo_rect.midtop = (x, y)
        self.tela.blit(self.pacman_start_logo_img, start_logo_rect)


    def mostra_tela_start(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_Audios,constantes.MUSICA_START))
        pygame.mixer.music.play()
        self.mostrar_texto('Pressione uma tecla para jogar', 32, constantes.AMARELO, constantes.LARGURA/2, 320)
        self.mostrar_start_logo(constantes.LARGURA/2,20)

        self.mostrar_texto('Desenvolvido por Ryan Junio', 19, constantes.BRANCO, constantes.LARGURA/2, 570)
    
        pygame.display.flip()
        self.esperar_por_jogador()

    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constantes.FPS) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorio_Audios,constantes.TECLA_START)).play()
                    

    def mostra_tela_game_over(self):
        pass

g = Game()
g.mostra_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostra_tela_game_over()
