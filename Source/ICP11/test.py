import cv2
import numpy as np
import tensorflow as tf

model4 = tf.keras.models.load_model('model4.h5')
import matplotlib.pyplot as plt
filename = "60.jpeg"


def PredictImg(file=filename):
    file = filename
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    img_size = 100
    new_img_array = cv2.resize(img_array, (img_size, img_size))
    plt.imshow(img_array)
    plt.title("animals[something[0]]")
    plt.show()
    test_images = np.array(new_img_array).reshape(-1, img_size, img_size, 1)
    something = model4.predict_classes(test_images)

    animals = ["dog", "horse", "elephant", "butterfly", "chicken", "cat", "cow", "sheep", "squirrel", "spider"]
    result = animals[something[0]]
    plt.imshow(img_array)
    plt.title(animals[something[0]])
    plt.show()
    return result

# result = PredictImg(filename)
# print(result)