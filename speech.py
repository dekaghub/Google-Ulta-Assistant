import speech_recognition as sr
import webbrowser as webbrowser


chrome_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

r3 = sr.Recognizer()
r2 = sr.Recognizer()
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("OPTIONS:\\n[Search Web | Search Music ]")
    print("Say something")
    audio= r.listen(source)

if "web" in r.recognize_google(audio):
    r2 = sr.Recognizer()
    url="https://en.wikipedia.org/wiki/"
    with sr.Microphone() as source :
        print("Searching for Scientist :: \n Please state his /her name :")
        audio= r.listen(source)

            
        try:
            get=r2.recognize_google(audio)
            print("Google thinks you said this: \n" + get)
            webbrowser.open_new(url+get)
        except sr.UnknownValueError:
            print("Sorry couldnt understand Audio")
        except sr.RequestError as e:
            print("Failed to retrieve results".format(e))



if "music" in r3.recognize_google(audio):
    r2 = sr.Recognizer()
    url2="https://www.youtube.com/results?search_query="
    r3=sr.Recognizer()

    with sr.Microphone() as source :
        print("Searching for Music Video :: \n Please state the name music: ")
        audio= r.listen(source)

        try:
            text=r3.recognize_google(audio)
            print("Google thinks you said this: \n" + text)
            webbrowser.open_new(url2+text)

        except sr.UnknownValueError:
             print("Sorry couldnt understand Audio")
        except sr.RequestError as e:
            print("Failed to retrieve results".format(e))



'''
except Exception as e:
    print(e)
    print("Got it! Now to recognize it..")


try:
    text=r.recognize_google(audio)
    print("you said \n"+ r.recognize_google(audio))
    wb.get(chrome_path).open(text)
except Exception as e:
    print(e)
    '''