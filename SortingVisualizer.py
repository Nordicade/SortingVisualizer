# Created by Nicholas Nord
# July 22, 2019
#
import pygame
import time
import random

pygame.init()

display_width = 1200
display_height = 800

black = (0,0,0)
gray = (214,214,214, 1)
white = (255,255,255)

left_array_dimensions = 0,0,0,0
middle_array_dimensions = 0,0,0,0
right_array_dimensions = 0,0,0,0

sorting_algo = None
pause_UI = False

original_array = []
current_array = []

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Data Sorting Visualizer')
start_time = time.time()

class line_element:
    def __init__(self):
        self.line_length: 0

def build_line_array(array_size):
    #build an array of size / 2
    line_array = []
    for index in range(1, array_size):
        temp = line_element()
        temp.line_length = index
        line_array.append(temp)
    return line_array

def insertion_sort_line():
    global pause_UI
    global current_array
    for index in range(1, len(current_array)):
        current_element = current_array[index]
        current_length = (current_array[index]).line_length
        checking_index = index - 1
        while checking_index >= 0 and (current_array[checking_index]).line_length > current_length:
            #current_array[index], current_array[checking_index] = current_array[checking_index], current_array[index]
            current_array[checking_index + 1] = current_array[checking_index]
            checking_index = checking_index - 1
            #draw_element_array()
            print("adjustment")
            #time.sleep(1)
        current_array[checking_index + 1] = current_element
    draw_element_array()
    pause_UI = False

def draw_element_array():
    global current_array
    display.fill(white)
    index = 0
    for element in current_array:
        pygame.draw.line(display, black, (100 + (index * 2) , display_height - 50), ( 100 + (index * 2), element.line_length) , 1)
        pygame.display.update()
        index = index + 1

def initial_build():
    element_array = build_line_array(300)
    global original_array
    global current_array
    original_array = element_array.copy()
    current_array = element_array
    random.shuffle(element_array)
    draw_element_array()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def draw_sort_buttons():
    b1 = pygame.Rect(0,0,(display_width /5) * 1, 100)
    b2 = pygame.Rect((display_width /5) * 1,0,(display_width /5) * 1, 100)
    b3 = pygame.Rect((display_width /5) * 2,0,(display_width /5) * 1, 100)
    b4 = pygame.Rect((display_width /5) * 3,0,(display_width /5) * 1, 100)
    b5 = pygame.Rect((display_width /5) * 4,0,(display_width /5) * 1, 100)

    pygame.draw.rect(display, black,b1)
    pygame.draw.rect(display, gray, (b1.x + 5, b1.y + 5, b1.width - 10, b1.height - 10))
    pygame.draw.rect(display, black,b2)
    pygame.draw.rect(display, gray, (b2.x + 5, b2.y + 5, b2.width - 10, b2.height - 10))
    pygame.draw.rect(display, black,b3)
    pygame.draw.rect(display, gray, (b3.x + 5, b3.y + 5, b3.width - 10, b3.height - 10))
    pygame.draw.rect(display, black,b4)
    pygame.draw.rect(display, gray, (b4.x + 5, b4.y + 5, b4.width - 10, b4.height - 10))
    pygame.draw.rect(display, black,b5)
    pygame.draw.rect(display, gray, (b5.x + 5, b5.y + 5, b5.width - 10, b5.height - 10))


    #argeText = pygame.font.Font('freesansbold.ttf',115)
    #TextSurf, TextRect = text_objects("Insertion", pygame.font.get_default_font())
    #TextRect.center = ((display_width/2),(display_height/2))
    #display.blit(TextSurf, TextRect)

def main_loop():

    exit_request = False
    global pause_UI
    draw_sort_buttons()

    #for i in range(len(element_array)):
        #print(element_array[i].line_length)
        #print(original_array[i].line_length)

    while not exit_request:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[1] <= 100:
                    if pygame.mouse.get_pos()[0] <= 240 and pygame.mouse.get_pos()[0] > 0:
                        sorting_algo = "insertion"
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (5, 5, 230, 90))
                    if pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[0] > 240:
                        print("button 2")
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (240 + 5, 5, 230, 90))
                    if pygame.mouse.get_pos()[0] <= 720 and pygame.mouse.get_pos()[0] > 480:
                        print("button 3")
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (480+5, 5, 230, 90))
                    if pygame.mouse.get_pos()[0] <= 960 and pygame.mouse.get_pos()[0] > 720:
                        print("button 4")
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (720+5, 5, 230, 90))
                    if pygame.mouse.get_pos()[0] <= 1200 and pygame.mouse.get_pos()[0] > 960:
                        print("button 5")
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (960 + 5, 5, 230, 90))
            if event.type == pygame.KEYDOWN and pause_UI == False:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    insertion_sort_line()
                    pause_UI = True

        pygame.display.update()

        #print("--- %s seconds ---" % (time.time() - start_time))
initial_build()
main_loop()
pygame.quit()
quit()
