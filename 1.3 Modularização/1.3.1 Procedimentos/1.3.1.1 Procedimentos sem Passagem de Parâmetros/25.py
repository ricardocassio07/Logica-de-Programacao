# Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
hHI = (int(input("DIGITE O HORÁRIO DE INÍCIO DA PARTIDA! (APENAS AS HORAS, SEM O VALOR DOS MINUTOS! (XX:00))\n-> ")))
mMI = (int(input("DIGITE O MINUTO DO INÍCIO DA PARTIDA! (APENAS OS MINUTOS, SEM O VALOR DAS HORAS! (00:XX))\n-> ")))
hHF = (int(input("DIGITE O HORÁRIO DE TÉRMINO DA PARTIDA! (APENAS AS HORAS, SEM O VALOR DOS MINUTOS! (XX:00))\n-> ")))
mMF = (int(input("DIGITE O MINUTO DE TÉRMINO DA PARTIDA! (APENAS OS MINUTOS, SEM O VALOR DAS HORAS! (00:XX))\n-> ")))

if (hHI > hHF):
    diferencaHoras = ((24 - hHI) + hHF)
else:
    diferencaHoras = (hHF - hHI)
if (mMI <= mMF):
    diferencaMinutos = (mMF - mMI)
else:
    diferencaHoras = (diferencaHoras - 1)
    diferencaMinutos = (60 - (mMI - mMF))
if ((diferencaHoras == 0 and diferencaMinutos == 0) or diferencaHoras == 24):
    print("Os dados inseridos sobre a partida são inválidos, pois ela deve durar mais de 1 minuto e menos de 24 horas!")
else:
    print("A partida durou " + str(diferencaHoras) + " horas e " + str(diferencaMinutos) + " minutos!")