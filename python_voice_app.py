import speech_recognition as sr

# Loop for continuous recognition
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Fixing case-sensitivity
        print("Say something...")
        audio = r.listen(source)  # Listening to the microphone input

        try:
            filename = "draft.txt"
            
            # Open the file in append mode
            with open(filename, "a+") as f:

                # Use Google Speech Recognition to convert speech to text
                recognized_text = r.recognize_google(audio)
                print("Recognized text:", recognized_text)
                
                # Split the recognized text into chunks of 5 words
                remainder = recognized_text.split()

                # Write each chunk of 5 words to the file
                while remainder:
                    line, remainder = remainder[:5], remainder[5:]
                    f.write(' '.join(line) + "\n")  # Added space between words

                # If the user says 'bye', exit the loop
                if 'bye' in recognized_text.lower():
                    print("Exiting...")
                    break

        except sr.UnknownValueError:
            print("Google could not understand the audio")

        except sr.RequestError as e:
            print(f"Google Error; {e}")
