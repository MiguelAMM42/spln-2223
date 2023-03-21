# AULA 4

- ocorrecia de palavras no texto do Harry Potter
    - primeiro fazer tokenização e depois contar as palavras


- usar a linha de comandos com filtros unix

- usar o `grep`para procurar palavras no texto

- usar o `sort`para ordenar as palavras

- usar o `uniq`para contar as palavras

- usar o `wc`para contar as linhas

- `tr ' ' '\n' < data/Harry_Potter_e_A_Pedra_Filosofal.txt` --> transforma os espaços em `\n`

- `tr ' ' '\n' < data/Harry_Potter_e_A_Pedra_Filosofal.txt | sort | uniq -c | sort -n` --> ordena as ocorrencias de palavras


- `tr 'A-Z' 'a-z' < data/Harry_Potter_e_A_Pedra_Filosofal.txt | tr '.?!-,;)({}:"' ' ' | tr ' ' '\n' | tr '–' ' ' |sort | uniq -c | sort -n > output.txt`



-----------

- solução parecida à minha mas que elimina totalmente o ruído

```bash
tr 'A-Z' 'a-z' < data/Harry_Potter_e_A_Pedra_Filosofal.txt | tr -d '.?!-,;)({}:"' | tr ' ' '\n' |sort | uniq -c | sort -n > output.txt
```

- podia-se também usar o complemnto do tr

```bash
tr -sc 'A-Za-z' '\n' < data/Harry_Potter_e_A_Pedra_Filosofal.txt | sort | uniq -c | sort -n > output.txt
```

`-sc` devia ser com os acentos incluidos


----------------------------------------------------------------

# RIPGREP

```bash
rg -o '\w+|[.,!;?]+' data/Harry_Potter_e_A_Pedra_Filosofal.txt | sort | uniq -c | sort -n > output.txt
```

- este ripgrep é unicode aware

no outro teriamos de usar

```bash
grep -P -o '\w+|[.,!;?]+' data/Harry_Potter_e_A_Pedra_Filosofal.txt | sort | uniq -c | sort -n > output.txt
```

-------

- apanhar nomes compostos(tipo Harry Potter)

```bash
rg -o '[A-Z]\w+ [A-Z]\w+' data/Harry_Potter_e_A_Pedra_Filosofal.txt | sort | uniq -c | sort -n > output.txt
```

-----------

- apanhar esses nomes e também nomes únicos

```bash
rg -o '[A-Z]\w+( [A-Z]\w+)*' data/Harry_Potter_e_A_Pedra_Filosofal.txt | sort | uniq -c | sort -n > output.txt
```


-------

- Fazer anotações de entidades

```bash
rg '([A-Z]\w+ [A-Z]\w+)' -r '<e>$1</e>' data/Harry_Potter_e_A_Pedra_Filosofal.txt | sort | uniq -c | sort -n > output.txt
```

- f-score: para termos uma métrica definida: um equilibrio entre precisão e recall


-----


- 14-16 de segunda : gabinete JJ se for necessário rever a gramática



-----------------------

# TP1

- quando ligamos com linguagem natural há módulos que são classicos


- escolher alguns modulos e fazer uma aplicação que use esses modulos e uma apresentação sobre o assunto

- encontrar um caso de estudo para aplicar os modulos

- convencer que certos modulos sao uteis

- fazer uma apresentação sobre o(s) módulo(s) escolhido(s) e um caso de estudo: fazer uma brincadeira com o modulo: por exemplo algo com *web scrapping*, algo com *ocr* para extrair informação de imagens, algo com *nlp* para fazer uma análise de sentimentos, algo com *machine learning* para fazer uma previsão, etc.



------------------


# Tokenizador opinion

```
token é qq coisa  que pode ser separada por um espaço
Nomes proprios
frases(periodo) - uma linha
paragrafos identados no inicio com tab
```

- token é um programa python que recebe um token que recebe filtros

- estas 2 podem ser subelementos ou opçoes de linha de comando

- para identificar parafrafos
    - podemos ter uma linha em branco , uma taghtml `<p>` ou uma linha que começa com tab ou parecido ao que esteja no texto

- para identificar quebras de página
    - normalmente são marcadas com um caractere especial , o FF (form feed) ou ^L (control-L) ou uma linha em branco(o que acontece neste texto).


- a noção de poema neste caso não vai considerada, pois não somos capazes de o processar
automaticamente. se alguém nos dissesse ou marcasse um poema, poderiamos processá-lo.
    - tal poderia ser feito com uma tag html `<poem>` ou algo do género

- acabamos por definir uma tag `<poema>`


----------------

### TPC

- acabar exercicio da aula e extender 
- invocar como um filtro unix: com flags
- identificar problemas e tentar resolver
- usar na linha de comandos em qq path e com qq ficheiro
    - arranjar mais livros
    - adicionar ficheiros de configuracao