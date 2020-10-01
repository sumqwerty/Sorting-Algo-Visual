import pygame as pg
import random
import time
from os import path

WIDTH = 1000
HEIGHT = 700



BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
CYAN = (0,255,255)
GREEN = (19, 255, 8)
A_GREEN = (0,255,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)

BGCOLOR = BLACK

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.gameOver = False
        pg.display.set_caption("Sorting Algo")
        self.arr = []
        self.number = 100
        self.interval = int(WIDTH / self.number)
        self.generateRandom()
        game_folder = path.dirname(__file__)
        self.butn_font = path.join(game_folder, 'OpenSans_Semibold.ttf')


    def generateRandom(self):
        self.arr = random.sample(range(1,500),self.number)

    def shuffle(self):
        random.shuffle(self.arr)


##############################################################################################################
    def bars(self,coli,colj,colMin):
        color = (0,255,0)
        for i in range(0,len(self.arr)):
            if i == coli:
                color = (255,0,0)
            elif i == colj:
                color = (0,0,255)
            elif i == colMin:
                color = (255,0,255)
            else:
                color = (0,255,0)
                
            pg.draw.rect(self.screen,color,(i*self.interval,HEIGHT-self.arr[i],self.interval-5,self.arr[i]))


    def selectionSort(self):
        for i in range(0, len(self.arr)):
            min_index = i
            
            for j in range(i+1, len(self.arr)):
                
                if(self.arr[j] < self.arr[min_index]):
                    min_index = j                
                self.draw(i,j,min_index)


            if min_index != i:                
                self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]



    def bubbleSort(self):
        for i in range(0,len(self.arr)):
            flag = False
            for j in range(0,len(self.arr)-i-1):
                if self.arr[j] > self.arr[j+1]:
                    flag = True
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

                self.draw(j,j+1,-1)
                #time.sleep(0.01)
            if not flag:
                break


    def insertionSort(self):

        for i in range(1,len(self.arr)):
            j = i            
            while(self.arr[j] < self.arr[j-1] and j > 0):
                self.draw(j,j-1,i)
                self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]
                j -= 1


    def mergeSort(self):
        current_size = 1 
        while current_size < len(self.arr) - 1:
            left = 0
            while left < len(self.arr)-1:  
                mid = min((left + current_size - 1),(len(self.arr)-1)) 
 
                right = ((2 * current_size + left - 1,  
                        len(self.arr) - 1)[2 * current_size  
                            + left - 1 > len(self.arr)-1])  
                
                # Merge call for each sub array  
                self.merge(left, mid, right)  
                self.draw(left,mid,right)
                #time.sleep(0.1)
                left = left + current_size*2                
                  
            # Increasing sub array size by  
            # multiple of 2  
            current_size = 2 * current_size


    # Merge Function
    def merge(self,l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1): 
            L[i] = self.arr[l + i] 
        for i in range(0, n2): 
            R[i] = self.arr[m + i + 1] 

        i, j, k = 0, 0, l
        while i < n1 and j < n2: 
            if L[i] > R[j]: 
                self.arr[k] = R[j] 
                j += 1
            else: 
                self.arr[k] = L[i] 
                i += 1
                
            self.draw(l+i,m+1+j,r+k)
            k += 1

        while i < n1:
            self.arr[k] = L[i] 
            self.draw(l+i,m+1+j,r+k)
            i += 1
            k += 1

        while j < n2: 
            self.arr[k] = R[j]
            self.draw(l+i,m+1+j,r+k)
            j += 1
            k += 1




    def partn(self,low,high):
        i = low
        j = low

        pvt = self.arr[high]

        while(j<high):

            if self.arr[j] < pvt:
                self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
                i += 1
            j += 1
            
            self.draw(i,j,-1)


        self.arr[i], self.arr[high] = self.arr[high], self.arr[i]
        self.draw(i,j,-1)
        return i


    def quick_sort(self,low,high):
        if low < high:
            pi = self.partn(low,high)

            self.quick_sort(low,pi-1)
            self.quick_sort(pi+1,high)

        
    def quickSort(self):
        self.quick_sort(0,len(self.arr)-1)



    def heapify(self,sz):
        flag = False

        for i in range(1,sz+1):
            if i%2 != 0:
                j = i
                while(j > 0 and self.arr[j] > self.arr[(j-1)//2] ):
                    self.arr[j], self.arr[(j-1)//2] = self.arr[(j-1)//2], self.arr[j]
                    self.draw(i,j,(j-1)//2)
                    j = (j//2)-1
                    flag = True
            else:
                j = i
                while(j > 0 and self.arr[j] > self.arr[(j-2)//2]):
                    self.arr[j], self.arr[(j-2)//2] = self.arr[(j-2)//2], self.arr[j]
                    self.draw(i,j,(j-1)//2)
                    j = (j//2) - 1
                    flag = True

        if flag:
            self.heapify(sz-1)

        return


    def heap_sort(self,sz):
        if sz == 0:
            return

        self.heapify(sz)

        self.arr[0],self.arr[sz] = self.arr[sz],self.arr[0]
        #self.draw(self.arr[0],self.arr[sz],-1)
        self.heap_sort(sz-1)

    def heapSort(self):
        self.heap_sort(len(self.arr)-1)
    

##############################################################################################################



    def drawButton(self,x,y,w,h,p_color,a_color,function,text,sz):
        smallfont = pg.font.Font(self.butn_font, sz)
        txt = smallfont.render(text, True, BLACK)
        cur = pg.mouse.get_pos()
        pg.draw.rect(self.screen,p_color,(x,y,w,h))
        if x+w > cur[0] > x and y + h > cur[1] > y:
            pg.draw.rect(self.screen,a_color,(x,y,w,h))
            click = pg.mouse.get_pressed()
            if click[0] == 1:
                ev = pg.event.wait()
                function()
        self.screen.blit(txt,[x+5,y])



    def draw(self,i,j,m):
        self.screen.fill(BGCOLOR)

        self.drawButton(10,10,145,50,YELLOW,A_GREEN,self.insertionSort,"Insertion",30)
        self.drawButton(175,10,140,50,YELLOW,A_GREEN,self.selectionSort,"Selection",30)
        self.drawButton(335,10,120,50,YELLOW,A_GREEN,self.bubbleSort,"Bubble",30)
        self.drawButton(475,10,100,50,YELLOW,A_GREEN,self.mergeSort,"Merge",30)
        self.drawButton(595,10,90,50,YELLOW,A_GREEN,self.heapSort,"Heap",30)


        self.drawButton(10,145,80,30,CYAN,RED,self.shuffle,"Shuffle",20)
        self.drawButton(105,145,210,30,CYAN,RED,self.generateRandom,"New Random Values",20)

        #drawing bars
        self.bars(i,j,m)

        pg.draw.line(self.screen,WHITE,(0,(HEIGHT-515)),(WIDTH,(HEIGHT-515)),3)
        pg.display.flip()
        
    
    def main(self):

        while not self.gameOver:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.generateRandom();
                        
                    if event.key == pg.K_s:
                        self.selectionSort()

                    if event.key == pg.K_z:
                        self.bubbleSort()

                    if event.key == pg.K_x:
                        self.insertionSort()
                        
                    if event.key == pg.K_c:
                        self.mergeSort()

                    if event.key == pg.K_q:
                        self.quickSort()

                    if event.key == pg.K_h:
                        self.heapSort()
                        
                    if event.key == pg.K_p:
                        print(self.arr);

            self.draw(-1,-1,-1)





g = Game()
g.main()
