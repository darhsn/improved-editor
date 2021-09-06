# Configurate & Extend IME
To be more precise, IME isn't an editor, is a python module, infact to install
ime you need to install ime with pip (right now there isn't a package) or
manual install the ime module and then create an executable wrapper, this is an example:
```py
import ime

def keystroke_handler(key):
    if key == ord('q'):
        editor.quit()

editor = ime.ImeInstance(keystroke_handler = lambda k: keystroke_handler(k))
```
