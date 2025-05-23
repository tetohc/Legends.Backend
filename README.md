# Legends.Backend 

## 📖 Leyendas Costarricenses

Este proyecto es una API con **FastAPI** para administrar un libro virtual de leyendas costarricenses. Permite gestionar leyendas con sus respectivos datos y ubicaciones dentro de Costa Rica.

## 🗂️ Diagrama Entidad-Relación (ER)
Diagrama **Entidad-Relación (ER)** de la Base de Datos MySQL.
![DiagramaER](https://raw.githubusercontent.com/tetohc/MediaResources/refs/heads/main/images/covers/legendscr_diagram_er.png)
[Diagrama ER](https://dbdiagram.io/d/legends_cr-6830da99b9f7446da3ea432f)

## 📌 API Endpoints

### 🏛 Provincias
- **GET** `/provinces/` - Obtener todas las provincias.
- **GET** `/provinces/{province_id}` - Obtener una provincia por ID.

### 🏙 Cantones
- **GET** `/cantons/` - Obtener todos los cantones.
- **GET** `/cantons/by-province/{province_name}` - Obtener cantones por nombre de provincia.
- **GET** `/cantons/by-province-id/{province_id}` - Obtener cantones por ID de provincia.

### 📌 Distritos
- **GET** `/districts/` - Obtener todos los distritos.
- **GET** `/districts/by-canton/{canton_name}` - Obtener distritos por nombre de cantón.
- **GET** `/districts/by-canton-id/{canton_id}` - Obtener distritos por ID de cantón.

### 🏷 Categorías
- **GET** `/categories/` - Obtener todas las categorías.

### 📖 Leyendas
- **POST** `/legends/create` - Crear una leyenda.
- **PUT** `/legends/update/{legend_id}` - Actualizar una leyenda.
- **DELETE** `/legends/delete/{legend_id}` - Eliminar una leyenda.
- **GET** `/legends/{legend_id}` - Obtener una leyenda por ID.
- **GET** `/legends/` - Obtener todas las leyendas.

## 🖼️ Imágenes
![demo_0](https://raw.githubusercontent.com/tetohc/MediaResources/refs/heads/main/images/covers/demo_legends_api_0.png)

![demo_1](https://raw.githubusercontent.com/tetohc/MediaResources/refs/heads/main/images/covers/demo_legends_api.png)

## 🚀 Instalación

### Clonar el proyecto
Para clonar el repositorio desde GitHub, usa el siguiente comando:

```bash
git clone <https://github.com/tetohc/Legends.Backend.git>
```
### Instalar dependencias

El proyecto tiene un archivo requirements.txt que contiene  las dependencias necesarias. Para instalarlas, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

### Configurar conexión de base de datos

Debes agregar tu propia cadena de conexión en la variable DATABASE_URL del archivo .env.

```bash
DATABASE_URL = "sqlite:///./test.db" # Reemplaza con tu propia cadena de conexión
```

### Ejecutar el proyecto

Para ejecutar el proyecto, usa el siguiente comando en la terminal:

```bash
python .\main.py
```
El proyecto se levantará en el puerto 8080.
