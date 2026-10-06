# Lista de tareas en consola — primer ejercicio de Git

Programa de consola en **Python** para gestionar una lista de tareas (agregar, editar y eliminar) con un menú interactivo. Es el código base de mi primer ejercicio de **Git y GitHub**: crear el repositorio, hacer el primer commit y subirlo.

La evolución de este mismo código (refactor a funciones y a módulos, cada uno en su rama) está en [`ejercicios-git-`](https://github.com/Eidan210/ejercicios-git-).

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-primer_commit-F05032?style=flat-square&logo=git&logoColor=white)
![Sin dependencias](https://img.shields.io/badge/dependencias-ninguna-2E7D32?style=flat-square)
![Último commit](https://img.shields.io/github/last-commit/Eidan210/ejercicio-git?style=flat-square&label=último%20commit)

![Ejecución de la lista de tareas en la terminal](docs/consola.webp)

## El problema

Antes de trabajar con ramas y pull requests hace falta dominar lo básico: versionar un programa propio, escribir un commit con un mensaje que explique el cambio y publicarlo en GitHub. Una lista de tareas en consola es un proyecto lo bastante pequeño para centrarse en ese flujo.

## Tecnologías

| Tecnología | Para qué se usa |
| :--- | :--- |
| **Python 3** | Menú con `while True`, listas, `input()` y métodos de cadena como `capitalize()`. |
| **Git y GitHub** | Repositorio, primer commit y publicación del código. |

## Funciones clave

- **Menú interactivo** con 4 opciones que se repite hasta elegir *salir*.
- **Agregar tareas** normalizadas con mayúscula inicial, con la opción de seguir agregando.
- **Editar una tarea** buscándola por su texto y reemplazándola en su posición.
- **Eliminar una tarea**, comprobando antes que existe y avisando si no se encuentra.

## Evidencias

La captura de arriba es una ejecución real: se agregan dos tareas y se elimina una.

```mermaid
flowchart TD
    M["Menú"] -->|1| A["Agregar tarea<br/>.capitalize() + append"]
    M -->|2| E["Editar tarea<br/>index() + reemplazo"]
    M -->|3| D["Eliminar tarea<br/>si existe → remove()"]
    M -->|4| S["Salir"]
    A --> M
    E --> M
    D --> M
```

### Mejoras identificadas

Revisando el código encontré estos puntos. La versión modular de [`ejercicios-git-`](https://github.com/Eidan210/ejercicios-git-) ya corrige el mensaje de edición; el resto sigue pendiente:

- La validación `opcion <= 0 and opcion >= 5` nunca se cumple; debería usar `or`.
- `int(input(...))` termina el programa si se escribe algo que no es un número.
- Al editar se muestra `error` aunque el cambio se haya hecho bien, y si la tarea no existe, `index()` lanza un `ValueError`.

## Instalación y uso

Requiere Python 3:

```bash
git clone https://github.com/Eidan210/ejercicio-git.git
cd ejercicio-git
python codigo_base.py
```

## Aprendizajes

- **El flujo básico de Git:** `init`, `add`, `commit` y `push` sobre un proyecto propio.
- **Estructurar un programa de consola** con un bucle de menú y operaciones sobre listas.
- **Leer mi propio código con ojo crítico:** detectar condiciones que nunca se cumplen y entradas que rompen el programa.

---

Desarrollado por **Eidan Alexander Carreño** ([@Eidan210](https://github.com/Eidan210)).
