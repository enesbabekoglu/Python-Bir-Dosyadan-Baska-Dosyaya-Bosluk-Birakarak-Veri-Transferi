with open("eski.txt", "r") as dosya:

    print("eski.txt Dosyası: " + dosya.read());

    karakterler = dosya.read()
    
    print("yeni.txt Dosyası: ", end="")
        
    with open("eski.txt", "r") as dosyaTekrar:
        
        dosya2 = dosyaTekrar.read()

        with open("yeni.txt", "w") as yeni:

            i = 0
            while i < dosyaTekrar.tell():
                
                if(dosya2[i] != " "):
                    print(dosya2[i], end=" ")
                    yeni.write(dosya2[i] + " ")              
                else:
                    print(dosya2[i], end= "")
                    yeni.write(dosya2[i])
                
                i += 1
            


    
