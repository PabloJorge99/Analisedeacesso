# Comparacao de Acesso aos Servicos por Bairro

## Descricao do Projeto
Este projeto e um aplicativo interativo desenvolvido com **Streamlit** para analisar e comparar diferentes bairros de uma cidade em relacao ao acesso a servicos essenciais, como escolas, hospitais, pracas publicas, transporte publico e custo do aluguel. O objetivo e facilitar a visualizacao dos dados e ajudar na tomada de decisoes sobre qual bairro oferece melhores condicoes de acesso.

## Tecnologias Utilizadas
- **Python**
- **Streamlit** (para interface interativa)
- **Pandas** (para manipulacao de dados)
- **Plotly Express** (para visualizacao de dados)

## Funcionalidades
- Exibicao de metricas como tempo medio de deslocamento, distancia ate servicos essenciais e disponibilidade de transporte publico.
- Criacao de graficos comparativos para melhor visualizacao dos dados.
- Calculo de um **Indice de Facilidade de Acesso**, que pondera diferentes fatores para avaliar a conveniencia de cada bairro.
- Interface responsiva e interativa para selecao e comparacao de diferentes criterios.

## Como Executar o Projeto
1. Certifique-se de ter o **Python** instalado em seu computador.
2. Instale as dependencias necessarias:
   ```sh
   pip install streamlit pandas plotly
   ```
3. Salve o codigo em um arquivo **.py** (exemplo: `app.py`).
4. Execute o Streamlit:
   ```sh
   streamlit run app.py
   ```
5. O aplicativo sera aberto no navegador, permitindo a interacao com os dados e visualizacao dos graficos.

## Estrutura do Codigo
O codigo esta estruturado da seguinte forma:
1. **Configuracao da pagina**: Definicao do layout.
2. **Criacao dos dados**: Os dados sao armazenados manualmente em um **DataFrame Pandas**.
3. **Calculo do Indice de Acesso**: Formula ponderada para avaliar a facilidade de acesso em cada bairro.
4. **Configuracao do tema**: Aplicacao de um tema escuro usando CSS embutido.
5. **Criacao da Interface**:
   - Escolha do tipo de comparacao: Distancia media, tempo a pe ou tempo de carro.
   - Geracao de graficos dinamicos com **Plotly Express**.
   - Exibicao do Indice de Acesso em formato de tabela e grafico.
   - Comparacao dos valores de aluguel e transporte publico.

## Exemplo de Uso
Os usuarios podem selecionar diferentes metricas para comparar os bairros. O aplicativo exibe graficos interativos que mostram a distancia media, tempo de deslocamento e custo do aluguel, facilitando a analise dos melhores bairros de acordo com a necessidade do usuario.
