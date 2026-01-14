import pyautogui
import time

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")

pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=444, y=374)

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("davisdev25")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    
    pyautogui.click(x=454, y=254)    
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)     
      
    