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

# función para manejar la solicitud POST
@app.route('/', methods=['GET', 'POST'])
def ingresar_palabras():
    valores = {}
    if request.method == 'POST':
        for titulo, sugerencias in cuadros:
            valores[titulo] = request.form[titulo]
        return render_template('gracias.html', valores=valores)
    else:
        for titulo, sugerencias in cuadros:
            valores[titulo] = ''
        return render_template('palabras.html', cuadros=cuadros, valores=valores)

if __name__ == '__main__':
    app.run(debug=True)


