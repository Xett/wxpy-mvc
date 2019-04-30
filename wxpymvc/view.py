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
            'Frame':self.parseFrame,
            'MenuBar':self.parseMenuBar,
            'Menu':self.parseMenu,
            'MenuItem':self.parseMenuItem,
            'BoxSizer':self.parseBoxSizer,
            'StaticBoxSizer':self.parseStaticBoxSizer,
            'GridSizer':self.parseGridSizer,
            'GridBagSizer':self.parseGridBagSizer,
            'FlexGridSizer':self.parseFlexGridSizer,
            'WrapSizer':self.parseWrapSizer
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
        # Sizers
        self.boxSizerDefaults={
            'Orient': self.parseAttrOrient
        }
        self.staticBoxSizerDefaults={
            'Orient':self.parseAttrOrient,
            'Parent':self.parseAttrParent,
            'Label':self.parseAttrLabel
        }
        self.gridSizerDefaults={}
        self.gridBagSizerDefaults={}
        self.flexGridSizerDefaults={}
        self.wrapSizer={}
        # Panels
        self.panelDefaults={}
        # Attributes
        self.attributeIDs={
            "Open":wx.ID_OPEN,
            "Close":wx.ID_CLOSE,
            "New":wx.ID_NEW,
            "Save":wx.ID_SAVE,
            "SaveAs":wx.ID_SAVEAS,
            "Revert":wx.ID_REVERT,
            "Exit":wx.ID_EXIT,
            "Undo":wx.ID_UNDO,
            "Redo":wx.ID_REDO,
            "Help":wx.ID_HELP,
            "Print":wx.ID_PRINT,
            "PrintSetup":wx.ID_PRINT_SETUP,
            "PageSetup":wx.ID_PAGE_SETUP,
            "Preview":wx.ID_PREVIEW,
            "About":wx.ID_ABOUT,
            "HelpContents":wx.ID_HELP_CONTENTS,
            "HelpIndex":wx.ID_HELP_INDEX,
            "HelpSearch":wx.ID_HELP_SEARCH,
            "HelpCommands":wx.ID_HELP_COMMANDS,
            "HelpProcedures":wx.ID_HELP_PROCEDURES,
            "HelpContext":wx.ID_HELP_CONTEXT,
            "CloseAll":wx.ID_CLOSE_ALL,
            "Preferences":wx.ID_PREFERENCES,
            "Edit":wx.ID_EDIT,
            "Cut":wx.ID_CUT,
            "Copy":wx.ID_COPY,
            "Paste":wx.ID_PASTE,
            "Clear":wx.ID_CLEAR,
            "Find":wx.ID_FIND,
            "Duplicate":wx.ID_DUPLICATE,
            "SelectAll":wx.ID_SELECTALL,
            "Delete":wx.ID_DELETE,
            "Replace":wx.ID_REPLACE,
            "ReplaceAll":wx.ID_REPLACE_ALL,
            "Properties":wx.ID_PROPERTIES,
            "ViewDetails":wx.ID_VIEW_DETAILS,
            "ViewLargeIcons":wx.ID_VIEW_LARGEICONS,
            "ViewSmallIcons":wx.ID_VIEW_SMALLICONS,
            "ViewList":wx.ID_VIEW_LIST,
            "ViewSortDate":wx.ID_VIEW_SORTDATE,
            "ViewSortName":wx.ID_VIEW_SORTNAME,
            "ViewSortSize":wx.ID_VIEW_SORTSIZE,
            "ViewSortType":wx.ID_VIEW_SORTTYPE,
            "File":wx.ID_FILE,
            "File1":wx.ID_FILE1,
            "File2":wx.ID_FILE2,
            "File3":wx.ID_FILE3,
            "File4":wx.ID_FILE4,
            "File5":wx.ID_FILE5,
            "File6":wx.ID_FILE6,
            "File7":wx.ID_FILE7,
            "File8":wx.ID_FILE8,
            "File9":wx.ID_FILE9,
            "Ok":wx.ID_OK,
            "Cancel":wx.ID_CANCEL,
            "Apply":wx.ID_APPLY,
            "Yes":wx.ID_YES,
            "No":wx.ID_NO,
            "Static":wx.ID_STATIC,
            "Forward":wx.ID_FORWARD,
            "Backward":wx.ID_BACKWARD,
            "Default":wx.ID_DEFAULT,
            "More":wx.ID_MORE,
            "Setup":wx.ID_SETUP,
            "Reset":wx.ID_RESET,
            "ContextHelp":wx.ID_CONTEXT_HELP,
            "YesToAll":wx.ID_YESTOALL,
            "NoToAll":wx.ID_NOTOALL,
            "Abort":wx.ID_ABORT,
            "Retry":wx.ID_RETRY,
            "Ignore":wx.ID_IGNORE,
            "Add":wx.ID_ADD,
            "Remove":wx.ID_REMOVE,
            "Up":wx.ID_UP,
            "Down":wx.ID_DOWN,
            "Home":wx.ID_HOME,
            "Refresh":wx.ID_REFRESH,
            "Stop":wx.ID_STOP,
            "Index":wx.ID_INDEX,
            "Bold":wx.ID_BOLD,
            "Italic":wx.ID_ITALIC,
            "JustifyCenter":wx.ID_JUSTIFY_CENTER,
            "JustifyFill":wx.ID_JUSTIFY_FILL,
            "JustifyRight":wx.ID_JUSTIFY_RIGHT,
            "JustifyLeft":wx.ID_JUSTIFY_LEFT,
            "Underline":wx.ID_UNDERLINE,
            "Indent":wx.ID_INDENT,
            "Unindent":wx.ID_UNINDENT,
            "Zoom100":wx.ID_ZOOM_100,
            "ZoomFit":wx.ID_ZOOM_FIT,
            "ZoomIn":wx.ID_ZOOM_IN,
            "ZoomOut":wx.ID_ZOOM_OUT,
            "Undelete":wx.ID_UNDELETE,
            "RevertToSaved":wx.ID_REVERT_TO_SAVED,
            "CDRom":wx.ID_CDROM,
            "Convert":wx.ID_CONVERT,
            "Execute":wx.ID_EXECUTE,
            "Floppy":wx.ID_FLOPPY,
            "HardDisk":wx.ID_HARDDISK,
            "Bottom":wx.ID_BOTTOM,
            "First":wx.ID_FIRST,
            "Last":wx.ID_LAST,
            "Top":wx.ID_TOP,
            "Info":wx.ID_INFO,
            "JumpTo":wx.ID_JUMP_TO,
            "Network":wx.ID_NETWORK,
            "SelectColour":wx.ID_SELECT_COLOR,
            "SelectFont":wx.ID_SELECT_FONT,
            "SortAscending":wx.ID_SORT_ASCENDING,
            "SortDescending":wx.ID_SORT_DESCENDING,
            "SpellCheck":wx.ID_SPELL_CHECK,
            "Strikethrough":wx.ID_STRIKETHROUGH
        }
        self.attributeStyles={}
    def configure(self):
        self.XMLDoc=xml.dom.minidom.parse(self.pathToDefinitions+"\\MainWindow.xml")
    def parse(self):
        if self.XMLDoc.documentElement.tagName==self.rootTagName:
            args=self.parseAttributes(self.XMLDoc.documentElement, self.rootDefaults)
            # set dat root shit here
        for element in self.XMLDoc.documentElement.childNodes:
            self.parseElement(element)
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
    # Sizers
    def parseBoxSizer(self, element):
        args=self.parseAttributes(element, self.boxSizerDefaults)
        return
    def parseStaticBoxSizer(self, element):
        args=self.parseAttributes(element, self.staticBoxSizerDefaults)
        return
    def parseGridSizer(self, element):
        args=self.parseAttributes(element, self.gridSizerDefaults)
        return
    def parseGridBagSizer(self, element):
        args=self.parseAttributes(element, self.gridBagSizerDefaults)
        return
    def parseFlexGridSizer(self, element):
        args=self.parseAttributes(element, self.flexGridSizerDefaults)
        return
    def parseWrapSizer(self, element):
        args=self.parseAttributes(element, self.wrapSizerDefaults)
        return

    def parseAttributes(self, element, attributeDefaults):
        # args is a dictionary of the arguments that will be fed into the wx object being created
        # we copy it and clear all values
        args=copy.deepcopy(attributeDefaults)
        # arrtibuteDefaults, attributes and args all use the same keys
        for argAttrString, default in attributeDefaults.items():
            # we iterate through all attributes used by the widget we want to create
            # attr is the value read from the file for the attribute
            attr=element.getAttribute(argAttrString)
            # if the attribute is blank, we set it to the default
            if attr!='':
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
    def parseAttrOrient(self, attr):
        return
