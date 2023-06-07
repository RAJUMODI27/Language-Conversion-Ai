# Language-Conversion-Ai

The Speech-to-Text Translator application is a Python code that enables real-time translation of spoken language into the desired output language. It utilizes several libraries and APIs to provide a seamless translation experience.

Using the speech_recognition library, the application captures the user's speech input through a microphone. The pyttsx3 library is then employed to convert the translated text into speech output. For language translation, the code utilizes the translate library, which offers a convenient interface to translate text into various languages.

Upon launching the application, users are greeted with a friendly message introducing the Voice Translation AI. They are prompted to choose the desired output language from a list of available options, such as English, French, Spanish, and more. The chosen language is stored as a key-value pair, allowing easy access to the corresponding language code for translation.

Once the output language is selected, users can start speaking. The application employs speech recognition to convert the spoken words into text. The recognized text is then passed to the translation function, which utilizes the chosen output language code to translate the text accordingly.

To facilitate a seamless user experience, the translated text is transformed into speech output. This is achieved using the gTTS library, which converts the text into an audio file. The playsound library enables the playback of the generated audio, allowing users to hear the translated output in their selected language.

Overall, this Speech-to-Text Translator application provides an intuitive and efficient way for users to communicate in different languages. By leveraging speech recognition, translation, and text-to-speech technologies, it breaks down language barriers and promotes effective communication in a user-friendly manner.
