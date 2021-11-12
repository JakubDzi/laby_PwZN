import argparse
import numpy as np
from PIL import Image
from rich.progress import track

parser = argparse.ArgumentParser(description="Program wykonuje symulację modelu Isinga")
parser.add_argument('size', help='rozmiar siatki', type=int)
parser.add_argument('jval', help='wartość J', type=float)
parser.add_argument('beta', help='wartość beta', type=float)
parser.add_argument('bfld', help='wartość pola B', type=float)
parser.add_argument('number', help='ilość kroków symulacji', type=int)
parser.add_argument('-u', '--upa', help='początkowa gęstość spinów w górę (dom. 0,5)', type=float, default=0.5)
parser.add_argument('-f', '--file', help='nazwa pliku do zapisu (domyślnie step)', default="step")
parser.add_argument('-mf', '--magfile', help='nazwa pliku do zapisu magnetyzacji co krok (tylko jeśli nazwa jest podana)', default="")
parser.add_argument('-g', '--gifile', help='nazwa pliku do zapisu animacji (tylko jeśli nazwa jest podana)', default="")
args = parser.parse_args()

def hamilton(spins, jv, b):
    zwr=0
    for i in range(spins.shape[0]):
        for j in range(spins.shape[1]):
            zwr-=b*spins[(i,j)]
            if i>0:
                zwr-=jv*spins[(i,j)]*spins[(i-1,j)]
            if j>0:
                zwr-=jv*spins[(i,j)]*spins[(i,j-1)]
            if i<spins.shape[0]-1:
                zwr-=jv*spins[(i,j)]*spins[(i+1,j)]
            if j<spins.shape[1]-1:
                zwr-=jv*spins[(i,j)]*spins[(i,j+1)]
    return zwr

class Sim:
    def __init__(self, size, jvalue, beta, bfield, n, uparrow, file, magfile, hamilt, gifname):
        self.imgs=[]
        self.m=np.zeros(n)
        self.mgt=size**2
        self.size=size
        self.j=jvalue
        self.beta=beta
        self.b=bfield
        self.n=n
        self.dens=uparrow
        self.file=file
        self.spins=np.ones((size,size))
        limitgora=int((1-self.dens)*(self.size**2))
        for i in range(limitgora):
            chg=0
            while chg==0:
                x = np.random.randint(self.size)
                y = np.random.randint(self.size)
                if self.spins[(x,y)]==1:
                    self.spins[(x,y)]=-1
                    self.mgt += 2 * self.spins[(x, y)]
                    chg=1
        if magfile != "":
            self.mf=open(magfile+".txt", "w")
        h0 = hamilt(self.spins, self.j, self.b)
        #for step in track(range(self.n*(self.size**2))):
        for step in range(self.n * (self.size ** 2)):
            x = np.random.randint(self.size)
            y = np.random.randint(self.size)
            self.spins[(x, y)] *= -1
            h1 = hamilt(self.spins, self.j, self.b)
            self.spins[(x, y)] *= -1
            if (h1-h0)<0 or ((np.random.rand())<(np.exp(-(h1-h0)*self.beta))):
                self.spins[(x,y)] *= -1
                self.mgt+=2*self.spins[(x,y)]
                h0=h1
            if step%(self.size**2)==0:
                if magfile != "":
                    self.mf.write("Step "+str(int(step/(self.size**2))+1)+": ")
                    self.mf.write(str(self.mgt))
                    self.mf.write("\n")
                if self.size<100 and self.size>10:
                    obraz = np.zeros((self.size*10, self.size*10))
                    for i in range(self.size):
                        for j in range(self.size):
                            if self.spins[(i, j)] == 1:
                                for k in range(10):
                                    for l in range(10):
                                        obraz[(i*10+k, j*10+l)] = 255
                elif self.size<=10:
                    obraz = np.zeros((self.size * 100, self.size * 100))
                    for i in range(self.size):
                        for j in range(self.size):
                            if self.spins[(i, j)] == 1:
                                for k in range(100):
                                    for l in range(100):
                                        obraz[(i*100 + k, j*100 + l)] = 255
                else:
                    obraz = np.zeros((self.size, self.size))
                    for i in range(self.size):
                        for j in range(self.size):
                            if self.spins[(i, j)] == 1:
                                obraz[(i, j)] = 255
                im=Image.fromarray(obraz)
                im=im.convert('RGB')
                self.imgs.append(im)
                im.save(self.file+str(int(step/(self.size**2)))+".jpg")
        if gifname != "":
            self.imgs[0].save(fp=gifname+".gif", format='GIF', save_all=True, duration=0.1, loop=0, append_images=self.imgs)

symulacja = Sim(args.size, args.jval, args.beta, args.bfld, args.number, args.upa, args.file, args.magfile, hamilton, args.gifile)
