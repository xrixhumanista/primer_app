from flask import Flask, render_template, request

app = Flask(__name__)

# listas de palabras
cuadros = [
    ('Cuadro 1', ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'MySQL']),
    ('Cuadro 2', ['C', 'Java', 'Ruby', 'Perl', 'PHP', 'Scala']),
    ('Cuadro 3', ['Manzana', 'Naranja', 'Plátano', 'Piña', 'Mango', 'Fresa']),
    ('Cuadro 4', ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Naranja', 'Negro']),
    ('Cuadro 5', ['Perro', 'Gato', 'Conejo', 'Pez', 'Loro', 'Serpiente']),
    ('Cuadro 6', ['Casa', 'Apartamento', 'Oficina', 'Tienda', 'Hotel', 'Hospital']),
    ('Cuadro 7', ['Estados Unidos', 'México', 'Canadá', 'Argentina', 'Brasil', 'Chile']),
    ('Cuadro 8', ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Pinterest', 'Snapchat'])
]

@app.route('/', methods=['GET', 'POST'])
def ingresar_palabras():
    # crear un diccionario de valores para la plantilla
    valores = {}
    for i in range(1, 9):
        nombre_cuadro = 'cuadro{}'.format(i)
        if request.method == 'POST':
            # si el formulario se envió, obtener el valor del cuadro de texto
            valor = request.form[nombre_cuadro]
        else:
            # si el formulario no se envió, usar el valor preestablecido
            valor = ''
        valores[nombre_cuadro] = valor
    # si el formulario se envió, agregar nuevas palabras a la lista
    if request.method == 'POST':
        for cuadro, valor in request.form.items():
            if cuadro.startswith('cuadro') and valor not in palabras:
                palabras.append(valor)
    # agregar la lista de palabras al diccionario de valores para la plantilla
    valores['palabras'] = palabras
    # mostrar la plantilla
    return render_template('palabras_sugeridas.html', **valores)

if __name__ == '__main__':
    app.run(debug=True)


