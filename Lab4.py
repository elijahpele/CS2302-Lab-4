# CS2302
# Elijah Pele
# Lab 4
#
# Instructor: Diego Aguirre
# TA: Manoj Pravaka Saha
# Last Modified: 11/23/2018
#
# The purpose of this lab is to optiimize the previous lab. In the previos lab we used trees to store nodes of data. 
# Instead of using trees we instead use a hash table. The value node.word is hashed to store the node in a given index inside of an array.
# In case of a collision we chain the nodes together using node.next. 

from lab4node import Node
from HashTable import HashTable

# First, each line from the file is stored in to a single element in an array.    
def read_file(file1):    
    array = []
    file = open(file1, encoding = 'utf-8')
    
    # Each word and  its emebeddings are stored in an array as a single string.
    for line in file:         
        array.append(line)
    head = create_Linked_List_from_File(array)
    return head


# Auxiliary method to read_file, the array is turned in to a linked list.
def create_Linked_List_from_File(array):    
    head = Node("")
    node = Node("")
    head = node
    
    # This array will be used to make sure we are only considering groups of alphabetic symbols that create words.
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range((len(array))):
        # The string is split among white spaces
        temp = array[i].split()
        
        # This boolean will turn to True if the given sybols create a word. 
        is_a_word = False
        
        # The element in the 0th position should represent a valid word. If it is not, we ignore it.        
        word = temp[0]
        for i in range(len(alphabet)):
            letter = word[0]
            if(letter == alphabet[i]):
                is_a_word = True
        
        # Since 'is_a_word' equals True, we assign it to a node and add it to the linked list. 
        if(is_a_word == True):
            node.word = temp[0]
            
            # The embeddings are then assigned to the nodes embedding array.
            for i in range(1, 51):
                node.embeddings[i-1] = float(temp[i])
            node.next = Node("")
            node = node.next 
    return head


# Main method
hash_table = HashTable()
head = read_file("glove.6B.50d.txt")
temp = head
while temp.next is not None:
    hash_table.insert(temp)
    temp = temp.next   
load_factor =  hash_table.load_factor()
print("Hash Table Load factor is " +str(load_factor))
print("Total nodes in table: " +str(hash_table.number_of_items))