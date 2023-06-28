import inquirer
import sys
import colorama
import os
import time
import ctypes
import psutil
import requests
import googletrans
from googletrans import Translator
from os import system
from colorama import Back
from time import sleep
from colorama import Fore
from inquirer import prompt
from deep_translator import GoogleTranslator, LingueeTranslator, PonsTranslator

translatoren = GoogleTranslator(source="auto", target="english")


def connection():
    try:
        requests.head("http://www.google.com/", timeout=3)
        return True 
    except requests.ConnectionError:
        return False

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def startprg(prcname):
    system("cls")
    system(f"start {prcname}")
    print(Fore.GREEN + "Uygulama Başlatılıyor.")
    sleep(0.5)
    system("cls")
    print(Fore.GREEN + "Uygulama Başlatılıyor..")
    sleep(0.5)
    system("cls")    
    print(Fore.GREEN + "Uygulama Başlatılıyor...")
    sleep(0.5)
    system("cls")
    setup()

q = [
    inquirer.List("selected", message=f"{Fore.YELLOW}Hangi İşlemi Yapmak İstersiniz?", choices=["Bilgisiyarı Kapat.",
                                                                                    "Bilgisayarı Yeniden Başlat.",
                                                                                    "Oturumu Kapat.",
                                                                                    "BIOS Ayarlarını Aç.",
                                                                                    "Windows Bilgisayar Şifresini Değiştir. (Sadece Yerel Kullanıcılar.)",
                                                                                    "Uygulamalar Kısmını Aç.",
                                                                                    "Çıkış."], default="Çıkış.",
)
]

appss = [
    inquirer.List("app", message=f"{Fore.YELLOW}Hangi İşlemi Yapmak İstersiniz?", choices=[
                                                                                    "Görev Yöneticisini Aç.",
                                                                                    "CMD'yi Aç.",
                                                                                    "PowerShell'i Aç.",
                                                                                    "Hesap Makinesini Aç.",
                                                                                    "Disk Yöneticisini Aç.",
                                                                                    "Aygıt Yöneticisi Aç.",
                                                                                    "Olay Görüntüleyecisini Aç.",
                                                                                    "Paint'i Aç.",
                                                                                    "Ekran Okuyucusunu Aç.",
                                                                                    "Ekran Klavyesini Aç.",
                                                                                    "Yerel Grup Ekranını Aç.",
                                                                                    "Sistem Yapılandırmasını Aç",
                                                                                    "Sorun Tarama Aracını Aç",
                                                                                    "DirectX Ekranını Aç.",
                                                                                    "Bilgisiyar Yönetimini Aç.",
                                                                                    "Windows Kayıt Defterini Aç.",
                                                                                    "Disk Temizleyicisini Aç.",
                                                                                    "Karakter Görüntüleyecisini Aç.",
                                                                                    "Geri Dön."
                                                                                    ], default="Geri Dön.",
)
]

qexit = [
    inquirer.List("exit", message=f"{Fore.YELLOW}Gerçekten Çıkmak İstediğinize Emin Misiniz?", choices=["Evet.","Hayır."], default="Hayır.",
)]


qlang = [
    inquirer.List("exit", message=f"{Fore.YELLOW}Lütfen Seçmek İstediğiniz Dili Seçin.", choices=["Türkçe","English"], default="Hayır.",
)]

username = [
    inquirer.Text("name", message="Lütfen Kullanıcı Adını Yazınız. ")
]
password = [
    inquirer.Text("password", message="Lütfen Parola Seçiniz. ")
]


def init():
    colorama.init
    system("title \"MultiTool | Version 1.0 | created by kenanwastaken\"")
    setup()


def setup():
    Mod = ""
    if not is_admin():
        Mod = "Kullanıcı"
    else:
        Mod = "Yönetici"
        print(f"{Fore.BLACK}{Back.WHITE}Dil: Türkçe{Back.RESET}" + " " + f"{Fore.BLACK}{Back.WHITE}Versiyon: 1.0{Back.RESET}" + " " + f"{Fore.BLACK}{Back.WHITE}Mod: {Mod}{Back.RESET}")

    print(f"""

{Fore.GREEN}  _  __
{Fore.GREEN} | |/ /  {Fore.BLUE}| {Fore.CYAN}Windows Multi {Fore.YELLOW}Tool
{Fore.GREEN} | ' /   {Fore.BLUE}|
{Fore.GREEN} |  <    {Fore.BLUE}| {Fore.BLACK}{Back.WHITE}https://github.com/KenanWasTaken{Back.RESET}
{Fore.GREEN} | . \   {Fore.BLUE}| 
{Fore.GREEN} |_|\_\  {Fore.BLUE}| {Fore.YELLOW}made with ❤️ by{Fore.RED} kenanwastaken{Fore.RESET}

        """)
    main()

def main():
    result = inquirer.prompt(q)
    match result['selected']:
        case "Bilgisiyarı Kapat.":
            system("shutdown -s -t 02")
            system("cls")
            cls = "cls"
            while(True):
                print(Fore.GREEN + "Bilgisiyar Kapatılıyor.")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Bilgisiyar Kapatılıyor..")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Bilgisiyar Kapatılıyor...")
                sleep(0.5)
                system(cls)
        case "Bilgisayarı Yeniden Başlat.":
            system("shutdown -r -t 02")
            system("cls")
            cls = "cls"
            while(True):
                print(Fore.GREEN + "Bilgisiyar Yeniden Başlatılıyor.")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Bilgisiyar Yeniden Başlatılıyor..")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Bilgisiyar Yeniden Başlatılıyor...")
                sleep(0.5)
                system(cls)
        case "Oturumu Kapat.":
            system("shutdown -l")
            system("cls")
            cls = "cls"
            while(True):
                print(Fore.GREEN + "Bilgisiyar Oturum Kapatılıyor.")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Bilgisiyar Oturum Kapatılıyor..")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Bilgisiyar Oturum Kapatılıyor...")
                sleep(0.5)
                system(cls)
        case "BIOS Ayarlarını Aç.":
            system("shutdown -fw -t 02")
            system("cls")
            cls = "cls"
            while(True):
                print(Fore.GREEN + "Bilgisiyar BIOS'una Giriliyor.")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Bilgisiyar BIOS'una Giriliyor..")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Bilgisiyar BIOS'una Giriliyor...")
                sleep(0.5)
                system(cls)
        case "Windows Gelişmiş Başlangıça Git.":
            system("shutdown.exe /r /o /f /t 02")
            system("cls")
            cls = "cls"
            while(True):
                print(Fore.GREEN + "Windows Gelişmiş Başlangıça Giriliyor.")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Windows Gelişmiş Başlangıça Giriliyor...")
                sleep(0.5)
                system(cls)
                print(Fore.GREEN + "Windows Gelişmiş Başlangıça Giriliyor...")
                sleep(0.5)
                system(cls)
        case "Windows Bilgisayar Şifresini Değiştir. (Sadece Yerel Kullanıcılar.)":
            if not is_admin():
                system("cls")
                print(Fore.RED + "Lütfen Programı Yönetici Modunda Başlatın.")
                sleep(2)
                system("cls")
                setup()
            else:
                system("cls")
                print("Sistemdeki Kullanıcı Adları: ")
                system("net users")
                pusername = inquirer.prompt(username)
                ppassword = inquirer.prompt(password)
                ipassword = ppassword['password']
                iusername = pusername['name']
                system("net user " + f'"{iusername}"' + f" {ipassword}")
                print(Fore.GREEN + f"{iusername} Adlı Kullanıcının Parolası {ipassword} Olarak Başarılı Bir Şekilde Değiştirildi.")
                sleep(3)
                system("cls")
                setup()
        case "Uygulamalar Kısmını Aç.":
            system("cls")
            apps = inquirer.prompt(appss)
            match apps['app']:
                case "Görev Yöneticisini Aç.":
                    startprg("taskmgr")
                case "CMD'yi Aç.":
                    startprg("start cmd")
                case "PowerShell'i Aç.":
                    startprg("start powershell")
                case "Hesap Makinesini Aç.":
                    startprg("calc.exe")
                case "Disk Yöneticisini Aç.":
                    startprg("diskmgmt.msc")
                case "Aygıt Yöneticisi Aç.":
                    startprg("devmgmt.msc")
                case "Olay Görüntüleyecisini Aç.":
                    startprg("eventvwr.exe")
                case "Paint'i Aç.":
                    startprg("mspaint.exe")
                case "Ekran Okuyucusunu Aç.":
                    startprg("narrator.exe")
                case "Ekran Klavyesini Aç.":
                    startprg("osk.exe")
                case "Yerel Grup Ekranını Aç.":
                    startprg("gpedit.msc")
                case "Sistem Yapılandırmasını Aç.":
                    startprg("msconfig.exe")
                case "Sorun Tarama Aracını Aç.":
                    startprg("drwtsn32.exe")
                case "DirectX Ekranını Aç.":
                    startprg("dxdiag.exe")
                case "Bilgisayar Yönetimini Aç.":
                    startprg("compmgmt.msc")
                case "Windows Kayıt Defterini Aç.":
                    startprg("regedit")
                case "Disk Temizleyicisini Aç.":
                    startprg("cleanmgr.exe")
                case "Karakter Görüntüleyecisini Aç.":
                    startprg("charmap.exe")
                case "Geri Dön.":
                    system("cls")
                    setup()
                case _:
                    print(apps['app'])
        case "Dili Değiştir.":
            pass
        case "Çıkış.":
            system("cls")
            qresult = inquirer.prompt(qexit)
            match qresult['exit']:
                case "Evet.":
                    system("cls")
                    print(Fore.RED + "okay bro nvm" + Fore.RESET)
                    exit(0)
                case "Hayır.":
                    system("cls")
                    setup()
        case _:
            print(Fore.RED + "olm buraya nasi geldin la buga bak")
init()