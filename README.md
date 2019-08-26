# Kitten-and-Puppy-Classifier
This weekly project is to perform image classification between cat and dog. The labeled dataset consists of 25,000 images, specially selected for classifying whether images contain either a dog or a cat. Then building a Flask app to help user upload their image and get the result that is a cat or dog photo.  
![Cat and Dog](https://gimmeinfo.com/wp-content/uploads/2016/02/pets-cat-dog-2-1100x866.jpg)

### Project goal
* Build CNN model to classify whether images contain either a dog or a cat. Moreover the model has to reach more than 90% accuracy score
* Build a Flask app to predict cat or dog from the image uploaded by the user

### Understanding the dataset
* Label: 0 - dog, 1 - cat
* Image_path: Path to a image

### Link to the flask app
* https://github.com/hangnguyennn13/Kitten-and-Puppy-Classifier

### Tasks needed to be done
* Create VM on GCE with Deep learning platform: https://hackmd.io/SEVZeQMJRa2JJMxd9y8PnQ
* Build Model:
    * Load dataset + check data
        * The dataset contains 25,000 images.
        * Load only the image path using os and glob libraries
        * Image path follows the pattern: train/*.jpg (* can be dog or cat)
    * Preprocess data:
        * Label the image according to its path
        * If the path contain dog.*.jpg then 0 ortherwise 1
    * Save the image path + label in python dataframe
    * Check whether we have a balanced dataset or not using seaborn countplot on the label columns. If not then consider to choose between applying undersamplying or oversampling technique. However, we have a balanced dataset so we can skip this part
