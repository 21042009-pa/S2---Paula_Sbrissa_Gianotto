print ("vamos fazer a média de suas notas, para sair digite 0")
# Função para solicitar as notas do aluno
def solicitar_notas():
    soma_notas = 0
    quantidade_notas = 0

    while True:
        nota = float(input("Digite uma nota (ou 0 para sair): "))
        
        if nota == 0:
            break
        
        # Verificar se a nota é válida (de 1 a 10)
        if 1 <= nota <= 10:
            soma_notas += nota
            quantidade_notas += 1
        else:
            print("Nota inválida! Digite uma nota entre 1 e 10.")
    
    return soma_notas, quantidade_notas



# Função principal que integra todo o processo
def main():
    soma_notas, quantidade_notas = solicitar_notas()
    media = calcular_media(soma_notas, quantidade_notas)
    verificar_aprovacao(media)

# Chamar a função principal
main()