"""
 ___ __  __                              _ _____    _ _ _
|_ _|  \/  |_ __  _ __ _____   _____  __| | ____|__| (_) |_ ___  _ __
 | || |\/| | '_ \| '__/ _ \ \ / / _ \/ _` |  _| / _` | | __/ _ \| '__|
 | || |  | | |_) | | | (_) \ V /  __/ (_| | |__| (_| | | || (_) | |
|___|_|  |_| .__/|_|  \___/ \_/ \___|\__,_|_____\__,_|_|\__\___/|_|
           |_|
    D  e  f  a  u  l  t   C  o  n  f  i  g  u  r  a  t  i  o  n

 Default IME configuration by darhsn
"""
import ime

# Create new ImeInstance
editor = ime.ImeInstance(default_buf="Untitled", name="Ime Dev", debug_msg=False)

# Startup editor
editor.start()
