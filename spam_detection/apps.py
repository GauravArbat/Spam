from django.apps import AppConfig


class SpamDetectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spam_detection'




from flask import Flask, render_template, jsonify
import speech_recognition as sr

app = Flask(__name__)
def write_transcription_to_file(text: str, output_file: str) -> None:
    """
    Writes the transcribed text to the output file.
    """
    with open(output_file, 'w') as f:
        print("hello");
        f.write(text)

def transcribe_audio_from_mic(language: str) -> str:
    try:
        
        
        write_transcription_to_file("text","gaurav.txt")
    except Exception as e:
        print('Error:', e)
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.listen(source)
            print("Processing your speech...")
            text = recognizer.recognize_google(audio_data, language=language)
            
            return text
        
        
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start-detection', methods=['GET'])
def start_detection():
    try:
        language = "en-US"  # You can dynamically choose this via a dropdown or input
        transcription = transcribe_audio_from_mic(language)
        return jsonify({"message": transcription})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
