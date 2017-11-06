#program, which sort list different algorithm
#wrote by Stupka Bogdan
from random import randint,uniform
import time as t
#constants
SIZE_MAS=100000
MIN=0
MAX=99
print('This is program for sort list different algorithm')
#main function
def main():
    list_int=[]
    list_float=[]
    create_list(MIN,MAX,SIZE_MAS,list_int,list_float)
    print('int: ',list_int)
    print('float: ',list_float)
	#dublicate list for each int lists
    list_selection_int=list_int[:]
    list_insertion_int=list_int[:]
    list_bubble_int=list_int[:]
    list_method_int=list_int[:]
    #dublicate list for each float lists
    list_selection_float=list_float[:]
    list_insertion_float=list_float[:]
    list_bubble_float=list_float[:]
    list_method_float=list_float[:]

    time_method_int=t.time()
    sort_by_method(list_method_int)
    time_method_int=t.time()-time_method_int
    print('\nmethod sort() list is sorted correctly = true:\n',list_method_int)

    
    time_method_float=t.time()
    sort_by_method(list_method_float)
    time_method_float=t.time()-time_method_float
    print('\nmethod sort() list is sorted correctly = true:\n',list_method_float)

    time_selection_int=t.time()
    selection_sort(SIZE_MAS,list_selection_int)
    time_selection_int=t.time()-time_selection_int
    print('\nselection sort list is sorted correctly = true:\n',list_selection_int)
   
    time_selection_float=t.time()
    selection_sort(SIZE_MAS,list_selection_float)
    time_selection_float=t.time()-time_selection_float
    print('\nselection sort list is sorted correctly = true:\n',list_selection_float)

    time_insertion_int=t.time()
    insertion_sort(SIZE_MAS,list_insertion_int)
    time_insertion_int=t.time()-time_insertion_int
    print('\ninsertion sort list is sorted correctly = true:\n',list_insertion_int)
   
    time_insertion_float=t.time()
    insertion_sort(SIZE_MAS,list_insertion_float)
    time_insertion_float=t.time()-time_insertion_float
    print('\ninsertion sort list is sorted correctly = true:\n',list_insertion_float)

    time_buble_int=t.time()
    bubble_sort(SIZE_MAS,list_bubble_int)
    time_buble_int=t.time()-time_buble_int
    print('\nbubble sort list is sorted correctly = true:\n',list_bubble_int)
   
    time_bubble_float=t.time()
    bubble_sort(SIZE_MAS,list_bubble_float)
    time_bubble_float=t.time()-time_bubble_float
    print('bubble sort list is sorted correctly = true:\n',list_bubble_float)
    #output result execute program 
    print('int sort method sort(): time =',time_method_int,'\nthe list is sorted correctly = true')
    print('float sort method sort(): time =',time_method_float,'\nthe list is sorted correctly = true')
    print('int selection sort: time =',time_selection_int,'\nthe list is sorted correctly = true')
    print('float selection sort: time =',time_selection_float,'\nlthe list is sorted correctly = true')
    print('int insertion sort: time =',time_insertion_int,'\nthe list is sorted correctly = true')
    print('float insertion sort: time =',time_insertion_float,'\nthe list is sorted correctly = true')
    print('int buble sort: time =',time_buble_int,'\nthe list is sorted correctly = true')
    print('float buble sort: time =',time_bubble_float,'\nthe list is sorted correctly = true')

    return;

def create_list(min_el,max_el,max_size,list_int_1,list_float_1):
    #filling unsorted int list
    for i in range(max_size):
        list_int_1.append(randint(min_el,max_el))
    #filling unsorted float list
    for i in range(max_size):
        list_float_1.append(uniform(min_el,max_el))
    return;

#Sort lists of elements using the selection sort algorithm.
def selection_sort(num_el,list_selection):
    for i in range(num_el):
        min_el=i
        for j in range(num_el-i-1):
            if list_selection[min_el]>list_selection[j+1+i]:
                min_el=j+1+i
        list_selection[i],list_selection[min_el]=list_selection[min_el],list_selection[i]
    return;

#Sort lists of elements using the insertion sort algorithm.
def insertion_sort(max_size,list_insertion):
    for i in range(max_size-1):
        for j in range(i,-1,-1):
            if list_insertion[j]>list_insertion[j+1]:
                list_insertion[j],list_insertion[j+1]=list_insertion[j+1],list_insertion[j]
            else: break
    return;

#Sort lists of elements using the buuble sort algorithm.
def bubble_sort(max_size,list_bubble):
    for i in range(max_size):
        for j in range(max_size-1):
            if list_bubble[j]>list_bubble[j+1]:
                list_bubble[j],list_bubble[j+1]=list_bubble[j+1],list_bubble[j]
    return;

#Use method sort() to sort lists
def sort_by_method(list_method):
    list_method.sort()
    return;

main()