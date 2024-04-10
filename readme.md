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

#### 1.3 Instalar FastAPI y Uvicorn:

Con el entorno virtual activo, instala FastAPI y Uvicorn, que es el servidor ASGI recomendado para ejecutar aplicaciones FastAPI.

```Powershell
pip install fastapi uvicorn
```

#### 1.4 crear un archivo "requirements.txt"

Si ya sabes qué bibliotecas adicionales necesitas, puedes crear un archivo requirements.txt manualmente y listarlas allí. Por ejemplo:

```
fastapi==0.68.0
uvicorn==0.15.0
```

Asegúrate de reemplazar las versiones con las que desees usar.

#### 1.5 Instalar los requisitos del archivo requirements.txt:

Si ya tienes un archivo requirements.txt, puedes instalar todas las dependencias listadas en él con el siguiente comando:

```bash
pip install -r requirements.txt

```
