# metodoscuanticos

## Teoría de probabilidad
```
Experimento: Un proceso de observación
Evento: es un conjunto de resultados de un experimento
Espacio muestral (E): El conjunto de todos los posibles eventos.
```
### Propiedades
```
0 <= P(Ai) <= 1
∑ P(Ai) = i
```
## Permutaciones y Combinaciones 
```
Permutaciones:
Número de formas para seleccionar r de n elementos cuando el orden es importante
Combinaciones:
Número de formas para seleccionar r de n elementos cuando el orden no es importante
```
## Funciones de densidad de probabilidad
```
Variable aleatoria de Bernoulli: Cualquier variable aleatoria cuyos únicos valores
posibles son cero y uno
Las probabilidades asignadas a varios resultados en E determinan a su
vez las probabilidades asociadas con los valores de cualquier variable
aleatoria x particular.
La distribución de probabilidad de X indican cómo está distribuida
```

## Variable Aleatoria
```
Variable aleatoria discreta (x). Se le denomina a las variables que puede
tomar diferentes valores aleatorios (al azar) que solo puede tomar valores
enteros y un número finito de ellos.

Variable aleatoria continua (x). Se le denomina a las variables que pueden
tomar diferentes valores aleatorios que puedan tomar tanto valores enteros
como fraccionarios y un número infinito de ellos. Incluso puede contener en
una unión disjunta ciertos intervalos.

Por ejemplo [0,10] U [20,30]
```

## Distribucion discreta
```
X = Variable que solo toma valores enteros
1. p(xi)≥0
Las probabilidades asociadas a cada uno de los valores que toma x deben ser mayores o
iguales a cero.
2. ∑p(xi) = 1
La sumatoria de las probabilidades asociadas a cada uno de los valores que toma x debe ser
igual a 1.

Uniforme discreta
• Binomial
• Hipergeométrica
• Geométrica
• Poisson
```

## Distribucion acumulativa
```
F(x) es la probabilidad de que el valor observado de
X será cuando mucho x.
```

## Distribucion variables continuas
```
La probabilidad de que X asuma un valor en el intervalo [a,b] es el área sobre este intervalo y bajo la gráfica de la función de
densidad, como se ilustra en la figura, que normalmente se llama
curva de densidad.
Nula la probabilidad asociada a un punto
𝑃(𝑎 < 𝑋 < 𝑏)=𝑃(𝑎 ≤ 𝑋 < 𝑏)=𝑃(𝑎 < 𝑋 ≤ 𝑏)=𝑃(𝑎 ≤ 𝑋 ≤ 𝑏)=𝑃(𝑋 ≤ 𝑏)-𝑃(𝑋 ≤ 𝑎)=𝐹(𝑏) − 𝐹(𝑎)

𝑃(𝑎 ≤ 𝑋 ≤ 𝑏)= 𝐹(𝑏)− 𝐹(𝑎)= 𝑎∫𝑏 𝑓(𝑥)𝑑𝑥

𝑓(𝑥) ≥ 0 𝑐𝑜𝑛 𝑡𝑜𝑑𝑎𝑠 𝑙𝑎𝑠 𝑥
 −∞∫∞  𝑓( 𝑥) 𝑑𝑥 = á𝑟𝑒𝑎 𝑏𝑎𝑗𝑜 𝑡𝑜𝑑𝑎 𝑙𝑎 𝑔𝑟á𝑓𝑖𝑐𝑎 𝑑𝑒 𝑓 𝑥 = 1
```
## Distribución uniforme discreta 
```
Describe el comportamiento de una variable discreta que puede tomar n valores distintos con la misma
probabilidad cada uno de ellos.
n= número de pruebas en el experimento
p = probabilidad de éxito
k es el número de éxitos.
p es la probabilidad de éxito.
q es la probabilidad de fracaso.

```

## Distribucion Binomial
```
Esta distribución se aplica de forma natural al realizar repeticiones independientes de un
experimento que tenga respuestas binarias, generalmente clasificadas como “éxito” y “fracaso”
``` 

## Distribucion Poisson
``` 
𝑝(𝑥; 𝜆) es la probabilidad de que ocurra x éxitos por unidad de tiempo o espacio con
una media 𝜆
Se dice que una variable aleatoria discreta X tiene una distribución de Poisson
con parámetro 𝜆 = 𝑛𝑝 (λ > 0) 
Cada evento es al azar ya sea en unidad de tiempo o unidad de área.
Cada intervalo de tiempo o espacio es independiente de otro intervalo dado.
``` 

## Distribucion Normal 
```
Es simétrica respecto a la media µ.
Tiene un máximo en la media µ
Crece hasta la media µ y decrece a partir de ella.
En los puntos µ − σ y µ + σ presenta puntos de inflexión.
```

La probabilidad equivale al área encerrada bajo la curva
```
p(μ - σ < X ≤ μ + σ) = 0.6826 = 68.26 %
p(μ - 2σ < X ≤ μ + 2σ) = 0.954 = 95.4 %
p(μ - 3σ < X ≤ μ + 3σ) = 0.997 = 99.7 %
```
## Distribucion Normal Estandar
```
tiene por media, μ = 0, y desviación típica, σ =1. 
```

## Distribucion Normal NO Estandar
```
tiene una distribución normal con media μ y desviación estándar σ
```
![Alt text](./resources/Screenshot%20from%202018-02-11%2020-43-05.png)