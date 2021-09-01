"""
archivo=open("archivo.txt","w")
archivo.write("----------------\n")
archivo.write("Mi nombre es Daniel")
archivo.close()
"""
agenda=[]

def guardar_archivo():
  agenda_file=open("agenda.atm","w")
  for i in range (len(agenda)):
    agenda_file.write(agenda[i][0]+";"+agenda[i][1]+";"+agenda[i][2]+"\n")
  agenda_file.close()

try:
  agenda_read=open("agenda.atm","r")
  while True:
    contacto_readed=agenda_read.readline()
    if len(contacto_readed)==0:
     break
    contacto_convertido=contacto_readed.split(";")
    contacto_convertido[2]=contacto_convertido[2].replace("\n","")
    agenda.append(contacto_convertido)
  agenda_read.close()
except:
  pass

while True:
  print("Qué quieres hacer? \n 1) Leer agenda \n 2) Crear un contacto \n 3) Salir")
  respuesta=int(input())
  if respuesta==3:
    break
  elif respuesta==1:
    for i in range (len(agenda)):
      print(agenda[i])
  elif respuesta==2:
    print("Dame el nombre del conacto")
    nombre=input()
    print("Dame el teléfono del conacto")
    telefono=input()
    print("Dame el correo del contacto")
    correo=input()
    contacto=[nombre,telefono,correo]
    agenda.append(contacto)
    guardar_archivo()
    