# ZEP -> E*
# E -> EC
#    | ER
# EC -> num pals pos CORPO
# CORPO -> area LINGUAS
# LINGUAS -> pt pals
#          | en pals
#          | es pals
# ER -> pals VID
# VID -> Vid.- pals

import re

texto = open('data/medicina.xml', 'r').read()

def remove_trash(texto):
    texto = re.sub(r'<\?xml.*version.*>', r'', texto)
    texto = re.sub(r'<\!DOCTYPE.*>', r'', texto)
    texto = re.sub(r'<fontspec.*>', r'', texto)
    texto = re.sub(r'<.*pdf2xml.*>', r'', texto)
    texto = re.sub(r'<text.* font="5">\s<\/text>', r'', texto)

    return texto

texto = remove_trash(texto)

def remove_header_footer(texto):
    texto = re.sub(r'<text.* font="1">ocabulario.*</text>', r'###', texto)
    texto = re.sub(r'.*\n###\n.*\n', r'', texto)
    texto = re.sub(r'<page.*\n|</page>\n', r'', texto)
    
    return texto

texto = remove_header_footer(texto)

def marcaE(texto):
    texto = re.sub(r'<text.* font="3"><b>\s*(\d+.*)</b></text>', r'###C \1', texto)
    texto = re.sub(r'<text.* font="3"><b>\s*(\S.*)</b></text>', r'###R \1', texto)
    texto = re.sub(r'<text.* font="10"><i><b>(.*)</b></i></text>', r'###R \1', texto)
    texto = re.sub(r'<text.* font="11"><b>\s*(.*)</b></text>', r'###R \1', texto)
    return texto

texto = marcaE(texto)


def marcaSubdmonio(texto):
    texto = re.sub(r'<text.* font="6"><i>(.*)<\/i><\/text>', r'% \1', texto)
  
    return texto

texto = marcaSubdmonio(texto)


def marcaLinguas(texto):
    # @
    texto = re.sub(r'<text.* font="0">(.*)<\/text>', r'@ \1', texto)
    texto = re.sub(r'<text.* font="7"><i>(.*)<\/i><\/text>', r'@@ \1', texto)
  
    return texto

texto = marcaLinguas(texto)


def marcaVidSin(texto):
    texto = re.sub(r'<text.* font="5">.*SIN\.\-(.*)<\/text>', r'>SIN: \1', texto)
    texto = re.sub(r'<text.* font="5">.*Vid.\-(.*)<\/text>', r'>Vid: \1', texto)
    texto = re.sub(r'<text.* font="5">\s*(.*)<\/text>', r'> \1', texto)
  
    return texto
    
texto = marcaVidSin(texto)


def marcaNotas(texto):
    texto = re.sub(r'<text.* font="9">.*Nota\.\-(.*)<\/text>', r'&Nota: \1', texto)
    texto = re.sub(r'<text.* font="9">\s*(.*)<\/text>', r'& \1', texto)
  
    return texto

texto = marcaNotas(texto)


def removeOthers(texto):
    texto = re.sub(r'<text.* font="8"><b>(.*)<\/b><\/text>', r'\1', texto)
    texto = re.sub(r'<text.* font="4"><b>(.*)<\/b><\/text>', r'\1', texto)
    texto = re.sub(r'<text.* font="3"><b>(.*)<\/b><\/text>', r'\1', texto)
  
    return texto

texto = removeOthers(texto)

def marcaErradasRem(texto):
    texto = re.sub(r'<text.* font="2">\s*(\d+)\s*<\/text>', r'\1', texto)
    texto = re.sub(r'<text.* font="2">\s*<\/text>', r'', texto)
    texto = re.sub(r'<text.* font="12">\s*(\d+)\s*<\/text>', r'\1', texto)
    texto = re.sub(r'<text.* font="12">\s*<\/text>', r'', texto)
    texto = re.sub(r'(\d+)\n###R', r'###C \1', texto)

    return texto

texto = marcaErradasRem(texto)

def lostNumbers(texto):
    texto = re.sub(r'\n(.*)\n<text.* font="13"><b>\s*(\d+)\s*<\/b><\/text>', r'\n\1 \2\n', texto)
    texto = re.sub(r'\n(.*)\n<text.* font="15"><b>\s*(\d+)\s*<\/b><\/text>', r'\n\1 \2\n', texto)
    texto = re.sub(r'\n(.*)\n<text.* font="18"><b>\s*(\d+)\s*<\/b><\/text>', r'\n\1 \2\n', texto)
    texto = re.sub(r'\n(.*)\n<text.* font="13"><i>\s*(\d+)\s*<\/i><\/text>', r'\n\1 \2\n', texto)
    texto = re.sub(r'\n(.*)\n<text.* font="15"><i>\s*(\d+)\s*<\/i><\/text>', r'\n\1 \2\n', texto)
    texto = re.sub(r'\n(.*)\n<text.* font="18"><i>\s*(\d+)\s*<\/i><\/text>', r'\n\1 \2\n', texto)
    texto = re.sub(r'\n(.*)\n<text.* font="14">\s*(\d+)\s*<\/text>', r'\n\1 \2\n', texto)
    return texto

texto = lostNumbers(texto)

texto = re.sub(r'^\s*$', r'', texto, flags=re.MULTILINE)

def marcaEC(texto):
    pass

def marcaER(texto):
    pass


file = open('out/medicina_xml_processed.txt', 'w')

file.write(texto)