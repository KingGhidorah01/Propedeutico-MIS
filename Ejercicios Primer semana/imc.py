#Martín Josué Andrade Salazar
peso = input("Ingresa el peso en kilogramos: ")
estatura = input("Ingresa la estatura en metros: ")
formula = int(peso)/float(estatura)**2

if formula < 18.5:
    print("Bajo peso")
elif (formula == 18.5) and (formula <= 21.9):
    print("Normal")
elif (formula == 25) and (formula <= 29.9):
    print("Sobrepeso")
elif(formula == 30):
    print("Obesidad")
elif(formula > 30) and (formula <= 34.9):
    print("Obesidad I")
elif(formula >= 35) and (formula <= 39.5):
    print("Obesidad II")
elif(formula > 40):
    print("Obesidad III o Mórbida")