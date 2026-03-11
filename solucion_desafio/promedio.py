nota1 = float(input("ingrese la primera calificacion:"))
nota2 = float(input("ingrese la segunda calificacion:"))
nota3 = float(input("ingrese la tercera calificacion:"))
nota4 = float(input("ingrese la cuarta calificacion:"))
nota5 = float(input("ingrese la quinta calificacion:"))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("el promedio es:",promedio)

if promedio >= 60:
    print("aprobado")
elif promedio >= 40:
    print("en recuperacion")
else:
    print("reprobado")