import cv2

def main():
    imgpath = "D:\\Users\\DavidZ\\Desktop\\opencv-sandbox\\Python-OpenCV3-master\\Dataset\\4.2.04.tiff"
    img = cv2.imread(imgpath)

    outpath = "D:\\Users\\DavidZ\\Desktop\\opencv-sandbox\\Python-OpenCV3-master\\Output\\4.2.04.jpg"

    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')

if __name__ == "__main__":
    main()
