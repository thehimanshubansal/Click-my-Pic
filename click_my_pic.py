import cv2   # Opencv-pyhton best library for Image processing and much more

# GRAYSCALE IMAGE
def grayscale(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image",gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return gray_img

# BLACK AND WHITE IMAGE
def BW_img(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, bw_img = cv2.threshold(gray_img, 127,225,cv2.THRESH_BINARY)
    cv2.imshow("Black and White Image",bw_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_img(bw_img)

    return bw_img

# ORIGINAL IMAGE
def org_img(img):
    cv2.imshow("Original Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return img

def show_img(img):
    print("\nImage Display Type:\n1. Coloured Image\n2. Gray Image\n3. Black and White Image\n4. All")
    x = int(input("Enter:  "))
    match x:
        case 1:
            org_img(img)
        case 2:
            grayscale(img)
        case 3:
            BW_img(img)
        case 4:
            org_img(img)
            grayscale(img)
            BW_img(img)
        case _ :
            print("Invalid input!!")

def save_img(img):
        directory = "D:\Pictures D\Camera Roll"
        success = cv2.imwrite(directory +"\pycamera.jpg", img, [cv2.IMWRITE_JPEG_QUALITY,90])  # Quality Scale: [0 - 100]
        

        print("\nError saving captured image!") if not success else print("\nSaved successfully!")


print("\nBasic Image Conversion\n\n1. Gallery (Image from Gallery)\n2. Camera (Click now)\n")
i = int(input("Enter Operation No.: "))
match i:
    case 1:
        x = input("Enter the image path: ")    # D:\Pictures D\Camera Roll\WIN_20240504_10_41_31_Pro.jpg
        image = cv2.imread(x)
        
        show_img(image)

    case 2:

        # CAMERA
        cap = cv2.VideoCapture(0)
        ret, cap_img = cap.read()

        show_img(cap_img)

        print("\nWant to save the captured image?")
        x = (input("Enter (Yes/No): "))
        if x.lower() == "yes": save_img(cap_img) 
        
    case _ :
        print("Invalid input!!")
