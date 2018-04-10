
#####################################################################

import os

#####################################################################


class GameCoreX:
    def __init__(self):
        self.games = []
        self.cores = {}
        self.init()

    def init(self):
        print('***********    GameCoreX::init    ***********')
        print('')

        for file in os.listdir():
            if os.path.isdir(file):
                continue
            if file.startswith('GameCore_'):
                name, ext = os.path.splitext(file)
                if self.cores.get(name):
                    continue
                self.cores[name] = __import__(name).Core()
                print('core loaded  : %s' % name)

        removelist = []
        for name, core in self.cores.items():
            if not core.init():
                removelist.append(name)
                print('core init failed : %s' % name)

        for name in removelist:
            self.cores.pop(name)

        print('')
        print('############    end    #####################')
        print('')

    def adduserpath(self, userpath, factory_configer):
        print('***********    GameCoreX::adduserpath    ***********')
        print('')

        for d in os.listdir(userpath):
            try:
                abspath = os.path.join(userpath, d)
                print('finded   : %s' % abspath)
                configer = factory_configer()
                configer.load(os.path.join(abspath, d + configer.extconf))
                if not configer.ready():
                    print('error    : configer failed')
                    continue
                if not self.bindcore(configer):
                    print('error    : bindcore failed')
                    continue
                print('newgame  : %s - %s' % (configer.corename, configer.main))
                self.games.append(configer)
            finally:
                print('')

        print('############    end    #####################')
        print('')

    def bindcore(self, configer):
        ret = False
        try:
            configer.coreref = self.cores[configer.corename]
            ret = True
        finally:
            return ret


#####################################################################
