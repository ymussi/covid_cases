#!/usr/bin/env python
import configparser as _configparser
from os import getenv as _getenv
from os import path as _path


config_dir = _path.dirname(__file__)
# env = _getenv('DBENV', 'development')

# env = (env if env != "" else 'production')

Config = _configparser.ConfigParser()
Config.read(_path.join(config_dir, 'development', 'config.ini'))