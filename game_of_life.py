
"""Game of life 1 is alive 0 is dead"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import copy
matplotlib.use('qt5agg')
import sys
import csv
from collections import Counter

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


    def iteration(self, i, j, arr):
        #condition for counting as to whether they are neighbours there
        count = 0
        for k, l in [(-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1)]:
            if arr[(i + k)%self.size][(j+l)%self.size]:
                count += 1
        return count

    def count_active_sites(self, arr):
        arr_l = arr.flatten().tolist()
        return arr_l.count(1)

    def method_for_rules(self, arra):
        array_init = copy.deepcopy(arra)
        for i in range(self.size):
            for j in range(self.size):
                count = self.iteration(i, j, arra)
                if (count < 2) & (arra[i, j] == 1):
                    array_init[i, j] = 0
                if (arra[i, j] == 1) & (count>3):
                    array_init[i, j] = 0
                if (arra[i, j] == 0) & (count == 3):
                    array_init[i, j] = 1
        return array_init

    def starting_array(self, type_arr):
        if type_arr == "random":
            array = self.array
        elif type_arr == "glider":
            array = self.glider()
        elif type_arr == "beehive":
            array = self.beehive()
        elif type_arr == "blinker":
            array = self.blinker()
        return array

    def calling_and_plotting(self, n):
        type_arr = input("Please give initial state: random, glider, beehive, blinker :")
        array = self.starting_array(type_arr)
        #array = self.array #for collecting plots
        fig, ax = plt.subplots()
        fig.canvas.mpl_connect("close_event", lambda x: sys.exit())

        b = 0
        a = []
        time = []

        for i in range(n): 
            array = self.method_for_rules(array)
            active_site = self.count_active_sites(array)
            ax.cla()   #clears the figure plot to plot the next animation
            ax.imshow(array, animated=True, cmap='Blues')  #animates the spin lattice
            fig.canvas.draw()
            plt.pause(0.01)

            #code for collecting com for glider
            #com = self.cente_of_massx(array)
            #coy = self.cente_of_massy(array)
            #f = open("com_glider.csv", "a+")
            #writer = csv.writer(f)
            #writer.writerow((i, com, coy))
            #f.close()

            """data for active sites and plots
            if active_site == b:
                a.append(active_site)
                time.append(i)

            b = active_site
        
        max = Counter(a)
        val = max.most_common()[0][0]
        ind = a.index(val)

        #f = open("active_time_f.csv", "a+")
        #writer = csv.writer(f)
        #writer.writerow((a[ind], time[ind]))
        #f.close()
        """

    def cente_of_massx(self, arr):
        #code for centre of mass of the glider/array
        s = 0 
        coord_list = []
        for i in range(0, (self.size)):
            for j in range(0, (self.size)):
                if arr[i,j] == 1:
                    coord_list.append([j,i])
                s += j*arr[i,j]
        no_active_site = self.count_active_sites(arr)
        x_c = s/no_active_site

        x_vals = []
        y_vals = []
        for i in range(len(coord_list)):
            x_vals.append(coord_list[i][0])
            y_vals.append(coord_list[i][1])
        xmax, xmin  = np.max(x_vals), np.min(x_vals)
        ymax, ymin = np.max(y_vals), np.min(y_vals)

        if (abs(xmax-xmin) > (self.size/2)) | (abs(ymax-ymin) > (self.size/2)): #accounts for boundary conditions
            return 0
        else:
            return x_c


    def cente_of_massy(self, arr):
        s = 0 
        coord_list = []
        for i in range(0, (self.size)):
            for j in range(0, (self.size)):
                if arr[i,j] == 1:
                    coord_list.append([j,i])
                s += i*arr[i,j]
        no_active_site = self.count_active_sites(arr)
        y_c = s/no_active_site

        x_vals = []
        y_vals = []
        for i in range(len(coord_list)):
            x_vals.append(coord_list[i][0])
            y_vals.append(coord_list[i][1])
        xmax, xmin  = np.max(x_vals), np.min(x_vals)
        ymax, ymin = np.max(y_vals), np.min(y_vals)

        if (abs(xmax-xmin) > (self.size/2)) | (abs(ymax-ymin) > (self.size/2)):
            return 0
        else:
            return y_c

def main():
    ini_size = input("give size: ")
    game_life = Game_of_life(int(ini_size))
    game_life.calling_and_plotting(2500)

main()