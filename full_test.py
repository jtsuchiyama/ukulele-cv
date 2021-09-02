import os
import time
from matplotlib import pyplot as plt
from image import Image
from rotate_crop import rotate_neck_picture, crop_neck_picture
from grid_detection import string_detection, fret_detection
from finger_detection import hand_detection, locate_hand_region, skin_detection, finger_location_detection
import cv2
import copy

def full_test():
    i = 1
    plt.figure(1)
    for filename in os.listdir('./pictures/'):
        print("File found: " + filename + " - Processing...")
        start_time = time.time()
        chord_image = Image(path='./pictures/' + filename)
        rotated_image = rotate_neck_picture(chord_image)
        cropped_image = crop_neck_picture(rotated_image)
        orig_cropped_image = copy.deepcopy(cropped_image)

        neck_strings = string_detection(cropped_image)[0]
        neck_fret_img, neck_fret = fret_detection(cropped_image)
        for string, pts in neck_strings.separating_lines.items():
            cv2.line(neck_fret_img.image, pts[0], pts[1], (127, 0, 255), 2)

        plt.subplot(int("42" + str(i)))
        i += 1
        plt.imshow(cv2.cvtColor(chord_image.image, cv2.COLOR_BGR2RGB))
        plt.subplot(int("42" + str(i)))
        i += 1
        plt.imshow(cv2.cvtColor(neck_fret_img.image, cv2.COLOR_BGR2RGB))



        skin = skin_detection(orig_cropped_image.image)
        refined_hand_region = locate_hand_region(skin)
        contour_image, circular_hough, circles = hand_detection(refined_hand_region)



        finger_location_detection(neck_strings, neck_fret, circles)



        plt.subplot(int("42" + str(i)))
        i += 1
        plt.imshow(cv2.cvtColor(skin, cv2.COLOR_BGR2RGB))



        plt.subplot(int("42" + str(i)))
        i += 1
        plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))



        plt.subplot(int("42" + str(i)))
        i += 1
        plt.imshow(cv2.cvtColor(circular_hough, cv2.COLOR_BGR2RGB))


        for j in circles[0, :]:
            # Draw the outer circle
            cv2.circle(neck_fret_img.image, (j[0], j[1]), j[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(neck_fret_img.image, (j[0], j[1]), 2, (0, 0, 255), 3)


        plt.subplot(int("42" + str(i)))
        i += 1
        plt.imshow(cv2.cvtColor(neck_fret_img.image, cv2.COLOR_BGR2RGB))

        print("Done - Time elapsed: %s seconds" % round(time.time() - start_time, 2))

    plt.show()


if __name__ == "__main__":
    print("Running the full tests...")
    full_test()