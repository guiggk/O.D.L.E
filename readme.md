# O.D.L.E (Orientador de Distribuição de Lanches Escolar)

Este é um sistema interativo em prol de um projeto extensionista da faculdade, desenvolvido em Python com Streamlit que visa ajudar gestores escolares a analisarem o consumo de alimentos, presença de alunos e o desperdício na merenda escolar. Ele também utiliza um modelo de inteligência artificial (regressão linear) para prever o preparo ideal de alimentos com base na quantidade de alunos presentes.

## Funcionalidades

- Upload de arquivo CSV com dados reais.
- Visualização de gráficos interativos sobre presença, consumo, preparo e desperdício.
- Previsão inteligente de preparo ideal com base no número de alunos.
- Filtros por ano e intervalo de dias.
- Estilização com cores intuitivas e informações detalhadas em tabela.
- Modelo de aprendizado de máquina aplicado (regressão linear).

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/O.D.L.E.git
cd O.D.L.E
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode a aplicação:

```bash
streamlit run app.py
```

4. Faça o upload de um arquivo CSV com as seguintes colunas obrigatórias:

```
Dia, Ano, Alunos Presentes, Alimento Preparado (kg), Alimento Consumido (kg)
```

## Exemplo de CSV

```csv
Dia,Ano,Alunos Presentes,Alimento Preparado (kg),Alimento Consumido (kg)
1,2024,450,50,45
2,2024,420,48,43
...
```

## 🛠️ Tecnologias usadas

- Python
- Streamlit
- Pandas
- Plotly
- Scikit-learn

## 📄 Licença

Este projeto é de uso educacional e sem fins lucrativos. Você pode reutilizar o código livremente, com os devidos créditos.

## 👨‍💻 Desenvolvedor

**Guilherme Soares**  
🔗 [LinkedIn](https://www.linkedin.com/in/guiggk/)
