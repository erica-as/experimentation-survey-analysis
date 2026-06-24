import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configurações Iniciais e Estéticas
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (11, 6)
plt.rcParams['font.size'] = 12

# Garante que a pasta de output existe
os.makedirs('output', exist_ok=True)

# 2. Carregando os dados
# Substitua pelo caminho correto do seu arquivo
csv_path = os.path.join('data', 'survey_data.csv')
df = pd.read_csv(csv_path)

print("Colunas detectadas no formulário:")
print(df.columns.tolist())
print("-" * 50)

# ==============================================================================
# GRAFICO 1: Perfil Demográfico (Exemplo: Idade ou Período Acadêmico)
# ==============================================================================
coluna_periodo = 'Em qual período letivo você está matriculado?' # Mude para o seu texto exato

if coluna_periodo in df.columns:
    plt.figure()
    order = df[coluna_periodo].value_counts().index
    sns.countplot(data=df, y=coluna_periodo, order=order, palette='viridis')
    plt.title('Distribuição dos Alunos por Período Acadêmico', fontsize=16, pad=15)
    plt.xlabel('Quantidade de Respostas')
    plt.ylabel('Período')
    plt.tight_layout()
    plt.savefig('output/01_distribuicao_periodo.png', dpi=300)
    plt.close()
    print("Gráfico 1 gerado com sucesso!")

# ==============================================================================
# GRAFICO 2: Mercado de Trabalho (Exemplo: Modelo de Contratação)
# ==============================================================================
coluna_trabalho = 'Qual o seu modelo atual de trabalho?' # Mude para o seu texto exato

if coluna_trabalho in df.columns:
    plt.figure()
    dados_trabalho = df[coluna_trabalho].value_counts()
    plt.pie(dados_trabalho, labels=dados_trabalho.index, autopct='%1.1f%%', 
            colors=sns.color_palette('pastel'), startangle=140, 
            wedgeprops={'edgecolor': 'gray', 'linewidth': 0.5})
    plt.title('Situação Profissional / Modelo de Contratação da Turma', fontsize=16, pad=15)
    plt.tight_layout()
    plt.savefig('output/02_modelo_trabalho.png', dpi=300)
    plt.close()
    print("Gráfico 2 gerado com sucesso!")

# ==============================================================================
# GRAFICO 3: Múltipla Escolha - Tecnologias (Exemplo: Linguagens que domina)
# ==============================================================================
coluna_tech = 'Quais linguagens de programação você domina ou utiliza?' # Mude para o seu texto exato

if coluna_tech in df.columns:
    plt.figure()
    # Remove nulos, separa por vírgula e limpa espaços em branco extras
    tech_series = df[coluna_tech].dropna().str.split(',').explode().str.strip()
    tech_counts = tech_series.value_counts()
    
    sns.barplot(x=tech_counts.values, y=tech_counts.index, palette='magma')
    plt.title('Tecnologias e Linguagens mais Presentes na Turma', fontsize=16, pad=15)
    plt.xlabel('Número de Indicações')
    plt.ylabel('Tecnologia')
    plt.tight_layout()
    plt.savefig('output/03_tecnologias_dominadas.png', dpi=300)
    plt.close()
    print("Gráfico 3 gerado com sucesso!")

# ==============================================================================
# GRAFICO 4: Cruzamento Avançado (Senioridade vs Frequência de Métricas)
# Este gráfico analisa se quem é Pleno/Sênior usa mais métricas que Juniores
# ==============================================================================
coluna_senioridade = 'Qual o seu nível de senioridade atual?' # Mude para o seu texto exato
coluna_metricas = 'Com que frequência você utiliza métricas de software no trabalho?' # Mude para o seu texto exato

if coluna_senioridade in df.columns and coluna_metricas in df.columns:
    plt.figure()
    # Criando uma tabela cruzada percentual para melhor visualização
    tabela_cruzada = pd.crosstab(df[coluna_senioridade], df[coluna_metricas], normalize='index') * 100
    
    tabela_cruzada.plot(kind='barh', stacked=True, cmap='coolwarm', figsize=(11, 6))
    plt.title('Correlação: Nível Profissional vs Uso Prático de Métricas', fontsize=16, pad=15)
    plt.xlabel('Percentual (%) dentro da Categoria')
    plt.ylabel('Senioridade')
    plt.legend(title='Frequência de Uso', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('output/04_correlacao_senioridade_metricas.png', dpi=300)
    plt.close()
    print("Gráfico 4 (Cruzamento) gerado com sucesso!")

print("-" * 50)
print("Processo concluído! Verifique a pasta 'output' para ver as imagens.")