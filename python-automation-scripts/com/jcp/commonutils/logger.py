"""
Created on Mar 19, 2020

@author: kthangav
@version: 1.0
@Description: This is the main application class for Rpm Mdo price clearance feed check
"""
import logging.config
import logging
import os
import yaml

path = 'resources/logging.yml'
if os.path.exists(path):
    with open(path, 'rt') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
else:
    logging.basicConfig(level=logging.INFO)
Logger = logging.getLogger('logger')
Logger.info('Logger initialization from yaml success !')








