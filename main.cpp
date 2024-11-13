#include <iostream>
#include <opencv2/opencv.hpp>
#include <dirent.h>
#include <mutex>

std::mutex mtx;

bool compareFaces(const cv::Mat& image1, const cv::Mat& image2) {
    // Add your facial recognition code here to compare the images
    // Return true if a match is found, false otherwise
    // Implement your facial recognition algorithm
}

int main() {
    std::string data_folder = "data";
    std::string temp_folder = "temp";

    // Load the images from the "data" folder
    std::vector<cv::Mat> data_images;
    DIR* data_dir = opendir(data_folder.c_str());
    struct dirent* data_entry;
    while ((data_entry = readdir(data_dir)) != NULL) {
        std::string filename = data_entry->d_name;
        if (filename.find(".jpg") != std::string::npos) {
            std::string filepath = data_folder + "/" + filename;
            cv::Mat image = cv::imread(filepath);
            data_images.push_back(image);
        }
    }
    closedir(data_dir);

    // Load the images from the "temp" folder
    DIR* temp_dir = opendir(temp_folder.c_str());
    struct dirent* temp_entry;
    while ((temp_entry = readdir(temp_dir)) != NULL) {
        std::string filename = temp_entry->d_name;
        if (filename.find(".png") != std::string::npos) {
            std::string filepath = temp_folder + "/" + filename;
            cv::Mat image = cv::imread(filepath);

            // Perform facial recognition and compare the images
            for (const auto& data_image : data_images) {
                std::lock_guard<std::mutex> lock(mtx);  // Lock the mutex
                if (compareFaces(data_image, image)) {
                    std::cout << "Match found!" << std::endl;

                    // Display the matched photo from the "data" folder
                    cv::imshow("Matched Image", data_image);
                    cv::waitKey(0);
                    cv::destroyAllWindows();
                }
            }
        }
    }
    closedir(temp_dir);

    return 0;
}