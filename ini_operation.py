import configparser
import os.path

cp = configparser.ConfigParser()


def writeToIni():
    with open("config.ini", 'w', encoding="UTF-8") as f:
        cp.write(f)


def init():
    if os.path.exists("config.ini"):
        cp.read("config.ini")


def setToken(token):
    sections = cp.sections()
    if "auth" not in sections:
        cp.add_section("auth")
    cp.set("auth", "token", token)
    writeToIni()


def readToken():
    return cp.get("auth", "token")
