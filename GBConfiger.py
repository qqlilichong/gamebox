
#####################################################################

import os
import configparser

#####################################################################


class GBConfiger_INI:
    extconf = '.gbconf'
    encoding = 'utf-8'

    def __init__(self):
        self.coreref = None
        self.main = ''
        self.corename = ''
        self.preview = ''
        self.comment = ''
        self.desc = ''
        self.dir = ''

    def ready(self):
        return self.main and self.corename

    def load(self, cfgfile):
        if not os.path.exists(cfgfile):
            return
        try:
            parser = configparser.ConfigParser()
            parser.read(cfgfile, self.encoding)
            self.main = parser.get('config', 'main', fallback='')
            self.corename = parser.get('config', 'core', fallback='')
            self.preview = parser.get('config', 'preview', fallback='')
            self.comment = parser.get('config', 'comment', fallback='')
            self.desc = parser.get('config', 'desc', fallback='')
            self.dir = os.path.dirname(cfgfile)
        finally:
            return


#####################################################################
