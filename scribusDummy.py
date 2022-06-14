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

# Lines and stroke properties (Line style)
LINE_DASH = -1
LINE_DASHDOT = -1
LINE_DASHDOTDOT = -1
LINE_DOT = -1
LINE_SOLID = -1

# Lines and stroke properties (Line join)
JOIN_BEVEL = -1
JOIN_MITTER = -1
JOIN_ROUND = -1

# Lines and stroke properties (Line ending)
CAP_FLAT = -1
CAP_ROUND = -1
CAP_SQUARE = -1

# Fill modes
FILL_NOG = -1
FILL_HORIZONTALG = -1
FILL_VERTICALG = -1
FILL_DIAGONALG = -1
FILL_CROSSDIAGONALG = -1
FILL_RADIALG = -1

CSPACE_UNDEFINED = -1
CSPACE_RGB = -1
CSPACE_CMYK = -1
CSPACE_GRAY = -1
CSPACE_DUOTONE = -1
CSPACE_MONOCHROME = -1

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


def docChanged(bool: bool) -> None:
    """Enable/disable save icon in the Scribus icon bar and the Save menu item. It's useful to call this procedure when you're changing the document, because Scribus won't automatically notice when you change the document using a script."""


def getDocName() -> str:
    """Returns the name the document was saved under. If the document was not saved before the name is empty."""


def getUnit() -> int:
    """Returns the measurement units of the document. The returned value will be one of the UNIT_* constants: UNIT_INCHES, UNIT_MILLIMETERS, UNIT_PICAS, UNIT_POINTS"""


def haveDoc() -> int:
    """Returns the quantity of open documents: 0 if none are opened."""


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


def openDoc(name: str) -> None:
    """Opens the document "name".

    May raise ScribusError if the document could not be opened."""


def redrawAll() -> None:
    """Redraws all pages."""


def revertDoc() -> None:
    """Revert the current document to its last saved state."""


def saveDoc() -> None:
    """Saves the current document with its current name, returns true if successful. If the document has not already been saved, this may bring up an interactive save file dialog.

If the save fails, there is currently no way to tell."""


def saveDocAs(name: str) -> None:
    """Saves the current document under the new name "name" (which may be a full or relative path).

May raise ScribusError if the save fails."""


def setBaseLine(grid: float, offset: float) -> None:
    """Sets the base line settings of the document, grid spacing(grid), grid offset(offset). Values are given in the measurement units of the document - see UNIT_ constants."""


def setBleeds(lr: float, rr: float, tr: float, br: float) -> None:
    """Sets the bleeds of the document. Left(lr), Right(rr), Top(tr) and Bottom(br) bleeds are given in the measurement units of the document - see UNIT_ constants."""


def setDocType(facingPages: int, firstPageLeft: int) -> None:
    """Sets the document type. To get facing pages set the first parameter to FACINGPAGES, to switch facingPages off use NOFACINGPAGES instead. If you want to be the first page a left side set the second parameter to FIRSTPAGELEFT, for a right page use FIRSTPAGERIGHT."""


def setInfo(author: str, info: str, description: str) -> bool:
    """Sets the document information. "Author", "Info", "Description" are strings."""
    return success


def setMargins(lr: float, rr: float, tr: float, br: float) -> None:
    """Sets the margins of the document, Left(lr), Right(rr), Top(tr) and Bottom(br) margins are given in the measurement units of the document - see UNIT_ constants."""


def setRedraw(redraw: bool) -> None:
    """Disables page redraw when bool = False, otherwise redrawing is enabled. This change will persist even after the script exits, so make sure to call setRedraw(True) in a finally: clause at the top level of your script."""


def setUnit(type: int) -> None:
    """Changes the measurement unit of the document. Possible values for "unit" are defined as constants UNIT_.

May raise ValueError if an invalid unit is passed."""


# Master Page Commands
def applyMasterPage(masterPageName: str, pageNr: int) -> None:
    """Apply master page masterPageName on page pageNumber."""


def closeMasterPage() -> None:
    """Closes the currently active master page, if any, and returns editing to normal. Begin editing with editMasterPage()."""


def createMasterPage(pageName: str) -> None:
    """Creates a new master page named pageName and opens it for editing."""


def deleteMasterPage(pageName: str) -> None:
    """Delete the named master page."""


def editMasterPage(pageName: str) -> None:
    """Enables master page editing and opens the named master page for editing. Finish editing with closeMasterPage()."""


def getMasterPage(pageNr: int) -> None:
    """Returns the name of master page applied to page "nr".

May raise IndexError if the page number is out of range."""


def masterPageNames() -> None:
    """Returns a list of the names of all master pages in the document."""


# Layers
def createLayer(name: str) -> None:
    """Creates a new layer with the name "name".

May raise ValueError if the layer name isn't acceptable."""


def deleteLayer(layer: str) -> None:
    """Deletes the layer with the name "layer". Nothing happens if the layer doesn't exists or if it's the only layer in the document.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def getActiveLayer() -> str:
    """Returns the name of the current active layer."""


def getLayerBlendmode(layer: str) -> int:
    """Returns the "layer" layer blendmode,

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def getLayerTransparency(layer: str) -> float:
    """Returns the "layer" layer transparency,

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def getLayers() -> list:
    """Returns a list with the names of all defined layers."""


def isLayerFlow(layer: str) -> bool:
    """Returns whether text flows around objects on layer "layer", a value of True means that text flows around, a value of False means that the text does not flow around.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def isLayerLocked(layer: str) -> bool:
    """Returns whether the layer "layer" is locked or not, a value of True means that the layer "layer" is editable, a value of False means that the layer "layer" is locked.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def isLayerOutlined(layer: str) -> bool:
    """Returns whether the layer "layer" is outlined or not, a value of True means that the layer "layer" is outlined, a value of False means that the layer "layer" is normal.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def isLayerPrintable(layer: str) -> bool:
    """Returns whether the layer "layer" is printable or not, a value of True means that the layer "layer" can be printed, a value of False means that printing the layer "layer" is disabled.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def isLayerVisible(layer: str) -> bool:
    """Returns whether the layer "layer" is visible or not, a value of True means that the layer "layer" is visible, a value of False means that the layer "layer" is invisible.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def lowerActiveLayer() -> None:
    """Lowers the current active layer."""


def raiseActiveLayer() -> None:
    """Raises the current active layer."""


def sendToLayer(layer: str, name: str = None) -> None:
    """Sends the object "name" to the layer "layer". The layer must exist. If "name" is not given the currently selected item is used.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setActiveLayer(name: str) -> None:
    """Sets the active layer to the layer named "name".

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerBlendmode(layer: str, blend: int) -> None:
    """Sets the layers "layer" blendmode to blend.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerFlow(layer: str, flow: bool) -> None:
    """Sets the layers "layer" flowcontrol to flow. If flow is set to true text in layers above this one will flow around objects on this layer.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable"""


def setLayerLocked(layer: str, locked: bool) -> None:
    """Sets the layer "layer" to be locked or not. If locked is set to true the layer will be locked.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerOutlined(layer: str, outline: bool) -> None:
    """Sets the layer "layer" to be locked or not. If outline is set to true the layer will be displayed outlined.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerPrintable(layer: str, printable: bool) -> None:
    """Sets the layer "layer" to be printable or not. If is the printable set to false the layer won't be printed.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerTransparency(layer: str, trans: float) -> None:
    """Sets the layers "layer" transparency to trans.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerVisible(layer: str, visible: bool) -> None:
    """Sets the layer "layer" to be visible or not. If is the visible set to false the layer is invisible.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


# Page Commands
def currentPage() -> int:
    """Returns the number of the current working page. Page numbers are counted from 1 upwards, no matter what the displayed first page number of your document is."""


def deletePage(nr: int) -> None:
    """Deletes the given page. Does nothing if the document contains only one page. Page numbers are counted from 1 upwards, no matter what the displayed first page number is.

May raise IndexError if the page number is out of range"""


def getAllObjects(type: int = -1, index: int = 0, layer: str = None) -> list:
    """Returns a list containing the names of all objects of specified type and located on specified page and/or layer. This function accepts several optional keyword arguments: - type (optional) -> None: integer corresponding to item type, by default all items will be returned. - page (optional) -> None: index of page on which returned objects are located, by default the current page. The page index starts at 0 and goes to the total number of pages - 1. - layer (optional) -> None: name of layer on which returned objects are located, by default the function returns items located on all layers. May throw ValueError if page index or layer name is invalid."""


def getHGuides() -> list:
    """Returns a list containing positions of the horizontal guides. Values are in the document's current units - see UNIT_ constants."""


def getPageItems() -> list:
    """Returns a list of tuples with items on the current page. The tuple is: (name, objectType, order) E.g. [('Text1', 4, 0), ('Image1', 2, 1)] means that object named 'Text1' is a text frame (type 4) and is the first at the page..."""


def getPageMargins() -> tuple:
    """Returns the document page margins as a (top, left, right, bottom) tuple in the document's current units. See UNIT_ constants and getPageSize()."""


def getPageNMargins(nr: int) -> tuple:
    """Returns a tuple with a particular page's margins measured in the document's current units. See UNIT_ constants and getPageMargins()"""


def getPageSize(nr: int) -> tuple:
    """Returns a tuple with a particular page's size measured in the document's current units. See UNIT_ constants and getPageMargins()"""


def getPageSize() -> tuple:
    """Returns a tuple with document page dimensions measured in the document's current units. See UNIT_ constants and getPageMargins()"""


def getPageType() -> int:
    """Returns the type of the Page, 0 means left Page, 1 is a middle Page and 2 is a right Page"""


def getVGuides() -> list:
    """See getHGuides."""


def gotoPage(nr: int) -> None:
    """Moves to the page "nr" (that is, makes the current page "nr"). Note that gotoPage doesn't (currently) change the page the user's view is displaying, it just sets the page that script commands will operates on.

May raise IndexError if the page number is out of range."""


def importPage(fromDoc: str, pageList: tuple, create: bool = True, importWhere: int = -1,
               importPageWhere: int = 2) -> None:
    """Imports a set of pages (given as a tuple) from an existing document (the file name must be given). This functions maps the "Page->Import" dropdown menu function. fromDoc: string; the filename of the document to import pages from pageList: tuple with page numbers of pages to import create: number; 0 to replace existing pages, 1 (default) to insert new pages importWhere: number; the page number (of the current document) at which import the pages importWherePage: number; used if create==1; 0 to create pages before selected page; 1 to create pages after selected page; 2 (default) to create pages at the end of the document"""


def moveItemToPage(page: int, name: str = None) -> None:
    """Move the item to the given page (the first page being 0). If "name" is not given the currently selected item is moved."""


def newPage(where: int, masterpage: str = None) -> None:
    """Creates a new page. If "where" is -1 the new Page is appended to the document, otherwise the new page is inserted before "where". Page numbers are counted from 1 upwards, no matter what the displayed first page number of your document is. The optional parameter "masterpage" specifies the name of the master page for the new page.

May raise IndexError if the page number is out of range"""


def pageCount() -> int:
    """Returns the number of pages in the document."""


def setHGuides(guides: tuple) -> None:
    """Sets horizontal guides. Input parameter must be a list of guide positions measured in the current document units - see UNIT_ constants.

Example: setHGuides(getHGuides() + [200.0, 210.0] # add new guides without any lost setHGuides([90,250]) # replace current guides entirely"""


def setVGuides(guides: tuple) -> None:
    """See setHGuides."""


# Text styles
def createCharStyle(name: str, font: str = "Arial Regular", fontsize: float = 12.0, features: str = None,
                    fillcolor: str = "None", fillshade: float = 1.0,
                    strokecolor: str = "Black", strokehade: float = 1.0, baselineoffset: float = -1.0,
                    shadowxoffset: float = -1.0, shadowyoffset: float = -1.0,
                    outlinewidth: float = -1.0, underlineoffset: float = -1.0, underlinewidth: float = -1.0,
                    strikethroughoffset: float = -1.0,
                    strikethroughwidth: float = -1.0, scaleh: float = 1.0, scalev: float = 1.0, tracking: int = -1,
                    language: str = "en", fontfeatures: str = None) -> None:
    """Creates a character style. This function takes the following keyword parameters:

"name" [required] -> name of the char style to create

"font" [optional] -> name of the font to use

fontsize [optional] -> font size to set (double)

"features" [optional] -> nearer typographic details can be defined by a string that might contain the following phrases comma-seperated (without spaces!):

-> inherit

-> bold

-> italic

-> underline

-> underlinewords

-> strike

-> superscript

-> subscript

-> outline

-> shadowed

-> allcaps

-> smallcaps

"fillcolor" [optional], "fillshade" [optional] -> specify fill options

"strokecolor" [optional], "strokeshade" [optional] -> specify stroke options

baselineoffset [optional] -> offset of the baseline

shadowxoffset [optional], shadowyoffset [optional] -> offset of the shadow if used

outlinewidth [optional] -> width of the outline if used

underlineoffset [optional], underlinewidth [optional] -> underline options if used

strikethruoffset [optional], strikethruwidth [optional] -> strikethru options if used

scaleh [optional], scalev [optional] -> scale of the chars

tracking [optional] -> tracking of the text

"language" [optional] -> language code"""


def createParagraphStyle(name: str, linespacingmode: int = 0, linespacing: float = 12.0, alignment: int = 0,
                         leftmargin: float = 0.0, rightmargin: float = 0.0,
                         gapbefore: float = -1.0, gapafter: float = -1.0, firstindent: float = 0.0,
                         hasdropcap: bool = False, dropcaplines: int = -1,
                         dropcapoffset: float = -1.0, charstyle: str = "style", bullet: str = None,
                         tabs: tuple = "") -> None:
    """Creates a paragraph style. This function takes the following keyword parameters:

"name" [required] -> specifies the name of the paragraphstyle to create

linespacingmode [optional] -> specifies the linespacing mode; possible modes are:

fixed linespacing: 0

automatic linespacing: 1

baseline grid linespacing: 2

linespacing [optional] -> specifies the linespacing if using fixed linespacing

alignment [optional] -> specifies the alignment of the paragraph

-> left: 0

-> center: 1

-> right: 2

-> justify: 3

-> extend: 4

leftmargin [optional], rightmargin [optional] -> specify the margin

gapbefore [optional], gapafter [optional] -> specify the gaps to the heading and following paragraphs

firstindent [optional] -> the indent of the first line

hasdropcap [optional] -> specifies if there are caps (1 = yes, 0 = no)

dropcaplines [optional] -> height (in lines) of the caps if used

dropcapoffset [optional] -> offset of the caps if used

"charstyle" [optional] -> char style to use

"bullet" [optional] -> string to use as bullet

"tabs" [optional] -> a list containg tab definitions

-> a tab is defined as a tuple with the following format (position,type,fillchar)"

-> position [required] -> float value for the position

-> type [optional] -> left: 0 [default], right: 1, period: 2, comma: 3, center: 4

-> fillchar [optional] -> the char to fill the space; default is none"""


def getCharStyles() -> list:
    """Return a list of the names of all character styles in the current document."""


def getCharacterStyle(name: str = None) -> str:
    """Return name of character style applied to object named "name". If "name" is not given, the currently selected object is used. If current object has a text selection, the name of style applied to start of selection is returned. Otherwise the name of the item default character style is returned."""


def getParagraphStyle(name: str = None) -> str:
    """Return name of paragraph style applied to object named "name". If "name" is not given, the currently selected object is used. If current object has a text selection, the name of style applied to start of selection is returned. Otherwise the name of the item default style is returned."""


def getParagraphStyles() -> list:
    """Return a list of the names of all paragraph styles in the current document."""


def loadStylesFromFile(filename: str):
    """Loads paragraph styles from the Scribus document at "filename" into the current document."""


def setCharacterStyle(style: str, name: str = None):
    """Apply the named character "style" to the object named "name". If object name is not provided, style is applied on current object selection. If multiple objects are selected or if selected object has no text selection, style is applied on selected objects. Otherwise style is applied to the current text selection."""


def setParagraphStyle(style: str, name: str = None):
    """Apply the named paragraph "style" to the object named "name". If object name is not provided, style is applied on current object selection. If multiple objects are selected or if selected object has no text selection, style is applied on selected objects. Otherwise style is applied to the current text selection."""


# Other Styles
def createCustomLineStyle(styleName: str, style: dict) -> None:
    """Creates the custom line style 'styleName'.

styleName -> name of the custom line style to create

This function takes list of dictionary as parameter for "style". Each dictionary represent one subline within style. Dictionary can have those keys:

Color [optional] -> name of the color to use (string)

Dash [optional] -> type of line to use (integer)

LineEnd [optional] -> type of LineEnd to use (integer)

LineJoin [optional] -> type of LineJoin to use (integer)

Shade [optional] -> opacity of line (integer)

Width [optional] -> width of line (double)"""


def getCellStyle(row: int, column: int, name: str = None) -> str:
    """Returns the named style of the cell at "row", "column" in the table "name". If "name" is not given the currently selected item is used.

May throw ValueError if the cell does not exist."""


def getCellStyles() -> list:
    """Return a list of the names of all cell styles in the current document."""


def getCustomLineStyle(name: str = None) -> str:
    """Returns the styleName of custom line style for the object. If object's "name" is not given the currently selected item is used."""


def getLineStyle(name: str = None) -> int:
    """Returns the line style of the object "name". If "name" is not given the currently selected item is used. Line style constants are: LINE_DASH, LINE_DASHDOT, LINE_DASHDOTDOT, LINE_DOT, LINE_SOLID"""


def getLineStyles() -> list:
    """Return a list of the names of all line styles in the current document."""


def getTableStyle(name: str = None) -> str:
    """Returns the named style of the table "name". If "name" is not given the currently selected item is used."""


def getTableStyles() -> list:
    """Return a list of the names of all table styles in the current document."""


def setCellStyle(row: int, column: int, style: str, name: str = None):
    """Sets the named style of the cell at "row", "column" in the table "name" to "style". If "name" is not given the currently selected item is used.

May throw ValueError if the cell does not exist."""


def setCustomLineStyle(styleName: str, name: str = None):
    """Sets the custom line style of the object "name" to "styleName" Argument "styleName" is the name of line style as seen in Style Manager If "name" is not given the currently selected item is used."""


def setLineStyle(style: int, name: str = None):
    """Sets the line style of the object "name" to the style "style". If "name" is not given the currently selected item is used. Argument for this function is number - value from 1 to 37 There are few predefined constants for "style" - LINE_"""


# Selection
def deselectAll():
    """Deselects all objects in the whole document."""


def getSelectedObject(nr: int = 0):
    """Returns the name of the selected object. "nr" if given indicates the number of the selected object, e.g. 0 means the first selected object, 1 means the second selected Object and so on."""


def moveSelectionToBack():
    """Moves current selection to back."""


def moveSelectionToFront():
    """Moves current selection to front."""


def selectObject(name: str):
    """Selects the object with the given "name"."""


def selectionCount() -> int:
    """Returns the number of selected objects."""


# Frame Properties
def flipObject(H: bool, V: bool, name: str = None):
    """Toggle the object "name" horizontal and/or vertical flip. If "name" is not given the currently selected item is used. """


def getCornerRadius(name: str = None) -> int:
    """Returns the corner radius of the object "name". The radius is expressed in points. If "name" is not given the currently selected item is used."""


def getFillBlendmode(name: str = None) -> int:
    """Returns the fill blendmode of the object "name". If "name" is not given the currently selected Item is used."""


def getFillColor(name: str = None) -> str:
    """Returns the name of the fill color of the object "name". If "name" is not given the currently selected item is used."""


def getFillShade(name: str = None) -> int:
    """Returns the shading value of the fill color of the object "name". If "name" is not given the currently selected item is used."""


def getFillTransparency(name: str = None) -> float:
    """Returns the fill transparency of the object "name". If "name" is not given the currently selected Item is used."""


def getLineBlendmod(name: str = None) -> int:
    """Returns the line blendmode of the object "name". If "name" is not given the currently selected Item is used."""


def getLineCap(name: str = None) -> int:
    """Returns the line cap style of the object "name". If "name" is not given the currently selected item is used. The cap types are: CAP_FLAT, CAP_ROUND, CAP_SQUARE"""


def getLineColor(name: str = None) -> str:
    """Returns the name of the line color of the object "name". If "name" is not given the currently selected item is used."""


def getLineJoin(name: str = None) -> int:
    """Returns the line join style of the object "name". If "name" is not given the currently selected item is used. The join types are: JOIN_BEVEL, JOIN_MITTER, JOIN_ROUND"""


def getLineShade(name: str = None) -> int:
    """Returns the shading value of the line color of the object "name". If "name" is not given the currently selected item is used."""


def getLineTransparency(name: str = None) -> float:
    """Returns the line transparency of the object "name". If "name" is not given the currently selected Item is used."""


def getLineWidth(name: str = None) -> int:  # returns integer but wants to take float in setLineWidth?!
    """Returns the line width of the object "name". If "name" is not given the currently selected Item is used."""


def getObjectAttributes(name: str = None) -> list:
    """Returns a list containing all attributes of object \"name\""""


def getObjectType(name: str = None) -> str:
    """Get type of object "name" as a string."""


def getPosition(name: str = None) -> (float, float):
    """Returns a (x, y) tuple with the position of the object "name". If "name" is not given the currently selected item is used. The position is expressed in the actual measurement unit of the document - see UNIT_ for reference."""


def getRotation(name: str = None) -> int:
    """Returns the rotation of the object "name". The value is expressed in degrees, and clockwise is positive. If "name" is not given the currently selected item is used."""


def getSize(name: str = None) -> (float, float):
    """Returns a (width, height) tuple with the size of the object "name". If "name" is not given the currently selected item is used. The size is expressed in the current measurement unit of the document - see UNIT_ for reference."""


def getTextFlowMode(name: str = None) -> int:
    """Return the current text flow mode used by item "name" as an integer. If "name" is not given, the currently selected object is used.

The function will return one of the following value: - 0 : text flow around frame is disabled - 1 : text flow around frame shape - 2 : text flow around frame bounding box - 3 : text flow around frame contour line - 4 : text flow around image clip path"""


def isLocked(name: str = None) -> bool:
    """Returns true if is the object "name" locked. If "name" is not given the currently selected item is used."""


def lockObject(name: str = None) -> bool:
    """Locks the object "name" if it's unlocked or unlock it if it's locked. If "name" is not given the currently selected item is used. Returns true if locked."""


def moveObject(dx: float, dy: float, name: str = None):
    """Moves the object "name" by dx and dy relative to its current position. The distances are expressed in the current measurement unit of the document (see UNIT constants). If "name" is not given the currently selected item is used. If the object "name" belongs to a group, the whole group is moved."""


def moveObjectAbs(x: float, y: float, name: str = None):
    """Moves the object "name" to a new location. The coordinates are expressed in the current measurement unit of the document (see UNIT constants). If "name" is not given the currently selected item is used. If the object "name" belongs to a group, the whole group is moved."""


def rotateObject(rot: float, name: str = None):
    """Rotates the object "name" by "rot" degrees relatively. The object is rotated by the vertex that is currently selected as the rotation point - by default, the top left vertex at zero rotation. Positive values mean counter clockwise rotation when the default rotation point is used. If "name" is not given the currently selected item is used."""


def rotateObjectAbs(rot: float, name: str = None):
    """Sets the rotation of the object "name" to "rot". Positive values mean counter clockwise rotation. If "name" is not given the currently selected item is used."""


def setCornerRadius(radius: int, name: str = None):
    """Sets the corner radius of the object "name". The radius is expressed in points. If "name" is not given the currently selected item is used.

May raise ValueError if the corner radius is negative."""


def setFillBlendmode(blendmode: int, name: str = None):
    """Sets the fill blendmode of the object "name" to blendmode If "name" is not given the currently selected item is used."""


def setFillColor(color: str, name: str = None):
    """Sets the fill color of the object "name" to the color "color". "color" is the name of one of the defined colors. If "name" is not given the currently selected item is used."""


def setFillShade(shade: int, name: str = None):
    """Sets the shading of the fill color of the object "name" to "shade". "shade" must be an integer value in the range from 0 (lightest) to 100 (full Color intensity). If "name" is not given the currently selected Item is used.

May raise ValueError if the fill shade is out of bounds."""


def setFillTransparency(transparency: float, name: str = None):
    """Sets the fill transparency of the object "name" to transparency If "name" is not given the currently selected item is used."""


def setGradientFill(type: int, color1: str, shade1: int, color2: str, shade2: int, name: str = None):
    """Sets the gradient fill of the object "name" to type. Color descriptions are the same as for setFillColor() and setFillShade(). See the constants for available types (FILL_)."""


def setGradientStop(color: str, shade: int, opacity: float, ramppoint: float, name: str = None):
    """Set or add a gradient stop to the gradient fill of the object "name" at position ramppoint. Color descriptions are the same as for setFillColor() and setFillShade(). setGradientFill() must have been called previously for the gradient fill to be visible."""


def setitemname(newName: str,
                name: str = None):  # Not sure if this capitalization is correct, that's how it is in the docs
    """Sets the name of object "name" to newName and returns the name applied. If "name" is not given the currently selected item is used.

May raise NotFoundError if the object doesn't exist."""


def setLineBlendmod(blendmode: int, name: str = None):
    """Sets the line blendmode of the object "name" to blendmode If "name" is not given the currently selected item is used."""


def setLineCap(endType: int, name: str = None):
    """Sets the line cap style of the object "name" to the style "cap". If "name" is not given the currently selected item is used. There are predefined constants for "cap" - CAP_."""


def setLineColor(color: str, name: str = None) -> str:
    """Sets the line color of the object "name" to the color "color". If "name" is not given the currently selected item is used."""


def setLineJoin(join: int, name: str = None):
    """Sets the line join style of the object "name" to the style "join". If "name" is not given the currently selected item is used. There are predefined constants for join - JOIN_."""


def setLineShade(shade: int, name: str = None):
    """Sets the shading of the line color of the object "name" to "shade". "shade" must be an integer value in the range from 0 (lightest) to 100 (full color intensity). If "name" is not given the currently selected item is used.

May raise ValueError if the line shade is out of bounds."""


def setLineTransparency(transparency: float, name: str = None):
    """Sets the line transparency of the object "name" to transparency If "name" is not given the currently selected item is used."""


def setLineWidth(width: float, name: str = None):  # takes float but returns integer in getLineWidth?!
    """Sets line width of the object "name" to "width". "width" must be in the range from 0.0 to 12.0 inclusive, and is measured in points. If "name" is not given the currently selected item is used.

May raise ValueError if the line width is out of bounds."""


def setMultiLine(namedStyle: str, name: str = None):
    """Sets the line style of the object "name" to the named style "namedStyle". If "name" is not given the currently selected item is used.

May raise NotFoundError if the line style doesn't exist."""


def setOpjectAttributes(attributes: dict, name: str = None):
    """Sets attributes of the object "name". If "name" is not given the currently selected item is used.

attributes is a list of dictionary. Each dictionary must have those keys: Name, Type, Value, Parameter, Relationship, RelationshipTo, AutoAddTo All values must be strings.

May raise NotFoundError if the object doesn't exist."""


def setTextFlowMode(name: str, state: int):
    """Enables/disables "Text Flows Around Frame" feature for object "name". Called with parameters string name and optional int "state" (0 <= state <= 3). Setting "state" to 0 will disable text flow. Setting "state" to 1 will make text flow around object frame. Setting "state" to 2 will make text flow around bounding box. Setting "state" to 3 will make text flow around contour line. If "state" is not passed, text flow is toggled."""


def sizeObject(width: float, height: float, name: str = None):
    """Resizes the object "name" to the given width and height. If "name" is not given the currently selected item is used."""


def getObjectType(name: str = None) -> str:
    """Get type of object "name" as a string."""


def getPosition(name: str = None) -> (float, float):
    """Returns a (x, y) tuple with the position of the object "name". If "name" is not given the currently selected item is used. The position is expressed in the actual measurement unit of the document - see UNIT_ for reference."""


def getRotation(name: str = None) -> int:
    """Returns the rotation of the object "name". The value is expressed in degrees, and clockwise is positive. If "name" is not given the currently selected item is used."""


def getSize(name: str = None) -> (float, float):
    """Returns a (width, height) tuple with the size of the object "name". If "name" is not given the currently selected item is used. The size is expressed in the current measurement unit of the document - see UNIT_ for reference."""


def getTextFlowMode(name: str = None) -> int:
    """Return the current text flow mode used by item "name" as an integer. If "name" is not given, the currently selected object is used.

The function will return one of the following value: - 0 : text flow around frame is disabled - 1 : text flow around frame shape - 2 : text flow around frame bounding box - 3 : text flow around frame contour line - 4 : text flow around image clip path"""


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
