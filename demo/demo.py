#!/usr/bin/env python
import wx
import wxpy_mvc
if __name__=="__main__":
    m=wxpy_mvc.model.Model()
    v=wxpy_mvc.view.View('a')
    c=wxpy_mvc.controller.Controller(m, v)
