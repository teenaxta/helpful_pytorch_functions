import os
import numpy as np
from torch.utils.data import Dataset
from glob import glob
from PIL import Image


class ImageFolderwithPaths(Dataset):

    def __init__(self, path, transform=None):
        self.classes = os.listdir(path)
        self.classes_num = np.arange(len(self.classes))
        self.paths = glob(path+'*')

        self.labels = []
        self.files_path = []
        labels_counter = 0
        self.files_path = glob(path+'/**/*')
        self.tranform = transform

        for path in self.paths:
            img_paths = glob(path+'/*')
            self.labels+= [labels_counter]*len(img_paths)
            labels_counter+=1

    def __getitem__(self, index):
        image = Image.open(self.files_path[index]).convert('RGB')
        if self.tranform != None:
            image = self.tranform(image)
        
        return image, self.labels[index], self.files_path[index]

    def __len__(self):
        if len(self.labels) == len(self.files_path):
            return len(self.labels)
        else:
            print('Number of labels and images is not equal')
