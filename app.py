import eel

def exe_eel():
    # Inicializa o Eel, mas sem rodar o servidor
    eel.init('web')

    # Aqui, o parâmetro `block=False` impede que o servidor Eel seja iniciado,
    # e apenas abre a URL no navegador.
    eel.start('home', size=(800, 600), block=False, port=5000)

if __name__ == '__main__':
    exe_eel()