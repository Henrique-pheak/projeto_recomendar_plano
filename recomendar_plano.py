# recomendar_plano.py

def recomendar_plano(consumo):
    """
    Recomenda um plano de internet com base no consumo médio mensal de dados.

    Args:
        consumo (float): O consumo médio mensal de dados em GB.

    Returns:
        str: O plano de internet recomendado.
    """
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"
