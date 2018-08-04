import requests
import time
import os
from datetime import datetime

senha = raw_input("DIGITE A SENHA: ")

if senha == "nenhumsistemaestaasalvo":
    

    def main():
        print('\033[31m                          _             __  ')
        time.sleep(0.5)
        print('\033[32m__________    ________   | |           |  |          ')
        time.sleep(0.5)
        print('\033[32m|             |       |  | |           |  | ')
        time.sleep(0.5)
        print('\033[33m|             |       |  | |           |  |             ')
        print('RIPX')
        time.sleep(0.5)
        print('\033[34m|_________    |       |  | |           |  |           ')
        time.sleep(0.5)
        print('\033[35m         |    |_______|  | |           |  |               ')
        print('NONE SYSTEM ARE SAFE')
        time.sleep(0.5)
        print('\033[32m         |            |  | |           |  |          ')
        time.sleep(0.5)
        print('\033[32m         |            |  | |_________  |  |                   ')
        time.sleep(0.5)
        print('\033[32m_________|            |  |___________| |__|     \n\n \033[m')
        time.sleep(0.2)
        print('\033[31m             _____________________________')
        time.sleep(0.5)
        print('\033[31m            |          WELCOME            |')
        time.sleep(0.5)
        print('\033[31m            |CREATE BY: GHOSTSAD(PAULO)   |')
        time.sleep(0.5)
        print('\033[32m            |         VERSION:1.0         |')
        time.sleep(0.5)
        print('            |  EXEMPLE:HTTP://SITE.COM    |')
        time.sleep(0.5)
        print('\033[32m            |-----------------------------|')
   

        try:
            url = raw_input('\033[mWRITER THE SITE: \033[m')
            print('SEARCHING FOR FAILED...WAIT')
            time.sleep(0.5)
            if '\'' not in url:
                print('YOU NOT PASS NONE PARAMETER  VALID ')
                exit(0)
            else:
 
                 req = requests.get(url)
                 html = req.text


            if "mysql_fetch_array()" or "You have an error in your SQL syntax;"  in html:
                 print('\033[32mTHIS SITE IS VULNERABLE\n\n')
	         print('THANK YOU FOR ARE HERE. BACK FOREVER, EXITING...')
                 time.sleep(2.5)
                 os.system('clear')
                 exit(0)
  


           else:
                 print('\033[31mTHIS SITE NOT IS VULNERABLE.BUT NOT MEAN THAT NOT BE \033[m')
                 print('THANK YOU FOR ARE HERE. BACK FOREVER, EXITING...')
                 time.sleep(1)
                 exit(0)

        except Exception  as erro:
            print('ERRO: ', erro)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt):
        
        print("\nAAAH YOU CANCELED THE PROGRAM... IT'S OK, BUT YOU CAN ALWAYS COME BACK HERE.\n")
        print("XRIP")



