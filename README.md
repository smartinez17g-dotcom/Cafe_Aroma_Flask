# Café Aroma - Prototipo web modular con Flask

**Asignatura:** Fundamentos de programación web - UNIMINUTO
**Autor(es):** [Sergio Martinez y Steven Mendez]

## Descripción

Café Aroma es un prototipo de página web hecho con Python y Flask.
Tiene tres páginas (Inicio, Servicios y Contacto) que usan una plantilla base
(`base.html`) con los bloques `{% block title %}` y `{% block content %}`.
El encabezado, la barra de navegación y el pie de página están en archivos
separados y se agregan con `{% include %}`.

## Tecnologías

- Python 3
- Flask (Jinja2)
- HTML5
- CSS3
- JavaScript

## Estructura del proyecto

```
Cafe_Aroma_Flask/
├── app.py
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── servicios.html
│   ├── contacto.html
│   └── includes/
│       ├── header.html
│       ├── navbar.html
│       └── footer.html
└── static/
    ├── css/
    │   └── estilos.css
    └── script.js
```

## Instalación

1. Clonar el repositorio:

```
git clone [[URL-DE-TU-REPOSITORIO](https://github.com/TU-USUARIO/Cafe_Aroma_Flask)]
cd Cafe_Aroma_Flask
```

2. Instalar Flask:

```
pip install flask
```

## Ejecución

```
python app.py
```

Luego abrir en el navegador: http://127.0.0.1:5000

## Páginas

| Página   | Ruta         |
|----------|--------------|
| Inicio   | `/`          |
| Servicios| `/servicios` |
| Contacto | `/contacto`  |

## Referencias

- Adictos al trabajo. (2024). *Diseño y renderizado de páginas HTML en Python con Flask: guía completa.* https://adictosaltrabajo.com/2024/02/21/diseno-y-renderizado-de-paginas-html-en-python-con-flask-guia-completa/
- Navarro, A. (2025). *Extensiones en Flask: Guía práctica.* Junco TIC. https://juncotic.com/extensiones-en-flask-guia-practica/
- LabEx. (2025). *Generando plantillas dinámicas y seguras con Jinja2.* https://labex.io/es/tutorials/flask-generating-secure-dynamic-templates-with-jinja2-188849
