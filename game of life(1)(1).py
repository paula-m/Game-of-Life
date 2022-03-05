
"""Game of life 1 is alive 0 is dead"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import copy
#from matplotlib.animation import FuncAnimation
matplotlib.use('qt5agg')
import sys

class Game_of_life():
    def __init__(self, size_n):
        self.size = size_n
        self.array = np.random.randint(0,2,size=(self.size,self.size))

    def glider(self):
        arr = np.zeros((self.size,self.size))
        arr[1, 1], arr[2, 2], arr[3,0], arr[3, 1], arr[3,2] = 1, 1, 1, 1, 1
        return arr
    
    def beehive(self):
        arr = np.zeros((self.size,self.size))
        arr[1,4], arr[2,5], arr[3,5], arr[4, 4], arr[3, 3], arr[2, 3] = 1, 1, 1, 1, 1, 1
        return arr

    def blinker(self):
        arr = np.zeros((self.size,self.size))
        arr[2, 2], arr[2, 3], arr[2, 4] = 1, 1,1
        return arr


    def iterate_over_array(self, i, j, array):
        counter = 0
        if (array[(i+1)%self.size, j] == 1):
            counter +=1
        if (array[(i-1)%self.size, j] == 1):
            counter += 1
        if array[i, (j + 1)%self.size] == 1:
            counter += 1
        if (array[i, (j - 1)%self.size] == 1):
            counter += 1
        if (array[(i-1)%self.size, (j - 1)%self.size] == 1):
            counter += 1
        if (array[(i-1)%self.size, (j + 1)%self.size] == 1):
            counter += 1
        if (array[(i+1)%self.size, (j + 1)%self.size] == 1):
            counter += 1
        if (array[(i+1)%self.size, (j - 1)%self.size] == 1):
            counter += 1
        return counter

    def try_something_werid(self, small_lat):
        ar = list(small_lat)
        count = ar.count(1)
        print(count)
        return count
        

    def method_for_rules(self, arra):
        array_init = copy.deepcopy(arra)
        for i in range(self.size):
            for j in range(self.size):
                #small_ar = arra[(i-1) : (i+2), (j-1) : (j+2)]
                #print(small_ar)
                #count = self.try_something_werid(small_ar)
                count = self.iterate_over_array(i, j, arra)
                if (count < 2) & (arra[i, j] == 1):
                    array_init[i, j] = 0
                if (arra[i, j] == 1) & (count>3):
                    array_init[i, j] = 0
                if (arra[i, j] == 0) & (count == 3):
                    array_init[i, j] = 1
                
        return array_init

        
    def calling_stuff(self):
        #array = self.array
        #array = self.glider()
        array = self.beehive()
        #array = self.blinker()
        fig, ax = plt.subplots()
        fig.canvas.mpl_connect("close_event", lambda x: sys.exit())

        for i in range(1000): 
            array = self.method_for_rules(array)
            ax.cla()   #clears the figure plot to plot the next animation
            ax.imshow(array, animated=True, cmap='Blues')  #animates the spin lattice
            fig.canvas.draw()
            plt.pause(0.01)


def main():
    game_life = Game_of_life(10)
    game_life.calling_stuff()
main()