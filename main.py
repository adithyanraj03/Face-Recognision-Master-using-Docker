def compare_images():
    # Load the images from the "data" folder
    data_folder = 'data'
    data_images = []
    for filename in os.listdir(data_folder):
        if filename.endswith('.jpg'):
            image_path = os.path.join(data_folder, filename)
            image = cv2.imread(image_path)
            data_images.append(image)

    # Load the images from the "temp" folder
    temp_folder = 'temp'
    for filename in os.listdir(temp_folder):
        if filename.endswith('.png'):
            image_path = os.path.join(temp_folder, filename)
            image = cv2.imread(image_path)

            # Perform facial recognition and compare the images
            match_found = False
            for data_image in data_images:
                # Add your facial recognition code here to compare the images
                if compare_faces(data_image, image):
                    match_found = True
                    break

            if match_found:
                print("Match found!")
                # Display the matched photo from the "data" folder
                plt.imshow(cv2.cvtColor(data_image, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()