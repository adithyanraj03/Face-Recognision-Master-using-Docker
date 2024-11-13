# Face Recognition Master using Docker

## Project Overview

This project implements a face recognition system using Python and the `face_recognition` library. It utilizes Docker for containerization, ensuring a consistent and reproducible environment.

### Features

- **Face Detection**: Automatically find all the faces in an image.
- **Face Recognition**: Identify detected faces by comparing them to a database of known faces.
- **Facial Feature Manipulation**: Locate and outline facial features such as eyes, nose, mouth, and chin.
- **Docker Integration**: The project is containerized using Docker, making it easy to deploy and run on various environments.

## Installation and Setup

### Prerequisites

- Docker installed on your system.
- Python 3.3+ or Python 2.7 (though Python 3 is recommended).

### Steps to Set Up

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/adithyanraj03/face-recognition-master.git
   cd face-recognition-master
2. **Build the Docker Image**:
   ```bash
   docker build -t face-recognition.

2. **Run the Docker Container**:
   ```bash
   docker run -it face-recognition


### Usage

- Command-Line Interface
The face_recognition command can be used to recognize faces in photographs or folders full of photographs.
Recognize Faces:

  ```bash
  face_recognition./pictures_of_people_i_know/./unknown_pictures/

- Find Faces:
  ```bash
  face_recognition --show-distance true./pictures_of_people_i_know/./unknown_pictures/

- Code Snippets

  ```bash
  import face_recognition
  
  def encode_known_faces(model="hog", encodings_location="encodings.pkl"):
      names = []
      encodings = []
      
      for filepath in Path("training").glob("*/*"):
          name = filepath.parent.name
          image = face_recognition.load_image_file(filepath)
          face_locations = face_recognition.face_locations(image, model=model)
          face_encodings = face_recognition.face_encodings(image, face_locations)
          
          for encoding in face_encodings:
              names.append(name)
              encodings.append(encoding)
      
      # Save the encodings to a file
      data = {"encodings": encodings, "names": names}
      import pickle
      pickle.dump(data, open(encodings_location, "wb"))
  
  # Example usage
  encode_known_faces() 

## Dockerfile
-Here is an example Dockerfile to build the Docker image:
     ```bash
     
    FROM python:3.9-slim
    # Set working directory
    WORKDIR /app
    # Copy requirements file
    COPY requirements.txt.  
    # Install dependencies
    RUN pip install -r requirements.txt  
    # Copy the rest of the application code
    COPY..    
    # Install dlib (required for face_recognition)
    RUN apt-get update && apt-get install -y build-essential cmake libopenblas-dev liblapack-dev libatlas-base-dev libboost-python-dev libboost-thread-dev libgflags-dev libgoogle-glog-dev libhdf5-dev libleveldb-dev liblmdb-dev libopencv-dev libprotobuf-dev libsnappy-dev protobuf-compiler python-dev python-pip python-setuptools python-wheel    
    RUN pip install face_recognition   
    # Command to run the application
    CMD ["python", "detector.py"]
