
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COSINE DIVIDE ELSEIF FOR FUNC FUNC_CALL GREATERTHAN IF LESSTHAN LPAREN MINUS MULTIPLY NUMBER PI PLUS POWER PRINT RPAREN SINE SQUAREROOT TANGENT VALUE WHILEexpression : NUMBERexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression DIVIDE expressionexpression : expression MULTIPLY expressionexpression : SQUAREROOT LPAREN expression RPARENexpression : expression POWER expressionexpression : SINE LPAREN expression RPARENexpression : COSINE LPAREN expression RPARENexpression : TANGENT LPAREN expression RPARENexpression : PIexpression : FUNC_CALLexpression : PRINT LESSTHAN expression GREATERTHAN'
    
_lr_action_items = {'NUMBER':([0,10,11,12,13,14,15,16,17,18,19,],[2,2,2,2,2,2,2,2,2,2,2,]),'SQUAREROOT':([0,10,11,12,13,14,15,16,17,18,19,],[3,3,3,3,3,3,3,3,3,3,3,]),'SINE':([0,10,11,12,13,14,15,16,17,18,19,],[4,4,4,4,4,4,4,4,4,4,4,]),'COSINE':([0,10,11,12,13,14,15,16,17,18,19,],[5,5,5,5,5,5,5,5,5,5,5,]),'TANGENT':([0,10,11,12,13,14,15,16,17,18,19,],[6,6,6,6,6,6,6,6,6,6,6,]),'PI':([0,10,11,12,13,14,15,16,17,18,19,],[7,7,7,7,7,7,7,7,7,7,7,]),'FUNC_CALL':([0,10,11,12,13,14,15,16,17,18,19,],[8,8,8,8,8,8,8,8,8,8,8,]),'PRINT':([0,10,11,12,13,14,15,16,17,18,19,],[9,9,9,9,9,9,9,9,9,9,9,]),'$end':([1,2,7,8,20,21,22,23,24,30,31,32,33,34,],[0,-1,-11,-12,-2,-3,-4,-5,-7,-6,-8,-9,-10,-13,]),'PLUS':([1,2,7,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[10,-1,-11,-12,10,10,10,10,10,10,10,10,10,10,-6,-8,-9,-10,-13,]),'MINUS':([1,2,7,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[11,-1,-11,-12,11,11,11,11,11,11,11,11,11,11,-6,-8,-9,-10,-13,]),'DIVIDE':([1,2,7,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[12,-1,-11,-12,12,12,12,12,12,12,12,12,12,12,-6,-8,-9,-10,-13,]),'MULTIPLY':([1,2,7,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[13,-1,-11,-12,13,13,13,13,13,13,13,13,13,13,-6,-8,-9,-10,-13,]),'POWER':([1,2,7,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[14,-1,-11,-12,14,14,14,14,14,14,14,14,14,14,-6,-8,-9,-10,-13,]),'RPAREN':([2,7,8,20,21,22,23,24,25,26,27,28,30,31,32,33,34,],[-1,-11,-12,-2,-3,-4,-5,-7,30,31,32,33,-6,-8,-9,-10,-13,]),'GREATERTHAN':([2,7,8,20,21,22,23,24,29,30,31,32,33,34,],[-1,-11,-12,-2,-3,-4,-5,-7,34,-6,-8,-9,-10,-13,]),'LPAREN':([3,4,5,6,],[15,16,17,18,]),'LESSTHAN':([9,],[19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,10,11,12,13,14,15,16,17,18,19,],[1,20,21,22,23,24,25,26,27,28,29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',18),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','parser.py',22),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser.py',26),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_divide','parser.py',30),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_times','parser.py',34),
  ('expression -> SQUAREROOT LPAREN expression RPAREN','expression',4,'p_expression_squareroot','parser.py',41),
  ('expression -> expression POWER expression','expression',3,'p_expression_power','parser.py',52),
  ('expression -> SINE LPAREN expression RPAREN','expression',4,'p_expression_sine','parser.py',63),
  ('expression -> COSINE LPAREN expression RPAREN','expression',4,'p_expression_cosine','parser.py',76),
  ('expression -> TANGENT LPAREN expression RPAREN','expression',4,'p_expression_tangent','parser.py',87),
  ('expression -> PI','expression',1,'p_expression_pi','parser.py',98),
  ('expression -> FUNC_CALL','expression',1,'p_expression_func_call','parser.py',102),
  ('expression -> PRINT LESSTHAN expression GREATERTHAN','expression',4,'p_expression_print','parser.py',107),
]
