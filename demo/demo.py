import wx
import wxpy-mvc
if __name__=="__main__":
    m=wxpy-mvc.model.Model()
    v=wxpy-mvc.view.View()
    c=wxpy-mvc.controller.Controller(m, v)
