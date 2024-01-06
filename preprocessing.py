import cv2
import cv2.bgsegm
import numpy as np


class Filter_eye:
    def __init__(self):
        self.processed_images = {}

    def background_subtraction_MOG2(self, image):
        # A1
        # Create a background subtractor using MOG2 algorithm
        subtractor = cv2.createBackgroundSubtractorMOG2()
        result = subtractor.apply(image)
        self.processed_images['bs_mog2'] = result
        return result



    def background_subtraction_GMG(self, image):
        # A2
        # Create a background subtractor using GMG algorithm
        subtractor = cv2.bgsegm.createBackgroundSubtractorGMG()
        result = subtractor.apply(image)
        self.processed_images['bs_gmg'] = result
        return result

    def background_subtraction_KNN(self, image):
        # A3
        # Create a background subtractor using KNN algorithm
        subtractor = cv2.createBackgroundSubtractorKNN()
        result = subtractor.apply(image)
        self.processed_images['bs_mg'] = result
        return result    

    def blur_image(self,image, kernel_size=(5, 5)):
        # A4
        # Apply Gaussian blur to the image
        blurred = cv2.GaussianBlur(image, kernel_size, 0)
        self.processed_images['blurred'] = blurred
        return blurred

    def edge_detection(self,image, threshold1=100, threshold2=200):
        # A5
        # Perform edge detection on the image using Canny algorithm
        edges = cv2.Canny(image, threshold1, threshold2)
        self.processed_images['edges'] = edges
        return edges
    
    # def filterCombine(self, image_input, func_arr):
    #     # Create an empty list to store the processed results
    #     processed_results = []

    #     # Loop through each function in the func_arr
    #     for func in func_arr:
    #         # Call the function and pass the image as an argument
    #         image_output = func(image_input)

    #         # Append the processed result to the list
    #         self.processed_images[] = image_output

    #     # Process the results
    #     # ...

    #     # Return the processed data
    #     return image_output
