import pyautogui
import time


time.sleep(1)


positions = [(1645, 429), (1646, 403), (1647, 455), (1647, 426)]  


jaune_rgb = (250, 206, 21)  


repetitions = 100

for i in range(repetitions):
    
    for pos in positions:
        
        pyautogui.moveTo(pos[0], pos[1], duration=0.5)
        
        
        couleur = pyautogui.pixel(pos[0], pos[1])
        
        
        if couleur == jaune_rgb:
            pyautogui.click()
            break
        else:
            print(f"Pas de jaune à la position {pos}, vérification suivante...")
    
    
    deuxieme_position = (1188, 589)  
    pyautogui.moveTo(deuxieme_position[0], deuxieme_position[1], duration=0.5)
    pyautogui.click()
    
    
    time.sleep(1)
