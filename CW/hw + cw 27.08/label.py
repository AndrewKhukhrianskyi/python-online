import pygame as pg

class Label:
    def __init__(self, text = None):
        self.text = text
        self.font = pg.font.Font(None, 20)
    def add_score(self, score):
        score += 1
        return str(score)
    def kill_label(self):
        self.kill()