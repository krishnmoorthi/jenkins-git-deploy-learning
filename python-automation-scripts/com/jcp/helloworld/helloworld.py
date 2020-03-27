from com.jcp.commonutils.config_reader import ConfigReader
import logging

Logger = logging.getLogger('HelloWorld')


class HelloWorld:

    def __init__(self):
        ConfigReader.init_config()
        self.user_id = ConfigReader.properties['Secret']['user-id']

    def helloWorld(self):
        Logger.info('======================================================================')
        Logger.info('Welcome to Hello world : %s' % self.user_id)


if __name__ == '__main__':
    helloworld = HelloWorld()
    helloworld.helloWorld()

