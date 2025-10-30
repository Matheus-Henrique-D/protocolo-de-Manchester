from backend import SistemaTriagem


def menu_interativo():
    # Instancia o sistema de triagem
    sistema = SistemaTriagem()
    print("=== BEM-VINDO AO SISTEMA DE TRIAGEM MANCHESTER ===\n")

    # Loop principal do menu
    while True:
        print("\n=== SISTEMA DE TRIAGEM MANCHESTER ===")
        print("1 - Cadastrar paciente")
        print("2 - Chamar paciente")
        print("3 - Mostrar status das filas")
        print("0 - Sair")

        escolha = input("Escolha: ")

        try:
            # Opção 1: Cadastrar novo paciente
            if escolha == '1':
                sistema.cadastrar_paciente()

            # Opção 2: Chamar próximo paciente da fila mais urgente
            elif escolha == '2':
                sistema.chamar_paciente()

            # Opção 3: Mostrar o status de todas as filas
            elif escolha == '3':
                sistema.mostrar_status()

            # Opção 0: Encerrar o sistema
            elif escolha == '0':
                print("\nEncerrando o sistema. Até logo!")
                break

            # Opção inválida
            else:
                print("\n[ERRO] Opção inválida, por favor tente novamente.")

        except Exception as e:
            # Captura qualquer erro inesperado
            print(f"\n[ERRO INESPERADO] Ocorreu um problema: {e}")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu_interativo()