def main():
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import wikipedia
    import webbrowser
    import os
    import smtplib
    import subprocess
    import time
    from covid import Covid 
    import speedtest
    from googletrans import Translator
    import pyshorteners
    import cv2
    import pyautogui
    import imdb
    import phonenumbers
    # from Testphone import number
    from phonenumbers import geocoder
    from phonenumbers import carrier 
    import numpy as np 
    import imageio
    import scipy.ndimage
    from email.message import EmailMessage
    import imghdr
    from freebible import read_web
    from selenium import webdriver
    import pyowm
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from gtts import gTTS
    import random
    from playsound import playsound

    #Prints the first statment of ALEXA
    print("Initializing Alexa")


    #Voice recognition variable
    r = sr.Recognizer()

    #Creates a variable that holds the master name, or the controller of alexa. For further use..in wishme()
    MASTER = "Josue"

    #Covid library variable
    covid = Covid()


    #Send email variable
    hr = imdb.IMDb()

    #Variable for the bible command. (FreeBible library)
    web = read_web()

    #Stablishes the main voice of alexa.
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # engine.say('Initializing your voice assistant')
    engine.setProperty('voice', voices[1].id)

    #Define the wake words. In order to stablish when Alexa wakes up.
    def wakeWord(text):
            WAKE_WORDS = ['hi alexa', 'alexa turn on', 'good morning alexa', 'good night alexa']

            text = text.lower()

            for phrase in WAKE_WORDS:
                if phrase in text:
                    return True
                #wake word isnt find in the text from the loop
            return False

    #Possible variable that allows alexa to speak in format of an audio file, and later delete that audio file.
    def speak(audio_string):
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 10000000)
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)

    #Define the variable that will allow Alexa to recognize our voice and transform it into text. Main return: query
    def record_audio(ask = False):
        with sr.Microphone() as source:
            if ask:
               speak(ask)
            audio = r.listen(source)
            query = ''
            try:
                query = r.recognize_google(audio)
            except sr.UnknownValueError:
                speak('Sorry, I couldnt understand you well.. please try again')
            except sr.RequestError:
                speak('Sorry, my database is down')
                exit()
            return query

    #The first command word to make alexa function. Hi alexa. That is the two words.
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = "hi alexa"
            try:
                said = r.recognize_google(audio, language="en-us")
            except Exception as e:
                main()
                 #print("Exception:", str(e))

            return said.lower()

    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
    classes = []
    with open('coco.names', 'r') as f:
        classes = f.read().splitlines()

    cap = cv2.VideoCapture(0)
    #img = cv2.imread('image.jpg')

    while True: 
        _, img = cap.read()

        height, width, _ = img.shape

        blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
        net.setInput(blob)
        output_layers_names = net.getUnconnectedOutLayersNames()
        layerOutputs = net.forward(output_layers_names)

        boxes = []
        confidences = []
        class_ids = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)

                    x = int(center_x - w/2)
                    y = int(center_y - h/2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)


        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0, 255, size = (len(boxes), 3))

        if len(indexes)>0:
            for i in indexes.flatten():
                x, y, w, h = boxes [i]
                label = str(classes[class_ids[i]])
                confidence = str(round(confidences[i], 2))
                color = colors[i]
                cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
                inlabel = cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)
        if 'person' in label:
            break

        key = cv2.waitKey(1)
        if key == 27:
            break
            #From here, the logic for executing commands and complex tasks starts.
            #We make the machine to only receive the commands if you said Hi alexa. Thats why it has an if statement.
            # if 'hi alexa' in get_audio():
            #Speak function will pronounce the string which is passed to it
    def speak(text): 
        engine.say(text)
        engine.runAndWait()

    #This funciton will wish you as per the given time
    
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("Nice to have you back! How can I help you?")
        
            # break
        
        

    #This funciotn will take commands from your mic
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Processing...")
            query = r.recognize_google(audio, language = 'en-us')
            print(f"user said: {query}\n")

        except Exception as e:
            print("Please repeat. I couldnt understand what you said...")
            query = None
            
        return query

    #Un comment the line 162 if you want to have Alexa speaking each time it turns on.
    #speak("Initializing Alexa...")

    # wishMe()
    query = takeCommand()

    #The tasks lists starts here. All the tasks that Alexa can make. Read the "README" file to know exactly what to say for performing each tasks.
    def respond(query):

        if 'wikipedia' in query.lower():
            
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)

        if 'thanks' in query.lower():

            speak('Your Welcome Josue, do you need something else?')
            resul = takeCommand()
            if 'yes' in resul.lower():
                speak("Alright, tell me what do you need..." + MASTER)
                cmd = query

            if 'no' in resul.lower():
                speak("Alright, its been a pleasure to work with you today...bye!")
                main()

        elif "open bible" in query.lower():

            #Read the key_abbreviations_english.xlsx to know the extensions of the bible books
            
            libro = speak("What book of the bible do you want to search for?. Please enter your answer in the command prompt")
            bible = input("Please enter here the book of the bible that you want to search for:   ")
            capitulo_1 = speak("What chapter of" + bible)
            capitulo_2 = speak("do you want to search for?")
            capitulo = input("Please enter the chapter of the book that you want to search for:   ")
            res_1 = speak('What verse of'+bible+capitulo)
            res_2 = speak("do you need to search for?")
            versiculo = input("Please enter here the verse of the chapter that you want to search for:   ")
            output = (web[bible][capitulo][versiculo])
            print(output.text)
            speak('The lord says: ')
            speak(output.text)
            sentence_trans = str(output.text)
            translator_2 = Translator()
            translated_sentence_2 = translator_2.translate(sentence_trans, src='en', dest='es')
            print(translated_sentence_2.text)
            speak("Amen")

        elif 'open vanisio' in query.lower():
            
            url = "https://vanis.io/?thx4playingAlis"
            webbrowser.get().open(url)
            speak('Good luck!')

        elif 'open youtube' in query.lower():
            
            url = "https://youtube.com"
            webbrowser.get().open(url)
            speak('Have fun watching your favorite videos!')

        elif 'play music' in query.lower():
            
            subprocess.Popen("C:\\Users\\gaibo\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify")
            speak('Enjoy your favorite music!')
            
        elif 'time' in query.lower():
            
            string_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {string_time}")

        elif 'coronavirus total cases' in query.lower():
            
            total_Cases = speak("the total active cases are: ") 
            speak(covid.get_total_active_cases())
            print(covid.get_total_active_cases())

        if 'translate' in query.lower():
            while True:
                speak("Type in the command prompt the sentence or word you want to translate....  ")
                sentence = str(input("Please, type what you need to translate here....  "))
                translator = Translator()
                translated_sentence = translator.translate(sentence, src='es', dest='en')
                speak('Your translated sentence or word is: ')
                speak(translated_sentence.text)
                print(translated_sentence.text)

        if 'short url' in query.lower():

            while True:
                speak("Please enter the link you want to shortener in your command prompt")
                link = input("Enter the link here to start the process:  ")
                shortener = pyshorteners.Shortener()
                x = shortener.tinyurl.short(link)
                print(x)
                speak("Your url was shortened")

        if 'watch videos' in query.lower():
            
            speak("What is the title of the video that you want to search for?")
            video_searcher = takeCommand()

            PATH = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(PATH)

            driver.get('https://www.youtube.com/')

            search_1 = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')

            search_1.send_keys(video_searcher)

            searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            searchButton.click()

            driver.implicitly_wait(1)

            items = driver.find_element_by_class_name("style-scope ytd-video-renderer")
            items.click()

        elif 'record screen' in query.lower():
            
            speak("Screen Recording will start in 3 seconds")
            time.sleep(3)
            speak("Prees q, to save recording")
            screen_size = (1920,1080)
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            out = cv2.VideoWriter("output.avi",fourcc,20,0,(screen_size))
            while True:
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                out.write(frame)
                cv2.imshow("show", frame)
                if cv2.waitKey(1) == ord("q"):
                    break

            speak("Recording ended")

        elif 'coronavirus total recovered' in query.lower():
            
            total_recovered = speak("the total recovered cases are: ") 
            speak(covid.get_total_recovered())
            print(covid.get_total_recovered())

        elif 'coronavirus total deaths' in query.lower():
            
            total_deaths = speak("the total deaths are: ")
            speak(covid.get_total_deaths())
            print(covid.get_total_deaths())

        elif 'coronavirus information' in query.lower():
            
            alexa_question = speak("From which country do you need the information?")
            pais = takeCommand()
            speak("The data was found, now I will tell you what my database found ")
            cases = speak(covid.get_status_by_country_name(pais))
            # for x in cases:
            #     print(x, ":", cases[x])
            print(covid.get_status_by_country_name(pais))

        elif 'open code' in query.lower():
            
            subprocess.Popen("C:\\Users\\gaibo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            speak('Alright!, have a nice day')

        if "weather" in query.lower():
            
            driver = webdriver.Chrome()
            ask_for_city = speak("From what city do you need the weather forecast?")
            city = takeCommand()
            try:
                driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
                print(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
                speak("driver.find_elements_by_class_name('b-forecast__table-description-content')[0].text")
            except:
                print("Something went wrong")
                speak("Something went wrong")

        if 'phone information' in query.lower():
            
            speak("Please enter the phone number in your command prompt")
            number = input("Please enter the phone number here:  ")
            ch_nmber = phonenumbers.parse(number, 'CH')
            print(geocoder.description_for_number(ch_nmber, "en"))
            service_nmbr = phonenumbers.parse(number, "RO")
            print(carrier.name_for_number(service_nmbr, "en"))
            speak("Phone data ended successfully")

        elif 'transform image' in query.lower():
            
            speak("Please confirm that the image you want to transform to scketch is in this folder...")
            speak("Also, please check that in the source code of my database in the line 269 the name of the image is placed correctly")
            #!!!!!!!!!!!!!!!!!!!!!!!
            img = "NAME OF THE FILE"
            #!!!!!!!!!!!!!!!!!!!!!!!
            def grayscale(rgb):
                return np.dot(rgb[..., :3],[0.299,0.587,0.114])
            def dodge(front,back):
                result = front*255/(255-back)
                result[result>255]=255
                result[back==255]=255
                return result.astype('uint8')
            j = imageio.imread(img)
            g = grayscale(j)
            i = 255-g 
            b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
            r = dodge(b,g)
            cv2.imwrite('output.png', r)
            speak("The picture has been transformed succesfully")

        if 'open webcam' in query.lower():
            
            captura = cv2.VideoCapture(0)                           # Webcam 1,2,3
            while True:
                ret, frame = captura.read()

                cv2.imshow('Salida',frame)
                k = cv2.waitKey(24)&0xFF
                if k == 27:
                    break

            captura.release()
            cv2.destroyAllWindows()

        elif 'send email' in query.lower():
            
            EMAIL_ADRESS = "gaiborjimenezjosue@gmail.com"
            EMAIL_PASSWORD = "GOE2005@"

            speak("Sure, what is the subject of the email that you want to send?")

            subject_1 = takeCommand()

            msg = EmailMessage()
            msg['Subject'] = subject_1
            msg['From'] = EMAIL_ADRESS

            speak("Excelent, what is the body of the email that you want to send?")

            body_1 = takeCommand()

            # if 'type' in takeCommand():
            #     type_the_body = input("Please enter here the body of your email:  ")

            #     speak("Please enter the destinatary of your email in the command prompt")
            #     def receiver_1():
            #         recievers = input("Please enter here the destinatary of the email:   ")

            #     msg['To'] = receiver_1()

            #     msg.set_content(type_the_body)

            #     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            #         smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
            #         speak("Do you want to send the email?")
            #         answer = takeCommand()
            #         smtp.send_message(msg)
            #         speak("Email has been sent successfully!")
            msg.set_content(body_1)
            speak("Please enter the email adress of the destination in your command prompt")
            receiver_2 = input('Please enter the email here:   ')
                
            msg['To'] = receiver_2
            msg.set_content(body_1)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                speak('Do you want to send the email?')
                answer = takeCommand()
                if 'yes' in takeCommand():
                    smtp.send_message(msg)
                    speak("Email has been sent successfully!")

        if 'send file' in query.lower():
            
            EMAIL_ADRESS = "gaiborjimenezjosue@gmail.com"
            EMAIL_PASSWORD = "GOE2005@"

            speak("Sure, what is the subject of the email that you want to send?")

            subject_1 = takeCommand()

            msg = EmailMessage()
            msg['Subject'] = subject_1
            msg['From'] = EMAIL_ADRESS

            speak("Excelent, what is the body of the email that you want to send?")

            body_1 = takeCommand()

            msg.set_content(body_1)
            speak("Please enter the email adress of the destinatation in your command prompt")
            receiver_2 = input('Please enter the email here:   ')
                
            msg['To'] = receiver_2
            msg.set_content(body_1)
            speak("Please confirm that the file is in the same folder that in my database code")
            #!!!!!!!!!!!!!!!!!!!!!!!!!
            files = ['pdfexamples.pdf']
            #!!!!!!!!!!!!!!!!!!!!!!!!!
            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    # file_type = imghdr.what(f.name)
                    file_name = f.name
                
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                speak("File attached succesfullu")
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                speak('Do you want to send the email?')
                answer = takeCommand()
                if 'yes' in takeCommand():
                    smtp.send_message(msg)
                    speak("Email has been sent successfully!")

        elif 'search' in query.lower():
            
            question = speak('What do you need to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Sure Josue, google will open soon!')
        
        if 'movie information' in query.lower():
            
            speak("Please say the name of the movie that you need to find the description")
            movie_search = takeCommand()
            movies = hr.search_movie(str(movie_search))
            index = movies[0].getID()
            movie = hr.get_movie(index)
            title = movie['title']
            year = movie ['year']
            cast = movie ['cast']
            list_of_cast = ','.join(map(str,cast))
            speak("Please read your command prompt output for the movie description")
            #print the results
            print("title: ", title)
            print("year of release: ", year)
            print("full cast : ", list_of_cast)
            speak("Research has ended successfully")

        elif "open word" in query.lower():
            
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
            speak('Okay...word opening!')

        elif "open excel" in query.lower():
            
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            speak("Excel is opening...")

        elif "open power point" in query.lower():
            
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            speak("PowerPoint is opening...")

        elif "open pdf" in query.lower():
            
            subprocess.Popen("C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe")
            speak("Acrobat reader is opening...")

        elif "calculate" in query.lower():
            while True:
                speak("What is the first number?")
                f_1 = float(takeCommand())
                speak("What is the operator?")
                op = takeCommand()
                speak("What is the second number?")
                f_2 = float(takeCommand())

                if "addition" in op.lower():
                    print(f_1 + f_2)
                    speak(f_1 + f_2)



                if "substraction" in op.lower():
                    print(f_1 - f_2)
                    speak(f_1 - f_2)


                
                if "multiplication" in op.lower():
                    print(f_1 * f_2)
                    speak(f_1 * f_2)



                if "division" in op.lower():
                    print(f_1 / f_2)
                    speak(f_1 / f_2)


                    
                # else:
                #     print("Invalid sintax")
                #     break
                
                break
            
        elif "turn off" in query.lower():
            speak('Turning off...see you soon, bye'+ MASTER)
            quit()
        
        elif " " in query.lower():
            main()

        elif "school" in query.lower():
            
            url_school = "https://cebi.schoology.com/home"
            webbrowser.get().open(url_school)

            speak("Have a nice school day!")

        elif "space livestream" in query.lower():
            
            result = speak("'Awesome Josue!, im happy to show you mars space video, enjoy it!'")
            url_nasa = 'https://www.nasa.gov/nasalive'
            webbrowser.get().open(url_nasa)

    #Create a while statement to loop the main variables.
    while 1:
        query = record_audio()
        respond(query)
        get_audio()
                    
#Close the main loop. This will allow alexa to restart each time it finishes a task. So you can keep the task performing on.
main()