class View:
    def __init__(self):
        return
class ViewXMLParser:
    def __init__(self):
        self.DOMTree=None
        self.collection=None
    def configure(self, pathToDefinitions):
        self.DOMTree=xml.dom.minidom.parse(pathToDefinitions+"\\MainWindow.xml")
    def parse(self):
        self.collection=self.DOMTree.documentElement
        if self.collection.nodeName="Window":
            windowDef={
                'parent':None,
                'id':-1,
                'title':'Window',
                'pos':wx.DefaultPosition,
                'size':wx.DefaultSize,
                'style':wx.DEFAULT_FRAME_STYLE,
                'name':'Window'
                }
            args={
                'parent':None,
                'id':None,
                'title':None,
                'pos':None,
                'size':None,
                'style':None,
                'name':None
                }
            for arg, default in windowDef.items():
                _arg=self.collection.getAttribute(arg)
                if _arg=='':
                    _arg=default
                if arg=='pos':
                    #takes in '(x, y)'
                    x=None
                    y=None
                args[arg]=_arg
            window=wx.Frame(
                args['parent'],
                id=args['id'],
                title=args['title'],
                pos=args['pos'],
                size=args['size'],
                style=args['style'],
                name=args['name']
                )
