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

### 1.6 Crear el archivo deployment.yaml
Para crear un archivo llamado deployment.yaml dentro de una carpeta llamada kubernetes, ejecuta los siguientes comandos en la terminal:

```
mkdir kubernetes
cd kubernetes
nano deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fasapi-deployment
  labels:
    app: fasapi
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fasapi
  template:
    metadata:
      labels:
        app: fasapi
    spec:
      containers:
      - name: fasapi
        image: jamesacosta/fasapi:04
        ports:
        - containerPort: 5050
```
### 1.7 Instalar Minikube y Iniciar el Cluster
Para instalar la última versión estable de Minikube en Linux x86-64 utilizando la descarga binaria, ejecuta los siguientes comandos en la terminal:

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

### 1.8 Para iniciar el cluster, ejecuta el siguiente comando:
```
minikube start
```

### 2.0 Crear un Alias para kubectl
Puedes crear un alias para kubectl que apunte a la versión de kubectl de Minikube con el siguiente comando:

```
alias kubectl="minikube kubectl --"
```
### 2.1 Desplegar la Aplicación en Minikube
Para desplegar la aplicación en Minikube, asegúrate de estar en la carpeta donde se encuentra el archivo deployment.yaml, luego ejecuta el siguiente comando:

```
kubectl apply -f deployment.yaml
```

### 2.2 Con estos comandos podremos comprobar que todo se ejecuto correctamente y tenemos exito en la aplicacion, podremos usar un portforward para acceder a la aplicacion

```
kubectl port-forward pod/name-pod 5050:5050
```
