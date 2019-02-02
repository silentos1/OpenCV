import cv2
import numpy as np

plik1 = open('test1.txt', 'w')
plik2 = open('test2.txt', 'w')
 
MinProg = 5                      
MaxProg = 120                     
MinObszar = 60                          
MinKolistosc = .1
MinInertia = .3
 
kamera = cv2.VideoCapture(0)               # kamerka przypisana do zmiennej
kamera.set(15, -8)                         # ustawienie kamerki, 15- jasnoc , -8 zakres
 
zliczanie = 0                             # zmienna do powtorzen petli
listaodczyt = [0, 0]                       # lista do zapisu wyniku rzutu
listaoczko = [0, 0]                        # lista do wyswietlanai wyniku rzutu


 
while True:
    
 
    ret, klatka = kamera.read()                                  # klatka z kamerki     
 
    params = cv2.SimpleBlobDetector_Params()                     # parametry
    params.filterByArea = True
    params.filterByCircularity = True
    params.filterByInertia = True
    params.minThreshold = MinProg
    params.maxThreshold = MaxProg
    params.minArea = MinObszar
    params.minCircularity = MinKolistosc
    params.minInertiaRatio = MinInertia
  
    detektor = cv2.SimpleBlobDetector_create(params)              # obiekt typu blob dedector
 
	
    oczka = detektor.detect(klatka)                               # wykrycie keypoint
 
    
    klatka_z_oczkami = cv2.drawKeypoints(klatka, oczka, np.array([]), (0, 255, 0),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
    cv2.imshow("Kostka", klatka_z_oczkami)            
 
    liczba_oczek = len(oczka)                                
 
 
 
    if zliczanie % 4 == 0: 
	
        if	liczba_oczek < 7 :
		
			listaodczyt.append(liczba_oczek)                            
	 
			if listaodczyt[-1] == listaodczyt[-2] == listaodczyt[-3] == listaodczyt[-4]== listaodczyt[-5]:    
				listaoczko.append(listaodczyt[-1])                    
	 
			
			if listaoczko[-1] != listaoczko[-2] and listaoczko[-1] != 0:
				msg = "Wypadlo: " + str(listaoczko[-1])   + "\n"
				print(msg)
				
				
 
    zliczanie += 1
    

	
    k = cv2.waitKey(30) & 0xff                              
    if k == 27:
        break
		
plik1.write(str(listaoczko[-1]))
plik1.close()
		
print(listaodczyt)
plik2.writelines(str(listaoczko))		
plik2.close()
 
                                   