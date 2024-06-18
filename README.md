# Projeto Recomendar Plano

Este projeto recomenda um plano de internet com base no consumo médio mensal de dados informado pelo usuário.

## Estrutura do Projeto

- `recomendar_plano.py`: Contém a função `recomendar_plano` que recebe o consumo de dados e retorna o plano adequado.
- `main.py`: Interage com o usuário, solicita o consumo e exibe o plano recomendado.
- `README.md`: Este arquivo de documentação.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Navegue até o diretório do projeto.
3. Execute o arquivo `main.py`:
   ```sh
   python main.py
   ```

4. Insira o consumo médio mensal de dados quando solicitado.
5. O programa exibirá o plano recomendado com base no consumo informado.

## Exemplos

Aqui estão alguns exemplos de entrada e saída esperadas:

- Entrada: 8.5
  - Saída: Plano Essencial Fibra - 50Mbps
- Entrada: 15
  - Saída: Plano Prata Fibra - 100Mbps
- Entrada: 25
  - Saída: Plano Premium Fibra - 300Mbps
