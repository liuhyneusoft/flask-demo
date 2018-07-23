#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import config
app = Flask(__name__)

app.config.from_object('config')

# 路由
from main.routes import *
from main.routesTest import *
from main.routepkg.userRoute import *
from main.routepkg.fileRoute import *
