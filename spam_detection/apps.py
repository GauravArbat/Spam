from flask import Flask, render_template, jsonify, redirect, url_for
import speech_recognition as sr

app = Flask(__name__)

OUTPUT_FILE = "gaurav.txt"  # Save transcription in the same directory

def write_transcription_to_file(text: str, output_file: str) -> None:
    """
    Writes the transcribed text to the output file.
    """
    try:
        with open(output_file, 'w') as f:  # 'w' overwrites; 'a' appends
            f.write(text)
        print(f"Transcription successfully saved to {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def transcribe_audio_from_mic(language: str) -> str:
    """
    Records audio from the microphone and saves the transcription.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.listen(source)
            print("Processing your speech...")
            text = recognizer.recognize_google(audio_data, language=language)
            write_transcription_to_file(text, OUTPUT_FILE)
            print("Transcription:", text)
            return "Transcription successful!"
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."

@app.route('/start-detection', methods=['GET'])
def start_detection():
    language = "en-US"
    transcription = transcribe_audio_from_mic(language)
    return jsonify({"message": transcription})

if __name__ == '__main__':
    app.run(debug=True)
