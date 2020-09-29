import cv2
import os
import config
import sys

def gen_neg_samples(img_dir, output_dir, num_samples=2000):
    img_counter = 0
    # if (os.path.exists(output_dir) == False):
    #     os.mkdir(output_dir)
    
    # adding error checking for existence of image directory
    try:
        # for direct in os.listdir(img_dir):
        #     for file in os.listdir(img_dir + '/' + direct):
        #         if (img_counter == num_samples):
        #             break
        #         try:
        #             img = cv2.imread(img_dir + '/' + direct + '/' + file)
        #             img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #             cv2.imwrite(output_dir + '/' + str(img_counter) + '.jpg', img)
        #             img_counter += 1
        #         except:
        #             continue
        
        for file in os.listdir(img_dir):
            if(img_counter == num_samples):
                break
            try:
                img = cv2.imread(img_dir + '/' + direct + '/' + file)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(output_dir + '/' + str(img_counter) + '.jpg', img)
                img_counter += 1
            except:
                continue
    except FileNotFoundError:
        print('Negative image directory not found')


def gen_neg_txt(directory):
    for neg_file in os.listdir(directory):
        line = directory + '/' + neg_file + '\n'
        with open('bg.txt','a') as f:
            f.write(line)


def resize_pos_sample(img, size=25):
    pos_img = cv2.imread(img)
    pos_img = cv2.cvtColor(pos_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('resized_pos_sample.jpg', cv2.resize(pos_img, (size, size)))


def check_system_args():
    # number of required args for this script
    required_args = 5
    if (len(sys.argv) != required_args):
        return False
    return True


if __name__ == '__main__':
    if check_system_args() == False:
        print("Incorrect amount of system arguments")
    else:
        # neg_img_dir = config.NEG_IMG_DIR_PATH
        # neg_out_dir = config.CASCADE_NEG_OUT_DIR
        # pos_sample = config.POS_SAMPLE
        neg_img_dir = sys.argv[1]
        neg_out_dir = sys.argv[2]
        pos_sample = sys.argv[3]
        resize_val = sys.argv[4]
        gen_neg_samples(neg_img_dir, neg_out_dir)
        gen_neg_txt(neg_out_dir)
        resize_pos_sample(pos_sample, resize_val)