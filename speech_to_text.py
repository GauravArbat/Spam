import speech_recognition as sr

def transcribe_audio_from_mic(language: str) -> str:
    """
    Captures audio from the microphone and transcribes it to text using Google's speech recognition API.
    """
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak now...")
        try:
            # Adjust for ambient noise and record audio
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.listen(source)
            print("Processing your speech...")
            # Transcribe speech to text
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."


def write_transcription_to_file(text: str, output_file: str) -> None:
    """
    Writes the transcribed text to the output file.
    """
    with open(output_file, 'w') as f:
        f.write(text)


if __name__ == '__main__':
    print('Please enter the path to the output file (e.g., output.txt):')
    output_path = input().strip()
    print('Please enter the language code (e.g., en-US):')
    language = input().strip()
    try:
        transcription = transcribe_audio_from_mic(language)
        print('Transcription:')
        print(transcription)
        write_transcription_to_file(transcription, output_path)
        print(f'Transcription successfully saved to {output_path}')
    except Exception as e:
        print('Error:', e)