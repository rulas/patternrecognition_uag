from PIL import Image
from pylab import *

files_start = 0
files_end = 17


# things to recognize:
# calculator signs
# numeric characters 
# greek letters


def get_list_of_files():
    files = []
    filename = "frame"
    for number in range(files_start, files_end):
        files.append("%s_%03d.gif" % (filename, number))
    return files


def distance_norm_1(array):
    assert(array[0].dtype == np.int32)
    return sum(abs(array[0] - array[1]))


def distance_norm_2(array):
    return distance_norm_p(array, 2)


def distance_norm_p(array, p=2):
    return sum(abs(array[0] - array[1]) ** p) ** (1. / p)


def extract_img(fpath):
    img = Image.open(fpath)
    img.convert("1")
    imarray = np.array(img.getdata()).reshape(img.size[0], img.size[1])
    return imarray


def main():
    # start the gUI

    ###############################################################
    # Open images and calculate descriptor for each
    ###############################################################

    files = get_list_of_files()
    files_array = []
    files_descriptor_1 = []
    files_descriptor_2 = []
    img_data = []

    for fpath in files:
        #get the image information
        imarray = extract_img(fpath)
        desc1 = calculate_descriptor_1(array)
        desc2 = calculate_descriptor_2(array)
        img_data.append((imarray, desc1, desc2))

    img = get_image_from_gui()

    img1 = find_closest_desc1(img)
    img2 = find_closest_desc2(img)




if __name__ == "__main__":
    main()
