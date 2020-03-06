import cv2
import matplotlib.pyplot as plt

class debug():
    def __init__(self, torf = True, wholeSize = (20, 15), subNum = 10):
        self.enable = torf
        self.__debug_img_size = wholeSize
        self.__debug_img_num = subNum
    def initialize(self):
        self.__debug_num = 1
        self.fig = plt.figure(figsize=self.__debug_img_size)
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=0.05)
    def setWholeSize(wholeSize):
        self.__debug_img_size = wholeSize
    def setSubNum(subNum):
        self.__debug_img_num = subNum
    def draw(self, img, name, cmap = 'gray'):
        if self.enable == False:
            return
        self.ax = self.fig.add_subplot(1, self.__debug_img_num, self.__debug_num, xticks=[], yticks=[])
        self.__debug_num += 1
        self.ax.set_title(name)
        self.ax.imshow(img, cmap=cmap)
    def plot(self, img, name):
        if self.enable == False:
            return
        self.ax = self.fig.add_subplot(1, self.__debug_img_num, self.__debug_num, xticks=[], yticks=[])
        self.__debug_num += 1
        self.ax.set_title(name)
        self.ax.plot(img)    