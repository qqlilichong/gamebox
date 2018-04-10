
#####################################################################

import os
import subprocess

#####################################################################


class Core:
    def __init__(self):
        self.comment = 'DOS 核心'
        self.dosbox = 'C:/Program Files (x86)/DOSBox-0.74/dosbox.exe'

    def init(self):
        return os.path.exists(self.dosbox)

    def run(self, configer):
        cfgfile = os.path.join(configer.dir, configer.main)
        cfgfile += '.dosbox'
        with open(cfgfile, 'wt', encoding='utf-8') as fd:
            fd.write('[autoexec]' + '\n')
            fd.write('mount d ' + configer.dir + '\n')
            fd.write('d:' + '\n')
            fd.write(configer.main + '\n')

        subprocess.call([self.dosbox, '-conf', cfgfile])
        return True


#####################################################################
