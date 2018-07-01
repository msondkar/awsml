
# coding: utf-8
import boto3

def detect_pedestrian(imageFile):
    # open image file and detect labels with the the confidence threshold of 50%.
    with open(imageFile, 'rb') as image:
        response= client.detect_labels(Image={'Bytes': image.read()}, MinConfidence=50)
    
    # Initialize confidence score
    score = 0   
    
    # Find label name = 'Pedestrian' and store the confidence score
    for label in response['Labels']:
        if label['Name'] == 'Pedestrian':
            score = label['Confidence']
    
    #return score
    return score

####################### MainLine Logic ################################

# Open output file
f = open('Output.txt','w')
f.write('Pedestrian Detection Systems!')
f.write('\n ')

# A low-level client representing Amazon Rekognition
client = boto3.client('rekognition',
        region_name = 'eu-west-1'
                     )

# list to store image files
imageList = ['pedestrian.jpg', 'nopedestrian.jpg']

for imageFile in imageList:
    score = detect_pedestrian(imageFile)
    # if score is nonzero 
    if score == 0:
        f.write('\nPedestrian is not detected in the image file ' + '"' + str(imageFile) + '".')
    else:
        f.write('\nPedestrian is detected in the image file ' + '"' + str(imageFile) + '"' + \
		' with a confidence score of ' + str(round(score,2)) + '%.')

    f.write('\n')

