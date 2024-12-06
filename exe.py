def soma(a, b):
    return a + b

def mult(x, y):
    return x * y

def sub(w, z):
    return w - z

def div(c, d):
    if d == 0:  
        return "Erro! Divisão por zero."
    return c / d

def math():
    while True:
        print("\nBEM VINDO A CALCULADORA")
        print("Escolha uma das opções:")
        print("1. Soma")
        print("2. Multiplicar")
        print("3. Subtração")
        print("4. Divisão")
        print("5. Sair")
        
        option = input("Digite a opção: ")
        
        if option == "5":
            print("Saindo da calculadora...")
            break  
        
        if option in ["1", "2", "3", "4"]:
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, insira números válidos.")
                continue  
            
            if option == "1":
                print(f"{n1} + {n2} = {soma(n1, n2)}")
            elif option == "2":
                print(f"{n1} * {n2} = {mult(n1, n2)}")
            elif option == "3":
                print(f"{n1} - {n2} = {sub(n1, n2)}")
            elif option == "4":
                resultado = div(n1, n2)
                if isinstance(resultado, str):  
                    print(resultado)
                else:
                    print(f"{n1} / {n2} = {resultado}")
        else:
            print("Opção inválida! Tente novamente.")


math()
