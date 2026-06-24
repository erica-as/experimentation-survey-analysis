# Análise de Survey: Perfil da Turma & Expectativas de Mercado

Este repositório contém o pipeline de Engenharia de Dados e Análise Estatística desenvolvido pelo **Grupo 3** para a disciplina de **Medição e Experimentação em Engenharia de Software**. O objetivo do projeto é mapear o perfil sócio-profissional, o domínio técnico e as expectativas de carreira dos estudantes da turma, utilizando o framework GQM (Goal-Question-Metric).

---

## Estrutura de Metas (Framework GQM)

O projeto foi estruturado sob três grandes metas de medição:

1. **GQM 1 (Perfil Demográfico):** Caracterizar a maturidade profissional e acadêmica do grupo.
2. **GQM 2 (Maturidade Técnico-Métrica):** Identificar o nível de adoção de métricas de software e ferramentas modernas na rotina de trabalho dos alunos.
3. **GQM 3 (Expectativas e IA):** Antecipar as tendências de carreira (mercado global) e o impacto das IAs Generativas na produtividade.

---

## Estrutura do Repositório

├── data/
│   └── survey_data.csv
├── src/
│   └── gerar_graficos.py
├── output/
│   └── graficos_formulario/
├── .gitignore
├── requirements.txt
└── README.md

---

## Como Executar o Projeto Localmente

Siga os passos abaixo para clonar o repositório, configurar o ambiente virtual, instalar as dependências e gerar os gráficos automaticamente.

### 1. Pré-requisitos

Certifique-se de ter instalado em sua máquina:

* **Git**
* **Python 3.8 ou superior**

### 2. Configurar o Ambiente Virtual (venv)

É uma boa prática isolar as dependências do projeto para evitar conflitos:

* **No Windows (Prompt de Comando / CMD):**
python -m venv venv
venv\Scripts\activate
* **No Linux / macOS:**
python3 -m venv venv
source venv/bin/activate

Ao ativar, o prefixo (venv) deverá aparecer no início da linha do seu terminal.

### 3. Instalar as Dependências

Com o ambiente virtual ativo, instale as bibliotecas necessárias listadas no arquivo requirements.txt executando:

pip install -r requirements.txt

### 4. Preparar os Dados Brutos

1. Baixe o arquivo de respostas do Google Forms no formato .csv.
2. Renomeie o arquivo exatamente para: survey_data.csv
3. Salve o arquivo dentro da pasta data/ na raiz do seu projeto.

### 5. Executar o Script de Gráficos

Para rodar o processamento automatizado das 19 perguntas e gerar as imagens, execute:

python src/gerar_graficos.py

Após o término da execução, todas as imagens em alta resolução estarão disponíveis prontas para uso nos slides dentro da pasta:
output/graficos_formulario/

---

## Tecnologias Utilizadas

* **Python:** Linguagem base do ecossistema de dados.
* **Pandas:** Manipulação, limpeza e estruturação dos dados tabulares.
* **Matplotlib & Seaborn:** Renderização de gráficos estatísticos avançados e estilização visual moderna.