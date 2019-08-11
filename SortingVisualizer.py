# Created by Nicholas Nord
# July 22, 2019
#
import pygame
import time
import math
import random
import matplotlib.pyplot as plt

pygame.init()

display_width = 1200
display_height = 600

black = (0,0,0)
gray = (214,214,214, 1)
white = (255,255,255)
red = (255, 0 , 0)
blue = (0, 0, 255)

visualizer_dim = 50,125,1100,300

sorting_algo = 1
visualizer_array_size = 20
n_factor = 6
delay = .2
trial_count = 3
pause_UI = False

original_array = []
current_array = []

# Arrays holding timestamps for sorting arrays. (each element increases array size by 10^n where 0>n>10)
best_times = []
avg_times = []
worst_times = []

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Data Sorting Visualizer')
start_time = time.time()

class line_element:
    def __init__(self):
        self.line_length: 0

def build_line_array(array_size):
    line_array = []
    for index in range(1, array_size):
        temp = line_element()
        temp.line_length = index
        line_array.append(temp)
    return line_array

def insertion_sort(unsorted_array):
    for index in range(len(unsorted_array)):
        current_element = unsorted_array[index]
        checking_index = index - 1
        while checking_index >= 0 and (unsorted_array[checking_index]) > current_element:
            unsorted_array[checking_index + 1] = unsorted_array[checking_index]
            checking_index = checking_index - 1
        unsorted_array[checking_index + 1] = current_element
    return unsorted_array

def demo_insertion_sort():
    global current_array
    global visualizer_dim
    global delay
    for index in range(1, len(current_array)):
        # select first element to be index
        current_element = current_array[index]
        current_length = (current_array[index]).line_length
        checking_index = index - 1
        # compare the index with the element that came before index
        while checking_index >= 0 and (current_array[checking_index]).line_length > current_length:
            draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
            draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
            time.sleep(delay)
            display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
            # if a swap is needed, keep shifting and overwriting elements until correct spot is found
            current_array[checking_index + 1] = current_array[checking_index]
            checking_index = checking_index - 1
        current_array[checking_index + 1] = current_element
    display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
    draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
    draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))

def selection_sort(unsorted_array):
    for sorting_index in range(len(unsorted_array)):
        min_index = sorting_index
        for unsorted_index in range(sorting_index+1, len(unsorted_array)):
            if unsorted_array[min_index] > unsorted_array[unsorted_index]:
                # set as current_min and proceed looking throughout list
                min_index = unsorted_index
        #swap current index with current min
        temp = unsorted_array[sorting_index]
        unsorted_array[sorting_index] = unsorted_array[min_index]
        unsorted_array[min_index] = temp

def demo_selection_sort():
    global current_array
    global visualizer_dim
    global delay

    for sorting_index in range(len(current_array)):
        min_index = sorting_index
        for unsorted_index in range(sorting_index+1, len(current_array)):
            if current_array[min_index].line_length > current_array[unsorted_index].line_length:
                # set as current_min and proceed looking throughout list
                min_index = unsorted_index
        #swap current index with current min
        temp = current_array[sorting_index]
        current_array[sorting_index] = current_array[min_index]
        current_array[min_index] = temp
        #draw changes to display and sleep for desired delay
        display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
        draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
        draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
        time.sleep(delay)

# BIG help from https://www.pythoncentral.io/quick-sort-implementation-guide/
# This method is a clean method that takes in an unsorted array and sorts using median of 3 quick sort
def quick_sort(unsorted_array):
    #initial quick sort call that calls the recursive function
    quick_sort_recursive(unsorted_array, 0, len(unsorted_array) - 1)

# This method is called on repeat to divide the array into smaller chunks, finding new partitions each time
def quick_sort_recursive(unsorted_array, left_index, right_index):
    if left_index < right_index:
        # calls helper method to find partition, then calls this method for each sub-array (excluding pivot)
        pivot_index = quick_sort_partition(unsorted_array, left_index, right_index)
        #print(str(left_index) + " and " + str(pivot_index - 1))
        #print(len(unsorted_array))
        quick_sort_recursive(unsorted_array, left_index, pivot_index - 1)
        quick_sort_recursive(unsorted_array, pivot_index + 1, right_index)

#this method finds the true position of the pivot point and sets unordered smaller/larger elements on their respective sides
def quick_sort_partition(unsorted_array, left_index, right_index):
    #pick a pivot point using median of 3, sorting first,middle, and last element in the process
    middle_index = (left_index + (right_index)) //2
    pivot_index = median_of_three(unsorted_array, left_index, middle_index, right_index)
    pivot_value = unsorted_array[pivot_index]
    smaller = left_index + 1
    larger = right_index
    true_pivot_found = False
    #SWAPPING PIVOT WITH FIRST ELEMENT!
    swap(unsorted_array, pivot_index, left_index)

    while not true_pivot_found:
        while smaller <= larger and unsorted_array[smaller] <= pivot_value:
            smaller = smaller + 1
        while smaller <= larger and unsorted_array[larger] >= pivot_value:
            larger = larger - 1
        if larger < smaller:
            true_pivot_found = True
        else:
            swap(unsorted_array, smaller, larger)

    #SWAPPING PIVOT WITH FIRST ELEMENT!
    swap(unsorted_array, pivot_index, left_index)
    return larger

#helper method that performs the swap using a temp variable (imo cleaner than the # python swap)
def swap(array, left_index, right_index):
#    array[left_index], array[right_index] = array[right_index], array[left_index]
        temp = array[left_index]
        array[left_index] = array[right_index]
        array[right_index] = temp

# Reads the first/center/last positioned elements within array, sorts the 3, and returns the median element
def median_of_three(unsorted_array, left_index, middle_index, right_index):
    if unsorted_array[right_index] < unsorted_array[left_index]:
        swap(unsorted_array, left_index, right_index)
    if unsorted_array[middle_index] < unsorted_array[left_index]:
        swap(unsorted_array, left_index, middle_index)
    if unsorted_array[right_index] < unsorted_array[middle_index]:
        swap(unsorted_array, middle_index, right_index)
    pivot = middle_index
    #print("After: L: "+str(unsorted_array[left_index]) +" Mid: "+str(unsorted_array[middle_index])+" R: "+str(unsorted_array[right_index]))
    return pivot

def demo_quick_sort():
    global current_array
    global visualizer_dim
    global delay

    display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
    draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
    draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
    time.sleep(delay)

    demo_quick_sort_recursive(current_array, 0, len(current_array) - 1)

    display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
    draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
    draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
    time.sleep(delay)

def demo_quick_sort_recursive(unsorted_array, left_index, right_index):
    if left_index < right_index:
        # calls helper method to find partition, then calls this method for each sub-array (excluding pivot)
        pivot_index = demo_quick_sort_partition(unsorted_array, left_index, right_index)
        #print(str(left_index) + " and " + str(pivot_index - 1))
        #print(len(unsorted_array))
        display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
        draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
        draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
        time.sleep(delay)

        demo_quick_sort_recursive(unsorted_array, left_index, pivot_index - 1)
        demo_quick_sort_recursive(unsorted_array, pivot_index + 1, right_index)
    #    print("done")
    #    for n in range(len(current_array)):
    #        print(current_array[n].line_length)

#this method finds the true position of the pivot point and sets unordered smaller/larger elements on their respective sides
def demo_quick_sort_partition(unsorted_array, left_index, right_index):
    #pick a pivot point using median of 3, sorting first,middle, and last element in the process
    middle_index = (left_index + (right_index)) //2
    pivot_index = demo_median_of_three(unsorted_array, left_index, middle_index, right_index)
    pivot_value = unsorted_array[pivot_index].line_length
    smaller = left_index + 1
    larger = right_index
    true_pivot_found = False

    #SWAPPING PIVOT WITH FIRST ELEMENT!
    swap(unsorted_array, pivot_index, left_index)

    display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
    #draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
    draw_element_array_comparison(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3], pivot_index, pivot_index)
    draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
    time.sleep(delay)

    while not true_pivot_found:
        while smaller <= larger and unsorted_array[smaller].line_length <= pivot_value:
            smaller = smaller + 1
        while smaller <= larger and unsorted_array[larger].line_length >= pivot_value:
            larger = larger - 1
        if larger < smaller:
            true_pivot_found = True
        else:
            swap(unsorted_array, smaller, larger)
            display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
            #draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
            draw_element_array_comparison(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3], left_index, pivot_index)
            draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
            time.sleep(delay)

    #RESWAPPING PIVOT WITH FIRST ELEMENT!
    swap(unsorted_array, left_index, larger)
    display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
    draw_element_array_comparison(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3], pivot_index, pivot_index)
    draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
    time.sleep(delay)
    return larger

# Reads the first/center/last positioned elements within array, sorts the 3, and returns the median element
def demo_median_of_three(unsorted_array, left_index, middle_index, right_index):
    if unsorted_array[right_index].line_length < unsorted_array[left_index].line_length:
        swap(unsorted_array, left_index, right_index)
    if unsorted_array[middle_index].line_length < unsorted_array[left_index].line_length:
        swap(unsorted_array, left_index, middle_index)
    if unsorted_array[right_index].line_length < unsorted_array[middle_index].line_length:
        swap(unsorted_array, middle_index, right_index)
    pivot = middle_index
    print("After: L: "+str(unsorted_array[left_index].line_length) +" Mid: "
    +str(unsorted_array[middle_index].line_length)+" R: "+str(unsorted_array[right_index].line_length))
    return pivot

# help from https://www.geeksforgeeks.org/merge-sort/
def merge_sort(unsorted_array):
    left_sub, right_sub = [], []
    # this creates base case for merge sort recursive call
    if len(unsorted_array) > 1:
        middle = (len(unsorted_array)) // 2
        # splitting unsorted array into subarrays is easy when using python's slicing!
        left_sub = unsorted_array[:middle]  #having no value for "x:middle" means it starts at the beginning of array
        right_sub = unsorted_array[middle:] #having no value for "middle:x" means it ends at the end of array
        merge_sort(left_sub)
        merge_sort(right_sub)

        # at this point, merging subarrays begins (adding smallest element from sub, into merge arr)
        left_sub_index, right_sub_index, merge_sub_index = 0,0,0
        while(left_sub_index < len(left_sub)) and (right_sub_index < len(right_sub)):
            if left_sub[left_sub_index] < right_sub[right_sub_index]:
                unsorted_array[merge_sub_index] = left_sub[left_sub_index]
                left_sub_index = left_sub_index + 1
            else:
                unsorted_array[merge_sub_index] = right_sub[right_sub_index]
                right_sub_index = right_sub_index + 1
            merge_sub_index = merge_sub_index + 1

        #while loop above exits when one array is emptied. This while loop adds any remaining elements to merge arr
        while (left_sub_index < len(left_sub)):
            unsorted_array[merge_sub_index] = left_sub[left_sub_index]
            left_sub_index = left_sub_index + 1
            merge_sub_index = merge_sub_index + 1
        while (right_sub_index < len(right_sub)):
            unsorted_array[merge_sub_index] = right_sub[right_sub_index]
            right_sub_index = right_sub_index + 1
            merge_sub_index = merge_sub_index + 1

def demo_merge_sort():
    global current_array
    global visualizer_dim
    global delay

    demo_merge_sort_recursive(current_array)

def demo_merge_sort_recursive(unsorted_array):
    global current_array
    global visualizer_dim
    global delay

    left_sub, right_sub = [], []
    # this creates base case for merge sort recursive call
    if len(unsorted_array) > 1:
        middle = (len(unsorted_array)) // 2
        # splitting unsorted array into subarrays is easy when using python's slicing!
        left_sub = unsorted_array[:middle]  #having no value for "x:middle" means [start, middle)
        right_sub = unsorted_array[middle:] #having no value for "middle:x" means [middle, end]

        demo_merge_sort_recursive(left_sub)
        demo_merge_sort_recursive(right_sub)

        # at this point, merging subarrays begins (adding smallest element from sub, into merge arr)
        left_sub_index, right_sub_index, merge_sub_index = 0,0,0
        while(left_sub_index < len(left_sub)) and (right_sub_index < len(right_sub)):
            if left_sub[left_sub_index].line_length < right_sub[right_sub_index].line_length:
                unsorted_array[merge_sub_index] = left_sub[left_sub_index]
                left_sub_index = left_sub_index + 1
            else:
                unsorted_array[merge_sub_index] = right_sub[right_sub_index]
                right_sub_index = right_sub_index + 1
            merge_sub_index = merge_sub_index + 1

            display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
            draw_element_array_comparison(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3], 0, merge_sub_index)
            draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
            time.sleep(delay)

        #while loop above exits when one array is emptied. This while loop adds any remaining elements to merge arr
        while (left_sub_index < len(left_sub)):
            unsorted_array[merge_sub_index] = left_sub[left_sub_index]
            left_sub_index = left_sub_index + 1
            merge_sub_index = merge_sub_index + 1

            display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
            draw_element_array_comparison(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3], 0, merge_sub_index)
            draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
            time.sleep(delay)

        while (right_sub_index < len(right_sub)):
            unsorted_array[merge_sub_index] = right_sub[right_sub_index]
            right_sub_index = right_sub_index + 1
            merge_sub_index = merge_sub_index + 1

            display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
            draw_element_array_comparison(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3], 0, merge_sub_index)
            draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
            time.sleep(delay)

        if(len(unsorted_array) == len(current_array)):
            for n in range(len(unsorted_array)):
                print(unsorted_array[n].line_length)
            current_array = unsorted_array
            display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
            draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
            draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
            draw_outline((visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3]))
            print("B")
            time.sleep(delay)

def heap_sort():
    print("heap")
def demo_heap_sort():
    print("heap")

def draw_element_array(x, y, width, height):
    global current_array
    width_var = (width / len(current_array))
    height_var = (height/ len(current_array))
    adjustment_var = (width / (2 * len(current_array)))
    index = 1
    for element in current_array:
        element_rect = pygame.Rect(x + (index * width_var), y + height, width / len(current_array), (height_var * element.line_length))
        element_rect.midbottom = x + (index * width_var) - adjustment_var ,(y + height)
        pygame.draw.rect(display, black, element_rect, 3)
        pygame.display.update()
        index = index + 1

def draw_element_array_comparison(x, y, width, height, comparison_a, comparison_b):
    global current_array
    width_var = (width / len(current_array))
    height_var = (height/ len(current_array))
    adjustment_var = (width / (2 * len(current_array)))
    index = 1
    for element in current_array:
        if index == comparison_a:
            element_rect = pygame.Rect(x + (index * width_var), y + height, width / len(current_array), (height_var * element.line_length))
            element_rect.midbottom = x + (index * width_var) - adjustment_var ,(y + height)
            pygame.draw.rect(display, blue, element_rect, 0)
        elif index == comparison_b:
            element_rect = pygame.Rect(x + (index * width_var), y + height, width / len(current_array), (height_var * element.line_length))
            element_rect.midbottom = x + (index * width_var) - adjustment_var ,(y + height)
            pygame.draw.rect(display, red, element_rect, 0)
        else:
            element_rect = pygame.Rect(x + (index * width_var), y + height, width / len(current_array), (height_var * element.line_length))
            element_rect.midbottom = x + (index * width_var) - adjustment_var ,(y + height)
            pygame.draw.rect(display, black, element_rect, 3)
        pygame.display.update()
        index = index + 1

def initial_build():
    global original_array
    global current_array
    global visualizer_dim
    global visualizer_array_size
    element_array = build_line_array(visualizer_array_size)
    original_array = element_array.copy()
    current_array = element_array
    random.shuffle(element_array)
    draw_outline(visualizer_dim)

def draw_outline(dimensions):
    x, y, width, height = dimensions[0], dimensions[1], dimensions[2], dimensions[3]
    rectangle = [(x,y) , (x + width, y), (x+width , y+height), (x , y+height)]
    pygame.draw.lines(display, black,True,rectangle, 3)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def retrieve_best_case(array_size):
    global sorting_algo
    best_case_array = []
    if(sorting_algo == 1):
        #best case for insertion sort is a fully sorted array
        for value in range(array_size):
            best_case_array.append(value)
        return best_case_array
    if(sorting_algo == 2):
        #best case for selection sort is same as worst case, but without swaps. so also sorted.
        for value in range(array_size):
            best_case_array.append(value)
        return best_case_array
    if(sorting_algo == 3):
        #best case for quick sort is a sorted array (pivot will be 50)
        for value in range(array_size):
            best_case_array.append(value)
        return best_case_array
    if(sorting_algo == 4):
        #best case for quick sort is a sorted array (pivot will be 50)
        for value in range(array_size):
            best_case_array.append(value)
        return best_case_array

def retrieve_worst_case(array_size):
    global sorting_algo
    worst_case_array = []
    if(sorting_algo == 1):
        #worst case for insertion sort is a inversely sorted array
        for value in range(array_size):
            worst_case_array.insert(0,value)
        return worst_case_array
    if(sorting_algo == 2):
        #worst case for selection sort is same as best case, but with swaps. so also inversely sorted.
        for value in range(array_size):
            worst_case_array.insert(0,value)
        return worst_case_array
    if(sorting_algo == 3):
        #worst case for merge sort is when each pair leads to a swap
        for value in range(array_size):
            worst_case_array.append(value)
        worst_case_array = merge_scramble(worst_case_array)
        return worst_case_array
    if(sorting_algo == 4):
        #current worst case is when median of three pivot is the second to smallest/largest elements
        for value in range(array_size):
            worst_case_array.append(value)
        #for value in range(len(worst_case_array)):
        #    print(worst_case_array[value])
        left, right, = 0, len(worst_case_array) - 1
        middle = right - left // 2
        while(right - left >= 4):
            #swap middle element with second to first
            swap(worst_case_array, middle, left + 1)
            left = left + 2
            middle = right - left // 2
        #for value in range(len(worst_case_array)):
        #    print(worst_case_array[value])
        return worst_case_array

# helper method that inversely builds worst case
# (help from https://stackoverflow.com/questions/24594112/when-will-the-worst-case-of-merge-sort-occur)
def merge_scramble(sorted_array):
    if len(sorted_array) == 1:
        return sorted_array
    #swap the sorted array to become unsorted
    if len(sorted_array) == 2:
        swap(sorted_array, 0, 1)
    i, j = 0,0
    middle = (len(sorted_array) + 1) // 2
    left_sub, right_sub = [], []
    # splitting unsorted array into subarrays is easy when using python's slicing!
    left_sub = sorted_array[:middle]  #having no value for "x:middle" means it starts at the beginning of array
    right_sub = sorted_array[middle:] #having no value for "middle:x" means it ends at the end of array

    while(i < len(sorted_array)):
        left_sub[j] = sorted_array[i]
        i = i + 2
        j = j + 1

    i, j = 1,0
    while(i < len(sorted_array)):
        right_sub[j] = sorted_array[i]
        i = i + 2
        j = j + 1

    merge_scramble(left_sub)
    merge_scramble(right_sub)
    merge(sorted_array, left_sub, right_sub)
    return sorted_array

def merge(sorted_array, left_sub, right_sub):
    i, j = 0,0
    while(i < len(left_sub)):
        sorted_array[i] = left_sub[i]
        i = i + 1
    while(j < len(right_sub)):
        sorted_array[i] = right_sub[j]
        j = j + 1
        i = i + 1

def retrieve_avg_case(array_size):
    average_case_array = []
    for value in range(array_size):
        average_case_array.append(value)
    random.shuffle(average_case_array)
    return average_case_array

def sorting_switch(integer):
    #print(integer)
    switcher = {
    1: demo_insertion_sort,
    2: demo_selection_sort,
    3: demo_merge_sort,
    4: demo_quick_sort,
    5: demo_heap_sort,
    }
    switcher[integer]()

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

def record_sorting_time(unsorted_array, case):
    global sorting_algo
    global worst_times
    global avg_times
    global best_times
    if(sorting_algo == 1):
        sort_time_start = time.time() - start_time
        insertion_sort(unsorted_array)
        sort_time_end = time.time() - start_time
        if(case == 0):
            worst_times.append(sort_time_end - sort_time_start)
        elif(case == 1):
            avg_times.append(sort_time_end - sort_time_start)
        else:
            best_times.append(sort_time_end - sort_time_start)
    if(sorting_algo == 2):
        sort_time_start = time.time() - start_time
        selection_sort(unsorted_array)
        sort_time_end = time.time() - start_time
        if(case == 0):
            worst_times.append(sort_time_end - sort_time_start)
        elif(case == 1):
            avg_times.append(sort_time_end - sort_time_start)
        else:
            best_times.append(sort_time_end - sort_time_start)
    if(sorting_algo == 3):
        sort_time_start = time.time() - start_time
        merge_sort(unsorted_array)
        sort_time_end = time.time() - start_time
        if(case == 0):
            worst_times.append(sort_time_end - sort_time_start)
        elif(case == 1):
            avg_times.append(sort_time_end - sort_time_start)
        else:
            best_times.append(sort_time_end - sort_time_start)
    if(sorting_algo == 4):
        sort_time_start = time.time() - start_time
        quick_sort(unsorted_array)
        sort_time_end = time.time() - start_time
        if(case == 0):
            worst_times.append(sort_time_end - sort_time_start)
        elif(case == 1):
            avg_times.append(sort_time_end - sort_time_start)
        else:
            best_times.append(sort_time_end - sort_time_start)

def main_loop():

    global pause_UI
    global sorting_algo
    global current_array
    global n_factor
    global trial_count
    global visualizer_array_size
    global worst_times
    global avg_times
    global best_times
    exit_request = False
    x = []
    draw_sort_buttons()
    draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])

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
                        new_array = build_line_array(visualizer_array_size)
                        random.shuffle(new_array)
                        current_array = new_array
                        display.fill(white, (visualizer_dim[0]+1,visualizer_dim[1]+1,visualizer_dim[2]-2,visualizer_dim[3]-2))
                        draw_element_array(visualizer_dim[0],visualizer_dim[1],visualizer_dim[2],visualizer_dim[3])
                    if pygame.mouse.get_pos()[0] >= 855 and pygame.mouse.get_pos()[0] < 1026:
                        print("example button for stats")
                        # find time cost for sorting arrays of increasing size (max size determined by n_factor)
                        for index in range(1, n_factor):
                            best_case = retrieve_best_case(int(math.pow(10, index)))
                            worst_case = retrieve_worst_case(int(math.pow(10, index)))
                            avg_case = retrieve_avg_case(int(math.pow(10, index))) #int(1000 * index)
                            x.append(int(math.pow(10, index)))
                            # run test on the same sized array x number of times (where x = trial_count)
                            for trial in range(trial_count):
                                record_sorting_time(best_case, 2)
                                record_sorting_time(avg_case, 1)
                                record_sorting_time(worst_case, 0)
                                # remove all time trials for same sized array and replace with 1 average time
                                if len(best_times) == (index - 1) + trial_count:
                                    sum_time = 0
                                    for sum_count in range(trial_count):
                                        removed_element = best_times.pop(-1)
                                        sum_time = sum_time + removed_element
                                    best_times.append(sum_time / trial_count)
                                    sum_time = 0
                                    for sum_count in range(trial_count):
                                        removed_element = avg_times.pop(-1)
                                        sum_time = sum_time + removed_element
                                    avg_times.append(sum_time / trial_count)
                                    sum_time = 0
                                    for sum_count in range(trial_count):
                                        removed_element = worst_times.pop(-1)
                                        sum_time = sum_time + removed_element
                                    worst_times.append(sum_time / trial_count)

                            print_val = len(best_times)
                            print(print_val)
                            print("best at " + str(index)+ " " + str(best_times[print_val - 1]))
                            print("avg at " + str(index)+ " " +  str(avg_times[print_val - 1]))
                            print("worst at " + str(index)+ " " +  str(worst_times[print_val - 1]))
                        print(len(x))
                        print(len(best_times))
                        plt.plot(x, best_times, label = "Best case")
                        plt.plot(x, avg_times, label = "Average case")
                        plt.plot(x, worst_times, label = "Worst case")

                        plt.xlabel("Elements within list")
                        plt.ylabel("Time elapsed in seconds")
                        plt.legend()
                        if(sorting_algo == 1):
                            plt.title("Complexity of Insertion Sort")
                        if(sorting_algo == 2):
                            plt.title("Complexity of Selection Sort")
                        if(sorting_algo == 3):
                            plt.title("Complexity of Merge Sort")
                        if(sorting_algo == 4):
                            plt.title("Complexity of Quick Sort")
                        if(sorting_algo == 5):
                            plt.title("Complexity of Heap Sort")
                        plt.show()
                        best_times = []
                        avg_times = []
                        worst_times = []
                        x = []
        pygame.display.update()

        print("--- %s seconds ---" % (time.time() - start_time))
display.fill(white)
initial_build()
main_loop()
pygame.quit()
quit()
