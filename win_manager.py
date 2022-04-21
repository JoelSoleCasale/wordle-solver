import pyautogui as pg
import time

class Manager:

    url = 'https://www.nytimes.com/games/wordle/index.html'

    def exec(self, instruction):
        time.sleep(1)
        pg.typewrite(instruction)
        return self
        
    def openWordle(self):
        pg.hotkey("win")
        self.exec("google").exec("\n").exec(self.url).exec("\n")