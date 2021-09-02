# IMproved-Editor
IMproved-Editor or IME is a open-source ncurses terminal based text editor written in
python, the main goals are:
 - Python configuration with a custom wrapper
 - Minimalistic and lightweight editor
 - Modal editor with vim-based (hjkl) movement keys

## Documentation
IME is a modal editor, it has 2 modes, `CNTRL`, to do advanced operations and
`INSRT` to insert new text into the file, to swap mode you press `^D`, for
example if you are in `INSRT` mode and you press `^D` now you are in `CNTRL`
mode, these are the main bindings
### Control mode
- 'q' quits
- 'qf' force quit without savings
- 'ec' edit configuration
- 'op' open palette with command list
- 'of' opens file

## Screenshots
**TODO**: Add screenshots
(screenshot)[./screenshot/ime-dev-1.png]
