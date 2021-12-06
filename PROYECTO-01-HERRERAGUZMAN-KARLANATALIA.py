3
"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
#programa que encuentra el ranking de productos (mas vendidos o menos vendidos) por mes en cada categoria
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches 

print("Usuario=Python Contraseña=1234") #este es un mensaje para que el usuario sepa cuáles son los datos correctos para que el programa siga

print("Ingresa el usuario") #mensaja a usuario
usuario = input()#asignar los datos introducidos por el usuario a una variable llamada "usuario"

#mientras no se ingrese bien el usuario, el programa no avanzará
while (usuario!='Python'):
  print("Ingresa el usuario correcto")
  usuario = input()

print("Ingresa la contraseña")#mensaja a usuario
password = input()#asignar los datos introducidos por el usuario a una variable llamada "password"

#mientras no se ingrese bien la contraseña, el programa no avanzará
while (password!='1234'):
  print("Ingresa la contraseña correcta")
  password = input()

#declarar las listas
categorias = [] 
ventas_categorias = []
busquedas_categorias = []
calificaciones_categorias = []


for i in range(len(lifestore_products)):
  categoria_prod=lifestore_products[i][3]
  if categoria_prod in categorias:
    continue
  else:
    #creando la lista de categorias llamada "categorias"
    categorias.append(categoria_prod)
    #inicializar en cero las listas 
    ventas_categorias.append(0)
    busquedas_categorias.append(0)
    calificaciones_categorias.append(0)
#print(categorias)


entrada='9'
while entrada!='0':#elegir una opción válida para el mes
  print("¿De qué mes quieres el reporte (número)?")
  while True:
      try:
          
          mes=int(input())  
          if mes>=0 and mes<13: #si el número del mes está entre 1 y 12, es una entrada válida y le asigna a "mes" el valor 
            break

          else: #si no es un valor entre 1 y 12 continua preguntando por un valor válido
            print("Da un valor válido")
            print("¿De qué mes quieres el reporte (número)?")
            continue
      except:
          print("Da un valor válido")
          print("¿De qué mes quieres el reporte (número)?")
  print("Elige la caregoría de la que quieres hacer el reporte")

  #imprime las categorias para que el ususario pueda elegir una según el número asignado y verifica que se ingrese un valor valido
  for i in range(len(categorias)):
    print(f"{i}.- {categorias[i]}")
  while True:
      try:
          categoria_elegida=int(input())
          if categoria_elegida>=0 and categoria_elegida<len(categorias):
            break

          else:
            print("Da un valor valido")
            print("Elige la caregoría de la que quieres hacer el reporte")
            continue
      except:
          print("Da un valor valido")
          print("Elige la caregoría de la que quieres hacer el reporte")

  Productos_Categoria=[]
  j=0
  #lista de productos que pertenecen a la categoria seleccionada
  for i in range(len(lifestore_products)):
    if lifestore_products[i][3]==categorias[categoria_elegida]:
      Productos_Categoria.append(lifestore_products[i])
      Productos_Categoria[j].append(j+1)
      j+=1

  #print(Productos_Categoria)

  ventas_mes = []
  for i in range(len(lifestore_sales)):
    fecha=lifestore_sales[i][3]
    if int(fecha[3:5])==mes:
      ventas_mes.append(lifestore_sales[i])
  #print(ventas_mes)
  #print(busquedas_categorias)
  #print(calificaciones_categorias)

  '''declarar listas'''
  ventas = []
  busqueda = []
  calificacion = []
  top_ventas = []
  top_busqueda = []
  top_calificacion = []
  bandera_uso_ventas = []
  bandera_uso_busqueda = []
  bandera_uso_calificacion = []
  ventas_brutas=[] #ventas sin tomar en cuenta refund

  #for para inicializar la lista ventas
  for i in range(len(Productos_Categoria)+1):
    ventas.append(0)
    busqueda.append(0)
    calificacion.append(0)
    top_ventas.append(0)
    top_busqueda.append(0)
    top_calificacion.append(0)
    bandera_uso_ventas.append(True)
    bandera_uso_busqueda.append(True)
    bandera_uso_calificacion.append(True)
    ventas_brutas.append(0)
  #la posicion en las listas corresponde al producto en la entrada x de lifestore_products, es decir ventas[3] corresponde a las ventas del producto en la tercera entrada de lifestore_products, la entrada 0 no corresponde a ningun producto

  ingresos_totales=0
  for vendidos in ventas_mes:
    id_sale=vendidos[0]
    for j in range(len(Productos_Categoria)):
      if vendidos[1]==Productos_Categoria[j][0]:
        id_product=Productos_Categoria[j][5]
        score=vendidos[2]
        date_venta=vendidos[3]
        refund=vendidos[4]
        calificacion[id_product]+=score
        ventas_brutas[id_product]+=1
  #  for k in range(len(categorias)):
  #    if Productos_Categoria[id_product-1][3]==categorias[k]:
  #      ventas_categorias[k]+=1
  #      calificaciones_categorias[k]+=score
        if refund ==0 and mes==int(date_venta[3:5]):
          ingresos_totales+=Productos_Categoria[id_product][2]
          ventas[id_product]+=1
  #        for i in range(1,13):
  #          if i==int(date_venta[3:5]):
  #            ventas_mes[i]+=1
  #            ingresos_mes[i]+=Productos_Categoria[id_product][2]
  #            break
  print(ventas)
  #print(ingresos_mes)
  #print(ingresos_totales)
  #print(ventas_categorias)

  #print(ventas)


  productos_con_reseñas=0
  for i in range(len(Productos_Categoria)+1):
    if calificacion[i]>0:
      productos_con_reseñas+=1
  #hacer el promedio 
  for i in range(len(Productos_Categoria)+1):
    if ventas[i]!=0:
      calificacion[i]/=ventas_brutas[i]
  print(calificacion)
  print(ventas_brutas)
  #calif_categorias=[]
  #for k in range(len(categorias)):
  #  calificaciones_categorias[k]/=ventas_categorias[k]
  #  calif_categorias.append("{:.2f}".format(calificaciones_categorias[k]))
  #print(calificaciones_categorias)
  #print(calif_categorias)

  for buscados in lifestore_searches:
    id_search=buscados[0]
    for j in range(len(Productos_Categoria)):
      if buscados[1]==Productos_Categoria[j][0]:
        id_product=Productos_Categoria[j][5] 
        busqueda[id_product]+=1
  #      for k in range(len(categorias)):
  #        if lifestore_products[id_product-1][3]==categorias[k]:
  #          busquedas_categorias[k]+=1
  #print(busqueda)

  comp_v=-1
  comp_b=-1
  comp_c=-1
  j_v=-1
  j_b=-1
  j_c=-1
  #i es el numero de ventas
  #j es la posicion en la lista ventas que es equivalente al id_producto
  for k in range(1,len(ventas)):#k es el lugar en el top
    for i in range(1,len(ventas)):#encuentra el numero mayor
      if bandera_uso_ventas[i]:#revisar si ya se le asignó el lugar (top) a ese producto
        if ventas[i]>comp_v:
          comp_v=ventas[i] #encontrar el mas grande
          j_v=i #j_v es la posicion en ventas correspondiente al numero de ventas mas grande
      if bandera_uso_busqueda[i]:#revisar si ya se le asignó el lugar (top) a ese producto
        if busqueda[i]>comp_b:
          comp_b=busqueda[i] #encontrar el mas grande
          j_b=i #j_b es la posicion en busquedas correspondiente al numero de busquedas mas grande
      if bandera_uso_calificacion[i]:#revisar si ya se le asignó el lugar (top) a ese producto
        if calificacion[i]>comp_c:
          comp_c=calificacion[i] #encontrar el mas grande
          j_c=i #j_c es la posicion en calificacion correspondiente a la calificacion mas grande
    comp_v=-1
    comp_b=-1
    comp_c=-1
    top_ventas[j_v]= k #el numero de ventas se pone en la entrada j_v de la lista
    top_busqueda[j_b]= k #el numero busquedas se pone en la entrada j_b de la lista
    top_calificacion[j_c]= k #el numero de calificacion se pone en la entrada j_c de la lista
    bandera_uso_ventas[j_v] = False
    bandera_uso_busqueda[j_b] = False
    bandera_uso_calificacion[j_c] = False
  
  while entrada!='0':
    print("""\tIngresa 1 para imprimir una lista con los 5 productos más vendidos
    Ingresa 2 para imprimir una lista con los 10 productos más buscados
    Ingresa 3 para imprimir una lista con los 5 productos menos vendidos
    Ingresa 4 para imprimir una lista con los 10 productos menos buscados
    Ingresa 5 para imprimir una lista con los 5 productos mejor calificados
    Ingresa 6 para imprimir una lista con los 5 productos peor calificados
    Ingresa 7 para imprimir un reporte de ingresos y ventas por mes
    Ingresa 8 para volver a elegir mes y categoría
    Ingresa 0 para salir""")
    entrada=input()
    if entrada=='1':
      print("\n5 productos más vendidos")
      print("rank\tid\t#ventas\t\tnombre del producto")
      for i in range(1,6):
        for j in range(1,len(top_ventas)-1):
          if top_ventas[j]==i:
            print(f" {i}\t\t{Productos_Categoria[j-1][0]}\t  {ventas[j]}\t\t{Productos_Categoria[j-1][1][:40]} \n")

    elif entrada=='2':
      print("\n10 productos más buscados")
      print("rank\tid\t#busquedas\t\tnombre del producto")
      for i in range(1,11):
        for j in range(1,len(top_busqueda)):
          if top_busqueda[j]==i:
            print(f"{i}\t{Productos_Categoria[j-1][0]}\t{busqueda[j]}\t{Productos_Categoria[j-1][1][:30]} ")

    elif entrada=='3':
      print("\n5 productos menos vendidos")
      print("rank\tid\t#ventas\t\tnombre del producto")
      for i in range(1,7):
        for j in range(1,len(top_ventas)):
          if top_ventas[j]==len(top_ventas)-i+1:
            print(f"{top_ventas[j]}\t{Productos_Categoria[j-1][0]}\t{ventas[j]}\t{Productos_Categoria[j-1][1][:30]} ")

    elif entrada=='4':
      print("\n10 productos menos buscados")
      print("rank\tid\t#busquedas\t\tnombre del producto")
      for i in range(1,11):
        for j in range(1,len(top_busqueda)):
          if top_busqueda[j]==len(top_busqueda)-i:
            print(f"{top_busqueda[j]}\t{Productos_Categoria[j-1][0]}\t{busqueda[j]}\t{Productos_Categoria[j-1][1][:30]} ")

    elif entrada=='5':
      print("\n5 productos mejor calificados")
      print("rank\tid\tcalificacion\t\tnombre del producto")
      for i in range(1,6):
        for j in range(1,len(top_calificacion)-1):
          if top_calificacion[j]==i:
            print(f"{i}\t{Productos_Categoria[j-1][0]}\t{calificacion[j]}\t{Productos_Categoria[j-1][1][:30]} ")

    elif entrada=='6':
      print("\n5 productos peor calificados")
      print("rank\tid\tcalificacion\t\tnombre del producto")
      for i in range(1,6):
        for j in range(1,len(top_calificacion)):
          if top_calificacion[j]==len(top_calificacion)-i:
            print(f"{top_calificacion[j]}\t{Productos_Categoria[j-1][0]}\t{calificacion[j]}\t{Productos_Categoria[j-1][1][:30]} ")

    elif entrada=='7':
      print("Ingresos y ventas por mes")
      print(f"\tIngresos en el mes {mes}:{ingresos_totales}\n")

    elif entrada=='8':
      break

    elif entrada =='0':
      break

    else:
      print("Ingresa una opción válida")


"""print("Producto\t Ventas \t  Top")
for i in range(1,len(ventas)):
  print("\t",i,"\t ",ventas[i],"\t",top_ventas[i])
#  print(i,"\t",busqueda[i],"\t",top_busqueda[i])
#  print(i,"\t",calificacion[i],"\t",top_calificacion[i])"""
