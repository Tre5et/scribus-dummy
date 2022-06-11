# Constants
# Measurement units
UNIT_C = -1
UNIT_CENTIMETRES = -1
UNIT_CICERO = UNIT_C
UNIT_CM = UNIT_CENTIMETRES
UNIT_IN = -1
UNIT_INCHES = UNIT_IN
UNIT_MILLIMETERS = -1
UNIT_MM = UNIT_MILLIMETERS
UNIT_P = -1
UNIT_PICAS = UNIT_P
UNIT_POINTS = -1
UNIT_PT = UNIT_POINTS

# Unit Conversion
pt = -1
inch = -1
p = -1
cm = -1
mm = -1

# Page orientation
PORTRAIT = 0
LANDSCAPE = 1

# Page sizes
PAPER_A0 = [2380, 3368]
PAPER_A0_MM = [841, 1189]
PAPER_A1 = [1684, 2380]
PAPER_A1_MM = [594, 841]
PAPER_A2 = [1190, 1684]
PAPER_A2_MM = [420, 594]
PAPER_A3 = [842, 1190]
PAPER_A3_MM = [297, 420]
PAPER_A4 = [595, 842]
PAPER_A4_MM = [210, 297]
PAPER_A5 = [421, 595]
PAPER_A5_MM = [148, 210]
PAPER_A6 = [297, 421]
PAPER_A6_MM = [105, 148]
PAPER_A7 = [210, 297]
PAPER_A7_MM = [74, 105]
PAPER_A8 = [148, 210]
PAPER_A8_MM = [52, 74]
PAPER_A9 = [105, 148]
PAPER_A9_MM = [37, 52]
PAPER_B0 = [2836, 4008]
PAPER_B0_MM = [1000, 1414]
PAPER_B1 = [2004, 2836]
PAPER_B1_MM = [707, 1000]
PAPER_B2 = [1418, 2004]
PAPER_B2_MM = [500, 707]
PAPER_B3 = [1002, 1418]
PAPER_B3_MM = [353, 500]
PAPER_B4 = [709, 1002]
PAPER_B4_MM = [250, 353]
PAPER_B5 = [501, 709]
PAPER_B5_MM = [176, 250]
PAPER_B6 = [355, 501]
PAPER_B6_MM = [125, 176]
PAPER_B7 = [250, 355]
PAPER_B7_MM = [88, 125]
PAPER_B8 = [178, 250]
PAPER_B8_MM = [62, 88]
PAPER_B9 = [125, 178]
PAPER_B9_MM = [44, 62]
PAPER_B10 = [89, 125]
PAPER_B10_MM = [31, 44]
PAPER_C5E = [462, 649]
PAPER_COMM10E = [298, 683]
PAPER_DLE = [312, 624]
PAPER_EXECUTIVE = [542, 720]
PAPER_FOLIO = [595, 935]
PAPER_LEDGER = [1224, 792]
PAPER_LEGAL = [612, 1008]
PAPER_LETTER = [612, 792]
PAPER_TABLOID = [792, 1224]

# Document layout
FACINGPAGES = -1
NOFACINGPAGES = -1
FIRSTPAGELEFT = -1
FIRSTPAGERIGHT = -1

# Layer modes
NORMAL = -1
DARKEN = -1
LIGHTEN = -1
MULTIPLY = -1
SCREEN = -1
OVERLAY = -1
HARD_LIGHT = -1
SOFT_LIGHT = -1
DIFFERENCE = -1
EXCLUSION = -1
COLOR_DODGE = -1
COLOR_BURN = -1
HUE = -1
SATURATION = -1
COLOR = -1
LUMINOSITY = -1

ITEM_IMAGEFRAME = -1
ITEM_TEXTFRAME = -1
ITEM_LINE = -1
ITEM_POLYGON = -1
ITEM_POLYLINE = -1
ITEM_PATHTEXT = -1
ITEM_LATEXFRAME = -1
ITEM_OSGFRAME = -1
ITEM_SYMBOL = -1
ITEM_GROUP = -1
ITEM_REGULARPOLYGON = -1
ITEM_ARC = -1
ITEM_SPIRAL = -1
ITEM_TABLE = -1
ITEM_NOTEFRAME = -1
ITEM_MULTIPLE = -1
ALIGN_LEFT = -1
ALIGN_CENTERED = -1
ALIGN_RIGHT = -1
ALIGN_FORCED = -1
ALIGN_BLOCK = -1
ALIGNV_TOP = -1
ALIGNV_CENTERED = -1
ALIGNV_BOTTOM = -1
FLOP_REALGLYPHHEIGHT = -1
FLOP_FONTASCENT = -1
FLOP_LINESPACING = -1
FLOP_BASELINEGRID = -1
LINE_DASH = -1
LINE_DASHDOT = -1
LINE_DASHDOTDOT = -1
LINE_DOT = -1
LINE_SOLID = -1
JOIN_BEVEL = -1
JOIN_MITTER = -1
JOIN_ROUND = -1
CAP_FLAT = -1
CAP_ROUND = -1
CAP_SQUARE = -1
CSPACE_UNDEFINED = -1
CSPACE_RGB = -1
CSPACE_CMYK = -1
CSPACE_GRAY = -1
CSPACE_DUOTONE = -1
CSPACE_MONOCHROME = -1
FILL_NOG = -1
FILL_HORIZONTALG = -1
FILL_VERTICALG = -1
FILL_DIAGONALG = -1
FILL_CROSSDIAGONALG = -1
FILL_RADIALG = -1
BUTTON_ABORT = 262144
BUTTON_CANCEL = 4194304
BUTTON_IGNORE = 1048576
BUTTON_NO = 65536
BUTTON_NONE = None
BUTTON_OK = 1024
BUTTON_RETRY = 524288
BUTTON_YES = 16384
BUTTON_DEFAULT = -1
BUTTON_ESCAPE = -1
ICON_CRITICAL = -1
ICON_INFORMATION = -1
ICON_NONE = -1
ICON_WARNING = -1
TAB_LEFT = -1
TAB_RIGHT = -1
TAB_PERIOD = -1
TAB_COMMA = -1
TAB_CENTER = -1
PRNLANG_POSTSCRIPT1 = -1
PRNLANG_POSTSCRIPT2 = -1
PRNLANG_POSTSCRIPT3 = -1
PRNLANG_WINDOWSGDI = -1
PRNLANG_PDF = -1


# Errors
class Error(Exception):
    pass


class NoDocOpenError(Error):
    pass


class ScribusError(Error):
    pass


class NameExistsError(Error):
    pass


class NotFoundError(Error):
    pass


class WrongFrameTypeError(Error):
    pass


# Document Commands
def closeDoc() -> None:
    """Closes the current document without prompting to save.
    May throw NoDocOpenError if there is no document to close"""
    pass


def docChanged(bool: bool) -> None:
    """Enable/disable save icon in the Scribus icon bar and the Save menu item. It's useful to call this procedure when you're changing the document, because Scribus won't automatically notice when you change the document using a script."""
    pass


def getDocName() -> str:
    """Returns the name the document was saved under. If the document was not saved before the name is empty."""
    pass

def getUnit() -> int:
    """Returns the measurement units of the document. The returned value will be one of the UNIT_* constants: UNIT_INCHES, UNIT_MILLIMETERS, UNIT_PICAS, UNIT_POINTS"""
    pass


def haveDoc() -> int:
    """Returns the quantity of open documents: 0 if none are opened."""
    pass


def newDocument(size: tuple, margins: tuple, orientation: int, firstPageNumber: int, unit: int, pagesType: int,
                firstPageOrder: int, numPages: int) -> bool:
    """Creates a new document and returns true if successful. The parameters have the following meaning:

    size = A tuple (width, height) describing the size of the document. You can use predefined constants named PAPER_ e.g. PAPER_A4 etc.

    margins = A tuple (left, right, top, bottom) describing the document margins

    orientation = the page orientation - constants PORTRAIT, LANDSCAPE

    firstPageNumer = is the number of the first page in the document used for pagenumbering. While you'll usually want 1, it's useful to have higher numbers if you're creating a document in several parts.

    unit: this value sets the measurement units used by the document. Use a predefined constant for this, one of: UNIT_INCHES, UNIT_MILLIMETERS, UNIT_PICAS, UNIT_POINTS.

    pagesType = One of the predefined constants PAGE_n. PAGE_1 is single page, PAGE_2 is for facing pages documents, PAGE_3 is for 3 pages fold and PAGE_4 is 4-fold.

    firstPageOrder = What is position of first page in the document. Indexed from 0 (0 = first).

    numPage = Number of pages to be created.

    The values for width, height and the margins are expressed in the given unit for the document. PAPER_* constants are expressed in points. If your document is not in points, make sure to account for this.

    example: newDocument(PAPER_A4, (10, 10, 20, 20), LANDSCAPE, 7, UNIT_POINTS, PAGE_4, 3, 1)

    May raise ScribusError if is firstPageOrder bigger than allowed by pagesType."""
    pass


def openDoc(name: str) -> None:
    """Opens the document "name".

    May raise ScribusError if the document could not be opened."""
    pass


def redrawAll() -> None:
    """Redraws all pages."""
    pass


def revertDoc() -> None:
    """Revert the current document to its last saved state."""
    pass


def saveDoc() -> None:
    """Saves the current document with its current name, returns true if successful. If the document has not already been saved, this may bring up an interactive save file dialog.

If the save fails, there is currently no way to tell."""
    pass


def saveDocAs(name: str) -> None:
    """Saves the current document under the new name "name" (which may be a full or relative path).

May raise ScribusError if the save fails."""
    pass


def setBaseLine(grid: float, offset: float) -> None:
    """Sets the base line settings of the document, grid spacing(grid), grid offset(offset). Values are given in the measurement units of the document - see UNIT_ constants."""
    pass


def setBleeds(lr: float, rr: float, tr: float, br: float) -> None:
    """Sets the bleeds of the document. Left(lr), Right(rr), Top(tr) and Bottom(br) bleeds are given in the measurement units of the document - see UNIT_ constants."""
    pass


def setDocType(facingPages: int, firstPageLeft: int) -> None:
    """Sets the document type. To get facing pages set the first parameter to FACINGPAGES, to switch facingPages off use NOFACINGPAGES instead. If you want to be the first page a left side set the second parameter to FIRSTPAGELEFT, for a right page use FIRSTPAGERIGHT."""
    pass


def setInfo(author: str, info: str, description: str) -> bool:
    """Sets the document information. "Author", "Info", "Description" are strings."""
    return success


def setMargins(lr: float, rr: float, tr: float, br: float) -> None:
    """Sets the margins of the document, Left(lr), Right(rr), Top(tr) and Bottom(br) margins are given in the measurement units of the document - see UNIT_ constants."""
    pass


def setRedraw(redraw: bool) -> None:
    """Disables page redraw when bool = False, otherwise redrawing is enabled. This change will persist even after the script exits, so make sure to call setRedraw(True) in a finally: clause at the top level of your script."""
    pass


def setUnit(type: int) -> None:
    """Changes the measurement unit of the document. Possible values for "unit" are defined as constants UNIT_.

May raise ValueError if an invalid unit is passed."""
    pass


# Master Page Commands
def applyMasterPage(masterPageName: str, pageNr: int) -> None:
    """Apply master page masterPageName on page pageNumber."""
    pass


def closeMasterPage() -> None:
    """Closes the currently active master page, if any, and returns editing to normal. Begin editing with editMasterPage()."""
    pass


def createMasterPage(pageName: str) -> None:
    """Creates a new master page named pageName and opens it for editing."""
    pass


def deleteMasterPage(pageName: str) -> None:
    """Delete the named master page."""
    pass


def editMasterPage(pageName: str) -> None:
    """Enables master page editing and opens the named master page for editing. Finish editing with closeMasterPage()."""
    pass


def getMasterPage(pageNr: int) -> None:
    """Returns the name of master page applied to page "nr".

May raise IndexError if the page number is out of range."""
    pass


def masterPageNames() -> None:
    """Returns a list of the names of all master pages in the document."""
    pass


# Layers
def createLayer(name: str) -> None:
    """Creates a new layer with the name "name".

May raise ValueError if the layer name isn't acceptable."""
    pass


def deleteLayer(layer: str) -> None:
    """Deletes the layer with the name "layer". Nothing happens if the layer doesn't exists or if it's the only layer in the document.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass


def getActiveLayer() -> str:
    """Returns the name of the current active layer."""
    pass


def getLayerBlendmode(layer: str) -> int:
    """Returns the "layer" layer blendmode,

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass


def getLayerTransparency(layer: str) -> float:
    """Returns the "layer" layer transparency,

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def getLayers() -> list:
    """Returns a list with the names of all defined layers."""
    pass


def isLayerFlow(layer: str) -> bool:
    """Returns whether text flows around objects on layer "layer", a value of True means that text flows around, a value of False means that the text does not flow around.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def isLayerLocked(layer: str) -> bool:
    """Returns whether the layer "layer" is locked or not, a value of True means that the layer "layer" is editable, a value of False means that the layer "layer" is locked.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass


def isLayerOutlined(layer: str) -> bool:
    """Returns whether the layer "layer" is outlined or not, a value of True means that the layer "layer" is outlined, a value of False means that the layer "layer" is normal.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def isLayerPrintable(layer: str) -> bool:
    """Returns whether the layer "layer" is printable or not, a value of True means that the layer "layer" can be printed, a value of False means that printing the layer "layer" is disabled.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def isLayerVisible(layer: str) -> bool:
    """Returns whether the layer "layer" is visible or not, a value of True means that the layer "layer" is visible, a value of False means that the layer "layer" is invisible.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def lowerActiveLayer() -> None:
    """Lowers the current active layer."""
    pass

def raiseActiveLayer() -> None:
    """Raises the current active layer."""
    pass

def sendToLayer(layer: str, name: str = None) -> None:
    """Sends the object "name" to the layer "layer". The layer must exist. If "name" is not given the currently selected item is used.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def setActiveLayer(name: str) -> None:
    """Sets the active layer to the layer named "name".

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def setLayerBlendmode(layer: str, blend: int) -> None:
    """Sets the layers "layer" blendmode to blend.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def setLayerFlow(layer: str, flow: bool) -> None:
    """Sets the layers "layer" flowcontrol to flow. If flow is set to true text in layers above this one will flow around objects on this layer.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable"""
    pass

def setLayerLocked(layer: str, locked: bool) -> None:
    """Sets the layer "layer" to be locked or not. If locked is set to true the layer will be locked.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def setLayerOutlined(layer: str, outline: bool) -> None:
    """Sets the layer "layer" to be locked or not. If outline is set to true the layer will be displayed outlined.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def setLayerPrintable(layer: str, printable: bool) -> None:
    """Sets the layer "layer" to be printable or not. If is the printable set to false the layer won't be printed.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def setLayerTransparency(layer: str, trans: float) -> None:
    """Sets the layers "layer" transparency to trans.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""
    pass

def setLayerVisible(layer: str, visible: bool) -> None:
    """Sets the layer "layer" to be visible or not. If is the visible set to false the layer is invisible.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


# Page Commands
def currentPage() -> int:
    """Returns the number of the current working page. Page numbers are counted from 1 upwards, no matter what the displayed first page number of your document is."""
    pass


def deletePage(nr: int) -> None:
    """Deletes the given page. Does nothing if the document contains only one page. Page numbers are counted from 1 upwards, no matter what the displayed first page number is.

May raise IndexError if the page number is out of range"""
    pass


def getAllObjects(type: int = -1, index: int = 0, layer: str = None) -> list:
    """Returns a list containing the names of all objects of specified type and located on specified page and/or layer. This function accepts several optional keyword arguments: - type (optional) -> None: integer corresponding to item type, by default all items will be returned. - page (optional) -> None: index of page on which returned objects are located, by default the current page. The page index starts at 0 and goes to the total number of pages - 1. - layer (optional) -> None: name of layer on which returned objects are located, by default the function returns items located on all layers. May throw ValueError if page index or layer name is invalid."""
    pass


def getHGuides() -> list:
    """Returns a list containing positions of the horizontal guides. Values are in the document's current units - see UNIT_ constants."""
    pass


def getPageItems() -> list:
    """Returns a list of tuples with items on the current page. The tuple is: (name, objectType, order) E.g. [('Text1', 4, 0), ('Image1', 2, 1)] means that object named 'Text1' is a text frame (type 4) and is the first at the page..."""
    pass

def getPageMargins() -> tuple:
    """Returns the document page margins as a (top, left, right, bottom) tuple in the document's current units. See UNIT_ constants and getPageSize()."""
    pass

def getPageNMargins(nr: int) -> tuple:
    """Returns a tuple with a particular page's margins measured in the document's current units. See UNIT_ constants and getPageMargins()"""
    pass

def getPageSize(nr: int) -> tuple:
    """Returns a tuple with a particular page's size measured in the document's current units. See UNIT_ constants and getPageMargins()"""
    pass

def getPageSize() -> tuple:
    """Returns a tuple with document page dimensions measured in the document's current units. See UNIT_ constants and getPageMargins()"""
    pass


def getPageType() -> int:
    """Returns the type of the Page, 0 means left Page, 1 is a middle Page and 2 is a right Page"""


def getVGuides() -> list:
    """See getHGuides."""
    pass


def gotoPage(nr: int) -> None:
    """Moves to the page "nr" (that is, makes the current page "nr"). Note that gotoPage doesn't (currently) change the page the user's view is displaying, it just sets the page that script commands will operates on.

May raise IndexError if the page number is out of range."""
    pass


def importPage(fromDoc: str, pageList: tuple, create: bool = True, importWhere: int = -1, importPageWhere: int = 2) -> None:
    """Imports a set of pages (given as a tuple) from an existing document (the file name must be given). This functions maps the "Page->Import" dropdown menu function. fromDoc: string; the filename of the document to import pages from pageList: tuple with page numbers of pages to import create: number; 0 to replace existing pages, 1 (default) to insert new pages importWhere: number; the page number (of the current document) at which import the pages importWherePage: number; used if create==1; 0 to create pages before selected page; 1 to create pages after selected page; 2 (default) to create pages at the end of the document"""
    pass


def moveItemToPage(page: int, name: str = None) -> None:
    """Move the item to the given page (the first page being 0). If "name" is not given the currently selected item is moved."""
    pass


def newPage(where: int, masterpage: str = None) -> None:
    """Creates a new page. If "where" is -1 the new Page is appended to the document, otherwise the new page is inserted before "where". Page numbers are counted from 1 upwards, no matter what the displayed first page number of your document is. The optional parameter "masterpage" specifies the name of the master page for the new page.

May raise IndexError if the page number is out of range"""
    pass


def pageCount() -> int:
    """Returns the number of pages in the document."""
    pass


def setHGuides(guides: tuple) -> None:
    """Sets horizontal guides. Input parameter must be a list of guide positions measured in the current document units - see UNIT_ constants.

Example: setHGuides(getHGuides() + [200.0, 210.0] # add new guides without any lost setHGuides([90,250]) # replace current guides entirely"""
    pass


def setVGuides(guides: tuple) -> None:
    """See setHGuides."""
    pass


# Creating & Destroying Objects
def createBezierLine(list: tuple, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name


def createEllipse(x: float, y: float, width: float, height: float, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def createImage(x: float, y: float, width: float, height: float, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def createLine(x1: float, y1: float, x2: float, y2: float, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def createPathText(x: float, y: float, textbox: str, beziercurve: str, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    objExists = False
    if objExists:
        raise NotFoundError
    return name


def createPolyLine(list: tuple, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name


def createPolygon(list: tuple, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name


def createRect(x: float, y: float, width: float, height: float, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def createText(x: float, y: float, width: float, height: float, name: str = "name") -> None:
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def deleteObject(name: str) -> None:
    pass


def objectExists(name: str) -> None:
    exists: bool
    return exists


# Selecting Objects
def deselectAll() -> None:
    pass


def getSelectedObject(nr: int = 0) -> None:
    name: str
    return name


def moveSelectionToBack() -> None:
    pass


def moveSelectionToFront() -> None:
    pass


def selectionCount() -> None:
    count: int
    return count


def selectObject(name: str) -> None:
    pass


# Setting Object Properties



# Creating & Manipulating Styles
def createCharStyle(name: str, font: str = "Arial Regular", fontsize: float = 12.0, features: str = None,
                    fillcolor: str = "None", fillshade: float = 1.0,
                    strokecolor: str = "Black", strokehade: float = 1.0, baselineoffset: float = -1.0,
                    shadowxoffset: float = -1.0, shadowyoffset: float = -1.0,
                    outlinewidth: float = -1.0, underlineoffset: float = -1.0, underlinewidth: float = -1.0,
                    strikethroughoffset: float = -1.0,
                    strikethroughwidth: float = -1.0, scaleh: float = 1.0, scalev: float = 1.0, tracking: int = -1,
                    language: str = "en", fontfeatures: str = None) -> None:
    pass


def createCustomLineStyle(styleName: str, style: dict) -> None:
    pass


def createParagraphStyle(name: str, linespacingmode: int = 0, linespacing: float = 12.0, alignment: int = 0,
                         leftmargin: float = 0.0, rightmargin: float = 0.0,
                         gapbefore: float = -1.0, gapafter: float = -1.0, firstindent: float = 0.0,
                         hasdropcap: bool = False, dropcaplines: int = -1,
                         dropcapoffset: float = -1.0, charstyle: str = "style", bullet: str = None, tabs: tuple = "") -> None:
    pass


def getAllStyles() -> None:
    names: str
    return names


# Handling Text Frames
def dehyphenateText(name: str = "name") -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass


def deleteText(name: str = "name") -> None:
    pass


def getAllText(name: str = "name") -> None:
    text: str
    return text


def getColumnGap(name: str = "name") -> None:
    gap: float
    return gap


def getColumns(name: str = "name") -> None:
    columns: int
    return columns


def getFirstLineOffset(name: str = "name") -> None:
    firstLineOffset: int
    return firstLineOffset


def getFirstLinkedFrame(name: str = "name") -> None:
    firstLinkedFrameName: str
    return firstLinkedFrameName


def getFont(name: str = "name") -> None:
    fontName: str
    return fontName


def getFontSize(name: str = "name") -> None:
    fontSize: float
    return fontSize


def getFrameText(name: str = "name") -> None:
    visibleText: str
    return visibleText


def getLastLinkedFrame(name: str = "name") -> None:
    lastLinkedFrameName: str
    return lastLinkedFrameName


def getLineSpacing(name: str = "name") -> None:
    lineSpacing: float
    return lineSpacing


def getNextLinkedFrame(name: str = "name") -> None:
    nextLinkedFrameName: str
    return nextLinkedFrameName


def getPrevLinkedFrame(name: str = "name") -> None:
    prevLinkedFrameName: str
    return prevLinkedFrameName


def getTextColor(name: str = "name") -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    colorName: str
    return colorName


def getTextDistances(name: str = "name") -> None:
    textDistances: tuple
    return textDistances


def getTextLength(name: str = "name") -> None:
    textLength: int
    return textLength


def getTextLines(name: str = "name") -> None:
    textLines: int
    return textLines


def getTextShade(name: str = "name") -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    textShade: int
    return textShade


def getTextVerticalAlignment(name: str = "name") -> None:
    textVerticalAlignment: int
    return textVerticalAlignment


def hyphenateText(name: str = "name") -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    success: bool
    return success


def insetHtmlText(file: str, name: str = "name") -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass


def insertText(text: str, pos: int, name: str = "name") -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass


def isPDFBookmark(name: str = "name") -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pdfBookmark: bool
    return pdfBookmark


def layoutText(name: str = "name") -> None:
    pass


def layoutTextChain(name: str = "name") -> None:
    pass


def linkTextFrames(firstFrame: str, secondFrame: str) -> None:
    rulesViolated = False
    if rulesViolated:
        return ScribusError
    pass


def selectFrameText(start: int, count: int, name: str = "name") -> None:
    outsideRange = False
    if outsideRange:
        raise IndexError
    pass


def selectText(start: int, count: int, name: str = "name") -> None:
    outsideRange = False
    if outsideRange:
        raise IndexError
    pass


def setColumns(nr: int, name: str = "name") -> None:
    if nr < 1:
        raise ValueError
    pass


def setColumnGap(size: float, name: str = "name") -> None:
    if size < 0:
        raise ValueError
    pass


def setFirstLineOffset(offset: int, name: str = "name") -> None:
    invalidConstant = False
    if invalidConstant:
        raise ValueError
    pass


def setFont(font: str, name: str = "name") -> None:
    fontNotFound = False
    if fontNotFound:
        raise ValueError
    pass


def setFontSize(size: float, name: str = "name") -> None:
    if not 1 <= size <= 512:
        raise ValueError
    pass


def setLineSpacing(size: float, name: str = "name") -> None:
    if size < 0:
        raise ValueError
    pass


def setLineSpacingMode(mode: int, name: str = "name") -> None:
    invalidMode = False
    if invalidMode:
        raise ValueError
    pass


def setPDFBookmark(toggle: bool, name: str = "name") -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass


def setText(text: str, name: str = "name") -> None:
    pass


def setTextAlignment(align: int, name: str = "name") -> None:
    invalidAlign = False
    if invalidAlign:
        raise ValueError
    pass


def setTextDistances(left: float, right: float, top: float, bottom: float, name: str = "name") -> None:
    if left < 0 or right < 0 or top < 0 or bottom < 0:
        raise ValueError
    pass


def setTextScalingH(scale: float, name: str = "name") -> None:
    pass


def setTextScalingV(scale: float, name: str = "name") -> None:
    pass


def setTextColor(color: str, name: str = "name") -> None:
    pass


def setTextShade(shade: float, name: str = "name") -> None:
    pass


def setTextStroke(color: str, name: str = "name") -> None:
    pass


def setTextVerticalAlignment(align: float, name: str = "name") -> None:
    invalidAlign = False
    if invalidAlign:
        raise ValueError
    pass


def textOverflows(name: str = "name", nolinks=False) -> None:
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    overflows: bool
    return overflows


def unlinkTextFrames(name: str = "name") -> None:
    rulesViolated = False
    if rulesViolated:
        raise ScribusError
    pass


# Using Dialogs
def fileDialog(caption: str, filter: str = "comment(*.type1 *.type2)", defaultname: str = "defaultname",
               haspreview: bool = False, issave: bool = False,
               isdir: bool = False) -> None:
    fileName: str
    return fileName


def fileQuit() -> None:
    pass


def getGuiLanguage() -> None:
    language: str
    return language


def messageBox(caption: str, message: str, icon: int = ICON_NONE, button1: int = BUTTON_OK | BUTTON_DEFAULT,
               button2: int = BUTTON_NONE,
               button3: int = BUTTON_NONE) -> None:
    buttonClicked: int
    return buttonClicked


def newDocDialog() -> None:
    wasCreated: bool
    return wasCreated


def newStyleDialog() -> None:
    styleName: str
    return styleName


def statusMessage(string: str) -> None:
    pass


def progressReset() -> None:
    pass


def progressSet(nr: int) -> None:
    pass


def progressTotal(max: int) -> None:
    pass


def valueDialog(caption: str, message: str, defaultValue: str = None) -> None:
    value: str
    return value
