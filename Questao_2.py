def seq_fibo(n):
    sequencia_fib = [0, 1]

    while sequencia_fib[-1] < n:
        prox_num = sequencia_fib[-1] + sequencia_fib[-2]
        sequencia_fib.append(prox_num)


    return sequencia_fib

def verif_fibo(numero):
    sequencia_fibo = seq_fibo(numero)

    if numero in sequencia_fibo:
        return f"{numero} pertence á sequencia de Fibonacci"
    else:
        return f"{numero} NÃO pertence á sequencia de Fibonacci"
    
if __name__ == "__main__":
        # Solicita que o usuário informe um número
        numero = int(input("Informe um número: "))
        
        # Verifica se o número fornecido está na sequência de Fibonacci e imprime a mensagem correspondente
        print(verif_fibo(numero))

    
