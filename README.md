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
    1. Load dataset + check data
        * The dataset contains 25,000 images.
        * Load only the image path using os and glob libraries
        * Image path follows the pattern: train/*.jpg (* can be dog or cat)
        
    2. Preprocess data:
        * Label the image according to its path
        * If the path contain dog.*.jpg then 0 ortherwise 1
        
    3. Save the image path + label in python dataframe

    4. Check whether we have a balanced dataset or not using seaborn countplot on the label columns. If not then consider to choose between applying undersamplying or oversampling technique. However, we have a balanced dataset so we can skip this part
    
    5. **CNN architecture**:
        * **Input Layer:** It represent input image data. It will reshape image into single diminsion array. Example your image is 64x64 = 4096, it will convert to (4096,1) array.

        * **Conv Layer:** This layer will extract features from image.

        * **Pooling Layer:** This layerreduce the spatial volume of input image after convolution.

        * **Fully Connected Layer:** It connect the network from a layer to another layer

        * **Output Layer:** It is the predicted values layer.
        
        * **Loss:**- To make our model better we either minimize loss or maximize accuracy. NN always minimize loss. To measure it we can use different formulas like 'categorical_crossentropy' or 'binary_crossentropy'. Here I have used binary_crossentropy

        * **Optimizer :**- If you know a lil bit about mathematics of machine learning you might be familier with local minima or global minima or cost function. To minimize cost function we use different methods For ex :- like gradient descent, stochastic gradient descent. So these are call optimizers. We are using a default one here which is adam

        * **Metrics :**- This is to denote the measure of your model. Can be accuracy or some other metric.
        
    6. Define a Sequential model

    7. Fine Tune
        * **Early Stopping:**
        * **Reduce Learning rate:**
