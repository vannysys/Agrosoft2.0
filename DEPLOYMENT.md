# Guía de Despliegue - Agrosoft en Render

## Prerrequisitos
- Cuenta en [Render.com](https://render.com)
- Cuenta en [GitHub](https://github.com) (opcional, pero recomendado)

## Pasos para desplegar en Render

### 1. Preparar el repositorio
```bash
# Asegúrate de tener todos los archivos de configuración:
- render.yaml
- requirements.txt
- .gitignore
- gunicorn.conf.py
```

### 2. Subir a GitHub (opcional pero recomendado)
```bash
git init
git add .
git commit -m "Preparado para despliegue en Render"
git branch -M main
git remote add origin [URL_DEL_REPOSITORIO]
git push -u origin main
```

### 3. Desplegar en Render

#### Opción A: Usando render.yaml (Recomendado)
1. Ve a [Render Dashboard](https://dashboard.render.com)
2. Haz clic en "New +" y selecciona "Blueprint"
3. Conecta tu repositorio de GitHub (si lo subiste)
4. O sube el archivo `render.yaml` directamente
5. Render detectará automáticamente la configuración

#### Opción B: Configuración manual
1. Ve a [Render Dashboard](https://dashboard.render.com)
2. Haz clic en "New +" y selecciona "Web Service"
3. Conecta tu repositorio de GitHub
4. Configura el servicio:
   - **Name**: agrosoft
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn agrosoft.wsgi:application`
   - **Plan**: Free

### 4. Configurar variables de entorno en Render
En el dashboard de tu servicio web en Render, ve a la sección "Environment" y configura:

**Variables requeridas:**
- `SECRET_KEY`: [Generar una clave secreta segura]
- `DEBUG`: `False`
- `OPENWEATHER_API_KEY`: `3faff5e1a4b40f2e39babbe38f98365e`

**Variables de base de datos** (se configuran automáticamente si usas render.yaml):
- `DATABASE_URL`: [Render la proporciona automáticamente]

### 5. Configurar la base de datos
Si usas el archivo `render.yaml`, Render creará automáticamente una base de datos PostgreSQL.

### 6. Ejecutar migraciones
Después del despliegue, necesitas ejecutar las migraciones:

```bash
# En la consola de Render o usando SSH
python manage.py migrate
```

### 7. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

## Configuración de Email
Para que el sistema de email funcione, necesitas configurar las variables de entorno de email en Render con tus credenciales reales de Gmail.

## Solución de problemas comunes

### Error de archivos estáticos
Si hay problemas con archivos estáticos, ejecuta:
```bash
python manage.py collectstatic
```

### Error de base de datos
Verifica que las migraciones se hayan ejecutado correctamente.

### Error de permisos
Asegúrate de que todas las variables de entorno estén configuradas correctamente.

## URLs importantes
- **Aplicación**: https://agrosoft.onrender.com (o el dominio que Render te asigne)
- **Admin**: https://agrosoft.onrender.com/admin

## Notas importantes
- El plan free de Render puede tener tiempos de inactividad
- Las variables sensibles como contraseñas deben manejarse a través de variables de entorno
- Recomendado: Usar un dominio personalizado para producc