# Taller Técnico: Entrenamiento de Redes Neuronales
> **Resolución de Problemas de Regresión y Clasificación con Python**

Este repositorio contiene el material didáctico, los cuadernos de código e interfaces visuales utilizados en el taller práctico de Redes Neuronales Artificiales dictado para el personal científico-técnico de la **Agencia Bolivariana para Actividades Espaciales (ABAE)**.

El objetivo fundamental es dotar a los participantes de los cimientos teóricos y prácticos indispensables para modelar magnitudes físicas continuas y procesar matrices multidimensionales (tensores) enfocadas en visión por computador.

---

## 🚀 Entorno de Ejecución

Para garantizar una experiencia fluida y **cero configuraciones locales de hardware o dependencias (CUDA, Anaconda, etc.)**, el taller se imparte de forma nativa sobre **Google Colab**. 

### Presentación del taller

Disponible en el siguiente [enlace](https://hmartinezdev.com:8081/storage/uploads/simpleproject_6a22f2e272919_introduccion-nn-python.html).

### Cuadernos de Práctica (Notebooks)
Puedes ejecutar los laboratorios directamente en la nube haciendo clic en los siguientes botones:

| Sesión | Componente Práctico | Enlace de Ejecución |
| :--- | :--- | :--- |
| **Sesión 1** | Laboratorio de Regresión en Física (Estimación Continua) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hmartinez00/introduccion-nn-python/blob/main/notebooks/sesion_1_regresion.ipynb#copy=true) |
| **Sesión 2** | Laboratorio de Clasificación de Imágenes (Vision Artificial) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hmartinez00/introduccion-nn-python/blob/main/notebooks/sesion_2_clasificacion.ipynb#copy=true) |
| **Cuaderno práctico GNSS** | Laboratorio de retos - Navegación | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hmartinez00/introduccion-nn-python/blob/main/notebooks/practicas_gnss.ipynb#copy=true) |
| **Cuaderno práctico SS** | Laboratorio de retos - Sistemas Espaciales | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hmartinez00/introduccion-nn-python/blob/main/notebooks/labs/practica_sistemas_espaciales.ipynb#copy=true) |


---

## 📋 Estructura General del Taller

El programa está diseñado para ejecutarse en una modalidad intensiva de **2 horas en total**, dividida en dos bloques de 60 minutos cada uno:

### 🔹 Sesión 1: Regresión en Física (60 Minutos)
Orientada al modelado de magnitudes continuas a partir de observaciones experimentales, eludiendo la necesidad de codificar la ecuación física analítica de control.
* **Bloque Teórico (15 min):** Fundamentos de la neurona artificial (pesos, sesgos, combinaciones lineales), funciones de activación intermedias (ReLU), salida lineal y criterios de topología para mitigar el infra o sobreajuste (*underfitting/overfitting*).
* **Bloque Práctico (35 min):** Construcción de un modelo con la API Keras Sequential, optimizador Adam, función de pérdida Error Cuadrático Medio (MSE) y monitoreo de curvas de convergencia.
* **Debate y Cierre (10 min):** Validación analítica mediante métricas alternativas (MAE).

### 🔹 Sesión 2: Clasificación de Imágenes (60 Minutos)
Orientada al tratamiento de matrices multidimensionales (tensores) en visión por computador y el mapeo probabilístico de salidas.
* **Bloque Teórico (15 min):** Preprocesamiento y normalización escalar en el rango $[0, 1]$, mecánica de aplanado de datos (Capa `Flatten`), activación terminal `Softmax` y pérdida *Sparse Categorical Cross-Entropy*.
* **Bloque Práctico (35 min):** Importación del benchmark clásico **Fashion-MNIST** (70,000 muestras digitalizadas de prendas en escala de grises), codificación de la arquitectura MLP (784 $\rightarrow$ 128 $\rightarrow$ 10 nodos) y evaluación con el conjunto de testeo independiente.
* **Debate y Cierre (10 min):** Interpretación del vector de probabilidad de salida y cálculo del *Accuracy*.

---

## 🛠️ Estructura del Repositorio

Para mantener el orden del proyecto, se sugiere organizar los archivos bajo el siguiente árbol de directorios:

```text
├── presentation/
│   └── introduccion-nn-python.html  # Presentación interactiva y responsiva del taller
├── notebooks/
│   ├── sesion_1_regresion.ipynb     # Cuaderno interactivo de la Sesión 1
│   └── sesion_2_clasificacion.ipynb # Cuaderno interactivo de la Sesión 2
└── README.md                        # Documentación principal del repositorio

```

---

## 🚫 Límites Operacionales (Fuera de Alcance)

Para cumplir rigurosamente con el itinerario de tiempo establecido, quedan excluidos de esta introducción:

* Arquitecturas profundas complejas de convolución espacial (CNN).
* Técnicas de aumento sintético de datos (*Data Augmentation*).
* Despliegue operativo en producción, empaquetado en contenedores o consumo mediante APIs Cloud.

---

## 👤 Facilitador

* **Héctor Martínez**
* Jefe (E) de la Unidad de Telecomunicaciones / OMS
* *Agencia Bolivariana para Actividades Espaciales (ABAE)*
