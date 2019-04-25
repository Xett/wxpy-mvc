import wx
import wxpy-mvc
from wxpy-mvc import model.Model as Model
from wxpy-mvc import view.View as View
from wxpy-mvc import controller.Controller as Controller
if __name__=="__main__":
    m=Model()
    v=View('a')
    c=Controller(m, v)
