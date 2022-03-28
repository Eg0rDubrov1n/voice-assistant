import speech_recognition as sr
import os
import pyttsx3
import webbrowser as wb
from datetime import datetime
import requests
from bs4 import BeautifulSoup
opts = {
    "alias": ('Алиса','Кеш','Джарвис'),
    "tbr": ('скажи','расскажи','покажи','сколько','Сколько','произнеси'),
    "goodbye":("до свидания","пока"),
    "time":("время"),
    "newFolder":("новая папка","создать папку"),
    "deleteFolder":("удалить папку"),
    "newFile":("новый файл","создать файл"),
    "WriteToFile":("Запиши в файл"),
    "deleteFile":("удалить файл"),
    "NEWS":("новости"),
    "openProgrammFileExe":("открой","Открой"),
    "HELP":("на помощь","помоги")
}
path = os.path.join(os.path.join(os.path.expanduser('~')),'Desktop\\')


    # -------------------------------------------------------
    #Сказать что либо fd = f.read()
    # -------------------------------------------------------
# class User:
#     def __init__():
#         my_file = open('__info__.txt', "a+")
#         my_file.write(name+\n)
#         my_file.close()
#     def __init__():
    # def writeToInfoInTheMainFile()
class Microphone:
    def Speak(What):
            speak=pyttsx3.init()
            speak.say(What)
            speak.runAndWait()
        # -------------------------------------------------------
        # все устройства
        # -------------------------------------------------------
    def Device(self):
            mic=sr.Microphone()
            list_mic=sr.Microphone.list_microphone_names()
            for i in range(0,len(list_mic)):
                print(i,list_mic[i])
        # -------------------------------------------------------
        # Ввод данных с микро
        # -------------------------------------------------------
    def ReadingInformationFromMicro():
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:#ждем даных с микро
                print("Say something!")
                audio = recognizer.listen(source)
            return recognizer,audio
        # -------------------------------------------------------
        # Переодим данные с микро в строку
        # -------------------------------------------------------
    def ConvertDataFromMicroToString(recognizer,audio):
        try:
            string=recognizer.recognize_google(audio,language="ru-RU")
            if string.startswith(opts["alias"]):
                for x in opts['alias']:
                    string = string.replace(x, "").strip()
                for x in opts['tbr']:
                    string = string.replace(x, "").strip()
                print(string)
                return string,1
            return string,0
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None",0
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None",0


    def dataFromMicro():
            recognizer,audio=Alisa.ReadingInformationFromMicro()
            convertedSignalFromMicro,theyTurnedToMe=Alisa.ConvertDataFromMicroToString(recognizer,audio)
            return convertedSignalFromMicro
    def dataFromMicroAndtheyTurnedToMe():
            recognizer,audio=Alisa.ReadingInformationFromMicro()
            convertedSignalFromMicro,theyTurnedToMe=Alisa.ConvertDataFromMicroToString(recognizer,audio)
            return convertedSignalFromMicro,theyTurnedToMe

class Alisa(Microphone):
        # -------------------------------------------------------
        #Поиск в Google
        # -------------------------------------------------------
    def GoogleSearch():

                Microphone.Speak("Говорите свой запрос")
                inquiry=Microphone.dataFromMicro()
                Microphone.Speak("Веду поиск")
                wb.open('http://www.google.com/search?q=' + inquiry)

        # -------------------------------------------------------
        #Time
        # -------------------------------------------------------
    def Time():
            current_datetime = datetime.now()
            Microphone.Speak(str(current_datetime.hour)+"часов"+str(current_datetime.minute)+"минут")   
            
        # -----------------------------------------------------------------------------
    def Yendexnews():
            url="https://yandex.ru/news/"
            r=requests.get(url)
            soup=BeautifulSoup(r.text,'lxml')
            films=soup.findAll('div',class_='mg-grid__col mg-grid__col_xs_4')
            for i in range(len(films)):
                Microphone.Speak(films[i])
     # -----------------------------------------------------------------------------
    def newFolder():
            try:
                Microphone.Speak("Говорите имя папки")
                
                os.mkdir(path+Microphone.dataFromMicro())
                Microphone.Speak("Папка создана")
            except:
                print("Ошибка эта папка уже существует")        
    def deleteFolder():
            try:
                Microphone.Speak("Говорите имя папки")
                os.rmdir(path+Microphone.dataFromMicro())
                Microphone.Speak("Папка удалена")
            except:
                print("Ошибка такой папки нет")
    def newFile():
            try:
                Microphone.Speak("Говорите имя файла")
                my_file = open(path+Alisa.dataFromMicro()+'.txt', "w+")
                my_file.close()
                Microphone.Speak("файл СОЗДАН")
            except:
                print("Error")
    def WriteToFile():
            try:
                Microphone.Speak("Говорите имя файла")
                my_file = open(path+Microphone.dataFromMicro()+'.txt', "a+")
                Microphone.Speak("Записоваю")
                my_file.write(Microphone.dataFromMicro())
                my_file.close()
            except:
                print("Error")
    def deleteFile():
            try:
                Alisa.Speak("Говорите имя файла")
                os.remove(path+Microphone.dataFromMicro()+'.txt')
            except:
                print("Error")
    def passage(findThis, beginSearchThere):
        for dirpath, dirnames, filenames in os.walk(beginSearchThere):
            for filename in filenames:
                if(filename.find(".exe")!=-1):
                    # print(filename)
                    if (filename.lower() == findThis.lower()):
                        find = True
                        filesPath = '\''+ dirpath + '\''
                        return filesPath
        return None
    def openProgrammFileExe(sought):
        for x in opts['openProgrammFileExe']:
            sought = sought.replace(x, "").strip()
        a=Alisa.passage(sought+'.exe', "D:\\")
        if(a!=None):
            a=a.translate({ord('\''): None})
            os.startfile(a+"\\"+sought+'.exe')
            Microphone.Speak("Готово")
            return 1
        a=Alisa.passage(sought+'.exe', "C:\\")
        if(a!=None):
            a=a.translate({ord('\''): None})
            os.startfile(a+"\\"+sought+'.exe')
            Microphone.Speak("Готово")
            return 1
        else:
            print("None")
        return 0


    def HELP():
        print(opts)
        #-----------------------------------------------------------------------------
    def start(self):
            Microphone.Speak("Здравствуйте ваше привосходительство")         
            while(True):
                while(True):
                    convertedSignalFromMicro,theyTurnedToMe=Microphone.dataFromMicroAndtheyTurnedToMe()
                    if(theyTurnedToMe==1):
                        break
                if(convertedSignalFromMicro.startswith(opts["goodbye"])):
                    Alisa.Speak("Прощайте мой господин")
                    break

                elif(convertedSignalFromMicro=="Google"):
                    Alisa.GoogleSearch()
            # ----------------------------------------------------------------------------------------------------
                elif(convertedSignalFromMicro.startswith(opts["time"])):
                    Alisa.Time()
            # ----------------------------------------------------------------------------------------------------
                elif(convertedSignalFromMicro.startswith(opts["newFolder"])):
                    Alisa.newFolder()
            # ----------------------------------------------------------------------------------------------------
                elif(convertedSignalFromMicro.startswith(opts["deleteFolder"])):
                    Alisa.deleteFolder()
            # ----------------------------------------------------------------------------------------------------
                elif(convertedSignalFromMicro.startswith(opts["newFile"])):
                    Alisa.newFile()
            # ----------------------------------------------------------------------------------------------------
                elif(convertedSignalFromMicro.startswith(opts["WriteToFile"])):
                    Alisa.WriteToFile()
            # ----------------------------------------------------------------------------------------------------
                elif(convertedSignalFromMicro.startswith(opts["deleteFile"])):
                    Alisa.deleteFile()
                elif(convertedSignalFromMicro.startswith(opts["NEWS"])):
                    Alisa.Yendexnews()
                elif(convertedSignalFromMicro.startswith(opts["openProgrammFileExe"])and len(convertedSignalFromMicro)>len(opts["openProgrammFileExe"][0])):    
                    Alisa.openProgrammFileExe(convertedSignalFromMicro)
                elif(convertedSignalFromMicro.startswith(opts["HELP"])):
                    Alisa.HELP()
ClassName1=Alisa() 
ClassName1.start() 