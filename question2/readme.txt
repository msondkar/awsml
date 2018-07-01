1) Created a Collection ‘myfacecollection’ for storing the set of face image attributes.
AWS CLI command used for creating a collection, 
aws rekognition create-collection --collection-id "myfacecollection"

2) Stored the training face images in a bucket ‘msondkarface’. There are two set of face images belonging to two different persons.

3) Run ‘training.py’ program for adding face images to collection ‘myfacecollection’. The program uses the ‘IndexFaces’ operation todetect faces in an image and add them to collection. Used ‘ExternalImageId’ field in the ‘IndexFace’ operation to associate a name with an image. 
The ‘ListFaces’ operation is then used to return faces stored in the collection. This data is written in the 'trainingOutput.txt' file.

4) Run ‘faceverification.py’ program that takes face image from a webcam and uses the ‘SeachFacesByImage’ operation to search faces in a collection that matches the face in webcam.
Program successfully matched a webcam face image with training images in a collection. Output text file is ‘faceverificationOutput.txt’ and saved webcam image name is ‘faceverificationSuccessImage.jpg’.
Program also unable to match a webcam face image where it is not trained on. Output text file is ‘faceverificationError.txt’ and saved webcam image name is ‘faceverificationErrorImage.jpg’.
