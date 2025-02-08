from flask import Flask, render_template, jsonify, request, url_for,redirect
import speech_recognition as sr

app = Flask(__name__)

def write_transcription_to_file(text: str, output_file: str) -> None:
    """
    Writes the transcribed text to the output file.
    """
    with open(output_file, 'w') as f:
        f.write(text)

def transcribe_audio_from_mic(language: str) -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.listen(source)
            print("Processing your speech...")
            text = recognizer.recognize_google(audio_data, language=language)
            write_transcription_to_file(text, "project.txt")  # Save the transcription
            print(text)
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."
    return redirect(url_for('spam_dec'))


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

@app.route('/spam_dec')
def spam_dec():
    return render_template('spam_dec.html')


if __name__ == '__main__':
    app.run(debug=True)