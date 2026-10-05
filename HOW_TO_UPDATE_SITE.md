# Cómo actualizar la web

La web activa se mantiene en el repositorio `LeandroZipitria.github.io`.
El contenido se edita en archivos `.qmd`; los documentos descargables viven en `files/`.

## Regla general

- **Texto y estructura de una página** → editar el `.qmd` correspondiente.
- **PDF, CV, paper, clase, audio u otro archivo descargable** → guardar/reemplazar el archivo dentro de `files/`.
- **Imágenes del diseño** → `assets/`.
- **Diseño global** → `styles.css`.
- **Navegación y configuración** → `_quarto.yml`.
- `texflow.qmd` conserva más HTML que el resto porque funciona como landing de producto.

## Qué archivo controla cada página

| Página | Fuente |
|---|---|
| Home | `index.qmd` |
| About | `bio.qmd` |
| Research | `research.qmd` |
| Teaching | `teaching.qmd` |
| Professional | `professional.qmd` |
| TeXFlow | `texflow.qmd` |
| Writing & Media | `blog.qmd` |
| Personal | `personal.qmd` |
| Reading | `reading.qmd` |
| Contact | `contact.qmd` |

## Cambiar el PDF de un paper sin cambiar el texto

Si la URL debe permanecer igual, simplemente reemplazar el PDF dentro de `files/` conservando el mismo nombre.

Ejemplo:

```text
files/Chain Pricing and Long-Run Retail Price Divergence.pdf
```

No es necesario tocar `research.qmd` si el nombre y el enlace no cambian.

## Agregar o editar un paper en Research

En `research.qmd`, las entradas tienen este formato:

```markdown
::: {.research-entry}
::: {.research-year}
2026
:::

::: {.research-copy}
**Borraz, Fernando and Leandro Zipitría.** [Chain Pricing and Long-Run Retail Price Divergence](<files/Chain Pricing and Long-Run Retail Price Divergence.pdf>). Submitted. [Code](https://github.com/LeandroZipitria/Convergence).
:::
:::
```

Para modificar un paper, normalmente alcanza con editar la línea dentro de `.research-copy`.

Si el paper también está entre los tres destacados, editar además el bloque correspondiente en `Selected research` dentro de `research.qmd` y, si aparece en Home, en `index.qmd`.

## Agregar una clase

Guardar el PDF en la carpeta del curso, por ejemplo:

```text
files/teaching/current/desarrollo-economico/9-nueva-clase.pdf
```

Después agregar una línea a la lista numerada en `teaching.qmd`:

```markdown
10. [Nueva clase](files/teaching/current/desarrollo-economico/9-nueva-clase.pdf)
```

La numeración y el formato visual los maneja `styles.css`.

## Actualizar un documento de guidelines o un caso

En `teaching.qmd`, buscar el tema por su nombre y cambiar solo el enlace o el texto correspondiente.

Ejemplo:

```markdown
[EU]{.pill .eu} [2024]{.pill .current} [Market Definition Notice](https://...)
```

## Ver la web antes de publicar

Desde la raíz del repositorio:

```bash
quarto preview
```

Cerrar el preview con `Ctrl + C`.

Para un render completo:

```bash
quarto render
```

## Publicar

Después de revisar la web:

```bash
git status
git add -A
git commit -m "Update website"
git push origin master
```

GitHub Actions renderiza y publica automáticamente la nueva versión.

## Carpetas que no se editan como fuente

- `_site/` — generado por Quarto.
- `.quarto/` — archivos temporales de Quarto.
- `.Rproj.user/` — estado local de RStudio.
- `quarto_site_overlay/` — carpeta usada durante la migración; no es la web activa.

El libro de regulación sigue siendo un proyecto separado. La web contiene únicamente su versión publicada bajo `libro-regulacion/`.
