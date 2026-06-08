## Para el ejemplo 1.1

> cambiar de 60 epocas a 200 cambia sensiblemente la aproximacion del sesgo del modelo


## Para el ejemplo 1.2

Configuraciones:

1. set 1 (Lineal)
```py
model_rf = keras.Sequential([
    keras.Input(shape=(1,)), # Recommended way to define input shape
    keras.layers.Dense(units=8),
    keras.layers.Dense(units=8),
    keras.layers.Dense(units=1)
])

epochs=200
```

2. set 2 (Se espera que esta rompa la linealidad!)
```py
model_rf = keras.Sequential([
    keras.Input(shape=(1,)), # Recommended way to define input shape
    keras.layers.Dense(units=8, activation='relu'),
    keras.layers.Dense(units=8, activation='relu'),
    keras.layers.Dense(units=1)
])

epochs=200
```

3. set 3
```py
model_rf = keras.Sequential([
    keras.Input(shape=(1,)), # Recommended way to define input shape
    keras.layers.Dense(units=32, activation='relu'),
    keras.layers.Dense(units=16, activation='relu'),
    keras.layers.Dense(units=1)
])

epochs=200
```