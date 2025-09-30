import os
import cv2
import numpy as np

# Define the folder containing the images
folder = './Data/Images/'
# folder_mask = './Data/mask/'

# Function to get all PNG files from the folder, excluding those ending with "mask.png"
def get_pngs_from_folder_except_masks(f):
    all_images = []
    for images in os.listdir(f):
    
        # check if the image ends with png
        if (images.endswith(".png")) and (not images.endswith("mask.png")):
            all_images.append(images)
    return all_images

# Function to get all PNG files from the folder that have corresponding mask images
def get_pngs_from_folder_having_masks(f):
    all_images_having_masks = []
    all_pngs = os.listdir(f)
    for images in all_pngs:
    
        # check if the image ends with png
        if (images.endswith(".png")) and (images[:-4] + "_mask.png" in all_pngs):
            all_images_having_masks.append(images)
    return all_images_having_masks

# Get all PNG images from the folder that have corresponding masks
all_images_png_having_masks = get_pngs_from_folder_having_masks(folder)

# Window name for displaying images
window_name = "Next image = N, Finish = ESC"
# Get all PNG images from the folder excluding masks
all_pngs_except_masks = get_pngs_from_folder_except_masks(folder)
# Get all PNG images without corresponding masks
all_pngs_without_masks = list(set(all_pngs_except_masks) - set(all_images_png_having_masks))
# Print the number of images without masks
print('There are still', len(all_pngs_without_masks), 'images without masks.')

# Initialize the image index
id_png = 0

# Read the first image without a mask
img = cv2.imread(folder + all_pngs_without_masks[id_png])
# Initialize a mask with zeros (black image)
mask = np.zeros(img.shape[:2], dtype="uint8")

# Function to draw a circle on the image and mask when the left mouse button is clicked
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: 
        cv2.circle(img, (x, y), 30, (0, 255, 0), -1) 
        
        cv2.circle(mask, (x, y), 30, 255, -1)
                
        cv2.imwrite(folder + all_pngs_without_masks[id_png][:-4] + '_mask.png', mask)
    
# Create a named window
cv2.namedWindow(winname = window_name)
# Set the mouse callback function to 'draw_circle'
cv2.setMouseCallback(window_name, draw_circle) 

# Loop to display images and handle user inputs
while True:
    cv2.imshow(window_name, img) # Show the current image

    # If 'n' key is pressed, move to the next image
    if cv2.waitKey(10) == ord('n'):
        if id_png < len(all_pngs_without_masks) - 1:
            id_png += 1
            img = cv2.imread(folder + all_pngs_without_masks[id_png]) # Load the next image
            mask = np.zeros(img.shape[:2], dtype="uint8") # Reset the mask
            cv2.imshow(window_name, img) # Show the next image
            print(str(id_png),': ', all_pngs_without_masks[id_png]) # Print the current image index and name
    cv2.imshow(window_name, img)

    # Break the loop if 'Esc' key is pressed
    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()