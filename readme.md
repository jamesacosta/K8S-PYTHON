<!-- Para iniciar un proyecto de Python utilizando FastAPI desde la creación de un entorno virtual (venv) hasta la instalación de los requisitos (requirements.txt), puedes seguir los siguientes pasos en la terminal de tu sistema operativo. Asumiré que ya tienes Python instalado en tu sistema.


1. Crear un entorno virtual:
	1.1 Primero, navega hasta la carpeta donde quieres crear tu proyecto y luego ejecuta:
		bash
		python -m venv venv
		Esto creará un entorno virtual en una carpeta llamada venv.
	1.2 Activar el entorno virtual:
		Luego, activa el entorno virtual. La forma de hacerlo varía según el sistema operativo:
	1.3 En Windows:
		bash
		.\venv\Scripts\activate
		En macOS y Linux:
		bash
		source venv/bin/activate
	1.4 Instalar FastAPI y Uvicorn:
		Con el entorno virtual activo, instala FastAPI y Uvicorn, que es el servidor ASGI recomendado para ejecutar aplicaciones FastAPI.
		bash
		pip install fastapi uvicorn
		Crear un archivo requirements.txt:
	1.5 Si ya sabes qué bibliotecas adicionales necesitas, puedes crear un archivo requirements.txt manualmente y listarlas allí. Por ejemplo:
		fastapi==0.68.0
		uvicorn==0.15.0
	1.6 Asegúrate de reemplazar las versiones con las que desees usar.
	1.7 Instalar los requisitos del archivo requirements.txt:
	1.8 Si ya tienes un archivo requirements.txt, puedes instalar todas las dependencias listadas en él con el siguiente comando:
		bash
		pip install -r requirements.txt
		python -m venv venv
		.\venv\Scripts\activate
		pip install -r requirements.txt -->

# Iniciar un Proyecto de FastAPI

Para iniciar un proyecto de Python utilizando FastAPI desde la creación de un entorno virtual (venv) hasta la instalación de los requisitos (`requirements.txt`), puedes seguir los siguientes pasos en la terminal de tu sistema operativo. Este tutorial asume que ya tienes Python instalado en tu sistema.

## Pasos

### 1. Crear un entorno virtual

#### 1.1 Primero, navega hasta la carpeta donde quieres crear tu proyecto y luego ejecuta:

```bash
python -m venv venv
```

Esto creará un entorno virtual en una carpeta llamada venv.

#### 1.2 Luego, activa el entorno virtual. La forma de hacerlo varía según el sistema operativo:

##### En windows:

```Powershell
		.\venv\Scripts\activate
```

##### En MacOs y Linux:

```Powershell
		source venv/bin/activate
```
