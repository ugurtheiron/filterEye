import cv2
import cv2
import numpy as np
import math

import preprocessing


def main():
    # Create a VideoCapture object
    cap = cv2.VideoCapture('/mnt/c/workspaces/tenisProject/detectionHighFreq/src/video/video-1.mp4')

    while True:
        # Read the current frame from the video capture
        ret, frame = cap.read()
        # use preprocessing here
        # Display the resulting frame
        filterManager = preprocessing.Filter_eye()

        bs_frame_mog2 = filterManager.background_subtraction_MOG2(frame)
        bs_frame_gmg = filterManager.background_subtraction_GMG(frame)
        bs_frame_knn = filterManager.background_subtraction_KNN(frame)
        blr_frame = filterManager.blur_image(frame)
        edge_frame = filterManager.edge_detection(frame)
        #filterManager.display_images()

        # Display the frame
        image_arrray = [frame, bs_frame_mog2, bs_frame_gmg, bs_frame_knn, blr_frame, edge_frame]
        display_image_grid(image_arrray, image_size=(300, 300))

        

        # Check for key press
    #     key = cv2.waitKey(1) & 0xFF
    #     if key == ord('q'):
    #         break
    #     elif key == ord(' '):
    #         # Pause or play the video
    #         if cv2.waitKey(0) & 0xFF == ord(' '):
    #             continue
    #     elif key == 83:  # Right arrow key
    #         # Go one frame forward
    #         cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + 1)
    #     elif key == 81:  # Left arrow key
    #         # Go one frame backward
    #         cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) - 1)

    # # Release the video capture object and close the window
    # cap.release()
    # cv2.destroyAllWindows()


def display_image_grid(image_frames, image_size):
    window_names = ['Original', 'MOG2', 'GMG', 'KNN', 'Blur', 'Edge']
    for i, frame in enumerate(image_frames):
        cv2.namedWindow(window_names[i], cv2.WINDOW_NORMAL)
        cv2.imshow(window_names[i], cv2.resize(frame, image_size))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# def display_image_grid(image_frames, image_size):
#     window_names = ['Original', 'MOG2', 'GMG', 'KNN', 'Blur', 'Edge']
#     for i, frame in enumerate(image_frames):
#         cv2.imshow(window_names[i], cv2.resize(frame, image_size))

    

# # Example usage
# image_paths = ['path_to_image_1', 'path_to_image_2', 'path_to_image_3', 'path_to_image_4']
# display_image_grid(image_paths, image_size=(300, 300))


if __name__ == '__main__':
    main()
