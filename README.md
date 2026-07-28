# Taller 3 - Programación discreta
## Matemáticas Discretas I — Universidad Nacional de Colombia

Criptografía, grafos, álgebra de Boole, Shannon y un primer vistazo cuántico.

## Integrantes

- Sebastián González Torres
- Jorge Eduardo Piratoba Tocarruncho

## Lenguaje usado

Python 3.11. No se usaron librerías externas: todo el código corre solo con
la librería estándar de Python (`math`, `random`).

## Cómo ejecutar

Cada ejercicio es un script independiente y se ejecuta por separado.

1. Clonar el repositorio y ubicarse en la carpeta raíz.
2. (Opcional) Crear y activar un entorno virtual:
```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
```
3. Instalar pytest para correr las pruebas:
```powershell
   pip install pytest
```
4. Ejecutar un ejercicio puntual, por ejemplo:
```powershell
   python src/cripto/Ejercicio_1.py
```
5. Ejecutar todas las pruebas del taller:
```powershell
   pytest
```
   o una en particular:
```powershell
   pytest tests/Test_Ejercicio_1.py -v
```

## Estructura del repositorio
├── src/
│ ├── cripto/ (ejercicios 1, 2, 3, 9)
│ ├── grafos/ (ejercicios 4, 5, 6)
│ ├── boole/ (ejercicios 7, 8)
│ └── cuantica/ (ejercicio 10)
├── tests/ (pruebas con pytest de los 10 ejercicios)
└── README.md

## Ejercicios desarrollados

| #  | Ejercicio                            | Archivo                        |
|----|--------------------------------------|--------------------------------|
| 1  | Cifrado César                        | `src/cripto/Ejercicio_1.py`    |
| 2  | RSA de juguete                       | `src/cripto/Ejercicio_2.py`    |
| 3  | MPC básico (suma secreta)            | `src/cripto/Ejercicio_3.py`    |
| 4  | Ruta más corta (Dijkstra)            | `src/grafos/Ejercicio_4.py`    |
| 5  | Cierre de una estación               | `src/grafos/Ejercicio_5.py`    |
| 6  | Coloreo de grafos                    | `src/grafos/Ejercicio_6.py`    |
| 7  | Tablas de verdad y circuitos lógicos | `src/boole/Ejercicio_7.py`     |
| 8  | Simplificación booleana              | `src/boole/Ejercicio_8.py`     |
| 9  | Entropía de Shannon                  | `src/cuantica/Ejercicio_9.py`  |
| 10 | Simulador cuántico básico (1 qubit)  | `src/cuantica/Ejercicio_10.py` |

La explicación matemática detallada de cada punto (qué problema resuelve,
qué idea matemática usa, cómo se ejecuta, qué pruebas se hicieron y qué
limitaciones tiene) está en el PDF dentro de `docs/`.