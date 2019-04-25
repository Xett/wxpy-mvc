class View:
    def __init__(self, pathToDefinitions):
        self.XMLParser=ViewXMLParser()
class ViewXMLParser:
    def __init__(self, pathToDefinitions):
        self.DOMTree=None
        self.collection=None
        self.pathToDefinitions=pathToDefinitions
    def configure(self, pathToDefinitions):
        self.DOMTree=xml.dom.minidom.parse(self.pathToDefinitions+"\\MainWindow.xml")
    def parse(self):
        self.collection=self.DOMTree.documentElement
        if self.collection.nodeName="Frame":
            frameDef={
                'parent':None,
                'id':-1,
                'title':'Frame',
                'pos':wx.DefaultPosition,
                'size':wx.DefaultSize,
                'style':wx.DEFAULT_FRAME_STYLE,
                'name':'Frame'
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
            for arg, default in frameDef.items():
                _arg=self.collection.getAttribute(arg)
                if _arg=='':
                    _arg=default
                if arg=='pos':
                    #takes in '(x, y)'
                    x=None
                    y=None
                args[arg]=_arg
            frame=wx.Frame(
                args['parent'],
                id=args['id'],
                title=args['title'],
                pos=args['pos'],
                size=args['size'],
                style=args['style'],
                name=args['name']
                )
