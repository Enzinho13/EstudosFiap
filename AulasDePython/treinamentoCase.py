num1 = float(input("digite um numero: "))
num2 = float(input("digite o segundo numero: "))

resul = print("1 Somar | 2 Subtrair | 3 Mutiplicar | 4 Dividir")
esco = input("Escolha uma dessas opçoes (numero ou texto): ")

um = num1 + num2
dois = num1 - num2 
tres = num1 * num2 
quatro = num1 / num2 

match esco:
    case "1" |"Somar" :
        print(f"O resultado da Soma foi de {um}")
    case "2" | "Subtrair":
        print(f"O resultado da sua subtração foi de {dois}")
    case "3" | "Mutiplicar":
        print(f"O resultado da sua Mutiplicação foi de {tres}")
    case "4" | "Dividir":
        print(f"O resultado da sua Divisão foi de {quatro}")
    case _:
        print("Isso nao é um numero. Resultado Invalido >:(")
