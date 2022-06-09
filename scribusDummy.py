# errors
class Error(Exception):
    pass
class NoDocOpenError(Error):
    pass
class ScribusException(Error):
    pass
class NameExistsError(Error):
    pass
class NotFoundError(Error):
    pass
class WrongFrameTypeError(Error):
    pass


# constants
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
PAPER_EXECUTIVE = [542,720]
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


# document commands
def closeDoc():
    raise NoDocOpenError
def docChanged(bool):
    pass
def getDocName():
    return ""
def getUnit():
    return -1
def haveDoc():
    return False
def loadStylesFromFile(filename):
    pass
def masterPageNames():
    return ["", ""]
def newDocument(size, margins, orientation, firstPageNumber, unit, pagesType, firstPageOrder, numPages):
    if firstPageOrder > pagesType:
        raise ScribusException
    return False
def openDoc(name):
    documentNotOpened = False
    if documentNotOpened:
        raise ScribusException
def placeEPS(filename, x, y):
    pass
def placeODG(filename, x, y):
    pass
def placeSVG(filename, x, y):
    pass
def placeSXD(filename, x, y):
    pass
def placeVectorFile(filename, x, y):
    pass
def revertDoc():
    pass
def saveDoc():
    pass
def saveDocAs(name):
    saveFailed = False
    if saveFailed:
        raise ScribusException
def setBaseLine(grid, offset):
    pass
def setBleeds(lr, rr, tr, br):
    pass
def setDocType(facingPages, firstPageLeft):
    pass
def setInfo(author, info, description):
    return False
def setMargins(lr, rr, tr, br):
    pass
def setUnit(type):
    invalidUnit = False
    if invalidUnit:
        raise ValueError
def scrollDocument(x, y):
    pass
def zoomDocument(zoom):
    pass


# master page
def masterPageNames():
    return ["pageName1", "pageName2"]
def applyMasterPage():
    pass
def closeMasterPage():
    pass
def createMasterPage(pageName):
    pass
def deleteMasterPage(pageName):
    pass
def editMasterPage(pageName):
    pass


# styles
def createCharStyle(name, font="Arial Regular", fontsize=12.0, features="", fillcolor="None", fillshade=1.0, strokecolor="Black", strokehade=1.0, baselineoffset=-1.1, shadowxoffset=-1.1, shadowyoffset=-1.1, outlinewidth=-1.1, underlineoffset=-1.1, underlinewidth=-1.1, strikethroughoffset=-1.1, strikethroughwidth=-1.1, scaleh=1.0, scalev=1.0, tracking=-11, language="en", fontfeatures=""):
    pass
def createCustomLineStyle(styleName, style):
    pass
def createParagraphStyle(name, linespacingmode=0, linespacing=12.0, alignment=0, leftmargin=0.0, rightmargin=0.0, gapbefore=-1.1, gapafter=-1.1, firstindent=0.0, hasdropcap=False, dropcaplines=-1, dropcapoffset=-1.1, charstyle="style", bullet="", tabs=""):
    pass
def getAllStyles():
    return ["styleName1", "styleName2"]


# creating objects
def createBezierLine(list, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name
def createEllipse(x, y, width, height, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name
def createImage(x, y, width, height, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name
def createLine(x1, y1, x2, y2, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name
def createPathText(x, y, textbox, beziercurve, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    objExists = False
    if objExists:
        raise NotFoundError
    return name
def createPolyLine(list, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name
def createPolygon(list, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    wrongValues = False
    if wrongValues:
        raise ValueError
    return name
def createRect(x, y, width, height, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name
def createText(x, y, width, height, name="name"):
    nameExists = False
    if nameExists:
        raise NameExistsError
    return name
def deleteObject(name):
    pass
def objectExists(name):
    return False


# selecting objects
def deselectAll():
    pass
def getSelectedObject(nr=0):
    return "name"
def moveSelectionToBack():
    pass
def moveSelectionToFront():
    pass
def selectionCount():
    return -1
def selectObject(name):
    pass


# text frames
def dehyphenateText(name="name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
def deleteText(name="name"):
    pass
def getAllText(name="name"):
    return "text"
def getColumnGap(name="name"):
    return -1.1
def getColumns(name="name"):
    return -1
def getFirstLineOffset(name="name"):
    return -1
def getFirstLinkedFrame(name="name"):
    return "frame"
def getFont(name="name"):
    return "font"
def getFontSize(name="name"):
    return -1.1
def getFrameText(name="name"):
    return "textVisible"
def getLastLinkedFrame(name="name"):
    return "frame"
def getLineSpacing(name="name"):
    return -1.1
def getNextLinkedFrame(name="name"):
    return "frame"
def getPrevLinkedFrame(name="name"):
    return "frame"
def getTextColor(name="name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    return "color"
def getTextDistances(name="name"):
    return [-1.1, -1.1, -1.1, -1.1]
def getTextLength(name="name"):
    return -1
def getTextLines(name="name"):
    return -1
def getTextShade(name="name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    return -1
def getTextVerticalAlignment(name="name"):
    return -1
def hyphenateText(name="name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    return False
def insetHtmlText(text, name="name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass
def insertText(text, pos, name="name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass
def isPDFBookmark(name="name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    return False
def layoutText(name="name"):
    pass
def layoutTextChain(name="name"):
    pass
def linkTextFrames(firstFrame, secondFrame):
    rulesViolated = False
    if rulesViolated:
        return ScribusException
    pass
def selectFrameText(start, count, name="name"):
    outsideRange = False
    if outsideRange:
        raise IndexError
    pass
def selectText(start, count, name="name"):
    outsideRange = False
    if outsideRange:
        raise IndexError
    pass
def setColumns(nr, name="name"):
    if nr < 1:
        raise ValueError
    pass
def setColumnGap(size, name="name"):
    if size < 0:
        raise ValueError
    pass
def setFirstLineOffset(offset, name="name"):
    invalidConstant = False
    if invalidConstant:
        raise ValueError
    pass
def setFont(font, name="name"):
    fontNotFound = False
    if fontNotFound:
        raise ValueError
    pass
def setFontSize(size, name="name"):
    if not 1 <= size <= 512:
        raise ValueError
    pass
def setLineSpacing(size, name="name"):
    if size < 0:
        raise ValueError
    pass
def setLineSpacingMode(mode, name="name"):
    invalidMode = False
    if invalidMode:
        raise ValueError
    pass
def setPDFBookmark(toggle, name="name"):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    pass
def setText(text, name="name"):
    pass
def setTextAlignment(align, name="name"):
    invalidAlign = False
    if invalidAlign:
        raise ValueError
    pass
def setTextDistances(left, right, top, bottom, name="name"):
    if left < 0 or right < 0 or top < 0 or bottom < 0:
        raise ValueError
    pass
def setTextScalingH(scale, name="name"):
    pass
def setTextScalingV(scale, name="name"):
    pass
def setTextColor(color, name="name"):
    pass
def setTextShade(shade, name="name"):
    pass
def setTextStroke(color, name="name"):
    pass
def setTextVerticalAlignment(align, name="name"):
    invalidAlign = False
    if invalidAlign:
        raise ValueError
    pass
def textOverflows(name="name", nolinks=False):
    wrongFrameType = False
    if wrongFrameType:
        raise WrongFrameTypeError
    return False
def unlinkTextFrames(name="name"):
    rulesViolated = False
    if rulesViolated:
        raise ScribusException


# dialogs
def fileDialog(caption, filter="comment(*.type1 *.type2)", defaultname="defaultname", haspreview=False, issave=False, isdir=False):
    return "filename"
def fileQuit():
    pass
def getGuiLanguage():
    return "language"
def messageBox(caption, message, icon=ICON_NONE, button1=BUTTON_OK|BUTTON_DEFAULT, button2=BUTTON_NONE, button3=BUTTON_NONE):
    return BUTTON_NONE
def newDocDialog():
    return False
def newStyleDialog():
    return "style name"
def statusMessage(string):
    pass
def progressReset():
    pass
def progressSet(nr):
    pass
def progressTotal(max):
    pass
def valueDialog(caption, message, defaultValue=""):
    return "value"