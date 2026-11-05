# Aula 11 - MLCB | Instruções de execução

## Parte 1 - Introdução ao Streamlit

Na raiz do repositório, instale as dependências e execute:

```bash
pip install -r requirements.txt
streamlit run app_streamlit.py
```

Registre doações de até **25 kg** cada até alcançar a meta de **200 kg**.
Após executar e testar o painel, capture a tela e salve a imagem em
`docs/teste_streamlit.png`.

## Parte 2 - AC-4 Parte 1

Execute na raiz do repositório:

```bash
streamlit run src/app.py
```

A aplicação integra os módulos já existentes:
- `src/nlu.py`: classifica a intenção da mensagem;
- `src/entities.py`: extrai alimento, quantidade e validade;
- `src/matchmaking.py`: localiza a ONG mais próxima com KNN;
- `mesafartai.db`: banco de dados SQLite do projeto.

Depois de executar a aplicação, capture a tela principal e salve em
`docs/etapa_ac4_parte1.png`.

**Observação:** os prints devem ser capturados com as aplicações em execução.
Este arquivo não contém capturas fictícias.
