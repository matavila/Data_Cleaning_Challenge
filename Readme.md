<h1 align="center">Data Cleaning Challenge</h1> 

Para esse projeto foi utilizado a seguinte stack: <br>
![Static Badge](https://img.shields.io/badge/Python-brightgreen)&nbsp;

As bibliotecas usadas foram: <br>

![Static Badge](https://img.shields.io/badge/pandas-blue)&nbsp;
<br>

O projeto foi hospedados usando:<br>
![Git](https://img.shields.io/badge/-Git-05122A?style=flat&logo=git)&nbsp;
![GitHub](https://img.shields.io/badge/-GitHub-05122A?style=flat&logo=github)&nbsp;
<br>

Professor:<br>
![Static Badge](https://img.shields.io/badge/Owner-RACHAEL%20TATMAN-brightgreen)

<h2 align = "left"> Primeiro Dia </h2>
<p>
Ao lidar com análises de dados, um dos desafios mais comuns é a presença de <strong>valores ausentes</strong> , 
também conhecidos como valores vazios ou NaN (Not a Number). 

    Esses valores podem surgir de várias formas, como falhas nos sensores de coleta, erros de entrada, problemas de 
    integração de dados ou até mesmo representarem informações não disponíveis.
    
Aqui é onde o pandas, uma biblioteca poderosa para manipulação e análise de dados em Python, se torna uma ferramenta
valiosa. O pandas oferece várias ferramentas para identificar e tratar valores vazios em um dataset de maneira eficiente.
Ao arrumar os valores vazios usando o pandas, podemos realizar as seguintes etapas:

    1. Identificar Valores Vazios: Com o pandas, é fácil identificar quais colunas e linhas 
    contêm valores vazios no dataset. O método isnull() pode ser aplicado ao DataFrame para 
    gerar uma matriz booleana indicando a presença de valores ausentes.


    2. Preencher Valores Vazios: O pandas fornece métodos como fillna() que permitem preencher
    os valores ausentes com uma variedade de estratégias, como preenchimento com valores constantes,
    média, mediana, ou até mesmo com os valores da próxima ou última linha.

    3. Excluir Linhas ou Colunas: Em algumas situações, é preferível remover linhas ou colunas que 
    contenham valores vazios. O método dropna() pode ser usado para eliminar as linhas ou colunas com
    valores ausentes.

    4. Interpolação de Valores: Quando os dados têm uma tendência, a interpolação pode ser uma opção 
    adequada para preencher valores ausentes com base na análise das observações adjacentes.

    5. Análise e Visualização: Após o tratamento dos valores vazios, o pandas permite realizar análises
    mais confiáveis e precisas, bem como criar visualizações mais coerentes dos dados.
</p>

<h2 align = "left"> Segundo Dia</h2>
<p>

A conversão de strings em objetos `datetime` é uma funcionalidade fundamental do Pandas quando trabalhamos com análises
de dados temporais. O Pandas oferece a função `pd.to_datetime()` para realizar essa conversão de forma simples e 
eficiente, permitindo que os dados em formato de texto contendo informações de datas sejam transformados em objetos
`datetime`, facilitando a manipulação e análise de dados temporais.

    Em casos em que a data está em um formato personalizado, como "25/07/2023" (dia/mês/ano), podemos utilizar a opção
    `format` na função `pd.to_datetime()` para especificar o formato correto. Dessa forma, o Pandas realizará a 
    conversão corretamente, considerando o formato fornecido.


Um ponto importante a ser considerado é quando o DataFrame contém datas em diferentes formatos na mesma coluna. Nesses
casos, podemos usar o argumento `errors='coerce'` na função `pd.to_datetime()`, que transforma conversões inválidas em
valores `NaT` (Not a Time), em vez de lançar erros, tornando o processo mais robusto.

</p>

<h2 align = "left">Observação</h2>
<p>
    Devido ao tamanho do banco de dados deixaremos um dos arquivos fora<br>
    <a>https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values/input</a>
</p>