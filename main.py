import cv2
import sys

"""Make sure to adjust the path before running"""

vidPath = r'C:\Users\coanh\Desktop\Desktop\Work\Computer Vision V2\1.mp4'
savePath = r'C:\Users\coanh\Desktop\Desktop\Work\Computer Vision V2'

cap = cv2.VideoCapture(vidPath)
font = cv2.FONT_HERSHEY_SIMPLEX

sub = cv2.createBackgroundSubtractorKNN()

imgCounter = 0
carCounter = 0

while True:
    hasFrame, frames = cap.read()

    if not hasFrame:
        sys.exit("Video Ended")

    """ Setting up mask, saving as img, and turning into binary img"""

    blur = cv2.GaussianBlur(frames, (21, 21), 0)

    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    mask = sub.apply(gray)


    """Change your save path to whatever file you want, but make sure to keep the 
    'str(imgCounter)+'.jpg'"""
    savePath = r'C:\Users\coanh\Desktop\Desktop\Work\Computer Vision V2\\'+str(imgCounter)+'.jpg'

    cv2.imwrite(savePath, mask)

    src = cv2.imread(savePath)

    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(src, 127, 255, 0)

    cv2.putText(frames, "Number of Cars "+str(carCounter), (0, 50), font, 1, (255, 0, 255), 2)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # 6 frames for the background subtractor to warm up.
    if imgCounter >= 6:
        if len(contours) != 0:
            lastContour = imgCounter
        else:
            if lastContour - prevCounter == -1:
                carCounter += 1

    cv2.putText(frames, "Number of Cars "+str(carCounter), (0, 50), font, 1, (0, 100, 255), 2)

    imgCounter += 1

    cv2.imshow("Car counter 2", frames)
    cv2.imshow("gray", gray)
    cv2.imshow("Thresh", thresh)


    if cv2.waitKey(33) == 27:
        break

    if imgCounter > 0:
        prevCounter = imgCounter

cv2.destroyAllWindows()


