#REQUIRED PACKAGES TO BE INSTALLED
#python 3.x
#matplotlib
#numpy
#pillow(support .jpg)

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def normlize_image(image , new_min , new_max):

        min = np.min(image)
        max = np.max(image)

        # create image with range new_min to new_max
        new_image = (new_max - new_min) * ((image-min)/(max-min)) + new_min

        return new_image

def padding_image(image , n_padd):

        ht , wd = image.shape
        hh , ww = ht + n_padd , wd + n_padd

        # compute center offset
        xx = (ww-wd)//2
        yy = (hh-ht)//2

        # create new image of desired size and color (black) for padding
        padded_image = np.zeros((hh,ww) , dtype=np.int32)

        # copy image into center of padded image
        padded_image[yy:yy+ht, xx:xx+wd] = image

        return padded_image

# convolution function 
# input: image , filter
# output: fitered image 
def convolution(image , filter):

        height_image , width_image = image.shape
        height_filter , width_filter = filter.shape

        filtered_image = np.zeros((height_image,width_image) , dtype=np.int32)

        # add padding to the image according to the filter size
        padded_image = padding_image(image , height_filter-1)

        # image convolution operation with filter
        for i in range(height_image):
                for j in range(width_image):
                        filtered_image[i][j] = filter.ravel().dot(padded_image[i:i+height_filter,j:j+width_filter].ravel())

        return filtered_image

if __name__ == "__main__":

        # title page
        print('\t\t************************************************')
        print('\t\t************************************************')
        print('\t\t*************** IMAGE PROCESSING ***************')
        print('\t\t************************************************')
        print('\t\t************************************************')
        print('\n')
        
        # get path image 
        path_image = input('Please,Enter the image path:').strip()

        # get filter size 
        size_filter = int(input('Please,Enter filter size:').strip())

        # get values filter and separating with Space
        values_filter = (input('Please,Enter filter values:').strip()).split(' ')

        # check 
        if len(values_filter) != pow(size_filter , 2):
               print('Error:')
               exit()
        else:
                # convert list to numpy array
                np_array= np.asarray(values_filter , dtype=np.float32)

                # reshape array(1,size_filter) to matrix(size_filter , size_filter)
                filter = np_array.reshape((size_filter , size_filter))

                # read image from path 
                original_image = mpimg.imread(path_image , 'r')


                # apply filters to the image with the convolution function
                filtered_image = convolution(original_image ,filter)

                # convert values image to range [0,255]
                normlize_filtered_image = normlize_image(filtered_image , 0 , 255)
                normlize_filtered_image.astype(int)

                # show orginal image and filtered image 
                fig , (ax1 , ax2) = plt.subplots(1,2)

                # plot original image and filtered imagem
                ax1.imshow(original_image , cmap='gray')
                ax2.imshow(normlize_filtered_image , cmap='gray')

                # plot image setting
                ax1.set_title('original Input Image')
                ax2.set_title('Mask Size:' + str(size_filter) + '*' + str(size_filter))
                ax1.axis('off')
                ax2.axis('off')
                plt.show()

