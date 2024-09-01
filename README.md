# Proyecto de Prueba con Click

Este proyecto es una simple demostración del uso de la librería [Click](https://click.palletsprojects.com/) en Python. Click es una biblioteca que facilita la creación de interfaces de línea de comandos (CLI).

## Requisitos

- Python 3.x instalado en tu sistema.
- Pip (gestor de paquetes de Python).

## Instrucciones para Configurar el Entorno

### 1. Clonar el Repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/lruizap/python-CLI.git
cd python-CLI
```

### 2. Crear y Activar el Entorno Virtual

Para mantener las dependencias aisladas, se recomienda utilizar un entorno virtual. Aquí te explicamos cómo hacerlo:

#### En Linux/MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### En Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar Dependencias

Una vez que el entorno virtual esté activado, instala las dependencias necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Probar el Proyecto

Ahora que todas las dependencias están instaladas, puedes probar el proyecto ejecutando uno de los comandos definidos con Click.

Por ejemplo:

```bash
python cli.py --help
```

Esto debería mostrarte la ayuda del CLI con las opciones y comandos disponibles.

## Estructura del Proyecto

- `cli.py`: El archivo principal que contiene la definición de la CLI con Click.
- `requirements.txt`: Archivo que lista las dependencias del proyecto.

---

¡Gracias por probar el proyecto con Click!
