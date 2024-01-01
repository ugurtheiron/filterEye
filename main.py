import cv2

def main():
    # Create a VideoCapture object
    cap = cv2.VideoCapture('/mnt/c/workspaces/tenisProject/detectionHighFreq/src/video/video-1.mp4')

    while True:
        # Read the current frame from the video capture
        ret, frame = cap.read()












        # Display the frame
        cv2.imshow('Video Capture', frame)

        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord(' '):
            # Pause or play the video
            if cv2.waitKey(0) & 0xFF == ord(' '):
                continue
        elif key == 83:  # Right arrow key
            # Go one frame forward
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + 1)
        elif key == 81:  # Left arrow key
            # Go one frame backward
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) - 1)

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
