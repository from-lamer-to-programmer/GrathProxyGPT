import speech_recognition as sr
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)


def chatgpt(req: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": req,
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)


def listen_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Listen to the microphone for 5 seconds

    return audio


def speech_to_text(audio):
    recognizer = sr.Recognizer()

    try:
        text = recognizer.recognize_google(audio)
        if isinstance(text, str) and text.startswith("Natasha"):
            chatgpt(text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")

    except sr.RequestError as e:
        print(f"Error with the Google Speech Recognition service; {e}")


if __name__ == "__main__":
    audio_data = listen_microphone()
    text = ""
    if audio_data:
        speech_to_text(audio_data)
        while text != "stop":
            audio_data = listen_microphone()
            if audio_data:
                text = speech_to_text(audio_data)
