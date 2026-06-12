## 📚 Programa de Especialización: Redes Neuronales Aprendizaje Profundo

### Módulo 1: Fundamentos Matemáticos y el Origen de la Neurona

*Objetivo:* Demantelar la "caja negra". Entender que una neurona es una combinación de álgebra lineal y optimización.

* **La neurona biológica al modelo matemático:** El Perceptrón de Rosenblatt.
* **Operaciones Fundamentales:** Combinación lineal ($z = \sum w_i x_i + b$) y por qué necesitamos funciones de activación no lineales (Sigmoide, Tanh, ReLU).
* **Mecanismo de Aprendizaje:** La función de pérdida (*Loss Function*) como brújula y el Descenso de Gradiente como el motor de optimización.

---

### Módulo 2: Redes Densas y Perceptrón Multicapa (MLP)

*Objetivo:* Aprender a conectar neuronas en cascada para resolver problemas no lineales (Tu Sesión 1).

* **Arquitectura Feedforward:** Capas de entrada, capas ocultas y capas de salida.
* **El algoritmo de Backpropagation:** Regla de la cadena matemática para calcular cómo influye cada peso en el error global.
* **Problemas Prácticos del Entrenamiento:** *Overfitting* (sobreajuste) vs. *Underfitting*. Técnicas de regularización: Dropout, regularización $L_1$/$L_2$ y normalización por lotes (*Batch Normalization*).
* **Proyecto Práctico:** Clasificación de datos tabulares complejos o predicción numérica (Regresión).

---

### Módulo 3: Visión Artificial y Redes Convolucionales (CNN)

*Objetivo:* Procesar datos con estructura espacial sin perder la geometría (Tu Sesión 2).

* **La operación de Convolución:** Filtros espaciales automáticos (repasando el concepto de detectores de bordes horizontales/verticales).
* **Capas de Reducción:** Max Pooling y Average Pooling.
* **Arquitecturas Clásicas de la Industria:** Estudio de cómo evolucionó el estado del arte (LeNet-5, AlexNet, VGG, y el hito de las conexiones residuales en ResNet).
* **Proyecto Práctico:** El pipeline completo que ya tienes de reconocimiento de caracteres (EMNIST) o clasificación de subtipos de infraestructura en imágenes de teledetección.

---

### Módulo 4: Redes Secuenciales y Procesamiento de Tiempo (RNN y LSTM)

*Objetivo:* Trabajar con datos donde el orden importa (series temporales, telemetría de sistemas, texto o audio).

* **El problema de la memoria:** Por qué las redes densas y convolucionales fallan al procesar secuencias (asumen que cada entrada es independiente).
* **Redes Neuronales Recurrentes (RNN):** Concepto de estado oculto (*recurrent loop*). El problema del desvanecimiento del gradiente (*Vanishing Gradient*).
* **Celdas de Memoria Avanzadas:** Arquitecturas LSTM (Long Short-Term Memory) y GRU. Cómo controlan el olvido y la retención de información a largo plazo.
* **Proyecto Práctico:** Predicción de series temporales (por ejemplo, comportamiento de variables meteorológicas, órbitas, o telemetría de sensores).

---

### Módulo 5: Modelos de Atención y la Revolución de los Transformers

*Objetivo:* Comprender la arquitectura que dejó atrás a las redes recurrentes y que sostiene a la Inteligencia Artificial moderna.

* **El mecanismo de Auto-Atención (Self-Attention):** Cómo la red aprende a relacionar partes distantes de una secuencia simultáneamente sin importar la distancia.
* **Arquitectura Transformer:** Desglose del bloque Encoder y Decoder (la base de BERT y GPT).
* **Aplicaciones Modernas:** Introducción al uso de modelos masivos preentrenados (*Large Language Models*) y técnicas de ajuste fino (*Fine-Tuning*).

---

### Módulo 6: Modelos Generativos y Aprendizaje No Supervisado

*Objetivo:* Enseñar a la red no solo a clasificar o predecir, sino a *crear* datos sintéticos realistas.

* **Autoencoders (AE y VAE):** Compresión de datos al espacio latente, eliminación de ruido y reconstrucción de información.
* **Redes Generativas Adversarias (GANs):** La competencia matemática entre dos redes (el Generador que falsifica y el Discriminador que inspecciona).
* **Proyecto Final de Egreso:** Implementación de un sistema de detección de anomalías o generación de datos sintéticos para aumentar datasets pequeños.

