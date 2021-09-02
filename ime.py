import curses

class ImeInstance:
    def __init__(self, **settings):
        self.settings = settings

    def start(self) -> None:
        self.running = True
        self._editor_loop()

    def _setup_ncurses(self) -> None:
        self.stdscr = curses.initscr()
        self.stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()

    def _end_ncurses(self) -> None:
        self.stdscr.keypad(True)
        curses.cbreak()
        curses.noecho()

    def _keystroke_handler(self, key: int, **data) -> None:
        return

    
    def _editor_loop(self) -> int:
        self._setup_ncurses()
        self.stdscr.clear()
        initial_message = True

        while self.running is True:
            if initial_message == True:
                if self.settings["debug_msg"] == True:
                    self.stdscr.addstr(0, 0, "Debug message")
                else:
                    self.stdscr.addstr(0, 1, "___ __  __                              _ _____    _ _ _\n|_ _|  \/  |_ __  _ __ _____   _____  __| | ____|__| (_) |_ ___  _ __\n | || |\/| | '_ \| '__/ _ \ \ / / _ \/ _` |  _| / _` | | __/ _ \| '__|\n | || |  | | |_) | | | (_) \ V /  __/ (_| | |__| (_| | | || (_) | |\n|___|_|  |_| .__/|_|  \___/ \_/ \___|\__,_|_____\__,_|_|\__\___/|_|\n           |_|")
                    self.stdscr.addstr(7, 1, "Hello, " + str(self.settings["name"]))
                    self.stdscr.addstr(8, 1, "Welcome to IME")
                    self.stdscr.addstr(9, 1, "1 - New File\n 2 - Open File\n 3 - Open Config\n 4 - Exit")
                    
                    self._keystroke_handler()
            else:
                pass

            self.stdscr.refresh()

        self._end_ncurses()
        return 0
