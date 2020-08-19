# -*- coding: utf-8 -*-
#
# Created by Alex
# august 2020
# 
# This project is licensed under CC License - see the LICENSE file for details.
# Copyright (c) 2020 Alejandro Molina Villegas
#
# Código de ejemplo para usar la expresión regular de voces misóginas

import re

# load the regexp
with open('voces-misoginas.re') as file:
	contents = file.read().replace('\n','')
	regex = re.compile(contents,flags=re.I|re.UNICODE)

# find every match
text = 'Esta vieja puta amargada es una zorra nalga Fácil'
for match in regex.findall(text):
	print(match)
