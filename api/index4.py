from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
	self.wfile.write('En teoria, esto andaria. test 123'.encode('utf-8'))
	#El dolor de cabeza del sabado a la noche (4 locos, 4 horas haciendo esto):

	print("Cajon Completo:")
	for i in range(10):
	    for j in range(10):
	        print(str(i)+str(j), end=" ") #Los str y el + hacen que los caracteres salgan juntos
	    print()  #Agregar un salto de línea después de cada fila
	print("")
	print("#"*50)
	print("")
	print("Cajon Vacio:")
	for i in range(10):
	    for j in range(10):
        	if i==0:
	            print(str(i)+str(j), end=" ")
        	elif i==9:
	            print(str(i)+str(j), end=" ")
        	else:
	            if j==0:
        	        print(str(i)+str(j), end=" ")
	            elif j==9:
        	        print(str(i)+str(j), end=" ")
	            else:
        	        print("  ", end=" ")
	    print()
	print("")
	print("#"*50)
	print("")
	print('"La Mira Loca:"')
	for i in range(10):
	    for j in range(10):
	        if i==0:
        	    print(str(i)+str(j), end=" ")
	        elif i==1:
        	    if j==0:
                	print(str(i)+str(j), end=" ")
	            elif j==9:
        	        print(str(i)+str(j), end=" ")
        	    else:
        	        print("  ", end=" ")
        	elif i==2:
        	    if j==1:
                	print("  ", end=" ")
	            elif j==8:
        	        print("  ", end=" ")
	            else:
        	        print(str(i)+str(j), end=" ")
	        elif i==4:
        	    if j==0:
                	print(str(i)+str(j), end=" ")
	            elif j==2:
	                print(str(i)+str(j), end=" ")
        	    elif j==4:
                	print(" ┘", end=" ")
	            elif j==5:
        	        print("└ ", end=" ")
	            elif j==7:
         	       print(str(i)+str(j), end=" ")
	            elif j==9:
        	        print(str(i)+str(j), end=" ")
	            else:
	                print("  ", end=" ")
	        elif i==5:
	            if j==0:
	                print(str(i)+str(j), end=" ")
	            elif j==2:
	                print(str(i)+str(j), end=" ")
	            elif j==4:
	                print(" ┐", end=" ")
        	    elif j==5:
                	print("┌ ", end=" ")
	            elif j==7:
        	        print(str(i)+str(j), end=" ")
	            elif j==9:
        	        print(str(i)+str(j), end=" ")
	            else:
        	        print("  ", end=" ")
	        elif i==7:
        	    if j==1:
	                print("  ", end=" ")
        	    elif j==8:
                	print("  ", end=" ")
	            else:
        	        print(str(i)+str(j), end=" ")
	        elif i==8:
        	    if j==0:
                	print(str(i)+str(j), end=" ")
	            elif j==9:
        	        print(str(i)+str(j), end=" ")
	            else:
        	        print("  ", end=" ")
	        elif i==9:
	            print(str(i)+str(j), end=" ")
	        else:
	            if j==0:
	                print(str(i)+str(j), end=" ")
	            elif j==2:
       	         print(str(i)+str(j), end=" ")
        	    elif j==7:
                	print(str(i)+str(j), end=" ")
	            elif j==9:
        	        print(str(i)+str(j), end=" ")
	            else:
        	        print("  ", end=" ")
	    print()
        return
