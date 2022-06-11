# Predefined Constants
UNIT_POINTS = 0
UNIT_MILLIMETERS = 1
UNIT_INCHES = 2
UNIT_PICAS = 3
pt = -1
inch = -1
p = -1
cm = -1
mm = -1
PORTRAIT = 0
LANDSCAPE = 1
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
FACINGPAGES = -1
NOFACINGPAGES = -1
FIRSTPAGELEFT = -1
FIRSTPAGERIGHT = -1
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
def closeDoc():
    raise NoDocOpenError


def docChanged(bool: bool):
    pass


def getDocName():
    name: str
    return name


def getUnit():
    unit: int
    return unit


def haveDoc():
    hasDoc: bool
    return hasDoc


def loadStylesFromFile(filename: str):
    pass


def masterPageNames():
    names: tuple
    return names


def newDocument(size: tuple, margins: tuple, orientation: int, firstPageNumber: int, unit: int, pagesType: int,
                firstPageOrder: int, numPages: int):
    if firstPageOrder > pagesType:
        raise ScribusError
    success: bool
    return success


def openDoc(name: str):
    documentNotOpened = False
    if documentNotOpened:
        raise ScribusError
    pass


def placeEPS(filename: str, x: float, y: float):
    pass


def placeODG(filename: str, x: float, y: float):
    pass


def placeSVG(filename: str, x: float, y: float):
    pass


def placeSXD(filename: str, x: float, y: float):
    pass


def placeVectorFile(filename: str, x: float, y: float):
    pass


def revertDoc():
    pass


def saveDoc():
    pass


def saveDocAs(name: str):
    saveFailed = False
    if saveFailed:
        raise ScribusError
    pass


def setBaseLine(grid: float, offset: float):
    pass


def setBleeds(lr: float, rr: float, tr: float, br: float):
    pass


def setDocType(facingPages: int, firstPageLeft: int):
    pass


def setInfo(author: str, info: str, description: str):
    success: bool
    return success


def setMargins(lr: float, rr: float, tr: float, br: float):
    pass


def setUnit(type: int):
    invalidUnit = False
    if invalidUnit:
        raise ValueError
    pass


def scrollDocument(x: float, y: float):
    pass


def zoomDocument(zoom: float):
    pass


# Page Commands
def currentPage():
    number: int
    return number

def deletePage(nr: int):
    pageNrOutOfRange = False
    if pageNrOutOfRange:
        raise IndexError
    pass

def getAllObjects(type: int = -1, index: int = 0, layer: str = ""):
    indexInvalid = False
    layerInvalid = False
    if indexInvalid or layerInvalid:
        raise ValueError
    objects: tuple
    return objects

def getHGuides():
    horizontalGuidePositions: tuple
    return horizontalGuidePositions

def getMasterPage(nr: int):
    nrOutOfRange = False
    if nrOutOfRange:
        raise IndexError
    masterPageName: str
    return masterPageName

def getPageType():
    type: int
    return type

def getPageItems():
    items: tuple
    return items

def getPageNMargins(nr: int):
    marigns: tuple
    return marigns

def getPageSize():
    dimensions: tuple
    return dimensions

def getPageNSize(nr: int):
    size: tuple
    return size

def getVGuides():
    verticalGuidePositions: tuple
    return verticalGuidePositions

def gotoPage(nr: int):
    nrOutOfRange = False
    if nrOutOfRange:
        raise IndexError
    pass

def importPage(fromDoc: str, pageList: tuple, create: bool = True, importWhere: int = -1, importPageWhere: int = 2):
    pass

def newPage(where: int, masterpage: str = ""):
    whereOutOfRange = False
    if whereOutOfRange:
        raise IndexError
    pass

def pageCount():
    count: int
    return count

def redrawAll():
    pass

def savePageAsEPS(name: str):
    saveFailed = False
    if saveFailed:
        raise ScribusError
    pass

def setHGuides(guides: tuple):
    pass

def setRedraw(redraw: bool):
    pass

def setVGuides(guides: tuple):
    pass


# Master Page Commands
def masterPageNames():
    names: tuple
    return names


def applyMasterPage(masterPageName: str, pageNr: int):
    pass


def closeMasterPage():
    pass


def createMasterPage(pageName: str):
    pass


def deleteMasterPage(pageName: str):
    pass


def editMasterPage(pageName: str):
    pass



# Creating & Destroying Objects
def createBezierLine(list: tuple, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name


def createEllipse(x: float, y: float, width: float, height: float, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def createImage(x: float, y: float, width: float, height: float, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def createLine(x1: float, y1: float, x2: float, y2: float, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def createPathText(x: float, y: float, textbox: str, beziercurve: str, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    objExists = False
    if objExists:
        raise NotFoundError
    return name


def createPolyLine(list: tuple, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name


def createPolygon(list: tuple, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name


def createRect(x: float, y: float, width: float, height: float, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def createText(x: float, y: float, width: float, height: float, name: str = "name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name


def deleteObject(name: str):
    pass


def objectExists(name: str):
    exists: bool
    return exists


# Selecting Objects
def deselectAll():
    pass


def getSelectedObject(nr: int = 0):
    name: str
    return name


def moveSelectionToBack():
    pass


def moveSelectionToFront():
    pass


def selectionCount():
    count: int
    return count


def selectObject(name: str):
    pass


# Creating & Manipulating Styles
def createCharStyle(name: str, font: str = "Arial Regular", fontsize: float = 12.0, features: str = "", fillcolor: str = "None", fillshade: float = 1.0,
                    strokecolor: str = "Black", strokehade: float = 1.0, baselineoffset: float = -1.0, shadowxoffset: float = -1.0, shadowyoffset: float = -1.0,
                    outlinewidth: float = -1.0, underlineoffset: float = -1.0, underlinewidth: float = -1.0, strikethroughoffset: float = -1.0,
                    strikethroughwidth: float = -1.0, scaleh: float = 1.0, scalev: float = 1.0, tracking: int = -1, language: str = "en", fontfeatures: str = ""):
    pass


def createCustomLineStyle(styleName: str, style: dict):
    pass


def createParagraphStyle(name: str, linespacingmode: int = 0, linespacing: float = 12.0, alignment: int = 0, leftmargin: float = 0.0, rightmargin: float = 0.0,
                         gapbefore: float = -1.0, gapafter: float = -1.0, firstindent: float = 0.0, hasdropcap: bool = False, dropcaplines: int = -1,
                         dropcapoffset: float = -1.0, charstyle: str = "style", bullet: str = "", tabs: tuple = ""):
    pass


def getAllStyles():
    names: str
    return names


# Handling Text Frames
def dehyphenateText(name: str = "name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass


def deleteText(name: str = "name"):
    pass


def getAllText(name: str = "name"):
    text: str
    return text


def getColumnGap(name: str = "name"):
    gap: float
    return gap


def getColumns(name: str = "name"):
    columns: int
    return columns


def getFirstLineOffset(name: str = "name"):
    firstLineOffset: int
    return firstLineOffset


def getFirstLinkedFrame(name: str = "name"):
    firstLinkedFrameName: str
    return firstLinkedFrameName


def getFont(name: str = "name"):
    fontName: str
    return fontName


def getFontSize(name: str = "name"):
    fontSize: float
    return fontSize


def getFrameText(name: str = "name"):
    visibleText: str
    return visibleText


def getLastLinkedFrame(name: str = "name"):
    lastLinkedFrameName: str
    return lastLinkedFrameName


def getLineSpacing(name: str = "name"):
    lineSpacing: float
    return lineSpacing


def getNextLinkedFrame(name: str = "name"):
    nextLinkedFrameName: str
    return nextLinkedFrameName


def getPrevLinkedFrame(name: str = "name"):
    prevLinkedFrameName: str
    return prevLinkedFrameName


def getTextColor(name: str = "name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    colorName: str
    return colorName


def getTextDistances(name: str = "name"):
    textDistances: tuple
    return textDistances


def getTextLength(name: str = "name"):
    textLength: int
    return textLength


def getTextLines(name: str = "name"):
    textLines: int
    return textLines


def getTextShade(name: str = "name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    textShade: int
    return textShade


def getTextVerticalAlignment(name: str = "name"):
    textVerticalAlignment: int
    return textVerticalAlignment


def hyphenateText(name: str = "name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    success: bool
    return success


def insetHtmlText(file: str, name: str = "name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass


def insertText(text: str, pos: int, name: str = "name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass


def isPDFBookmark(name: str = "name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pdfBookmark: bool
    return pdfBookmark


def layoutText(name: str = "name"):
    pass


def layoutTextChain(name: str = "name"):
    pass


def linkTextFrames(firstFrame: str, secondFrame: str):
    rulesViolated = False
    if rulesViolated:
        return ScribusError
    pass


def selectFrameText(start: int, count: int, name: str = "name"):
    outsideRange = False
    if outsideRange:
        raise IndexError
    pass


def selectText(start: int, count: int, name: str = "name"):
    outsideRange = False
    if outsideRange:
        raise IndexError
    pass


def setColumns(nr: int, name: str = "name"):
    if nr < 1:
        raise ValueError
    pass


def setColumnGap(size: float, name: str = "name"):
    if size < 0:
        raise ValueError
    pass


def setFirstLineOffset(offset: int, name: str = "name"):
    invalidConstant = False
    if invalidConstant:
        raise ValueError
    pass


def setFont(font: str, name: str = "name"):
    fontNotFound = False
    if fontNotFound:
        raise ValueError
    pass


def setFontSize(size: float, name: str = "name"):
    if not 1 <= size <= 512:
        raise ValueError
    pass


def setLineSpacing(size: float, name: str = "name"):
    if size < 0:
        raise ValueError
    pass


def setLineSpacingMode(mode: int, name: str = "name"):
    invalidMode = False
    if invalidMode:
        raise ValueError
    pass


def setPDFBookmark(toggle: bool, name: str = "name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass


def setText(text: str, name: str = "name"):
    pass


def setTextAlignment(align: int, name: str = "name"):
    invalidAlign = False
    if invalidAlign:
        raise ValueError
    pass


def setTextDistances(left: float, right: float, top: float, bottom: float, name: str = "name"):
    if left < 0 or right < 0 or top < 0 or bottom < 0:
        raise ValueError
    pass


def setTextScalingH(scale: float, name: str = "name"):
    pass


def setTextScalingV(scale: float, name: str = "name"):
    pass


def setTextColor(color: str, name: str = "name"):
    pass


def setTextShade(shade: float, name: str = "name"):
    pass


def setTextStroke(color: str, name: str = "name"):
    pass


def setTextVerticalAlignment(align: float, name: str = "name"):
    invalidAlign = False
    if invalidAlign:
        raise ValueError
    pass


def textOverflows(name: str = "name", nolinks=False):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    overflows: bool
    return overflows


def unlinkTextFrames(name: str = "name"):
    rulesViolated = False
    if rulesViolated:
        raise ScribusError
    pass


# Using Dialogs
def fileDialog(caption: str, filter: str = "comment(*.type1 *.type2)", defaultname: str = "defaultname", haspreview: bool = False, issave: bool = False,
               isdir: bool = False):
    fileName: str
    return fileName


def fileQuit():
    pass


def getGuiLanguage():
    language: str
    return language


def messageBox(caption: str, message: str, icon: int = ICON_NONE, button1: int = BUTTON_OK | BUTTON_DEFAULT, button2: int = BUTTON_NONE,
               button3: int = BUTTON_NONE):
    buttonClicked: int
    return buttonClicked


def newDocDialog():
    wasCreated: bool
    return wasCreated


def newStyleDialog():
    styleName: str
    return styleName


def statusMessage(string: str):
    pass


def progressReset():
    pass


def progressSet(nr: int):
    pass


def progressTotal(max: int):
    pass


def valueDialog(caption: str, message: str, defaultValue: str = ""):
    value: str
    return value