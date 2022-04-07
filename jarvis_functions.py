import speech_recognition as sr
import pyttsx3
import wolframalpha

def wfalpha_query(message, choice):
    client = wolframalpha.Client('6LLVTA-RYGLTXWWV4')
    r = client.query(message)
    resp = next(r.results).text
    if choice == 'clean':
        dc = '()|><'
        for c in dc:
            resp = resp.replace(c,'')
        return resp
    if choice == 'normal':
        return resp
    return 'Error -> missing argument'

def say_a_message(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def print_microphones():
    print(sr.Microphone.list_microphone_names())

def read_voice(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response