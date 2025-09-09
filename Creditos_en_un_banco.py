#Ejercicio 1--decidir aprobacion de cliente
#en un banco se calculan probabilidades de aprobacion de credito para un conjunto de clientes cada probabilidad es un numero entre 0 y 1
#diseñar una funcion que dado el listado de probabilidades,clasifique a cada cliente como "aprobado"o "rechazado"
#la desicion depende de un umbral,que debe tener un valor predeterminado pero que tambien pueda ser definido por el usuario

#creamos la lista
def clasificar_clientes(probabilidades, umbral=0.5):
    resultados = []
    for i, probabi in enumerate(probabilidades, start=1):  # recorre cada probabilidad
        if probabi >= umbral:   # comparación con el umbral
            resultados.append((f"Cliente{i}", "aprobado"))
        else:
            resultados.append((f"Cliente{i}", "rechazado"))
    return resultados  # devolvemos la lista de resultados

# Lista de probabilidades de ejemplo
probabilidades_clientes = [0.8, 0.4, 0.6, 0.3]

# El usuario puede cambiar el umbral
entrada = input("Ingrese un umbral (o Enter para usar 0.5): ")
if entrada.strip() != "":
    umbral = float(entrada)
else:
    umbral = 0.5

# Llamar a la función
resultado = clasificar_clientes(probabilidades_clientes, umbral)

# Mostrar resultados
print("\nResultados:")
for cliente, estado in resultado:
    print(cliente, "→", estado)


