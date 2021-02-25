import telepot
import picamera
import os
import time
import datetime
from telepot.loop import MessageLoop
from time import sleep
import RPi.GPIO as GPIO
import mysql.connector
from subprocess import call

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def handle(msg):
  global sendPhoto
  global sendVideo
  global chat_id
  
  chat_id = msg['chat']['id']
  command = msg['text']
  
  print('Message received from ' + str(chat_id))
  
  lenght2=len(command)
  #print(str(lenght2))
  #print(command[8:lenght2])
       
  
  if command == '/photo':
    sendPhoto = True
  
  elif command == '/start':
    bot.sendMessage(chat_id, 'Welcome to Dinear Petshop Bot\n\n''List of Command yang dapat Anda gunakan :\n\n'
                    '/photo untuk memfoto hewan hewan anda\n''/video untuk memvideokan hewan anda dengan video player eksternal seperti VLC\n'
                    '/status untuk menginfokan status preawatan yang telah diberikan\n''/time meng-infokan  waktu dan tanggal didenear petshop\n'
                    '/contact nomor telepon Dinear Petshop\n''/info List of Command sebagai command untuk interaksi dengan bot Dinear Petshop')

  elif command == '/contact':
     bot.sendMessage(chat_id, '(021)4600480')
     
  elif command == '/info':
     bot.sendMessage(chat_id, 'List of Command yang dapat Anda gunakan :\n\n'
                    '/photo untuk memfoto hewan hewan anda\n''/video untuk memvideokan hewan anda dengan video player eksternal seperti VLC\n'
                    '/status untuk menginfokan status preawatan yang telah diberikan\n''/time meng-infokan  waktu dan tanggal didenear petshop\n'
                    '/contact nomor telepon Dinear Petshop\n''/info List of Command sebagai command untuk interaksi dengan bot Dinear Petshop')  
    
  elif command == '/video':
    sendVideo= True

  elif command == '/time':
       bot.sendMessage(chat_id, str(datetime.datetime.now()))

  elif lenght2==7 and command == '/status':
        bot.sendMessage(chat_id, 'Ketikkan /status/[id]')

  elif lenght2>7 and command[0:8] == '/status/':
        cnx = mysql.connector.connect(user='root', password='your-root-password',
                              host='192.168.8.105',database='percobaan')

        command = command[8:lenght2]
        print('Message received from ' + str(command))
        cursor = cnx.cursor()
        #command = 'Reg01Ag'
        sql = "SELECT Status_Hewan FROM  petshop WHERE Kode_Pemilik= '%s'" %command
        cursor.execute(sql)
        results = cursor.fetchall()
        for data in results:
            print(data)
            bot.sendMessage(chat_id, results)
  else:
    bot.sendMessage(chat_id, 'Invalid command.')

def capture():
  print('Capturing photo...')
  camera = picamera.PiCamera()
  camera.start_preview()
  camera.rotation = 180
  sleep(5)
  camera.capture('./testt.jpg')
  camera.stop_preview()
  camera.close()
  print('Sending photo to ' + str(chat_id))
  bot.sendPhoto(chat_id, photo = open('./testt.jpg','rb'))


def recording():
  print('Capturing video...')
  camera = picamera.PiCamera()
  camera.start_preview()
  camera.rotation = 180
  camera.framerate = 25
  camera.start_recording('/home/pi/berhasil.h264')
  sleep(5)
  camera.stop_recording()
  camera.stop_preview()
  camera.close()
  your_command = "MP4Box -add berhasil.h264 berhasil.mp4" 
  call ([your_command], shell=True)
  print('Sending video to ' + str(chat_id))
  bot.sendVideo(chat_id, video = open('/home/pi/berhasil.mp4'))
  sleep(3)
  os.remove("berhasil.mp4")

bot = telepot.Bot('866250563:AAGJ3WhzwRsm-dUuzmpBB6elnBccXEUAG1o')
bot.message_loop(handle)

print('Bot ready!')

sendPhoto = False
sendVideo = False
try:
  while True:
    if sendPhoto == True:
      sendPhoto = False
      capture()
    elif sendVideo == True:
      sendVideo = False
      recording()       

except KeyboardInterrupt:
  GPIO.cleanup()

