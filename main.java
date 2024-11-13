import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfRect;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.core.Size;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.objdetect.CascadeClassifier;

public class FaceRecognition {
    public static void main(String[] args) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);

        // Path to the data and temp folders
        String dataFolderPath = "path/to/data/folder";
        String tempFolderPath = "path/to/temp/folder";

        // Get the list of JPG files in the data folder
        List<String> dataFiles = getFilesInFolder(dataFolderPath, ".jpg");

        // Get the list of PNG files in the temp folder
        List<String> tempFiles = getFilesInFolder(tempFolderPath, ".png");

        // Perform face recognition for each JPG file in the data folder
        for (String dataFile : dataFiles) {
            // Load the data file
            Mat dataImage = Imgcodecs.imread(dataFile);

            // Perform face detection
            CascadeClassifier faceCascade = new CascadeClassifier("path/to/haarcascade_frontalface_default.xml");
            MatOfRect faceDetections = new MatOfRect();
            faceCascade.detectMultiScale(dataImage, faceDetections);

            // Iterate over the detected faces
            for (Rect rect : faceDetections.toArray()) {
                // Perform face recognition for each PNG file in the temp folder
                for (String tempFile : tempFiles) {
                    // Load the temp file
                    Mat tempImage = Imgcodecs.imread(tempFile);

                    // Resize the temp image to match the size of the detected face
                    Mat resizedTempImage = new Mat();
                    Imgproc.resize(tempImage, resizedTempImage, new Size(rect.width, rect.height));

                    // Compare the data image with the resized temp image
                    if (Core.mean(dataImage).equals(Core.mean(resizedTempImage))) {
                        System.out.println("Match Found");

                        // Display the matched photo from the data folder
                        displayImage(dataImage);
                    }
                }
            }
        }
    }

    private static List<String> getFilesInFolder(String folderPath, String extension) {
        List<String> files = new ArrayList<>();
        File folder = new File(folderPath);
        File[] listOfFiles = folder.listFiles();

        if (listOfFiles != null) {
            for (File file : listOfFiles) {
                if (file.isFile() && file.getName().toLowerCase().endsWith(extension)) {
                    files.add(file.getAbsolutePath());
                }
            }
        }

        return files;
    }

    private static void displayImage(Mat image) {
        // Code to display the image
    }
}