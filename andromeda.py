
from simple_facerec import SimpleFacerec
import cv2


def main(name):
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
    import numpy as np
    import pyautogui
    import imdb
    import phonenumbers
    # from Testphone import number
    from phonenumbers import geocoder
    from phonenumbers import carrier
    import numpy as np
    import imageio
    import scipy.ndimage
    import cv2
    from email.message import EmailMessage
    import imghdr
    from freebible import read_web
    from selenium import webdriver
    import pyowm
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    print("Empezando Andromeda...")

    # Creates a variable that holds the master name, or the controller of alexa. For further use..in wishme()
    MASTER = name

    # Covid library variable
    covid = Covid()

    # Send email variable
    hr = imdb.IMDb()

    # Variable for the bible command. (FreeBible library)
    web = read_web()
    # Stablishes the main voice of alexa.
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # engine.say('Initializing your voice assistant')
    engine.setProperty('voice', voices[2].id)

    def takeCommand():

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Processing...")
            answer_2 = r.recognize_google(audio, language='es-ES')
            print(f"user said: {answer_2}\n")

        except sr.UnknownValueError:
            speak('Perdon, no te pude entender muy bien. Porfavor intenta nuevamente')
            respond()

        except sr.RequestError:
            speak('Sorry, my database is down')
            exit()

        return answer_2

    if 1 == 1:

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def wishMe():
            hour = int(datetime.datetime.now().hour)

            if hour >= 0 and hour < 12:
                speak("Buenos dias" + MASTER)

            elif hour >= 12 and hour < 18:
                speak("Buenas tardes" + MASTER)

            else:
                speak("Buenas noches" + MASTER)

            speak("Un gusto tenerlo de vuelta, como podria ayudarlo?")

        wishMe()

        def respond():
            query = takeCommand()

            if 'wikipedia' in query.lower():
                wikipedia.set_lang("es")
                speak('buscando wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)

            elif "abre la biblia" in query.lower():
                libro = speak(
                    "Que libro de la biblia necesitas que encuentre por ti? Porfavor escribe el libro biblico en ingles y en el cmd de tu computadora")
                bible = input(
                    "Ingresa aqui el libro de la biblia en ingles:   ")
                capitulo_1 = speak("Que capitulo de" +
                                   bible + "quieres encontrar")
                capitulo = input(
                    "Porfavor ingresa aqui el capitulo del libro biblico que quieres encontrar:   ")
                res_1 = speak('Que versiculo de'+bible +
                              capitulo + "quieres encontrar?")
                versiculo = input(
                    "Porfavor ingresa aqui el versiculo de la biblia que quieres encontrar:   ")
                output = (web[bible][capitulo][versiculo])
                print(output)
                speak('La palabra de Dios dice: ')
                sentence_trans = str(output)
                translator_2 = Translator()
                translated_sentence_2 = translator_2.translate(
                    sentence_trans, src='en', dest='es')
                print(translated_sentence_2.text)
                speak(translated_sentence_2.text)
                speak("Amen")
                respond()

            elif 'abre juego' in query.lower():
                url = "https://vanis.io/?thx4playingAlis"
                webbrowser.get().open(url)
                speak('Buena suerte!')

            elif 'videos' in query.lower():

                speak("What is the title of the video that you want to search for?")
                video_searcher = takeCommand()

                PATH = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(PATH)

                driver.get('https://www.youtube.com/')

                search_1 = driver.find_element_by_xpath(
                    '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')

                search_1.send_keys(video_searcher)

                searchButton = driver.find_element_by_xpath(
                    '//*[@id="search-icon-legacy"]')
                searchButton.click()

                driver.implicitly_wait(1)

                items = driver.find_element_by_class_name(
                    "style-scope ytd-video-renderer")
                items.click()

            elif 'pon musica' in query.lower():
                subprocess.Popen(
                    "C:\\Users\\gaibo\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify")
                speak('Disfruta de tu musica favorita!')

            elif 'hora' in query.lower():
                string_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"{MASTER} la hora es {string_time}")

            elif 'casos totales de coronavirus' in query.lower():
                total_Cases = speak("los casos totales y activos son: ")
                speak(covid.get_total_active_cases())
                print(covid.get_total_active_cases())

            if 'traduce' in query.lower():
                speak(
                    "Porfavor, ingesa la oracion o palabra que quieres que traduzca en el cmd de tu computadora... ")
                sentence = str(
                    input("Ingresa aqui la oracion o palabra que quieres traducir:  "))
                translator = Translator()
                translated_sentence = translator.translate(
                    sentence, src='es', dest='en')
                speak('Tu oracion o palabra traducida es: ')
                speak(translated_sentence.text)
                print(translated_sentence.text)

            if 'reducir el link' in query.lower():
                speak(
                    "Porfavor ingresa el link que quieres reducir en el cmd de tu computadora.")
                link = input("Ingresa aqui el link: ")
                shortener = pyshorteners.Shortener()
                x = shortener.tinyurl.short(link)
                print(x)
                speak("Tu url fue reducido con exito!")

            elif 'graba la pantalla' in query.lower():
                speak("La grabacion de la pantalla comenzara en tres segundos.")
                time.sleep(3)
                speak("Presiona Q para guardar la grabacion")
                screen_size = (1920, 1080)
                fourcc = cv2.VideoWriter_fourcc(*"XVID")
                out = cv2.VideoWriter(
                    "output.avi", fourcc, 20, 0, (screen_size))
                while True:
                    img = pyautogui.screenshot()
                    frame = np.array(img)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    out.write(frame)
                    cv2.imshow("show", frame)
                    if cv2.waitKey(1) == ord("q"):
                        break

                speak("Grabacion terminada")

            elif 'recuperaciones totales del coronavirus' in query.lower():
                total_recovered = speak(
                    "Los casos totales que se han recuperado son: ")
                speak(covid.get_total_recovered())
                print(covid.get_total_recovered())

            elif 'muertes totales por el coronavirus' in query.lower():
                total_deaths = speak(
                    "Los fallecimientos calculados por mi base de datos son: ")
                speak(covid.get_total_deaths())
                print(covid.get_total_deaths())

            elif 'covid' in query.lower():
                alexa_question = speak("De que pais necesitas la informacion?")
                pais = takeCommand()
                speak(
                    "La informacion fue encontrada exitosamente. Lo que mi base de datos obtuvo es: ")
                cases = speak(covid.get_status_by_country_name(pais))
                # for x in cases:
                #     print(x, ":", cases[x])
                print(covid.get_status_by_country_name(pais))

            elif 'abre codigo' in query.lower():
                subprocess.Popen(
                    "C:\\Users\\gaibo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                speak('Listo!, ten un buen dia.')

            if "clima" in query.lower():
                driver = webdriver.Chrome()
                ask_for_city = speak(
                    "De que cuidad necesitas el reportaje del clima?")
                city = takeCommand()
                try:
                    driver.get(
                        "https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
                    print(driver.find_elements_by_class_name(
                        "b-forecast__table-description-content")[0].text)
                    speak(
                        "driver.find_elements_by_class_name('b-forecast__table-description-content')[0].text")
                except:
                    print("Something went wrong")
                    speak("Something went wrong")

            if 'informacion del celular' in query.lower():
                speak(
                    "Porfavor ingresa el numero telefonico del cual necesitas informacion en el cmd de tu computadora.")
                number = input("Ingresa aqui el numero celular:  ")
                ch_nmber = phonenumbers.parse(number, 'CH')
                print(geocoder.description_for_number(ch_nmber, "en"))
                service_nmbr = phonenumbers.parse(number, "RO")
                print(carrier.name_for_number(service_nmbr, "en"))
                speak("Informacion recopilada exitosamente")

            elif 'transformar imagen' in query.lower():
                speak(
                    "Porfavor confirma que el archivo que quieres convertir este en la misma carpeta que mi codigo de fuente.")
                speak(
                    "Tambien, no te olvides de ingresar el nombre del archivo en el mismo codigo fuente de este comando.")
                #!!!!!!!!!!!!!!!!!!!!!!!
                img = "NAME OF THE FILE"
                #!!!!!!!!!!!!!!!!!!!!!!!

                def grayscale(rgb):
                    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

                def dodge(front, back):
                    result = front*255/(255-back)
                    result[result > 255] = 255
                    result[back == 255] = 255
                    return result.astype('uint8')
                j = imageio.imread(img)
                g = grayscale(j)
                i = 255-g
                b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
                r = dodge(b, g)
                cv2.imwrite('output.png', r)
                speak("La imagen ha sido transformada exitosamente.")

            if 'abre webcam' in query.lower():
                speak("Abriendo webcam")
                # Webcam 1,2,3
                captura = cv2.VideoCapture(0)
                while True:
                    ret, frame = captura.read()

                    cv2.imshow('Salida', frame)
                    k = cv2.waitKey(24) & 0xFF
                    if k == 27:
                        break

                captura.release()
                cv2.destroyAllWindows()

            elif 'send email' in query.lower():

                EMAIL_ADRESS = "gaiborjimenezjosue@gmail.com"
                EMAIL_PASSWORD = "GOE2005@"

                speak("Listo, cual es el titulo del email que quieres enviar?")

                subject_1 = takeCommand()

                msg = EmailMessage()
                msg['Subject'] = subject_1
                msg['From'] = EMAIL_ADRESS

                speak(
                    "Excelente, cual es el texto o contenido del email que quieres enviar?")

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
                speak(
                    "Porfavor ingresa el email del destinatario en el cmd de tu computadora")
                receiver_2 = input('Ingresa el email aqui: ')

                msg['To'] = receiver_2
                msg.set_content(body_1)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                    speak('Quieres enviar el email?')
                    answer = takeCommand()
                    if 'si' in takeCommand():
                        smtp.send_message(msg)
                        speak("El email ha sido enviado correctamente")

            if 'enviar archivo' in query.lower():
                EMAIL_ADRESS = "gaiborjimenezjosue@gmail.com"
                EMAIL_PASSWORD = "GOE2005@"

                speak("Listo, cual es el titulo del email que quieres enviar?")

                subject_1 = takeCommand()

                msg = EmailMessage()
                msg['Subject'] = subject_1
                msg['From'] = EMAIL_ADRESS

                speak(
                    "Excelente, cual es el contenido o texto del email que quieres enviar?")

                body_1 = takeCommand()

                msg.set_content(body_1)
                speak(
                    "Porfavor, ingresa el email del destinatario en el cmd de tu computadora")
                receiver_2 = input('Ingresa el email aqui: ')

                msg['To'] = receiver_2
                msg.set_content(body_1)
                speak(
                    "Porfavor confirma que el archivo esta en la misma ubicacion que mi codigo fuente.")
                #!!!!!!!!!!!!!!!!!!!!!!!!!
                files = ['pdfexamples.pdf']
                #!!!!!!!!!!!!!!!!!!!!!!!!!
                for file in files:
                    with open(file, 'rb') as f:
                        file_data = f.read()
                        # file_type = imghdr.what(f.name)
                        file_name = f.name

                    msg.add_attachment(
                        file_data, maintype='application', subtype='octet-stream', filename=file_name)
                    speak("Archvio adjuntado exitosamente!")

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                    speak('Quieres enviar el email?')
                    answer = takeCommand()
                    if 'si' in takeCommand():
                        smtp.send_message(msg)
                        speak("El email ha sido enviado correctamente!")

            elif 'buscar' in query.lower():
                question = speak('Que necesitas que investigue por ti?')
                search = takeCommand()
                url = 'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                speak('Excelente Josue, google se abrira muy pronto.')

            if 'informacion de una pelicula' in query.lower():
                speak("Porfavor dime el nombre de la pelicula que quieres encontrar")
                movie_search = takeCommand()
                movies = hr.search_movie(str(movie_search))
                index = movies[0].getID()
                movie = hr.get_movie(index)
                title = movie['title']
                year = movie['year']
                cast = movie['cast']
                list_of_cast = ','.join(map(str, cast))
                speak(
                    "Porfavor, lee la descripcion de la pelicula en el cmd de tu computadora")
                # print the results
                print("title: ", title)
                print("year of release: ", year)
                print("full cast : ", list_of_cast)
                speak("La investigacion ha culminado exitosamente")

            elif "abre word" in query.lower():
                subprocess.Popen(
                    'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
                speak('okey...word se esta abriendo.')

            elif "abre pdf" in query.lower():
                subprocess.Popen(
                    "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe")
                speak("Acrobat reader se esta abriendo...")

            elif "abre power point" in query.lower():
                subprocess.Popen(
                    "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                speak("PowerPoint se esta abriendo...")

            elif "abre excel" in query.lower():
                subprocess.Popen(
                    "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
                speak("Excel se esta abriendo...")

            elif "calculadora" in query.lower():
                while True:
                    speak("Cual es el primer numero?")
                    f_1 = float(takeCommand())
                    speak("Cual es el operador?")
                    op = takeCommand()
                    speak("Cual es el segundo numero?")
                    f_2 = float(takeCommand())

                    if "suma" in op.lower():
                        print(f_1 + f_2)
                        speak(f_1 + f_2)

                    if "resta" in op.lower():
                        print(f_1 - f_2)
                        speak(f_1 - f_2)

                    if "multiplicacion" in op.lower():
                        print(f_1 * f_2)
                        speak(f_1 * f_2)

                    if "division" in op.lower():
                        print(f_1 / f_2)
                        speak(f_1 / f_2)

                    # else:
                    #     print("Invalid sintax")
                    #     break

                    break

            if "apagar" in query.lower():
                speak('Apagando mis sistemas, nos vemos pronto' + MASTER)
                quit()

            # elif " " in query.lower():
            #     main()

            elif "plataforma" in query.lower():
                url = "https://cebi.schoology.com/"
                webbrowser.get().open(url)
                speak('Ten un bonito dia de clases!')

            elif 'gracias' in query.lower():
                speak('De nada josue, necesitas algo mas que haga por ti?')
                res = takeCommand()
                if 'si' in res:
                    speak("Claro, dime que necesitas que haga por ti" + MASTER)
                elif 'no' in res:
                    speak(
                        "Esta bien, fue un placer atender tus necesidades y requerimientos el dia de hoy... nos vemos pronto!")
                else:
                    main()

            elif "nasa" in query.lower():
                result = speak(
                    "Excelente, disfruta de la transmision en vivo!")
                url_nasa = 'https://www.nasa.gov/nasalive'
                webbrowser.get().open(url_nasa)

        while 1:
            respond()


# Part of this code (Facial recognition) is not completely mine, it was created by Pysource: https://pysource.com I added some custom code to satisfy my needs.
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(1)

counter = 0

while True:
    ret, frame = cap.read()
    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    if face_names == ['Edward Gaibor']:
        counter += 1
        if counter == 3:
            cap.release()
            main("Edward Gaibor")
    if face_names == ['Yadira Gaibor']:
        counter += 1
        if counter == 3:
            cap.release()
            main("Yadira Gaibor")
    if face_names == ['Sarahi Gaibor']:
        counter += 1
        if counter == 3:
            cap.release()
            main("Sarahi Gaibor")
