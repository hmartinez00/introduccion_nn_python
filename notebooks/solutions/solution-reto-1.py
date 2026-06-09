# =====================================================================
# FASE 0: SIMULACIÓN DE ATENUACIÓN ESTRUCTURAL EN CAÑONES URBANOS
# =====================================================================
# Importación del ecosistema de desarrollo para IA
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

print("Versión de TensorFlow en ejecución:", tf.__version__)

np.random.seed(42)

# Espesor de muros de concreto simulados (de 0.05 a 1.2 metros)
X_espesor = np.random.uniform(0.05, 1.2, 200)

# Física real: Caída exponencial de potencia (Atenuación severa asintótica en dB)
# A mayor espesor, la pérdida se dispara fuertemente
Y_atenuacion_db = 3.0 + (12.0 * np.exp(2.2 * X_espesor)) + np.random.normal(0, 1.5, 200)

# Partición Train/Val (80/20)
X_train_p3, X_val_p3 = X_espesor[:160], X_espesor[160:]
Y_train_p3, Y_val_p3 = Y_atenuacion_db[:160], Y_atenuacion_db[160:]

print("--> [Fase 0] Éxito: Dataset univariable de atenuación estructural cargado en memoria.")



# @title Solución Oficial - Problema 3 (Hacer doble clic para ver el código)
model_p3 = keras.Sequential([
    keras.layers.Dense(units=32, activation='softplus', input_shape=[1]),
    keras.layers.Dense(units=16, activation='softplus'),
    keras.layers.Dense(units=1)
])

model_p3.compile(optimizer=keras.optimizers.Adam(learning_rate=0.005), loss='mse')
history_p3 = model_p3.fit(X_train_p3, Y_train_p3, epochs=180, validation_data=(X_val_p3, Y_val_p3), verbose=0)

# Graficar el resultado para la auditoría visual del alumno
plt.figure(figsize=(6.5, 3.5))
plt.scatter(X_val_p3, Y_val_p3, color='#10b981', alpha=0.7, label='Muestras de Validación (Sensores)')
X_grid = np.linspace(0.05, 1.2, 100)
plt.plot(X_grid, model_p3.predict(X_grid, verbose=0), color='#0f172a', lw=3, label='Curva de Predicción IA')
plt.title("Auditoría Docente: Perfil de Atenuación Estructural")
plt.xlabel("Espesor del Muro de Concreto (metros)")
plt.ylabel("Atenuación de la Señal (dB)")
plt.grid(True, alpha=0.2)
plt.legend()
plt.show()

print(f"--> [ÉXITO] Desafío completado. Pérdida final (MSE): {history_p3.history['val_loss'][-1]:.4f}")