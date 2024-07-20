from flask import Flask, jsonify
from preparacion.perro import Perro
from preparacion.gato import Gato
from huronesyBoas.huron import Huron
from huronesyBoas.boa_constrictor import BoaConstrictor

app = Flask(__name__)

@app.route('/api/animales', methods=['GET'])
def get_animales():
    perro = Perro("Zeus", "Rottweiler", 45.8, 3)
    gato = Gato("Luna", 3.2, 2, "Blanco")
    huron = Huron("Fuzz", 1.2, 2, "USA", 50.0)
    boa = BoaConstrictor("Nagini", 30.0, 5, "Brasil", 150.0)

    animales = [
        {
            "tipo": "Perro",
            "nombre": perro.get_nombre(),
            "raza": perro.get_raza(),
            "peso": perro.get_peso(),
            "edad": perro.get_edad(),
            "sonido": perro.hacer_sonido()
        },
        {
            "tipo": "Gato",
            "nombre": gato.get_nombre(),
            "color": gato.get_color(),
            "peso": gato.get_peso(),
            "edad": gato.get_edad(),
            "sonido": gato.hacer_sonido()
        },
        {
            "tipo": "Hurón",
            "nombre": huron.get_nombre(),
            "peso": huron.get_peso(),
            "edad": huron.get_edad(),
            "pais_origen": huron.get_pais_origen(),
            "impuestos": huron.get_impuestos(),
            "sonido": huron.hacer_sonido()
        },
        {
            "tipo": "Boa Constrictor",
            "nombre": boa.get_nombre(),
            "peso": boa.get_peso(),
            "edad": boa.get_edad(),
            "pais_origen": boa.get_pais_origen(),
            "impuestos": boa.get_impuestos(),
            "ratones_comidos": boa.get_ratones_comidos(),
            "sonido": boa.hacer_sonido()
        }
    ]

    return jsonify(animales)

if __name__ == '__main__':
    app.run(debug=True)
