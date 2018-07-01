import boto3

if __name__ == "__main__":

    # Open File to write training output
    fo = open('trainingOutput.txt','w')

    bucket='msondkarface'
    collectionId='myfacecollection'
    maheshimages = ['Mahesh1.jpg', 'Mahesh2.jpg', 'Mahesh3.jpg', 'Mahesh4.jpg', 'Mahesh5.jpg']
    vinayakimages = ['Vinayak1.jpg', 'Vinayak2.jpg', 'Vinayak3.jpg', 'Vinayak4.jpg', 'Vinayak5.jpg']
	
    maheshimagesName='Mahesh'
    vinayakimagesName='Vinayak'
	
    tokens=True
    
    client=boto3.client('rekognition')

    response=client.index_faces
	
    for image in maheshimages:
        response=client.index_faces(CollectionId=collectionId,
                                   Image={'S3Object':{'Bucket':bucket,'Name':image}},
                                   ExternalImageId=maheshimagesName,
                                   DetectionAttributes=['ALL'])
								   
    for image in vinayakimages:
        response=client.index_faces(CollectionId=collectionId,
                                   Image={'S3Object':{'Bucket':bucket,'Name':image}},
                                   ExternalImageId=vinayakimagesName,
                                   DetectionAttributes=['ALL'])

    response=client.list_faces(CollectionId=collectionId,
                               MaxResults=10)
							   
    print('Faces in collection ' + collectionId)
    while tokens:
        faces=response['Faces']
        for face in faces:
            print (face)
            items = ', '.join('{} = {}'.format(key, value) for key, value in face.items())
            fo.write(items)
            fo.write('\n')
        if 'NextToken' in response:
            nextToken=response['NextToken']
            response=client.list_faces(CollectionId=collectionId,
                                       NextToken=nextToken,MaxResults=10)
        else:
            tokens=False

