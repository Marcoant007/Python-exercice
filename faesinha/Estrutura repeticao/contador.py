from time import sleep


#time é um comando que faz esperar

for min in range(10,-1,-1):
    for seg in range(59, -1, -1):
        print(f'{min:02d}:{seg:02d}')
        sleep(0.1)