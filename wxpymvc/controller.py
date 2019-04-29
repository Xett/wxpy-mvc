import wx
class Controller:
    def __init__(self, model, view):
        self.App=wx.App()
        self.Model=model
        self.View=view
        self.running=False
    def main(self):
        self.running=True
        self.View.XMLParser.configure()
        self.View.XMLParser.parse()
        while self.running:
            self.App.MainLoop()
            self.running=False
