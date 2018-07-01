# coding: utf-8

import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
from tempfile import gettempdir
import time
from urllib.request import urlopen
import json

# A low-level client representing Amazon Polly# A low 
polly = boto3.client("polly",
                    region_name = 'eu-west-1')

text = 'The sun does arise and make happy the skies. The merry bells ring to welcome the spring.'

# synthesize_speech function to covert a text into a stream of bytes. Output will be encoded into mp3 format. 
# The male voice of "Matthew" will be used for synthesis.
response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Matthew")

# Access the audio stream from the response
if "AudioStream" in response:   
    with closing(response["AudioStream"]) as stream:
        output = "polly_speech.mp3"
        try:
            # Open a file for writing the output as a binary stream
            with open(output, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            # Could not write to file, exit gracefully
            print(error)
            sys.exit(-1)
else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    sys.exit(-1)
    
# upload a file from local file system to bucket 'msondkarsongs' with 'polly_speec.mp3" as object name.
s3 = boto3.resource("s3",
                    region_name = 'eu-west-1')

s3.meta.client.upload_file("polly_speech.mp3", "msondkarsongs", "polly_speech.mp3")

# Start an asynchronous job to transcribe speech to text.
transcribe = boto3.client('transcribe',
                        region_name = 'eu-west-1') 
  
job_name = "msondkartrans12"
job_uri = "https://s3-eu-west-1.amazonaws.com/msondkarsongs/polly_speech.mp3"
transcribe.start_transcription_job(TranscriptionJobName=job_name,Media={'MediaFileUri': job_uri},
                                   MediaFormat='mp3', LanguageCode='en-US')


# check the job status and store a link to the JSON file cotaining result.
while True:
    job = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    job_status = job['TranscriptionJob']['TranscriptionJobStatus']
    if job_status in ['COMPLETED', 'FAILED']:
        break
        print("Not ready yet...")
    time.sleep(10)

if job_status == 'FAILED':
    print('Job failed')
    sys.exit(-1)
elif job_status == 'COMPLETED':
    url = job['TranscriptionJob']['Transcript']['TranscriptFileUri']

# if the job is completed succesfully, then load the josn file and check the transcript
with urlopen(url) as json_file:
    json_data = json.load(json_file)

# Write output text
with open('output.txt', 'w') as fo:
    fo.write('AWS Transcribe MP3 to text result : ' + str(json_data['results']['transcripts'][0]['transcript']))
