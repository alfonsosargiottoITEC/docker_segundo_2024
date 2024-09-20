# Resumen de CI/CD y GitHub Actions

## CI (Integración Continua): 
Es una práctica que implica integrar y probar el código frecuentemente (varias veces
al día) para detectar errores rápidamente. Cada vez que haces un cambio en el código y
lo subes al repositorio, se ejecutan automáticamente tareas como pruebas (tests) o análisis 
de calidad de código.

## CD (Entrega Continua o Despliegue Continuo): 
Va más allá de CI, y se encarga de automatizar el proceso de despliegue de la aplicación,
para que esté lista para ser lanzada o actualizada fácilmente. Con CD, puedes desplegar
una nueva versión del software de manera automática cada vez que los tests pasen exitosamente.

## GitHub Actions:
 Es la herramienta que ofrece GitHub para automatizar CI/CD. Permite configurar "workflows"
(flujos de trabajo) que se ejecutan automáticamente cuando sucede un evento, como un push
o pull request. Con GitHub Actions puedes ejecutar tests, hacer análisis de código, y
también desplegar la aplicación en diferentes servicios, todo desde GitHub.


## Workflows en este repositorio

#### Test Workflow
- Archivo: `ci-test.yml`
- Descripción: Ejecuta los tests con pytest en cada push y pull request.

#### Lint Workflow
- Archivo: `lint.yml`
- Descripción: Ejecuta Pylint para verificar la calidad del código en cada push o pull request.

#### Black Formatter
- Archivo: `black-format.yml`
- Descripción: Verifica el formateo del código usando Black en cada push o pull request.

#### Deploy Workflows
- Archivos: `deploy-heroku.yml`, `deploy-vercel.yml`, `deploy-github-pages.yml`
- Descripción: Despliegan la aplicación en los servicios correspondientes (Heroku, Vercel, GitHub Pages).
