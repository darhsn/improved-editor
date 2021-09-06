import curses

class ImeInstance:
    def __init__(self, **settings):
        if not "keystroke_handler" in settings:
            print("IME_FATAL_ERR: Invalid keystroke_handler!")
            self.quit()
        else:
            self.settings = settings

    def quit(self):
        self._end_ncurses()
        exit(0)
    
    def _start_ncurses(self):
        self.stdscr = curses.initscr()

        curses.cbreak()
        self.stdscr.keypad(True)
        curses.noecho()

        return

    def _end_ncurses(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

        return
    
    def start(self):
        self._start_ncurses()

        self.running = True

        while self.running:
            pressed_key = self.stdscr.getch()

            self.settings["keystroke_handler"](pressed_key)

        self._end_ncurses()

        return
            
