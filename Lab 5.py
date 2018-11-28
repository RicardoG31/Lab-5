# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:15:44 2018

@author: rgodoy
"""
# Course: CS2302
# Author: Ricardo Godoy
# Assignment: Lab 5 A
# T.A: Saha, Manoj
# Instructor: Diego Aguirre
# Date of last modification: 11/27/18

#The purpose of this lab is to implement a Min Heap. This program reads a text file with numbers
#separated by a coma, inserts them into a Heap, and sorts them accordingly.
            
class MinHeap:

    def __init__(self):
        self.heap_array = []
        
    def insert(self, k):
        # add the new value to the end of the array.
        print("insert(%d):" % k)
        self.heap_array.append(k)
        
        # percolate up from the last index to restore heap property.
        self.percolate_up(len(self.heap_array) - 1)  
        
        
        
    def percolate_up(self, node_index):
        while node_index > 0:
            # compute the parent node's index
            parent_index = (node_index - 1) // 2
            
            # check for a violation of the min heap property
            if self.heap_array[node_index] >= self.heap_array[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                print("   percolate_up() swap: %d <-> %d" % (self.heap_array[parent_index], self.heap_array[node_index]))
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                
                # continue the loop from the parent node
                node_index = parent_index
                
    def extract_min(self):
        if len(self.heap_array) < 0:
            return None 
        # save the min value from the root of the heap.
        min_elem = self.heap_array[0]
        
        # move the last item in the array into index 0.
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value
            
            # percolate up to restore min heap property.
            self.percolate_up(0)
                
        # return the min value
        print("Min element: ", min_elem)
        return min_elem


#Percolates down the elements on the min heap   
def min_heap_percolate_down(node_index, heap_list, list_size):
    child_index = 2 * node_index + 1
    value = heap_list[node_index]

    while child_index < list_size:
        # Find the max among the node and all the node's children
        min_value = value
        min_index = -1
        i = 0
        while i < 2 and i + child_index < list_size:
            if heap_list[i + child_index] > min_value:
                min_value = heap_list[i + child_index]
                min_index = i + child_index
            i = i + 1
                                    
        if min_value == value:
            return

        # Swap heap_list[node_index] and heap_list[max_index]
        temp = heap_list[node_index]
        heap_list[node_index] = heap_list[min_index]
        heap_list[min_index] = temp
        
        node_index = min_index
        child_index = 2 * node_index + 1
        
# Reads file and inserts items into heap        
def read_file(filename, h, input_list):
    
    f = open(filename)
    file = f.readline()
    numbers = file.split(",")
    for number in numbers:
        input_list.append(number)
        h.insert(int(number))
        print('   --> array: %s\n' % h.heap_array)

    
            
# Sorts the list of numbers using the heap sort algorithm
def heap_sort(numbers):
    # Heapify numbers list
    i = len(numbers) // 2 - 1
    while i >= 0:
        min_heap_percolate_down(i, numbers, len(numbers))
        i = i - 1
                
    i = len(numbers) - 1
    while i > 0:
        # Swap numbers[0] and numbers[i]
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp

        min_heap_percolate_down(0, numbers, i)
        i = i - 1
        
        
def main():
    h = MinHeap()
    input_list = []
    filename = "HeapFile.txt"
    
    read_file(filename, h, input_list)
    
    print("Unsorted Array: ", input_list)
    print("Min Heap: ", h.heap_array)
    h.extract_min()
    
    
main()
        
