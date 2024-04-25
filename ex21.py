import pygame

def main():
    pygame.init()
    nome_do_arquivo = "assets/music.mp3"  
    pygame.mixer.music.load(nome_do_arquivo)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
