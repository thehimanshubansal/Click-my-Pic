## Python Program for Capturing and Converting Images

The script, **`click_my_pic.py`**, is a camera and image-processing tool that allows users to capture photos using a webcam or load images from a gallery. It then provides options to convert the image into **grayscale** or **black and white** formats. The script uses the **OpenCV (`cv2`)** library for image processing.

---

### **How the Script Works**
1. **User Chooses an Option**
   - The user selects whether they want to:
     1. Load an image from the gallery.
     2. Capture a new image using the webcam.

2. **Processing an Image**
   - If the user loads an image from the gallery, they provide the image path.
   - If the user chooses to capture a photo, the script uses **OpenCV** to take a picture from the default webcam.

3. **Image Display Options**
   - The user can choose to display the:
     - **Original (Colored) Image**
     - **Grayscale Image**
     - **Black and White Image**
     - **All of the Above**
   - The script applies the relevant OpenCV image transformations and displays them in separate windows.

4. **Saving the Image**
   - The user is asked whether they want to save the captured or processed image.
   - If they choose to save, the image is stored in a predefined directory (`D:\Pictures D\Camera Roll`).
   - The image is saved as **JPEG** with **90% quality**.

---

### **Features**
✔ Capture images using a **webcam**  
✔ Load images from a **gallery**  
✔ Convert images to **grayscale** and **black & white**  
✔ Display images in different formats  
✔ Option to **save processed images**  

This script is a great **beginner-friendly** project that demonstrates **basic image processing with OpenCV** and can be expanded for more advanced applications. Although can add image processing features like **blur**, **edge detection**, or **color filtering** and can improve **GUI**. 📸✨
