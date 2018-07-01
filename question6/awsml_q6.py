
# coding: utf-8
import boto3
import json

def detect_faces(imageFile, f):
    # open image file and detect faces within an image.
    with open(imageFile, 'rb') as image:
        response= client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])
    
    f.write('\nNumber of faces detected in the image file ' + '"' + imageFile + '"' + ' is : ' + str(len(response['FaceDetails']))) 
    
    for faceDetail in response['FaceDetails']:
        f.write('\n ')
        f.write('\nGender : ' +  str(faceDetail['Gender']['Value']))
        f.write('\nAge Range : Between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']))
        f.write('\nSmiling face : ' + str(faceDetail['Smile']['Value']))
        f.write('\nWearing Sunglasses : ' + str(faceDetail['Sunglasses']['Value']))
        f.write('\nWearing Eyeglasses : ' + str(faceDetail['Eyeglasses']['Value']))
        f.write('\nHaving Beard : ' + str(faceDetail['Beard']['Value']))
        f.write('\nHaving Mustache : ' + str(faceDetail['Mustache']['Value']))
        
    f.write('\n ')
    f.write('\n-------------------------------------------------------------------------------')

################## Main Logic ########################

# open output file
f = open('Output.txt', 'w')
f.write('Face Detection System!')
f.write('\n ')

# A low-level client representing Amazon Rekognition
client = boto3.client('rekognition',
        region_name = 'eu-west-1'
)

# Defien a list to store images
imageList = ['noface.jpg', 'oneface.jpg', 'multifaces.jpg']

# detect faces
for imageFile in imageList:
    detect_faces(imageFile, f)

