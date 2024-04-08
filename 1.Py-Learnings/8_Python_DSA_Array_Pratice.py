# Python code to practice Dynamic Array

import ctypes

class LearnArray:

    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__creatArray(self.size)

    def __creatArray(self,capacity):
        #creates a ctype array with size capacity
        return (capacity*ctypes.py_object)()

    #Calling the Magic function to cal the length of array
    def __len__(self):
        return self.n

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

    def __getitem__(self, index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of Range'

    #Append the values to the list
    def append(self,item):
        #Check if the Array is empty
        if self.size == self.n:
            #resize
            self.__resize(self.size*2)

        #append value
        self.A[self.n] = item
        self.n = self.n + 1

    #Resize the array
    def __resize(self, new_cap):
        # create new array
        b = self.__creatArray(new_cap)
        # update the size with new cap
        self.size = new_cap

        #Copy the data of old array to new array
        for i in range(self.n):
            b[i] = self.A[i]
            # Reassign A with B
            self.A = b

    def pop(self):
        if self.n == 0:
            return 'Empty List'
        else:
            self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):

        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - Not in list'

    def insert(self,pos,item):
        if self.size == self.n:
            self.__resize(self.size * 2)

            for i in range(self.n,pos,-1):
                self.A[i] = self.A[i - 1]

            self.A[pos] == item
            self.n = self.n + 1


L = LearnArray()

print(len(L))

L.append('Rohan')

L.insert(0,'Naisha')
print(L)
