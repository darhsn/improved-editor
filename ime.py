import curses

class ImeInstance:
    def __init__(self, **settings):
        self.settings = settings

    def start(self):
        self.running = True
        self._editor_loop()

    def _setup_ncurses(self):
        self.stdscr = curses.initscr()
    
    def _editor_loop(self):
        while self.running is True:



