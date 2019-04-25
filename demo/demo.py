import wx
import wxpy-mvc
from wxpy-mvc.model import Model
from wxpy-mvc.view import View
from wxpy-mvc.controller import Controller
if __name__=="__main__":
    m=Model()
    v=View('a')
    c=Controller(m, v)
