
# coding: utf-8
import boto3

# Ask user to input a text
input_text = input('Enter some English text ')

# Define default text
default_text = 'The text you entered is '

# create output text by combining default text and text entered by user.
Output_text = default_text + input_text 

# Define a low-level client representing Amazon Polly
client = boto3.client('polly',
        region_name = 'eu-west-1'
)

# Synthesizes text to a stream of bytes.
polly_response = client.synthesize_speech(
                 OutputFormat='mp3',
                 Text=Output_text,
                 TextType='text',
                 VoiceId='Raveena'
)

# Store the stream to a mp3 file
with open('polly_speech.mp3', 'wb') as f:
    f.write(polly_response['AudioStream'].read())

# Write output text
with open('output.txt', 'w') as fo:
    fo.write(Output_text)
