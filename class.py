import os
import random
from scipy import ndarray
# image processing library
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io
class ImageAugment():
    # dictionary of the transformations we defined earlier
    self.available_transformations = {
        'rotate': self.random_rotation,
        'noise': self.random_noise,
        'horizontal_flip': self.horizontal_flip
    }
    def __init__ (self, root='.',num_files_desired=10):
        self.root = root
        self.num_files_desired = num_files_desired
    def random_rotation(self, image_array: ndarray):
        # pick a random degree of rotation between 25% on the left and 25% on the right
        random_degree = random.uniform(-25, 25)
        return sk.transform.rotate(image_array, random_degree)

    def random_noise(self, image_array: ndarray):
        # add random noise to the image
        return sk.util.random_noise(image_array)

    def horizontal_flip(self, image_array: ndarray):
        # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
        return image_array[:, ::-1]
    def augment(self, image_path):
        # find all files paths from the folder
        img_name = image_path.split('/')[-1]
        folder_path = image_path.split('/')[:-1]
        folder_path = '/'.join(folder_path)
        print(f'loaded {image_path}')
        num_generated_files, num_files_desired = 0, 10
        try:
            image_to_transform = sk.io.imread(image_path)
            while num_generated_files < num_files_desired:
                # random num of transformation to apply
                num_transformations_to_apply = random.randint(1, len(available_transformations))

                num_transformations = 0
                transformed_image = image_to_transform
                while num_transformations <= num_transformations_to_apply:
                    # random transformation to apply for a single image
                    key = random.choice(list(available_transformations))
                    print(f"iter :{num_transformations} {key}")
                    transformed_image = available_transformations[key](transformed_image)
                    num_transformations += 1
                new_file_path = f'{folder_path}/{img_name}_{num_generated_files}.png'

                # write image to the disk
                io.imsave(new_file_path, transformed_image)
                num_generated_files += 1
    def DFS(self, self.root, dirCallback = None, fileCallback = None):
        stack = []
        ret = []
        stack.append(self.root);
        while len(stack) > 0:
            tmp = stack.pop(len(stack) - 1)
            if(os.path.isdir(tmp)):
                ret.append(tmp)
                for item in os.listdir(tmp):
                    stack.append(os.path.join(tmp, item))
                if dirCallback:
                    dirCallback(tmp)
            elif(os.path.isfile(tmp)):
                ret.append(tmp)
                if fileCallback:
                    fileCallback(tmp)
        return ret
if __name__ == '__main__':
            a = ImageAugment()
