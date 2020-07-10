from random import randint
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

lista = ('Pedra', 'Papel', 'Tesoura')

r = sr.Recognizer()
mic = sr.Microphone()

while True:

    print('''#SUAS OPÇÕES 
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')

    with mic as fonte:
        r.adjust_for_ambient_noise(fonte)
        print("Fale sua jogada...")
        audio = r.listen(fonte)

        try:
            texto = r.recognize_google(audio, language="pt-BR")
            text = texto.split(" ")
            pc = randint(0, 2)
        except:
            print("NÃO ENTENDI PORRA NENHUMA")
            break

    print("Jogador jogou: {}".format(text[0]))
    engine.say("Jogador jogou: {}".format(text[0]))
    engine.runAndWait()

    if text[0] != 'pedra' and text[0] != 'papel' and text[0] != 'tesoura' and text[0] != 'sair':
        print("Jogada Inválida")
        engine.say("jogada inválida, vamos tentar de novo")
        engine.runAndWait()
        jogador = 4

    elif text[0] != 'sair':

        print("PC jogou: {}".format(lista[pc]))
        engine.say("Computador jogou: {} ".format(lista[pc]))
        engine.runAndWait()

        if text[0] == 'pedra':
            jogador = 0
        elif text[0] == 'papel':
            jogador = 1
        elif text[0] == 'tesoura':
            jogador = 2
        else:
            jogador = 5

        if pc == 0:
            if jogador == 0:  # PEDRA
                print("EMPATE")
                engine.say("empate")
                engine.runAndWait()

            elif jogador == 1:
                print("Jogador GANHOU")
                engine.say("jogador GANHOU")
                engine.runAndWait()

            elif jogador == 2:
                print("Jogador PERDEU")
                engine.say("jogador perdeu")
                engine.runAndWait()
        if pc == 1:
            if jogador == 0:  # PAPEL
                print("jogador GANHOU")
                engine.say("jogador ganhou")
                engine.runAndWait()
            elif jogador == 1:
                print("EMPATE")
                engine.say("empate")
                engine.runAndWait()
            elif jogador == 2:
                print("Jogador PERDEU")
                engine.say("jogador perdeu")
                engine.runAndWait()
        if pc == 2:
            if jogador == 0:  # TESOURA
                print("jogador PERDEU")
                engine.say("jogador perdeu")
                engine.runAndWait()
            elif jogador == 1:
                print("Jogador GANHOU")
                engine.say("jogador ganhou")
                engine.runAndWait()
            elif jogador == 2:
                print("EMPATE")
                engine.say("empate")
                engine.runAndWait()
        print("Vamos de novo")
        engine.say("Vamos de novo")
        engine.runAndWait()
    if not text[0] != "sair":
        break

print("Jogo encerrado")
engine.say("jogo encerrado")
engine.runAndWait()
engine.stop()