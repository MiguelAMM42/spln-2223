# SPLN (TPC1)

## Trabalho desenvolvido na aula:

- Obteve-se com comandos Unix as versões `.txt` e `.xml` do ficheiro `data/medicina.pdf` deste repositório.
    - `pdftotext -f 21 -l 30 -raw  data/medicina.pdf` : ordem correta, mas sem identações;
    - `pdftohtml -xml  data/medicina.pdf` : info de fontes, bolds, italicos, etc.

- Discutiram-se as diferenças entre as versões `.txt` e `.xml` e começou a ser desenvolvido o código para a marcação do texto, usando a versão `.xml` como base.

## TPC1

- No primeiro TPC optei por usar a versão `.txt` gerada e gerar o dicionário que pode ser observado no ficheiro `out/medicina_txt.json`.

- Mais tarde, optei por usar a versão `.xml` gerada e fazer a marcação do texto, conforme discutido em aula. O resultado pode ser visto em `out/medicina_xml_processed.txt`.


- Todo o trabalho desenvolvido neste TPC pode ser observado nos ficheiros `tpc1_txt.py` e `tpc1_xml.py`.
