# Aula 2

- Lark

- Ply

## Lembrar TPC 1

- meter README no git

PDF ---- pdfToHTML -XML ---------> .XML ----(substituiçao, add acucar sintatico)--->  marcas(processado).txt ----- (splits, subs, etc) ----> .JSON
 |
 |---------------------------------------- pdfToText -----------------------------------------------------> .TXT


 ----------------------------------------

 - o que fazer agora?
    - A) enunciado
    - B) tipo
    - C) como chegar ao JSON


- da STR monstruosa inicial fomos para uma estrutura intermédia e depois para o JSON

- B) tipo: um possivel tipo de dados para o JSON
```
DICIONARIO 
    | LISTA ENTRADAS COMPLETAS  ec*
    | LISTA ENTRADAS REMISSIVAS er*

ENTRADA COMPLETA
    | INDICE    N
    | TERMO(Ga) STR
    | CAT   {m,f,....}
    | AREAS termo*
    | SINONIMOS(Ga) termo*
    | VARIANTES(Ga) termo*
    | TRADUCOES: 
        | ES
        | EN
        | PT
        | LA
    | NOTA(Ga)  txt

ENTRADA REMISSIVA
    | DENOMINACAO   termo
    | REFERENCIA    termo inv termo x in some termo ec

Termo***
tem especificidades
CAT:... nos sin (m)
[POP.][cult.]......registo(mais ou menos coloquial)
[BR.][PT.]...........variante da lingua
(PS.)..........sigla

(um termo pode ou não ter estes atributos)

```



- Gramática
```

DIC -> meta E*
E -> termo ':' '{' NUMBER ';' GENDER ';' SUBDOMAIN ';' LANGUAGES ';' NOTES'}'
NUMBER -> /d+
GENDER -> [fmao]
SUDMONAIN -> \w+
LANGUAGES -> '[' LANG+ ']'
LANG -> '{' LANGCODE ':' txt '}' ','
LANGCODE -> "es" | "en" | "pt" | "la"
NOTES -> empty
       | \w+

```
tendo em conta:
```
{
   "á": {
    "gender": "f",
    "languages": {
     "en": "wing",
     "es": "ala",
     "la": "ala\n",
     "pt": "asa"
    },
    "notes": "",
    "number": 1,
    "remissiveEntries": "",
    "subdomain": "Anatomía"
   }
  },
  {
   "a termo": {
    "gender": "a",
    "languages": {
     "en": "full term",
     "es": "a término",
     "pt": "a termo\n"
    },
    "notes": "",
    "number": 2,
    "remissiveEntries": "",
    "subdomain": "Fisioloxía"
   }
  }

```

- sol prof (nao completa)

```

E->
    Area
    Ling *

Ling -> L ':' trad

trad -> Str atr

atr -> '+' id val
```

```
Area:----
GA:------
   ------
+var : --
EN:------
   ------
PT: -----
+var : BR
       --
+var : PT
```




DEfinicao
Hiperonimo hoponimo
pArt of
meronimo holonimo


---------

- Da gramatica construir o parser PLY ou Lark
- fazer travessia ao JSON normalizando-o para o conceito e nao ao PDF
- limar arestas do TPC1
- colocar um README para cada TPC: MINI relatorio(tipo "defesa do trabalho")

já temos: RS(pdf.......JSON): vista(Gal->info)
            |
            |
            |
            v
queremos: RS(dic médico ABSTRATO: galega é representado como uma lingua qq)
                    |
                    |
                    |
                    v
Ling DIC --------------------------tendo em conta a gramática definida


- sol prof(GRamatica definida)

```
DIC -> meta E*

E -> Item*

Item -> AT-conc
      | Lingua

AT-conc -> Id ':' val

Lingua -> ID-ling ':' T*

T -> Termo AT-T*

AT-T -> '+' id ':' val
                   str


```


- arranjar um exemplo minimo para o parser do TPC