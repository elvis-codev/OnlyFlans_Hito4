# OnlyFlans HITO 4 - Sitio Web de Pasteles y Postres
------
<div style="text-align:center">
    <img src="https://doc-images-adl.s3.sa-east-1.amazonaws.com/verde+en+fondo+blanco.png" alt="Texto alternativo 1" width="200" style="display:inline">
</div>

------
OnlyFlans es un proyecto de sitio web desarrollado en Django para una PYME dedicada a la venta de pasteles y postres, con un enfoque especial en el flan. El objetivo principal del sitio es presentar los productos de la empresa al público en general, así como también ofrecer productos especiales exclusivos para usuarios registrados.

## Screenshots de las Vistas
<div>
    <img src="https://github.com/elvis-codev/OnlyFlans_Hito3/blob/main/Screenshots/Captura1.png" width="200" />
    <img src="https://github.com/elvis-codev/OnlyFlans_Hito3/blob/main/Screenshots/Captura2.png" width="200" />
</div>

## Screenshots de Mejoras
<div>
    <img src="https://github.com/elvis-codev/OnlyFlans_Hito3/blob/main/Screenshots/Captura4.png" width="200" />
    <img src="https://github.com/elvis-codev/OnlyFlans_Hito3/blob/main/Screenshots/Captura5.png" width="200" />
    <img src="https://github.com/elvis-codev/OnlyFlans_Hito4/blob/main/Screenshots/Captura6.png" width="200" />
    <img src="https://github.com/elvis-codev/OnlyFlans_Hito4/blob/main/Screenshots/Captura7.png" width="200" />
</div>
## Características Principales

- Presentación de productos de pastelería y postres.
- Oferta de productos especiales exclusivos para usuarios registrados.
- Sistema de registro y autenticación de usuarios.
- Administración de productos a través del panel de administración de Django.
- Potencial para futuras características como la venta en línea.

## Requisitos de Instalación

Para ejecutar este proyecto localmente, asegúrate de tener instalado lo siguiente:

- Python 3.10.10
- Django 4.2.11
- Un entorno virtual en WSL

## Usuarios

| TIPO  | username  | password  |
|---|---|---|
| superusuario  | admin  | 1234  |
| user_staff  | administrador  | elvis1234  |
| user  | Elvis  | 1234  |
--- 

## Instrucciones de Instalación

1. Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu_usuario/onlyflans.git
```

2. Navega hasta el directorio del proyecto:
```bash
cd onlyflans
```

3. Instala las dependencias utilizando pip:
```bash
pip install -r requirements.txt
```

4. Realiza las migraciones de la base de datos:
```bash
python manage.py migrate
```

5. Inicia el servidor de desarrollo de Django:
```bash
python manage.py runserver
```

