# Scribus Dummy by TreSet

### Dummy Python file for scribus' scripter API, as it's not publicly accessible.
This API has no functionality, it is purely used to provide IntelliSense (autocomplete) for scripter scripts.

### Usage
To use the scribus API and also get IntelliSense from this dummy do the following:
- Download the ``scribusDummy.py`` script and place it into your project folder.
- Add the following code to the top of the file you want to use it in:
    ```python
    try:
        import scribus
    except ImportError:
        print("Unable to import the 'scribus' module. This script will only run within")
        print("the Python interpreter embedded in Scribus. Try Script->Execute Script.")
        import scribusDummy as scribus
        sys.exit(1)
    ```
  
### Features
- Functions as provided in the scripter documentation
- Function Arguments as documented (if documented having the correct default value, otherwise having a generic descriptive default value)
- Return Types as documented (if documented returning the correct value, otherwise returning a generic descriptive value)
- Throwable Errors as documented (behind descriptive if clauses that are always false)

### Currently Included
- Document Commands
- Master Page Commands
- Creating & Destroying Objects
- Selecting Objects
- Creating & Manipulating Styles
- Handling Text Frames
- Using Dialogs
- Predefined Constants
- Errors