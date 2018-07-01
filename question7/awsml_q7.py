
# coding: utf-8
import boto3

def aws_comprehend(text, f):

    # Detect the dominant language in text
    language_response = client.detect_dominant_language(Text=text)
    
    f.write('\n ')
    f.write('\nDominant language in the text is ' +  '"' + str(language_response['Languages'][0]['LanguageCode']) + '"' + \
	        ' with a confidence score of ' + str(round(language_response['Languages'][0]['Score'], 3)))
    f.write('\n ')

    # store the lagunage code for entity detection 
    langcode = str(language_response['Languages'][0]['LanguageCode'])
    
    # Detect the entities in text
    entities_response = client.detect_entities(Text=text, LanguageCode=langcode)

    # Display entity, it's type and score
    for entity in entities_response['Entities']:
        f.write('\nEntity : ' + '"' + str(entity['Text']) + '"' + ', Type : ' + '"' + str(entity['Type']) + '"' + \
		        ', Score : ' + str(round(entity['Score'], 3)))
    f.write('\n')
    
    # Detect the key phrases in text.
    key_phrases_response = client.detect_key_phrases(Text=text, LanguageCode=langcode)

    # Display key phrases and their score
    for phrase in key_phrases_response['KeyPhrases']:
        f.write('\nKey Phrase : ' + '"' + str(phrase['Text']) + '"' + ', Score : ' + str(round(phrase['Score'], 3)))
    f.write('\n ')
        
    # Get the sentiment from text
    sentiment_response = client.detect_sentiment(Text=text, LanguageCode=langcode)

    f.write('\nThe overall sentiment of text is ' + str(sentiment_response['Sentiment']))
    f.write('\n ')


################# Mainline Logic ##########################

# Open output file
f = open('output.txt', 'w')

# A low-level client representing Amazon Rekognition
client = boto3.client('comprehend',
        region_name = 'eu-west-1'
)

# English text
english_text = 'In the United States, Thanksgiving Day is one of the biggest holidays of the year. It is celebrated primarily in the United States and Canada. In the United States it is celebrated on the fourth Thursday of November. It is a day when families from all over the United States get together (sometimes travelling long distances) and prepare traditional dishes, watch football on TV and share a big meal.'
# Spanish text
spanish_text = 'Hola! Mi nombre es Michelle. Tengo 36 años, soy soltera y trabajo en un banco en la ciudad de Nueva York en el departamento de finanzas. Me encanta trabajar allí porque es muy interesante y la gente con la que trabajo es muy amable. Yo nací en Philadelphia pero me mudé a Nueva York hace 6 años. No me arrepiento de esto. Nueva York es una ciudad fascinante. Hay mucho que hacer aquí: museos, teatros, discotecas, tiendas, restaurantes, etc.'

# define a list for both the english and spanish text
Text = [english_text, spanish_text]
# define a list to store the Language name.
Language = ['English', 'Spanish']

# Run AWS Comprehend utility
for text, lang in zip(Text, Language):
    f.write('\nAWS Comprehend Summary for ' + str(lang) + ' Paragraph ' + '--------------------')
    aws_comprehend(text, f)
    f.write('\nAWS Comprehend Summary End --------------------------------------')
    f.write('\n ')

