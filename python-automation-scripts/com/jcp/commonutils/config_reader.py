"""
Created on Mar 16, 2020

@author: stuliche
@version: 1.0
@Description: This is the main application class for Rpm Mdo price clearance feed check
"""
import requests
import yaml
import os
import logging

# This is the own logger for config reader as a sub logger for Logger
Logger = logging.getLogger('ConfigReader')


class ConfigReader:

    properties = dict()

    @staticmethod
    def init_config():
        path = 'resources/bootstrap.yml'
        if os.path.exists(path):
            with open(path, 'rt') as file:
                ConfigReader.properties = yaml.safe_load(file.read())
        else:
            Logger.error('%s not found' % path)
            Logger.error("Terminating Application")
            exit(1)

        Logger.info("production mode : %s" % ConfigReader.properties['production'])

        if ConfigReader.properties['production']:
            response = requests.get('http://'+ConfigReader.properties['resources']['server']['host']+':'+str(ConfigReader.properties['resources']['server']['port'])+'/'+ConfigReader.properties['resources']['uri'])

            if response:
                ConfigReader.properties = yaml.safe_load(response.content.decode('utf-8'))
            else:
                Logger.error('empty configuration file %s' % (ConfigReader.properties['resources']['uri']))
                Logger.error("Terminating Application")
                exit(1)
        else:
            path = 'resources/application.yml'
            if os.path.exists(path):
                with open(path, 'rt') as file:
                    ConfigReader.properties = yaml.safe_load(file.read())
            else:
                Logger.error('%s not found' % path)
                Logger.error("Terminating Application")
                exit(1)

        Logger.info("application configuration complete !")


