#!/bin/env python

import yaml
import jinja2

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('gen', 'templates'))

try:
    sheet = yaml.load(open('test.sheet', 'r'))
except:
    print('error')

template = env.get_template('base.html')
template.stream(sheet=sheet).dump('test.html')
