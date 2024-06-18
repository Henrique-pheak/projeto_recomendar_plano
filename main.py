# main.py

from recomendar_plano import recomendar_plano

def main():
    """
    Função principal que interage com o usuário para recomendar um plano de internet.
    """
    try:
        consumo_mensal = float(input("Insira o seu consumo médio mensal de dados em GB: "))
        plano_recomendado = recomendar_plano(consumo_mensal)
        print("O plano recomendado é:", plano_recomendado)
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()
