# djangorestframework practice
De acuerdo, he actualizado la documentación para reflejar este cambio:

**Documentación de la aplicación de Django**

**Introducción**

Esta aplicación de Django es un ejemplo sencillo de cómo crear y documentar una API RESTful. La aplicación consta de tres ramas principales:

* **docs:** Esta rama contiene la documentación de la API.
* **api/v1:** Esta rama contiene la implementación de la API en su versión 1.
* **admin:** Esta rama contiene la aplicación administrativa de Django.

**Requisitos**

Para utilizar esta aplicación, es necesario tener instalado Python 3.8 o superior. Además, es necesario instalar los siguientes paquetes de Python:

* Django
* Django REST framework
* Coreapi

**Instalación**

Para instalar la aplicación, siga los siguientes pasos:

1. Clone el repositorio de GitHub:

```
git clone git@github.com:JuliusValentineI/djangorestframework.git
```

2. Cambie al directorio de la aplicación:

```
cd djangorestframework
```

3. Instale los paquetes de Python necesarios:

```
pip install -r requirements.txt
```

**Iniciar el servidor**

Para iniciar el servidor de Django, ejecute el siguiente comando:

```
python manage.py runserver
```

Esto iniciará el servidor en el puerto 8000.

**Documentación de la API**

La documentación de la API se encuentra en la rama `docs`. La documentación se genera automáticamente utilizando el paquete `Coreapi`.

Para acceder a la documentación, abra un navegador web y navegue a la siguiente URL:

```
http://localhost:8000/docs/
```

La documentación mostrará una lista de las rutas de la API, junto con la información sobre los métodos HTTP, los parámetros y los tipos de datos devueltos.

**Implementación de la API**

La implementación de la API se encuentra en la rama `api/v1`. La API implementa los siguientes recursos:

* **Programmers** Esta ruta permite crear, leer, actualizar y eliminar programadores.

Para acceder a la API, utilice los métodos HTTP apropiados para la ruta que desee utilizar. Por ejemplo, para crear un nuevo usuario, utilice el siguiente método HTTP:

```
POST /api/v1/programmers/
```

O acceder a ella atraves de:

```
http://localhost:8000/api/v1/[modelo] # En mi caso => /programmers
```

El cuerpo de la solicitud debe contener los datos del usuario que desea crear. Por ejemplo:

```
{
    "fullname": "Hernani Gonzalez",
    "nickname": "HG",
    "age": null,
    "is_active": false #Default = True
}
```

**Aplicación administrativa**

La aplicación administrativa de Django se encuentra en la rama `admin`. La aplicación administrativa permite gestionar los usuarios y los productos de la aplicación.

Para acceder a la aplicación administrativa, abra un navegador web y navegue a la siguiente URL:

```
http://localhost:8000/admin/
```

**Motivo de la creación de la aplicación**

Esta aplicación fue creada para practicar y demostrar el manejo de API RESTfull, tanto para crearlas como editarlas y documentarlas.

**Conclusión**

Esta aplicación es un ejemplo sencillo de cómo crear y documentar una API RESTfull. La aplicación puede utilizarse como punto de partida para crear aplicaciones más complejas.
