## Install library : pip install cerberus
from cerberus import *

"""
'type' => string,integer,float,boolean
'min'
'max'
'allowed' : [ , , , ]

"""
schema = {
	'nombre' : {'type': 'string', 'allowed':['Pedro','Juan']},
	'edad' : {'type': 'integer','min':0,'max':150}
}

v = Validator(schema)

mis_cosas = {'nombre' : 'Ignacio','edad':-20}

if(v.validate(mis_cosas)):
	print(mis_cosas)
else:
	print(v.errors)
	

