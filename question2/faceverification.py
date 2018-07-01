import cv2
import boto3

video=cv2.VideoCapture(0)
check, frame = video.read()
cv2.imshow("Color Frame",frame)
collection_name='myfacecollection'

client=boto3.client('rekognition', region_name='eu-west-1')    

response = client.search_faces_by_image(CollectionId=collection_name, Image={'Bytes': cv2.imencode('.jpg', frame)[1].tobytes()})
	
faceMatch=response['FaceMatches']
print (faceMatch)

if faceMatch:
    for match in faceMatch:
        output = match['Face']['ExternalImageId']
    print ('The Person name is ' + output)
	# open output file to write success message
    fo = open('faceverificationOutput.txt', 'w')
    fo.write('The Person name is ' + str(output))
	# save webcam image
    cv2.imwrite('faceverificationSuccessImage.jpg', frame)
else:
    print ('Unable to recognize the person')
	# open error file to write error message
    fe = open('faceverificationError.txt', 'w')
    fe.write('Unable to recognize the person')
	# save webcam image
    cv2.imwrite('faceverificationErrorImage.jpg', frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
