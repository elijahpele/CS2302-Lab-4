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

class Node(object):
    word  = ""
    embeddings =[0.0]*50
    next = None

    
    # Constructor with a word parameter creates the Node object.
    def __init__(self, word):
        self.word = word
        self.embeddings = [0.0]*50
        self.next = None 
        
class HashTable:
    from Node import Node
    def __init__(self):
        self.hash_array = [None] *(26*26*26*26*26)
        self.number_of_items = 0
    
    # This hash function relies on the nodes variable node.word
    def hash(self, node):     
        hash_val = 0
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','x','z']
        (letter) = str(node.word[0])
        for i in range(len(alphabet)):
            if(letter == alphabet[i]):
                hash_val = i
                if(len(node.word) > 1):
                    hash_val = self.hash2(node, hash_val + 1)
        return hash_val

    
    def hash2(self, node, k):
        hash_val = 0
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','x','z']
        letter = node.word[1]
        for i in range(len(alphabet)):
            if(letter == alphabet[i]):
                hash_val = (k * 26) + i
                if(len(node.word) > 2):                    
                    hash_val = self.hash3(node, hash_val)
        return hash_val


    def hash3(self, node, k):
        hash_val = 0
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','x','z']
        letter = node.word[2]
        for i in range(len(alphabet)):
            if(letter == alphabet[i]):
                hash_val = k * 26 + i
                if(len(node.word) > 3):                    
                    hash_val = self.hash4(node, hash_val)       
        return hash_val


    def hash4(self, node, k):
        hash_val = 0
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','x','z']
        letter = node.word[3]
        for i in range(len(alphabet)):
            if(letter == alphabet[i]):
                hash_val = k * 26 + i       
        return hash_val   
    
    # This insert method solves collisions by chaining.
    def insert(self, node):
        new_insert = Node("")
        new_insert.word = node.word
        new_insert.embeddings = node.embeddings
        hash_val = self.hash(node)
        
        if(self.hash_array[hash_val] is None):
            self.hash_array[hash_val] = new_insert
            self.number_of_items += 1
            return
        
        # If the hash_array at that hash_val is not  empty
        else:
            prev = Node(None)
            temp = self.hash_array[hash_val]
            # If the hash_array at that hash_val has only one node in it.
            if(prev is None):
                new_insert.next = Node(None)
                new_insert.next = temp
                self.hash_array[0] = new_insert
                self.number_of_items += 1
                return
            
            while(temp.next is not None):
                if(new_insert.word < temp.word):
                    prev.next = Node(None)
                    new_insert.next  = Node(None)
                    prev.next = new_insert
                    new_insert.next = temp
                    self.number_of_items += 1
                    return 
                   
                prev = temp
                temp = temp.next
                    
            if(temp.next is None):
                temp.next = Node(None)
                temp.next = new_insert                  
                self.number_of_items += 1
            return
            
            
    # The load factor is defined as the number of items in the table divided by the size of the table.        
    def load_factor(self):
        l_factor = self.number_of_items/len(self.hash_array)
        float(l_factor)
        return l_factor