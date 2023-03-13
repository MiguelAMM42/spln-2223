import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'HASH', 'LANG', 'RANG', 'VAR', 'SYN', 'VAL', 'NOTE',
    'REM', 'ENTRY', 'WORD', 'SEMI_COLON', 'COLON', 'GT', 'LT', 'EXCL'
]

t_HASH = r'\#'
t_LANG = r'\>'
t_RANG = r'\:'
t_VAR = r'\% variables'
t_SYN = r'\% synonyms'
t_VAL = r'\% values'
t_NOTE = r'\! notes'
t_REM = r'\& remissiveEntries'
t_ENTRY = r'\$'
t_SEMI_COLON = r'\;'
t_COLON = r'\:'
t_GT = r'\>'
t_LT = r'\<'
t_EXCL = r'\!'

t_ignore = '\n'

def t_WORD(t):
    r'[a-zA-Z0-9ñÑáéíóúÁÉÍÓÚäëïöüÄËÏÖÜçÇ\.\[\]\(\)\/\-\?\']+'
    return t

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lexer = lex.lex()

def p_entries(p):
    '''entries : entry
               | entries entry'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_entry(p):
    '''entry : HASH WORD LANG WORD RANG values notes remissiveEntries'''
    p[0] = {'term': p[2], 'language': p[4], 'values': p[6], 'notes': p[7], 'remissiveEntries': p[8]}

def p_values(p):
    '''values : VAR COLON WORD
              | SYN COLON WORD
              | VAL COLON WORD
              | values VAR COLON WORD
              | values SYN COLON WORD
              | values VAL COLON WORD'''
    if len(p) == 4:
        p[0] = {p[1].strip('%'): p[3]}
    else:
        p[1][p[2].strip('%')] = p[4]
        p[0] = p[1]

def p_notes(p):
    '''notes : NOTE WORD
             | notes NOTE WORD'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1] + '\n' + p[3]

def p_remissive_entries(p):
    '''remissiveEntries : REM ENTRY WORD SEMI_COLON WORD SEMI_COLON WORD
                        | remissiveEntries SEMI_COLON WORD SEMI_COLON WORD SEMI_COLON WORD'''
    if len(p) == 8:
        p[0] = {p[4]: p[6]}
    else:
        p[1][p[3]] = p[5]
        p[0] = p[1]

def p_error(p):
    raise TypeError("Syntax error in input!")

parser = yacc.yacc()


with open('out/medicina_treated.txt', 'r', encoding='utf-8') as f:
    data = f.read()

result = parser.parse(data)

