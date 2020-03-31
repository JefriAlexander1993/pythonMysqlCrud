# -*- coding: utf-8 -*-
import os, sys
from six.moves import input
import pymysql
import getpass 

def main():
    os.system('clear')
    print("---------------------------------------------")
    print("                  Bienvenido                 ")
    print("---------------------------------------------")
    print("Selecciona cualquiera de las siguientes opciones")
    print("1. Registar usuario.")
    print("2. Ingresar al sistema.")
    print("3. Salir")
    
while True:
    main()
    opcion = input("Ingrese una opcion:" )
    if opcion == "1":
        os.system('clear')
        mydb =   pymysql.connect(host='localhost',user='root',passwd='',db='crudpython')
        cursor = mydb.cursor()
        print("---------------------------------------------")
        print("                    REGISTRO                 ")
        print("---------------------------------------------")
        sql = "INSERT INTO users (id,name,password) VALUES (%s, %s, %s)"
        id=int(input("Ingrese su id: \n"))
        name=input("Ingrese su usuario: \n ")
        password=getpass.getpass("Ingrese su password: \n ")

        c= "SELECT name FROM users WHERE id = %s OR name = %s OR password = %s;"
        user =  cursor.execute(c,(id,name,password))
           
        if  user !=1:
            cursor.execute(sql, (id,name, password))
            mydb.commit()
            print("El usuario se agregado exitosamente")
            mydb.close()  
        else: 
            print("El usuario existe, intenta ingresando otro id,usuario, contraseña.")
            exit()  

    elif opcion == "2":           
        
        print("---------------------------------------------")
        print("                    LOGIN                    ")
        print("---------------------------------------------")

        # aqui pide el nombre del usuario y lo guarda en una variable nombre
        name=input("Ingrese su usuario:  ")
         
        password=getpass.getpass("Ingrese tu contraseña:")

        # aqui imprime la informacion que el usuario metio

        # aqui hacemos una condicion  if para que el usuario
        # cumpla con el requisito de la edad minima para entrar


        mydb =   pymysql.connect(host='localhost',user='root',passwd='',db='crudpython')
         
        cursor = mydb.cursor()

        consulta = "SELECT name FROM users WHERE name = %s AND password = %s;"
        user =  cursor.execute(consulta,(name,password))


        if not user :
            print('Verificar Sr.'+ name + " si el usuario y la contraseña es correcta.")
            sys.exit()
        else:
            print("Bienvenido " + name)


        def menu():
                os.system('clear')
                print("---------------------------------------------")
                print("                     MENU                    ")
                print("---------------------------------------------")

                print("Selecciona cualquiera de las siguientes opciones ")
                print("1. Mostrar personas.")
                print("2. Insertar persona.")
                print("3. Editar persona")
                print("4. Ver persona")
                print("5. Eliminar persona")
                print("6. Modo administrativo")
                print("7. Salir")   
        while True:
            menu()
          
            opcionmenu = input("Ingrese una opcion:" )
           
            if opcionmenu == "1":
                os.system('clear')
                print("---------------------------------------------")
                print("            MOSTRAR  PERSONA                 ")
                print("---------------------------------------------")
              
                conn =  pymysql.connect(host='localhost',user='root',passwd='',db='crudpython')
         

                cur = conn.cursor()
                cur.execute("SELECT id, name, lastname, address, phone FROM person")
                
                for id, name, lastname, address, phone  in cur.fetchall():
                     print("---------------------------------------------")
                     print("Id :"+ str(id))
                     print("Nombre :"+ name)
                     print("Apellido :"+ lastname)
                     print("Direccion :"+address)
                     print("Telefono :"+ phone)
                   
                conn.close()
                input("Has pulsado la opción 2...\npulsa una tecla para continuar")

              
            elif opcionmenu == "2":
                os.system('clear')
                print("---------------------------------------------")
                print("            INSERTAR  PERSONA                ")
                print("---------------------------------------------")

                mydb =   pymysql.connect(host='localhost',user='root',passwd='',db='crudpython')
         
                mycursor = mydb.cursor()
         
                sql = "INSERT INTO person (id,name, lastname,address,phone) VALUES (%s, %s, %s, %s, %s)"
                
                id=int(input("Ingrese su id: \n"))
                name=input("Ingrese su nombre: \n ")
                lastname=input("Ingrese su apellido: \n ")
                address=input("Ingrese su direccion: \n ")
                phone=input("Ingrese su telefono: \n ")
         
                mycursor.execute(sql, (id,name, lastname,address,phone))
         
                mydb.commit()
                mydb.close()
         
                print(mycursor.rowcount, "record inserted.")
                input("Has pulsado la opción 1...\n pulsa una tecla para continuar")

            elif opcionmenu == "3":
                os.system('clear')
                print("---------------------------------------------")
                print("            EDITAR  PERSONA                  ")
                print("---------------------------------------------")
                mydb =   pymysql.connect(host='localhost',user='root',passwd='',db='crudpython')
         
                cursor = mydb.cursor()
                
                idp=int(input("Ingresa el id de la persona que deseas modificar: "))
                consulta = "SELECT id,name,lastname,address,phone FROM person WHERE id = %s;"
                id =  cursor.execute(consulta,(idp))
                if not id:
                  print("El id ingresado no conside con los registrados ")
                  break              
                else:
                  print("El id ingresado conside con la siguiente persona registrada ")
                  for id, name, lastname, address, phone  in cursor.fetchall():
                     print("---------------------------------------------")
                     print("Id :"+ str(id))
                     print("Nombre :"+ name)
                     print("Apellido :"+ lastname)
                     print("Direccion :"+address)
                     print("Telefono :"+ phone)
                print("---------------------------------------------")
                print("Deseas modificarlo 1. Si o 2. No\n")
                mod= input("Eligue tu opcion:")
                print("La opcion elegida es:" +mod)
                
                if mod !="1":
                  print("Haz elegido no actualizar")
                  break
                pass
                print("---------------------------------------------")
                print("Actualizar informacion de " + name)
                print("---------------------------------------------")
                
                name=input("Ingrese su nombre: \n ")
                lastname=input("Ingrese su apellido: \n ")
                address=input("Ingrese su direccion: \n ")
                phone=input("Ingrese su telefono: \n ")
                sql = " UPDATE person SET name= %s,lastname = %s,address = %s,phone= %s WHERE id= %s;"
                edit = cursor.execute(sql, (name, lastname,address,phone,idp))
                mydb.commit()
                mydb.close()

                input("Has pulsado la opción 3...\npulsa una tecla para continuar")
            elif opcionmenu == "4":
                os.system('clear')
                
                print("---------------------------------------------")
                print("               VER  PERSONA                  ")
                print("---------------------------------------------")

                mydb =   pymysql.connect(host='localhost',user='root',passwd='',db='crudpython')
                cursor = mydb.cursor()
                idp=int(input("Ingresa el id de la persona que deseas ver: "))
               
                
                consulta = "SELECT id,name,lastname,address,phone FROM person WHERE id = %s;"
                person =  cursor.execute(consulta,(idp))
               
                print("El id ingresado conside con la siguiente persona")
                for id, name, lastname, address, phone  in cursor.fetchall():
                    print("---------------------------------------------")
                print("Id :"+ str(id))
                print("Nombre :"+ name)
                print("Apellido :"+ lastname)
                print("Direccion :"+address)
                print("Telefono :"+ phone)
                
            elif opcionmenu == "5":
                os.system('clear')
                print("---------------------------------------------")
                print("            ELIMINAR  PERSONA                ")
                print("---------------------------------------------")
                mydb =   pymysql.connect(host='localhost',user='root',passwd='',db='crudpython')
                cursor = mydb.cursor()
                id=int(input("Ingresa el id de la persona que deseas eliminar: "))
                consulta = "DELETE FROM person WHERE id = %s;"
                response =cursor.execute(consulta, (id))
                mydb.commit()

                if response:
                    print("Fue eliminado exitosamente")
                    mydb.close()
                else:
                  print("No hay personas para eliminar.")

            elif opcionmenu == "6":
                os.system('clear')
                print("---------------------------------------------")
                print("         MENU  ADMINISTRARIVO                ")
                print("---------------------------------------------")
                mydb =   pymysql.connect(host='localhost',user='root',passwd='',db='crudpython')
         
                cursor = mydb.cursor()

                name=input("Ingrese su usuario:  ")
         
                password=getpass.getpass("Ingrese tu contraseña:")
                consulta = "SELECT name FROM users WHERE name = %s AND password = %s AND role  ='admin';"
                user =  cursor.execute(consulta,(name,password))

                if not user:
                    print('Verificar Sr.'+ name + "no tiene el rol administrativo.")
                    sys.exit()
                else:
                    os.system('clear')
                    print("---------------------------------------------")
                    print("     AGREGAR USUARIO - MODO ADMINISTRADOR    ")
                    print("---------------------------------------------")
                    sql = "INSERT INTO users (id,name,password,role) VALUES (%s, %s, %s, %s)"
                    id=int(input("Ingrese su id: \n"))
                    name=input("Ingrese su usuario: \n ")
                    password=getpass.getpass("Ingrese su password: \n ")
                    role=input("Ingrese un rol: \n ")

                    c= "SELECT name FROM users WHERE id = %s OR name = %s OR password = %s;"
                    user =  cursor.execute(c,(id,name,password))
                  
                    
                    if  user !=1:
                        cursor.execute(sql, (id,name, password,role))
                        mydb.commit()
                        print("El usuario se agregado exitosamente")
                        mydb.close()  
                    else: 
                       print("El usuario c, intenta ingresando otro id,usuario, contraseña.")
                       exit()    
            elif opcionmenu == "7":
                sys.exit() 
            else:
                print("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    elif opcion == "3":     
        sys.exit()     

    else:
                print("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")    

         
