
#####################################################################

import os

#####################################################################


class Core:
    def __init__(self):
        self.comment = 'Win32 核心'

    def init(self):
        return True

    def run(self, configer):
        os.system(os.path.join(configer.dir, configer.main))
        return True


#####################################################################
