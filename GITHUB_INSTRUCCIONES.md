# INSTRUCCIONES PARA SUBIR A GITHUB

## PASO 1: Crear Repositorio en GitHub

1. Ve a https://github.com y inicia sesión con tu cuenta
2. Haz clic en el ícono "+" en la esquina superior derecha
3. Selecciona "New repository"
4. Completa los datos:
   - **Repository name**: `auditoria-ti-estructura-organizacional`
   - **Description**: "Herramienta de auditoría para evaluar la estructura organizacional del área de Sistemas de Información"
   - **Visibility**: Public (para que otros puedan verlo)
   - **Initialize this repository with**: Dejar vacío (ya tenemos commits locales)
5. Haz clic en "Create repository"

---

## PASO 2: Conectar Repositorio Local con GitHub

Una vez creado el repositorio en GitHub, ejecuta estos comandos en PowerShell:

```powershell
cd "c:\Users\dinop\Desktop\par2"

# Cambiar el nombre de la rama a 'main' (estándar de GitHub)
git branch -M main

# Agregar el repositorio remoto (reemplaza TU_USUARIO por tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/auditoria-ti-estructura-organizacional.git

# Subir los archivos a GitHub
git push -u origin main
```

### Ejemplo con usuario "dinop":
```powershell
git remote add origin https://github.com/dinop/auditoria-ti-estructura-organizacional.git
git push -u origin main
```

---

## PASO 3: Autenticación en GitHub

Si es la primera vez, GitHub te pedirá autenticación. Tienes 2 opciones:

### Opción A: Token Personal (Recomendado para 2025)
1. Ve a: https://github.com/settings/tokens
2. Haz clic en "Generate new token" → "Generate new token (classic)"
3. Dale un nombre: "Git CLI Token"
4. Selecciona scopes: `repo`, `write:repo_hook`
5. Copia el token
6. Cuando Git pida contraseña, pega el token

### Opción B: SSH Key
1. Genera clave SSH: `ssh-keygen -t ed25519 -C "tu_email@example.com"`
2. Copia la clave pública: `cat ~/.ssh/id_ed25519.pub`
3. Agrega en GitHub: Settings → SSH Keys → New SSH Key
4. Usa URL SSH en el remote: `git@github.com:usuario/repo.git`

---

## PASO 4: Verificar que se Subió

Luego de ejecutar `git push`, deberías ver:

```
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Writing objects: 100% (18/18), 145.2 KB, done.
Total 18 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/TU_USUARIO/auditoria-ti-estructura-organizacional.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

## PASO 5: Agregar más Detalles a GitHub (Opcional)

Una vez subido, puedes:

1. **Editar README en GitHub**
   - El archivo `README.md` aparecerá en la página principal
   - GitHub lo formatea automáticamente

2. **Agregar Topics**
   - En la página del repo, haz clic en el ícono de engranaje
   - Agrega topics: `python`, `auditoria`, `ti`, `estructura-organizacional`, `iso27001`

3. **Habilitar Wiki**
   - Settings → Features → Wiki (puede ser útil para documentación adicional)

4. **Agregar Badges**
   - Puedes agregar badges al README (Python version, License, etc.)

---

## ESTRUCTURA DEL REPOSITORIO EN GITHUB

Una vez subido, la estructura será:

```
auditoria-ti-estructura-organizacional/
├── README.md                    (Principal)
├── LICENSE                      (MIT)
├── .gitignore                   (Archivos ignorados)
├── DIAGRAMAS_UML.md            (Documentación)
├── ENTREGA.md                  (Resumen)
├── INDICE.txt
├── INICIO_RAPIDO.txt
├── RESUMEN_VISUAL.txt
├── _LEER_PRIMERO.txt
├── main.py                     (Entrada)
├── modelos.py                  (Clases)
├── motor_evaluacion.py         (Lógica)
├── interfaz.py                 (UI)
├── base_legal.py               (Normativa)
├── test_simple.py              (Pruebas)
└── prueba_demo.py              (Pruebas alternativas)
```

---

## COMANDOS GIT ÚTILES DESPUÉS

```powershell
# Ver el estado actual
git status

# Ver historial de commits
git log

# Ver cambios antes de commit
git diff

# Hacer nuevo commit después de cambios
git add .
git commit -m "Descripción del cambio"
git push

# Crear nueva rama
git checkout -b nueva-rama
git push -u origin nueva-rama
```

---

## LINK FINAL

Una vez subido, el repositorio estará en:

```
https://github.com/TU_USUARIO/auditoria-ti-estructura-organizacional
```

Puedes compartir este enlace para que otros vean tu proyecto.

---

## NOTAS IMPORTANTES

1. **Privacy**: Si quieres mantener privado: elige "Private" al crear el repo
2. **Colaboración**: Otros pueden hacer fork y pull requests si lo deseas
3. **Issues**: Pueden usarse para reportar bugs o sugerencias
4. **Discussions**: Puedes habilitar para que otros hagan preguntas
5. **GitHub Pages**: Puedes hospedar un sitio web del proyecto

---

## PROXIMOS PASOS

1. Ve a https://github.com/settings/tokens (si usas token)
2. Ejecuta los comandos de PASO 2
3. Verifica en https://github.com/TU_USUARIO/auditoria-ti-estructura-organizacional

¡Listo! Tu proyecto estará disponible públicamente en GitHub.

