# Created by Nicholas Nord
# July 22, 2019
#
import pygame
import time
import random
import matplotlib.pyplot as plt

pygame.init()

display_width = 1200
display_height = 600

black = (0,0,0)
gray = (214,214,214, 1)
white = (255,255,255)

visualizer_dim = 50,125,1100,300
left_dim = 50,450,350,300
middle_dim = 425,450,350,300
right_dim = 800,450,350,300

sorting_algo = 1
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

def insertion_sort():
    global pause_UI
    global current_array
    global visualizer_dim
    for index in range(len(current_array)):
        current_element = current_array[index]
        current_length = (current_array[index]).line_length
        checking_index = index - 1
        while checking_index >= 0 and (current_array[checking_index]).line_length > current_length:
            #current_array[index], current_array[checking_index] = current_array[checking_index], current_array[index]
            current_array[checking_index + 1] = current_array[checking_index]
            checking_index = checking_index - 1
            #draw_element_array()
            #time.sleep(1)
        current_array[checking_index + 1] = current_element
    for x in range(len(current_array)):
        print(x)
    draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])

def demo_insertion_sort():
    global pause_UI
    global current_array
    global visualizer_dim
    for index in range(1, len(current_array)):
        current_element = current_array[index]
        current_length = (current_array[index]).line_length
        checking_index = index - 1
        while checking_index >= 0 and (current_array[checking_index]).line_length > current_length:
            #current_array[index], current_array[checking_index] = current_array[checking_index], current_array[index]
            current_array[checking_index + 1] = current_array[checking_index]
            checking_index = checking_index - 1
            display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
            draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
            time.sleep(.075)
        current_array[checking_index + 1] = current_element
    display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
    draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])

def selection_sort():
    print("selection")
def quick_sort():
    print("quick")
def merge_sort():
    print("merge")
def heap_sort():
    print("heap")

def draw_element_array(x, y, width, height):
    global current_array
    width_var = (width / len(current_array))
    height_var = (height/ len(current_array))
    adjustment_var = (width / (2 * len(current_array)))
    index = 1
    for element in current_array:
        element_rect = pygame.Rect(x + (index * width_var), y + height, width / 20, (height_var * element.line_length))
        element_rect.midbottom = x + (index * width_var) - adjustment_var ,(y + height)
        pygame.draw.rect(display, black, element_rect, 1)
        pygame.display.update()
        index = index + 1

def initial_build():
    element_array = build_line_array(20)
    global original_array
    global current_array
    global visualizer_dim
    global left_dim
    global middle_dim
    global right_dim
    original_array = element_array.copy()
    current_array = element_array
    random.shuffle(element_array)
    draw_outline(visualizer_dim)
#    draw_outline(left_dim)
#    draw_outline(middle_dim)
#    draw_outline(right_dim)

def draw_outline(dimensions):
    x, y, width, height = dimensions[0], dimensions[1], dimensions[2], dimensions[3]
    rectangle = [(x,y) , (x + width, y), (x+width , y+height), (x , y+height)]
    pygame.draw.lines(display, black,True,rectangle, 1)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def draw_sort_buttons():
    b1 = pygame.Rect(0,0,(display_width /5) * 1, 100)
    b2 = pygame.Rect((display_width /5) * 1,0,(display_width /5) * 1, 100)
    b3 = pygame.Rect((display_width /5) * 2,0,(display_width /5) * 1, 100)
    b4 = pygame.Rect((display_width /5) * 3,0,(display_width /5) * 1, 100)
    b5 = pygame.Rect((display_width /5) * 4,0,(display_width /5) * 1, 100)

    b6 = pygame.Rect((display_width /7) * 1,450,(display_width /7) * 1, 100)
    b7 = pygame.Rect((display_width /7) * 3,450,(display_width /7) * 1, 100)
    b8 = pygame.Rect((display_width /7) * 5,450,(display_width /7) * 1, 100)

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

    pygame.draw.rect(display, black,b6)
    pygame.draw.rect(display, gray, (b6.x + 5, b6.y + 5, b6.width - 10, b6.height - 10))
    pygame.draw.rect(display, black,b7)
    pygame.draw.rect(display, gray, (b7.x + 5, b7.y + 5, b7.width - 10, b7.height - 10))
    pygame.draw.rect(display, black,b8)
    pygame.draw.rect(display, gray, (b8.x + 5, b8.y + 5, b8.width - 10, b8.height - 10))

    play_icon = [(225, 475), (225, 525), (280, 500), (225, 475)]
    restart_arrow = [(578,470),(598,460),(598,480),(578,470)]
    cover_up = [(598, 500),(598,460),(560, 480),(598,500)]

    pygame.draw.polygon(display, black, play_icon)
    pygame.draw.circle(display, black, (598, 500), 35, 5)
    pygame.draw.polygon(display, gray, cover_up)
    pygame.draw.polygon(display, black, restart_arrow)
    pygame.draw.rect(display, black, (887,520,30,20))
    pygame.draw.rect(display, black, (927,490,30,50))
    pygame.draw.rect(display, black, (967,460,30,80))


    draw_text(b1.x + (b1.width / 4), b1.y+ (b1.height / 3), "Insertion")
    draw_text(b2.x + (b2.width / 4), b2.y+ (b2.height / 3), "Selection")
    draw_text(b3.x + (b3.width / 4), b3.y+ (b3.height / 3), "Merge")
    draw_text(b4.x + (b4.width / 4), b4.y+ (b4.height / 3), "Quick")
    draw_text(b5.x + (b5.width / 4), b5.y+ (b5.height / 3), "Heap")


def draw_text(x, y, text):
    pygame.font.init()
    small_text = pygame.font.SysFont("arial.ttf", 35)
    text_surface = small_text.render(text, True, black)
    display.blit(text_surface, (x, y))

def sorting_switch(integer):
    print(integer)
    switcher = {
    1: demo_insertion_sort,
    2: selection_sort,
    3: merge_sort,
    4: quick_sort,
    5: heap_sort,
    }
    switcher[integer]()

def main_loop():

    exit_request = False
    global pause_UI
    global sorting_algo
    global current_array
    draw_sort_buttons()
    draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
    #for i in range(len(element_array)):
        #print(element_array[i].line_length)
        #print(original_array[i].line_length)

    while not exit_request:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and pause_UI is False:
                if pygame.mouse.get_pos()[1] <= 100:
                    if pygame.mouse.get_pos()[0] <= 240 and pygame.mouse.get_pos()[0] > 0:
                        sorting_algo = 1
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (5, 5, 230, 90))
                        draw_text(60, 33.3, "Insertion")
                    if pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[0] > 240:
                        sorting_algo = 2
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (240 + 5, 5, 230, 90))
                        draw_text(300, 33.3, "Selection")
                    if pygame.mouse.get_pos()[0] <= 720 and pygame.mouse.get_pos()[0] > 480:
                        sorting_algo = 3
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (480+5, 5, 230, 90))
                        draw_text(540, 33.3, "Merge")
                    if pygame.mouse.get_pos()[0] <= 960 and pygame.mouse.get_pos()[0] > 720:
                        sorting_algo = 4
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (720+5, 5, 230, 90))
                        draw_text(780,33.3, "Quick")
                    if pygame.mouse.get_pos()[0] <= 1200 and pygame.mouse.get_pos()[0] > 960:
                        sorting_algo = 5
                        draw_sort_buttons()
                        pygame.draw.rect(display, white, (960 + 5, 5, 230, 90))
                        draw_text(1020, 33.3, "Heap")
                if pygame.mouse.get_pos()[1]  >= 450 and pygame.mouse.get_pos()[1] < 550:
                    if pygame.mouse.get_pos()[0] >= 171 and pygame.mouse.get_pos()[0] < 342:
                        print("example button for play")
                        pause_UI = True
                        sorting_switch(sorting_algo)
                        pause_UI = False
                    if pygame.mouse.get_pos()[0] >= 513 and pygame.mouse.get_pos()[0] < 684:
                        print("example button for restart")
                        new_array = build_line_array(20)
                        random.shuffle(new_array)
                        current_array = new_array
                        display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
                        draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
                    if pygame.mouse.get_pos()[0] >= 855 and pygame.mouse.get_pos()[0] < 1026:
                        print("example button for stats")
            if event.type == pygame.KEYDOWN and pause_UI == False:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    print("space")
                    pause_UI = True
                    sorting_switch(sorting_algo)
                    pause_UI = False
        pygame.display.update()

        print("--- %s seconds ---" % (time.time() - start_time))
display.fill(white)
initial_build()
main_loop()
pygame.quit()
quit()
