# import pyttsx3
# import time

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# for voice in voices:
#     time.sleep(2)
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()
#     print("done")


import boto3

def polly_tts(text):

    client = boto3.client('polly')

    response = client.synthesize_speech(

    Text=text,

    OutputFormat='mp3',

    VoiceId='Joanna')

with open("speech.mp3", "wb") as file:

    file.write(response['AudioStream'].read())

    polly_tts("Hello, this is a test of Amazon Polly.")