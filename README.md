# Google Search Console Data Downloader

## Descripción

Este script en Python utiliza la API de Google Search Console para descargar datos de rendimiento de búsqueda y guardarlos en un archivo CSV. El script permite especificar el dominio, la cantidad de días de datos históricos a recuperar, y el nombre del archivo de credenciales.

## Requisitos

- Python 3.x
- Librerías necesarias: \`google-auth\`, \`google-auth-oauthlib\`, \`google-auth-httplib2\`, \`google-api-python-client\`

Puedes instalar las dependencias ejecutando:
\`\`\`bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
\`\`\`

## Configuración

- **GSC_JSON_FILE:** Ruta al directorio que contiene el archivo JSON de credenciales de Google Search Console.
- **OUTPUT_FILE_NAME:** Nombre del archivo CSV de salida que contendrá los datos descargados.

## Uso

1. Asegúrate de tener las dependencias instaladas.
2. Coloca el archivo JSON de credenciales de Google Search Console en la ubicación especificada por \`GSC_JSON_FILE\`.
3. Configura los parámetros de ejecución como el dominio (\`DOMAIN\`), la cantidad de días históricos (\`DAYS_AGO\`), y el nombre del archivo de credenciales (\`CREDENTIALS_FILE_NAME\`).
4. Ejecuta el script:
   \`\`\`bash
   python tu_script.py
   \`\`\`

## Contribución

Si deseas contribuir, ¡estamos abiertos a sugerencias y mejoras! Por favor, sigue las pautas de contribución.

## Licencia

Este script está bajo la Licencia MIT. Consulta el archivo \`LICENSE\` para obtener más detalles.

## Autor

[Nombre del Autor]

## Agradecimientos

Agradecimientos a las bibliotecas y herramientas de Google utilizadas en este script.

## Notas Adicionales

Cualquier información adicional que sea relevante para el usuario o el desarrollo del script.
