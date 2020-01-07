import numpy as np
import cv2 as cv

# out sketch generaion function
def sketch(img):
    # converting image to gray color
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # clean up image using guassian blur
    img_gray_blur = cv.GaussianBlur(img_gray, (5,5), 0)

    # extract edges
    canny_edges = cv.Canny(img_gray_blur, 10, 70)

    # Do an invert binarize images
    ret, mask = cv.threshold(canny_edges, 70, 255, cv.THRESH_BINARY_INV)
    # return img_gray

    M = np.ones(img.shape, dtype="uint8") * 175
    added = cv.add(img, M)
    subtrap = cv.subtract(img, M)
    return added



# open the web cam
cap = cv.VideoCapture(0)

while True:
    # ret have only true or false
    # frame have frames of the video
    ret, frame = cap.read()
    cv.imshow('mywindow', sketch(frame))
    if cv.waitKey(1) == 13: #13 is the enter key
        break

# release camerea and close window
cap.release()
cv.destroyAllWindows()