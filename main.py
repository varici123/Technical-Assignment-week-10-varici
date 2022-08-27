import hy_srf05
import time

try:
    jmlh = 0
    while True:
        dist = hy_srf05.ambil()
        if dist < 10 :
            jmlh += 1
            print(jmlh)
            time.sleep(0.05)
        
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!") 
