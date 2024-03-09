
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COSINE DIVIDE INVERSECOSINE INVERSESINE INVERSETANGENT MINUS MULTIPLY NUMBER PI PLUS POWER SINE SQUAREROOT TANGENTexpression : NUMBERexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression DIVIDE expressionexpression : expression MULTIPLY expressionexpression : expression SQUAREROOTexpression : expression POWER expressionexpression : expression SINEexpression : expression COSINEexpression : expression TANGENTexpression : expression INVERSESINEexpression : expression INVERSECOSINEexpression : expression INVERSETANGENTexpression : PI'
    
_lr_action_items = {'NUMBER':([0,4,5,6,7,9,],[2,2,2,2,2,2,]),'PI':([0,4,5,6,7,9,],[3,3,3,3,3,3,]),'$end':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[0,-1,-14,-6,-8,-9,-10,-11,-12,-13,-2,-3,-4,-5,-7,]),'PLUS':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[4,-1,-14,-6,-8,-9,-10,-11,-12,-13,4,4,4,4,4,]),'MINUS':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[5,-1,-14,-6,-8,-9,-10,-11,-12,-13,5,5,5,5,5,]),'DIVIDE':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[6,-1,-14,-6,-8,-9,-10,-11,-12,-13,6,6,6,6,6,]),'MULTIPLY':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[7,-1,-14,-6,-8,-9,-10,-11,-12,-13,7,7,7,7,7,]),'SQUAREROOT':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[8,-1,-14,-6,-8,-9,-10,-11,-12,-13,8,8,8,8,8,]),'POWER':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[9,-1,-14,-6,-8,-9,-10,-11,-12,-13,9,9,9,9,9,]),'SINE':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[10,-1,-14,-6,-8,-9,-10,-11,-12,-13,10,10,10,10,10,]),'COSINE':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[11,-1,-14,-6,-8,-9,-10,-11,-12,-13,11,11,11,11,11,]),'TANGENT':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[12,-1,-14,-6,-8,-9,-10,-11,-12,-13,12,12,12,12,12,]),'INVERSESINE':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[13,-1,-14,-6,-8,-9,-10,-11,-12,-13,13,13,13,13,13,]),'INVERSECOSINE':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[14,-1,-14,-6,-8,-9,-10,-11,-12,-13,14,14,14,14,14,]),'INVERSETANGENT':([1,2,3,8,10,11,12,13,14,15,16,17,18,19,20,],[15,-1,-14,-6,-8,-9,-10,-11,-12,-13,15,15,15,15,15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,5,6,7,9,],[1,16,17,18,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',6),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','parser.py',10),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser.py',14),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_divide','parser.py',18),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_times','parser.py',22),
  ('expression -> expression SQUAREROOT','expression',2,'p_expression_squareroot','parser.py',26),
  ('expression -> expression POWER expression','expression',3,'p_expression_power','parser.py',30),
  ('expression -> expression SINE','expression',2,'p_expression_sine','parser.py',34),
  ('expression -> expression COSINE','expression',2,'p_expression_cosine','parser.py',38),
  ('expression -> expression TANGENT','expression',2,'p_expression_tangent','parser.py',42),
  ('expression -> expression INVERSESINE','expression',2,'p_expression_inversesine','parser.py',46),
  ('expression -> expression INVERSECOSINE','expression',2,'p_expression_inversecos','parser.py',50),
  ('expression -> expression INVERSETANGENT','expression',2,'p_expression_inversetan','parser.py',54),
  ('expression -> PI','expression',1,'p_expression_pi','parser.py',58),
]
