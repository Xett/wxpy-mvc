import copy
import xml.dom.minidom
import wx
class View:
    def __init__(self, pathToDefinitions):
        self.XMLParser=ViewXMLParser(pathToDefinitions)
class ViewXMLParser:
    def __init__(self, pathToDefinitions):
        self.XMLDoc=None
        self.frames=[]
        self.pathToDefinitions=pathToDefinitions
        self.rootTagName='ViewXMLDef'
        # attributes is a dictionary of parsable attribute functions and the string used to identify them
        self.attributes={
            'parent':self.parseAttrParent,
            'id':self.parseAttrID,
            'title':self.parseAttrTitle,
            'pos':self.parseAttrPos,
            'size':self.parseAttrSize,
            'style':self.parseAttrStyle,
            'name':self.parseAttrName
        }
        self.elements={
            'Frame':self.parseFrame
        }
        self.rootDefaults={}
        self.frameDefaults={
            'parent':None,
            'id':-1,
            'title':'Frame',
            'pos':wx.DefaultPosition,
            'size':wx.DefaultSize,
            'style':wx.DEFAULT_FRAME_STYLE,
            'name':'Frame'
        }
        self.attributeStyles{}
    def configure(self):
        self.XMLDoc=xml.dom.minidom.parse(self.pathToDefinitions+"\\MainWindow.xml")
    def parse(self):
        if self.XMLDoc.documentElement.tagName==self.rootTagName:
            self.parseRoot()
        for element in self.XMLDoc.documentElement.childNodes:
            self.parseElement(element)
    def parseRoot(self):
        args=self.parseAttributes(self.XMLDoc.documentElement, self.rootDefaults)
        return
    def parseElement(self, element):
        for elementString, func in self.elements.items():
            self.elements[element.tagName](element)
            for childElement in element.childNodes:
                self.parseElement(childElement)
    def parseFrame(self, element):
        args=self.parseAttributes(element, self.frameDefaults)
        frame=wx.Frame(
            args['parent'],
            id=args['id'],
            title=args['title'],
            pos=args['pos'],
            size=args['size'],
            style=args['style'],
            name=args['name']
        )
        frame.Show()
        self.frames.append(frame)
    def parseAttributes(self, element, attributeDefaults):
        # args is a dictionary of the arguments that will be fed into the wx object being created
        # we copy it and clear all values
        args=copy.deepcopy(attributeDefaults)
        for argAttrString, default in args.items():
            default=None
        # arrtibuteDefaults, attributes and args all use the same keys
        for argAttrString, default in attributeDefaults.items():
            # we iterate through all attributes used by the widget we want to create
            # attr is the value read from the file for the attribute
            attr=element.getAttribute(argAttrString)
            # if the attribute is blank, we set it to the default
            if attr=='':
                attr=default
            # argAttrString is the key, so we can use them in both attributes
            # args[argAttrString] is the attribute we want to set
            # attributes[argAttrString](attr) calls the parsing function for the attribute
            args[argAttrString]=self.attributes[argAttrString](attr)
        return args
    def parseAttrParent(self, attr):
        return wx.Window.FindWindowByName(attr)
    def parseAttrID(self, attr):
        return attr
    def parseAttrTitle(self, attr):
        return attr
    def parseAttrPos(self, attr):
        # takes in '(x,y)'
        x, y=attr[1:-1].split(',')
        attr=wx.Point(int(x), int(y))
        return attr
    def parseAttrSize(self, attr):
        # takes in '(width,height)'
        width, height=attr[1:-1].split(',')
        attr=wx.Size(int(width), int(height))
        return attr
    def parseAttrStyle(self, attr):
        # takes in (style1,style2,...,stylen)
        styleStrings=attr[1:-1].split(',')
        return attr
    def parseAttrName(self, attr):
        return attr
