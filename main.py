# Importaciones
from machine import Pin as pin
import utime
from time import localtime
from machine import PWM
import time 
import json
import urequests
import network
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME
import ufirebase as firebase


# Relay
rel=pin (14,pin.OUT)
ledAbierto=pin (22,pin.OUT)
ledCerrado=pin (26,pin.OUT)

#Funcion Hora
def hora():
    #while True:
        hora=f"{localtime()[3]}:{localtime()[4]}:{localtime()[5]}"
        fecha=f"{localtime()[2]}/{localtime()[1]}/{localtime()[0]}"
        registroHora = print (f"la hora del ingreso a la vivienda es:  {hora} del día {fecha}" )
        firebase.put("Seguridad/registroHoraESP", hora, bg=0)
        print ("envio el dato", hora)
        rel.value(1)
        utime.sleep(500)
        borradoDatos()
        #utime.sleep(0)
        #utime.sleep
        #rel.init(14,pin.OUT,value=0)
        #rel.off(0)
        
#Función envio data a Firebase        
def envioDatos():
  firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
  firebase.get("Seguridad/registroAndroidVersion", "registroAndroidVersion")
  registroAndroidVersion=(str(firebase.registroAndroidVersion))
  print(registroAndroidVersion)
  firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
  firebase.get("Seguridad/registroFlag", "registroFlag")
  registroFlag =(int(firebase.registroFlag))
  print(registroFlag)
  firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
  firebase.get("Seguridad/registroBoard", "registroBoard")
  registroBoard=(str(firebase.registroBoard))
  print(registroBoard)
  firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
  firebase.get("Seguridad/registroDeviceID", "registroDeviceID")
  registroDeviceID=(str(firebase.registroDeviceID))
  print(registroDeviceID)
  firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
  firebase.get("Seguridad/registroFingerprint", "registroFingerprint")
  registroFingerprint=(str(firebase.registroFingerprint))
  print(registroFingerprint)
  firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
  firebase.get("Seguridad/registroHardware", "registroHardware")
  registroHardware=(str(firebase.registroHardware))
  print(registroHardware)
  firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
  firebase.get("Seguridad/registroNumeroTel", "registroNumeroTel")
  registroNumeroTel=(str(firebase.registroNumeroTel))
  print(registroNumeroTel)

# firebase.put("Registro/Usuario", {"edades": [33,19,44], "area": "Tesorerea"}, bg=0)
  

#FUncion conexión Wifi
def wifi():
    print("Conectando al WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('JuanchoCPaez', 'a1b2c3d4')
    while not sta_if.isconnected():
      print(".", end="")
      time.sleep(0.1)
      led=pin (26,pin.OUT)
    print(" Connected!")
    envioDatos()


#FUncion para obtener datos
def obtenerDatos():
  
    firebase.get("Seguridad/registroImei","x")
    print(f"Registro Imei: {str(firebase.x)} ")
    firebase.put("Seguridad/registroHora", hora, bg=0)
    firebase.get("Seguridad/registroID","x")
    x=(int(firebase.x))
    IDReg = x + 1
    print(IDReg)
    firebase.put("Seguridad/registroID", IDReg, bg=0)
    
def borradoDatos():
   print("entro")
   borrado=0
   firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
   firebase.put("Seguridad/registroAndroidVersion", borrado)
   registroAndroidVersionPut=(str(firebase.registroAndroidVersionPut))
   print(registroAndroidVersionPut)
   firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
   firebase.put("Seguridad/registroFlag", borrado)
   registroFlagPut =(int(firebase.registroFlagPut))
   print(registroFlagPut)
   firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
   firebase.put("Seguridad/registroBoard", borrado)
   registroBoardPut=(str(firebase.registroBoardPut))
   print(registroBoardPut)
   firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
   firebase.put("Seguridad/registroDeviceID", borrado)
   registroDeviceIDPut=(str(firebase.registroDeviceIDPut))
   print(registroDeviceIDPut)
   firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
   firebase.put("Seguridad/registroFingerprint", borrado)
   registroFingerprintPut=(str(firebase.registroFingerprintPut))
   print(registroFingerprintPut)
   firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
   firebase.put("Seguridad/registroHardware", borrado)
   registroHardwarePut=(str(firebase.registroHardwarePut))
   print(registroHardwarePut)
   firebase.setURL("https://seguridad-d6b34-default-rtdb.firebaseio.com/")
   firebase.put("Seguridad/registroNumeroTel", borrado)
   registroNumeroTelPut=(str(firebase.registroNumeroTelPut))
   print(registroNumeroTelPut)
#Inicialización de las funciones
wifi()
obtenerDatos()


    
hora()


valorRegistroAndroidVersion 
valorRegistroBoard
valorRegistroDeviceID
valorRegistroFingerprint
valorRegistroFlag
valorRegistroHardware
valorRegistroHora
valorRegistroID
valorRegistroNumeroTel