import os,sys
import numpy as np
import cv2




def main(inputFile):
    #outputFile = inputFile.split('.')[0]+'-rect.'+'.'.join(inputFile.split('.')[1:])
    #print(outputFile)
    img = cv2.imread(inputFile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rc,thresh = cv2.threshold(gray, 150, 255,cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    dilated = cv2.dilate(thresh, kernel, iterations= 13)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        [x, y, w, h] = cv2.boundingRect(contour)

        if h > 300 and w > 300:
            print("[Bigger Height={0}, Weight={1}, X={2}, Y={3}".format(h, w, x, y))
            continue
        if h < 40 and w < 40:
            print("[Smoll Height={0}, Weight={1}, X={2}, Y={3}".format(h, w, x, y))
            continue
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)

    cv2.imwrite("result.jpg", img)

    cv2.imshow('original', img)

    cv2.waitKey(5)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv[1])