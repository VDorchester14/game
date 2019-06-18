'''
# Hopefully this library will manage the intro menu and later on the
# pause menu as well.
'''

import pygame as py
from display_manager import display_manager

'''
# Wrapper class
'''
class menu_manager():

    MAIN_MENU_BACKGROUND = (50,76,119)
    WHITE = (255,255,255)
    BLACK = (0,0,0)

    resolution = None
    # init function
    def __init__(self, passed_display_manager):
        self.dm = passed_display_manager
        self.resolution = self.dm.disp.get_size()
        py.font.init()
        return

    # set text objects
    def text_objects(self, text, font):
        text_surface = font.render(text, True, self.WHITE)
        return text_surface, text_surface.get_rect()

    # game main menu
    # can use this logic to do a pause screen
    def main_menu(self):
        intro = True # we are in the intro

        # intro background and set font
        self.dm.disp.fill(self.MAIN_MENU_BACKGROUND)
        main_font = py.font.SysFont("Helvetica", 72)
        small_font = py.font.SysFont("Helvetica", 24)

        TextSurface, TextRect = self.text_objects("Welcome!", main_font)
        start_surf, start_rect = self.text_objects("Start", small_font)
        leave_surf, leave_rect = self.text_objects("Leave", small_font)

        TextRect.center = ((self.resolution[0]/2),(self.resolution[1]/2))
        self.dm.disp.blit(TextSurface, TextRect) # put the font on the display

        self.dm.update_display()

        # now do the buttons
        start_pos = (self.resolution[0]/2 - 50, self.resolution[1]/2 + 100, 100, 50)
        leave_pos = (self.resolution[0]/2 - 50, self.resolution[1]/2 + 160, 100, 50)

        start = py.draw.rect(self.dm.disp, (0,255,0), start_pos) # start button
        leave = py.draw.rect(self.dm.disp, (255,0,0), leave_pos) # exit button

        # text for buttons
        start_rect.center = (start_pos[0] + start_pos[2]/2, start_pos[1] + start_pos[3]/2)
        leave_rect.center = (leave_pos[0] + leave_pos[2]/2, leave_pos[1] + leave_pos[3]/2)
        self.dm.disp.blit(start_surf, start_rect)
        self.dm.disp.blit(leave_surf, leave_rect)

        self.dm.update_display()

        # Wait for the user to exit
        while(intro):

            mouse = py.mouse.get_pos()

            # interactive button colors
            if(start.collidepoint(mouse)):
                start = py.draw.rect(self.dm.disp, (0,200,0), (self.resolution[0]/2 - 50, self.resolution[1]/2 + 100, 100, 50)) # start button
                for event in py.event.get():
                    if event.type == py.MOUSEBUTTONUP:
                        intro=False

            elif(leave.collidepoint(mouse)):
                leave = py.draw.rect(self.dm.disp, (200,0,0), (self.resolution[0]/2 - 50, self.resolution[1]/2 + 160, 100, 50)) # exit button
                for event in py.event.get():
                    if event.type == py.MOUSEBUTTONUP:
                        py.quit()
                        quit()
            else:
                start = py.draw.rect(self.dm.disp, (0,255,0), (self.resolution[0]/2 - 50, self.resolution[1]/2 + 100, 100, 50)) # start button
                leave = py.draw.rect(self.dm.disp, (255,0,0), (self.resolution[0]/2 - 50, self.resolution[1]/2 + 160, 100, 50)) # exit button



            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        intro = False
                elif event.type == py.QUIT:
                    py.quit()

            self.dm.update_display()

        # back to black
        self.dm.disp.fill(self.BLACK)
        self.dm.update_display()

        return

'''
# end class
'''
