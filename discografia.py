from bs4 import BeautifulSoup
import requests

def album(c):
      page=requests.get(c)
      soup=BeautifulSoup(page.content,"html.parser")
      can=soup.find_all("h2",style="white-space:pre-wrap;")
      canciones=[]
      for i in can:
            canciones.append(i.text)
      print(canciones)

def tc(la,las,als):
      la=["dynamite","mots7-the-journey","mots-7","ights-boy-with-luv","bts-world-ost","mots-persona","fakelove-airplanept2","y-answer","ly-tear","face-yourself","micdrop-dna-crystalsnow","ly-her","chi-ase-namida","ynwa","wings","youth","hyyh-young-forever","run","i-need-u","hyyh-pt2","for-yo","hyyh-pt1","wake-up","danger","dark-and-wild","bil","nmd","sla-sa","sla","orul82","2c4s"]
      las=["Be(Deluxe Edition)","Dynamite","Map of the Soul: 7 ~The Journey~","MAP OF THE SOUL: 7","Lights / Boy With Luv","ABTS World OST","MAP OF THE SOUL: PERSONA","FAKE LOVE / AIRPLANE PT.2","LOVE YOURSELF 結 'ANSWER'","LOVE YOURSELF 轉 'TEAR'","Face Yourself","MIC DROP / DNA / CRYSTAL SNOW","LOVE YOURSELF 承 'HER'","血、汗、涙 (CHI, ASE, NAMIDA) / Blood Sweat &Tears","You Never Walk Alone","WINGS","YOUTH","화양연화: YOUNG FOREVER","RUN","I Need U","화양연화 PT. 2 (The Most Beautiful Moment in Life, PT. 2)","For You"
"화양연화 PT. 1 (The Most Beautiful Moment in Life, PT. 1)","Wake Up","Danger","Dark & Wild","Boy in Luv","No More Dream","Skool Luv Affair Special Addition","Skool Luv Affair","O!RUL8,2?","2 COOL 4 SKOOL"]
      for i in la:
            if i in range(la,len(la)):
                  c=("https://www.usbtsarmy.com/discography/",la[i])
                  page=requests.get(c)
                  soup=BeautifulSoup(page.content,"html.parser")
                  can=soup.find_all("h2",style="white-space:pre-wrap;")
                  c=("canciones",la.index(i))
                  c=[]
                  for i in can:
                        c.append(i.text)
                  print("Las canciones de ",las[i], c)
      
print ("Selecciona una Album")
print ("\n1 - Be(Deluxe Edition)")
print ("\n2 - Dynamite")
print ("\n3 - Map of the Soul: 7 ~The Journey~")
print ("\n4 - MAP OF THE SOUL: 7")
print ("\n5 - Lights / Boy With Luv")
print ("\n6 - ABTS World OST")
print ("\n7 - MAP OF THE SOUL: PERSONA")
print ("\n8 - FAKE LOVE / AIRPLANE PT.2")
print ("\n9 - LOVE YOURSELF 結 'ANSWER'")
print ("\n10 - LOVE YOURSELF 轉 'TEAR'")
print ("\n11 - Face Yourself")
print ("\n12 - MIC DROP / DNA / CRYSTAL SNOW")
print ("\n13 - LOVE YOURSELF 承 'HER'")
print ("\n14 - 血、汗、涙 (CHI, ASE, NAMIDA) / Blood Sweat &Tears")
print ("\n15 - You Never Walk Alone")
print ("\n16 - WINGS")
print ("\n17 - YOUTH")
print ("\n18 - 화양연화: YOUNG FOREVER")
print ("\n19 - RUN")
print ("\n20 - I Need U")
print ("\n21 - 화양연화 PT. 2 (The Most Beautiful Moment in Life, PT. 2)")
print ("\n22 - For You")
print ("\n23 - 화양연화 PT. 1 (The Most Beautiful Moment in Life, PT. 1)")
print ("\n24 - Wake Up")
print ("\n25 - Danger")
print ("\n26 - Dark & Wild")
print ("\n27 - Boy in Luv")
print ("\n28 - No More Dream")
print ("\n29 - Skool Luv Affair Special Addition")
print ("\n30 - Skool Luv Affair")
print ("\n31 - O!RUL8,2?")
print ("\n32 - 2 COOL 4 SKOOL")
print ("\n33 - Todas las canciones")
print ("\n34 - Regresar")
opcionMenu=input()

if opcionMenu=="1":
      print ("")
      c="https://www.usbtsarmy.com/discography/be"
      album(c)
if opcionMenu=="2":
      print ("")
      c="https://www.usbtsarmy.com/discography/dynamite"
      album(c)
if opcionMenu=="3":
      print ("")
      c="https://www.usbtsarmy.com/discography/mots7-the-journey"
      album(c)
if opcionMenu=="4":
      print ("")
      c="https://www.usbtsarmy.com/discography/mots-7"
      album(c)
if opcionMenu=="5":
      print ("")
      c="https://www.usbtsarmy.com/discography/lights-boy-with-luv"
      album(c)
if opcionMenu=="6":
      print ("")
      c="https://www.usbtsarmy.com/discography/bts-world-ost"
      album(c)
if opcionMenu=="7":
      print ("")
      c="https://www.usbtsarmy.com/discography/mots-persona"
      album(c)
if opcionMenu=="8":
      print ("")
      c="https://www.usbtsarmy.com/discography/fakelove-airplanept2"
      album(c)
if opcionMenu=="9":
      print ("")
      c="https://www.usbtsarmy.com/discography/ly-answer"
      album(c)
if opcionMenu=="10":
      print ("")
      c="https://www.usbtsarmy.com/discography/ly-tear"
      album(c)
if opcionMenu=="11":
      print ("")
      c="https://www.usbtsarmy.com/discography/face-yourself"
      album(c)
if opcionMenu=="12":
      print ("")
      c="https://www.usbtsarmy.com/discography/micdrop-dna-crystalsnow"
      album(c)
if opcionMenu=="13":
      print ("")
      c="https://www.usbtsarmy.com/discography/ly-her"
      album(c)
if opcionMenu=="14":
      print ("")
      c="https://www.usbtsarmy.com/discography/chi-ase-namida"
      album(c)
if opcionMenu=="15":
      print ("")
      c="https://www.usbtsarmy.com/discography/ynwa"
      album(c)
if opcionMenu=="16":
      print ("")
      c="https://www.usbtsarmy.com/discography/wings"
      album(c)
if opcionMenu=="17":
      print ("")
      c="https://www.usbtsarmy.com/discography/youth"
      album(c)
if opcionMenu=="18":
      print ("")
      c="https://www.usbtsarmy.com/discography/hyyh-young-forever"
      album(c)
if opcionMenu=="19":
      print ("")
      c="https://www.usbtsarmy.com/discography/run"
      album(c)
if opcionMenu=="20":
      print ("")
      c="https://www.usbtsarmy.com/discography/i-need-u"
      album(c)
if opcionMenu=="21":
      print ("")
      c="https://www.usbtsarmy.com/discography/hyyh-pt2"
      album(c)
if opcionMenu=="22":
      print ("")
      c="https://www.usbtsarmy.com/discography/for-you"
      album(c)
if opcionMenu=="23":
      print ("")
      c="https://www.usbtsarmy.com/discography/hyyh-pt1"
      album(c)
if opcionMenu=="24":
      print ("")
      c="https://www.usbtsarmy.com/discography/wake-up"
      album(c)
if opcionMenu=="25":
      print ("")
      c="https://www.usbtsarmy.com/discography/danger"
      album(c)
if opcionMenu=="26":
      print ("")
      c="https://www.usbtsarmy.com/discography/dark-and-wild"
      album(c)
if opcionMenu=="27":
      print ("")
      c="https://www.usbtsarmy.com/discography/bil"
      album(c)
if opcionMenu=="28":
      print ("")
      c="https://www.usbtsarmy.com/discography/nmd"
      album(c)
if opcionMenu=="29":
      print ("")
      c="https://www.usbtsarmy.com/discography/sla-sa"
      album(c)
if opcionMenu=="30":
      print ("")
      c="https://www.usbtsarmy.com/discography/sla"
      album(c)
if opcionMenu=="31":
      print ("")
      c="https://www.usbtsarmy.com/discography/orul82"
      album(c)
if opcionMenu=="32":
      print ("")
      c="https://www.usbtsarmy.com/discography/2c4s"
      album(c)
#if opcionMenu=="33":
      


