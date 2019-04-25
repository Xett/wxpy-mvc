import wx
class Controller:
    def __init__(self, model, view):
        self.App=wx.App()
        self.Model=model
        self.View=view
        self.running=False
    def main(self):
        self.running=True
        while self.running:
            self.App.MainLoop()
