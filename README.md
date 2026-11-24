<div align="center">

# Juego de Profesores

**Practicá cara a cara con tus profesores antes del parcial.**

[![Versión](https://img.shields.io/github/v/release/germanlauria/Juego-Profesores-Descargas?style=for-the-badge&label=versi%C3%B3n&color=f6c945&labelColor=172036)](https://github.com/germanlauria/Juego-Profesores-Descargas/releases/latest)
[![Publicada](https://img.shields.io/github/release-date/germanlauria/Juego-Profesores-Descargas?style=for-the-badge&label=publicada&color=1f7a52&labelColor=172036)](https://github.com/germanlauria/Juego-Profesores-Descargas/releases)
[![Descargas](https://img.shields.io/github/downloads/germanlauria/Juego-Profesores-Descargas/total?style=for-the-badge&label=descargas&color=3f8fd2&labelColor=172036)](https://github.com/germanlauria/Juego-Profesores-Descargas/releases)

![Estado](https://img.shields.io/badge/estado-en%20desarrollo-e8674f?style=flat-square)
![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D4?style=flat-square)
![Android](https://img.shields.io/badge/Android-7.0%20o%20m%C3%A1s-34A853?style=flat-square&logo=android&logoColor=white)
![Idioma](https://img.shields.io/badge/idioma-espa%C3%B1ol%20%28Argentina%29-75AADB?style=flat-square)
![Sin conexión](https://img.shields.io/badge/funciona-sin%20internet-1f4d42?style=flat-square)
[![Problemas abiertos](https://img.shields.io/github/issues/germanlauria/Juego-Profesores-Descargas?style=flat-square&label=problemas%20abiertos)](https://github.com/germanlauria/Juego-Profesores-Descargas/issues)

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Preact](https://img.shields.io/badge/Preact-673AB8?style=flat-square&logo=preact&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Tauri](https://img.shields.io/badge/Tauri-24C8DB?style=flat-square&logo=tauri&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Capacitor](https://img.shields.io/badge/Capacitor-119EFF?style=flat-square&logo=capacitor&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white)
![Fastify](https://img.shields.io/badge/Fastify-000000?style=flat-square&logo=fastify&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

[Descargar](#versión-actual) · [Qué es](#qué-es) · [Cómo se juega](#cómo-se-juega) · [Instalación](#instalación) · [Preguntas](#preguntas-frecuentes)

</div>

---

<!-- VERSION:INICIO -->
## Versión actual

Todavía no hay instaladores publicados. Cuando salga la primera versión, los enlaces van a aparecer acá.
<!-- VERSION:FIN -->

## Qué es

Un juego educativo para la **Tecnicatura en Análisis de Sistemas**. Elegís un profesor, aparece frente a vos en el aula y practicás con él: te explica, te pregunta, te responde y te toma examen.

Es 100% 2D y liviano, pensado para andar bien en computadoras y celulares de gama baja.

## Características

- **Cuatro formas de practicar** con cada profesor.
- **Corrección al momento**, con puntaje y devolución.
- **Profesores animados**: mueven la boca, parpadean y gesticulan solo cuando hablan.
- **Tus propios apuntes**: los sumás y el profesor los usa para responderte.
- **Puntos, niveles y rachas**, por profesor y por materia.
- **Logros** para desbloquear.
- **Funciona sin internet**, con el contenido que trae adentro.
- **Se actualiza desde el juego**, sin desinstalar.
- **Ajustes para equipos lentos**: animaciones, bajo consumo, volumen y tamaño de texto.

## Cómo se juega

| Modo | Qué hace |
| --- | --- |
| **El profesor me explica** | Elegís un tema y te lo cuenta como en clase. |
| **El profesor me pregunta** | Respondés y te corrige al momento. |
| **Yo le pregunto al profesor** | Le consultás una duda y te responde. |
| **Armar evaluación** | Te arma un parcial, lo resolvés y te lo corrige con nota. |

### Con y sin servidor

| | Sin servidor | Con servidor |
| --- | :---: | :---: |
| Los cuatro modos | ✅ | ✅ |
| Puntos, niveles y logros | ✅ | ✅ |
| Apuntes propios de texto | ✅ | ✅ |
| Apuntes en PDF o Word | ❌ | ✅ |
| Respuestas y correcciones con IA | ❌ | ✅ |
| Voz de los profesores | ❌ | ✅ |
| Imitar un examen real con una foto | ❌ | ✅ |

El servidor es opcional: se carga su dirección en **Configuración → Servidor**. La IA, la voz y las fotos dependen de que ese servidor las tenga activadas.

## Instalación

### Windows

1. Descargá el `.exe` de la [versión actual](#versión-actual).
2. Abrilo y seguí los pasos. No hace falta ser administrador.
3. Si aparece "Windows protegió su PC", es porque la app no tiene un certificado pago. Comprobá que el archivo salió de esta página y tocá **Más información** → **Ejecutar de todas formas**.

### Android

1. Desde el celular, descargá el `.apk` de la [versión actual](#versión-actual).
2. Abrilo. Si te lo pide, permití instalar aplicaciones de esa fuente.
3. Tocá **Instalar**.

### Actualizaciones

El juego avisa en el menú cuando hay una versión nueva y se instala encima de la anterior: no hace falta desinstalar y no se pierde el progreso. En Android, el sistema siempre pide confirmar la instalación.

También podés buscarla a mano en **Configuración → Buscar actualizaciones**.

## Hecho con

| Parte | Tecnología |
| --- | --- |
| Lenguaje | TypeScript |
| Juego | Preact + Vite, 2D con imágenes en capas y CSS |
| App de Windows | Tauri (Rust) |
| App de Android | Capacitor (Java) |
| Servidor opcional | Node.js + Fastify + SQLite |
| IA y voz opcionales | Claude y ElevenLabs, a través del servidor |

## Privacidad

- El progreso se guarda en tu dispositivo.
- Sin servidor, lo que escribís no sale del dispositivo. Las apps solo se conectan a GitHub para ver si hay una versión nueva.
- En Android, el dictado lo hace el servicio de voz de tu teléfono.
- Con servidor, tus preguntas, respuestas, apuntes y fotos se le envían para poder responderte, y pueden procesarse con servicios de IA y de voz. Antes de subir un examen, tapá nombres y notas de otras personas.

## Preguntas frecuentes

<details>
<summary><b>¿Necesito internet?</b></summary>

Solo para descargarlo, actualizarlo y usar un servidor. Para practicar, no.
</details>

<details>
<summary><b>¿Pierdo mi progreso al actualizar?</b></summary>

No. Se instala encima de la versión anterior. Sí se pierde si desinstalás la app o borrás sus datos.
</details>

<details>
<summary><b>¿Puedo dictar las respuestas?</b></summary>

En Android, con el botón del micrófono. En Windows, con el dictado del sistema: <kbd>Windows</kbd> + <kbd>H</kbd>.
</details>

<details>
<summary><b>¿Reemplaza a las clases?</b></summary>

No. Es una herramienta para practicar y puede equivocarse: ante la duda, vale lo que diga tu docente.
</details>

<details>
<summary><b>Encontré un error, ¿dónde lo aviso?</b></summary>

En [Problemas](https://github.com/germanlauria/Juego-Profesores-Descargas/issues). Contá qué dispositivo usás, qué versión y qué hiciste antes de que fallara.
</details>

---

<div align="center">

Este repositorio publica solo los instaladores. La versión, los enlaces y los cartelitos se actualizan solos.

</div>
