# Relatório — Fase 1, Etapa 2
## Projeto MESAFARTAI — AC-3

### 1. Número de árvores utilizadas

O motor NLU utiliza o algoritmo Random Forest com **80 árvores de decisão**, configuradas pelo parâmetro `n_estimators=80`.

### 2. Valor de Threshold utilizado

Foi utilizado o threshold de **0,60 (60%)**. Quando a confiança máxima é inferior a esse valor, o sistema retorna uma resposta de fallback. Mensagens classificadas como `fora_de_escopo` também recebem fallback, mesmo quando a confiança é superior ao limite.

### 3. Resultado da primeira execução

O modelo TF-IDF + Random Forest foi treinado e executado sem erros. Os resultados dos quatro testes foram:

- **Mensagem:** "Tenho 30 kg de banana para doar". Resultado: `cadastrar_doacao`, com confiança de 0,93 (92,5% exibidos na resposta).
- **Mensagem:** "Nossa instituição precisa de mantimentos". Resultado: `fallback`, com confiança de 0,41.
- **Mensagem:** "Qual é a receita de bolo de cenoura?" Resultado: `fallback`, com confiança de 0,49.
- **Mensagem:** "coisa comida doar la". Resultado: `fallback`, com confiança de 0,42.

Os testes demonstraram que o sistema reconheceu a mensagem de doação e encaminhou as outras três mensagens para fallback.

### 4. Como melhorar os resultados dos testes

Para melhorar a classificação, podemos ampliar e diversificar a base de treinamento, incluindo diferentes formas de escrever as solicitações, sinônimos, erros de digitação e exemplos de mensagens reais. Também podemos avaliar o desempenho do modelo com dados separados para teste, analisar a matriz de confusão e ajustar os parâmetros após a avaliação. Isso pode ajudar o sistema a reconhecer melhor as intenções sem comprometer a segurança do fallback.

### 5. Por que utilizar Random Forest nesta fase?

O Random Forest combina vários modelos de árvores de decisão para realizar a classificação. Nesta etapa, ele foi utilizado com o TF-IDF para trabalhar com as características textuais das mensagens e estimar probabilidades para as intenções. O método permite obter probabilidades de classificação, utilizadas na implementação da trava de threshold. Sua adequação definitiva deve ser avaliada com testes e comparação com outros classificadores.

