
#####################################################################

import GameCoreX
import GBConfiger
import GBForm

#####################################################################

if __name__ == '__main__':
    corex = GameCoreX.GameCoreX()
    corex.adduserpath('g:/test', GBConfiger.GBConfiger_INI)

    app = GBForm.MainApp(corex)
    app.showform()
    app.waitexit()

#####################################################################
