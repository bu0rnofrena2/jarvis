import jarvis_functions as jf
import speech_recognition as sr
import time
import keyboard

if __name__ == "__main__":

	recognizer = sr.Recognizer()
	microphone = sr.Microphone()

	while True:
		jf.say_a_message('ask a question or say finish')
		a = jf.read_voice(recognizer, microphone)
		query = a["transcription"]
		query_lower = str(query).lower()
		
		if query_lower == "finish":
			jf.say_a_message('Closing the system')
			break
		if query_lower != "finish":
			res = jf.wfalpha_query(query, "normal")
			print(res)
			jf.say_a_message(res)

