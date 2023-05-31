import cv2, uuid, os, time

# Create the labels for the picture, this tells the computer what each picture is to learn from.
labels = ["Thumbs Up", "Thumbs Down", "Thank you", "Live"]
img_count = 5 #Collect 5 images of each label in the labels list

# The path of the images
IMAGE_PATH = os.path.join('images', 'collectedimages')

# setup the folders
print(IMAGE_PATH)
if not os.path.exists(IMAGE_PATH):
    if os.name == 'nt':
        os.makedirs(IMAGE_PATH)
        
for label in labels:
    path = os.path.join(IMAGE_PATH, label)
    if not os.path.exists(path):
        os.makedirs(path)
         
# Capture the images from webcam

for label in labels:
    cap = cv2.VideoCapture(0) # Connects to the webcam
    print("Collecting images for {}".format(label))
    time.sleep(5) # allows us to change position to identify next image. Remove for real time constant identification. 

    for imgnum in range(img_count):
        print("Collecting images {}".format(imgnum))
        ret,frame = cap.read()
        imgName = os.path.join(IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1()))) #Creates new image and adds to image path with correct label
        # Write image to file and show it. 
        cv2.imwrite(imgName, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows
