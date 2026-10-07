# ESCOPO DO PROJETO – MESAFARTAI

## 1. Problema de Negócio

Diariamente, alimentos próprios para consumo são descartados por supermercados, restaurantes, feirantes e produtores por excesso de estoque, proximidade da data de validade ou pequenos defeitos estéticos. Ao mesmo tempo, ONGs, abrigos e cozinhas comunitárias enfrentam dificuldades para conseguir alimentos para pessoas em situação de vulnerabilidade.

O principal problema está na falta de uma comunicação rápida e de uma logística eficiente entre quem possui alimentos disponíveis para doação e quem precisa recebê-los.

O MESAFARTAI busca solucionar esse problema por meio de uma plataforma inteligente desenvolvida em Python, capaz de receber mensagens dos usuários, compreender suas necessidades e auxiliar na conexão entre doadores e ONGs.

## 2. Público-Alvo

O sistema terá dois principais tipos de usuários:

### Doadores

Supermercados, restaurantes, feirantes, produtores e outras pessoas ou estabelecimentos que possuem alimentos disponíveis para doação.

O doador poderá informar pelo chat os alimentos disponíveis, quantidade, prazo de validade e outras informações necessárias para realizar a doação.

### ONGs

ONGs, abrigos, cozinhas comunitárias e instituições que necessitam receber alimentos.

As ONGs poderão utilizar o sistema para solicitar alimentos e consultar informações relacionadas às doações disponíveis.

## 3. Intenções Tratadas pelo Sistema

O sistema utilizará Processamento de Linguagem Natural (NLU) para identificar a intenção presente na mensagem enviada pelo usuário.

Inicialmente serão trabalhadas as seguintes intenções:

- cadastrar_doacao: identificar quando um doador deseja cadastrar alimentos para doação;
- solicitar_alimentos: identificar quando uma ONG deseja solicitar alimentos;
- consultar_status: permitir a consulta do andamento ou situação de uma doação;
- fora_de_escopo: identificar mensagens que não estão relacionadas às funcionalidades do MESAFARTAI.

Caso o sistema não tenha confiança suficiente para identificar a intenção da mensagem, será utilizada uma trava de segurança com Threshold/Fallback, solicitando que o usuário forneça mais informações.

## 4. Dados Coletados no Chat

Durante a conversa, o sistema poderá coletar informações necessárias para realizar o cadastro e o direcionamento das doações, como:

- tipo ou descrição do alimento;
- quantidade disponível, como kg, caixas ou unidades;
- prazo ou data de validade;
- localização do usuário;
- CEP;
- identificação do doador ou ONG;
- informações necessárias para acompanhar o status da doação.

Algumas dessas informações serão identificadas automaticamente na mensagem do usuário utilizando técnicas de processamento de texto e Regex.

Os dados coletados serão utilizados para registrar as doações no banco de dados e auxiliar o algoritmo de matchmaking na identificação da ONG receptora mais adequada e próxima.
