
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON ENTRY EXCL GT HASH LANG LT NOTE RANG REM SEMI_COLON SYN VAL VAR WORDentries : entry\n               | entries entryentry : HASH WORD LANG WORD RANG values notes remissiveEntriesvalues : VAR COLON WORD\n              | SYN COLON WORD\n              | VAL COLON WORD\n              | values VAR COLON WORD\n              | values SYN COLON WORD\n              | values VAL COLON WORDnotes : NOTE WORD\n             | notes NOTE WORDremissiveEntries : REM ENTRY WORD SEMI_COLON WORD SEMI_COLON WORD\n                        | remissiveEntries SEMI_COLON WORD SEMI_COLON WORD SEMI_COLON WORD'
    
_lr_action_items = {'HASH':([0,1,2,4,21,45,46,],[3,3,-1,-2,-3,-13,-12,]),'$end':([1,2,4,21,45,46,],[0,-1,-2,-3,-13,-12,]),'WORD':([3,6,17,18,19,20,22,24,25,26,31,33,39,40,43,44,],[5,7,27,28,29,30,32,34,35,36,37,38,41,42,45,46,]),'LANG':([5,],[6,]),'RANG':([7,],[8,]),'VAR':([8,9,28,29,30,34,35,36,],[10,14,-4,-5,-6,-7,-8,-9,]),'SYN':([8,9,28,29,30,34,35,36,],[11,15,-4,-5,-6,-7,-8,-9,]),'VAL':([8,9,28,29,30,34,35,36,],[12,16,-4,-5,-6,-7,-8,-9,]),'NOTE':([9,13,27,28,29,30,32,34,35,36,],[17,22,-10,-4,-5,-6,-11,-7,-8,-9,]),'COLON':([10,11,12,14,15,16,],[18,19,20,24,25,26,]),'REM':([13,27,32,],[23,-10,-11,]),'SEMI_COLON':([21,37,38,41,42,45,46,],[31,39,40,43,44,-13,-12,]),'ENTRY':([23,],[33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'entries':([0,],[1,]),'entry':([0,1,],[2,4,]),'values':([8,],[9,]),'notes':([9,],[13,]),'remissiveEntries':([13,],[21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> entries","S'",1,None,None,None),
  ('entries -> entry','entries',1,'p_entries','plyParser.py',36),
  ('entries -> entries entry','entries',2,'p_entries','plyParser.py',37),
  ('entry -> HASH WORD LANG WORD RANG values notes remissiveEntries','entry',8,'p_entry','plyParser.py',44),
  ('values -> VAR COLON WORD','values',3,'p_values','plyParser.py',48),
  ('values -> SYN COLON WORD','values',3,'p_values','plyParser.py',49),
  ('values -> VAL COLON WORD','values',3,'p_values','plyParser.py',50),
  ('values -> values VAR COLON WORD','values',4,'p_values','plyParser.py',51),
  ('values -> values SYN COLON WORD','values',4,'p_values','plyParser.py',52),
  ('values -> values VAL COLON WORD','values',4,'p_values','plyParser.py',53),
  ('notes -> NOTE WORD','notes',2,'p_notes','plyParser.py',61),
  ('notes -> notes NOTE WORD','notes',3,'p_notes','plyParser.py',62),
  ('remissiveEntries -> REM ENTRY WORD SEMI_COLON WORD SEMI_COLON WORD','remissiveEntries',7,'p_remissive_entries','plyParser.py',69),
  ('remissiveEntries -> remissiveEntries SEMI_COLON WORD SEMI_COLON WORD SEMI_COLON WORD','remissiveEntries',7,'p_remissive_entries','plyParser.py',70),
]