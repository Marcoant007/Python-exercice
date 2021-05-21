temp = float(input("Temperatura: "))
horas = int(input("Horas do dia: "))


if horas > 22 or horas < 6:
    if temp > 26:
        print("ligar")

    elif temp < 20:
        print("desligar")