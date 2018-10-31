# Instal·lació de Fedora 27 a portàtil

Repositori amb els guions de la instal·lació de Fedora 27 feta a diferents portàtils, conservant o no el sistem a operatiu preexistent. O sigui que el portàtil tindrà arrancada dual o no.

El fitxer markdown tindrà com a títol el model de portàtil utilitzat, però el nom del fitxer markdown només contindrà caràcters de l'alfabet anglès.

Els guions es dividiran en diferents seccions: 

## Especificacions (RAM, disc dur, arquitectura, targeta gràfica, targeta wifi, touchpad ...).

- PC Gaming - ASUS 
- RAM: 8 GB DDR3 1600MHZ DUAL CHANNEL
- Disco duro: 1 Tera
- Tarjeta gráfica: Gtx 960 4GB DDR5
- Procesador: i5 3500K
- Arquitectura: 64 bits


## Tipus d'arrencada (dual o no).
Dual, Windows 7 y Linux Fedora 27

## Tipus d'instal·lació: BIOS legacy o UEFI.

Instalación con BIOS UEFI.

## Links de referència per fer la instal·lació.

[Web para instalar Windows 10 y Fedora 27 en Dual.]( https://www.solvetic.com/tutoriales/article/4514-como-instalar-fedora-27-con-windows-10-arranque-dual-boot/)

## Links de referència de problemes d'algun element del maquinari del portàtil amb Fedora 27.

No he tenido ningún problema al instalar Fedora 27.

## Canvis a la BIOS en funció de la instal·lació escollida (UEFI, legacy, amb secure boot o sense ).

El único cambio que he hecho es poner que al iniciar el equipo inicie el usb. Se encuentra en el apartado **boot** y ahí nos saldrá en que orden queremos que inicie el equipo.

## Tipus de taula de particions escollida (DOS/GPT).

Particion **DOS**

El disco tiene 3 particiones, 2 Para Windows que una será una para el sistema y la otra para archivos y 1 particion para el Fedora 27.

## Preparació particions.

Como ya tenia las 2 particiones hechas del Windows lo que he hecho es coger la partición grande que tengo para archivos de Windows y hacer una partición nueva de 100GB para el fedora 27. 
Para hacer la partición he entrado con una live del Fedora, me he instalado el gparted y desde ahí he hecho una nueva partición con ext4.

## Instal·lació.

- Pinchamos el usb y desde la bios ponemos que al iniciar el equipo, inicie con el usb.
- Al iniciar el usb iniciará el instalador de fedora 27. Seguimos los pasos que nos salen y a la hora de seleccionar donde queremos instalar el fedora, seleccionamos la partición que hemos creado anteriormente.
- Creamos el usuario y el usuario root y esperamos hasta que termine la instalación.

## Post-instal·lació.

Una vez instalado el fedora 27, lo primero que debemos hacer es abrir un terminal, loguearnos con el usuario root y hacemos el comando **# yum update**.

**yum update** --> Sirve para actualizar el software del sistema con las versiones más recientes.

## Problemes (troubleshooting) i resolucions.

> Farem servir les característiques que ens proporciona el llenguatge markdown (links, imatges, llistes, títols, èmfasi, més èmfasi ...)
