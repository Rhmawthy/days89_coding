while True :
	angka = int(input("masukkan angka : "))
		
	if angka %2 == 0 :
			h = ' '
			for i in range (2,angka+1,2):
				h += str(i) + ' '
				print (h)
	elif angka %2 != 0:
		break
		
	
	
	