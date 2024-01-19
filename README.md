# Entorno virtual de pádel para el aprendizaje por refuerzo

## Descripción general

El entorno virtual de pádel para el aprendizaje por refuerzo es un proyecto desarrollado en Unity que permite entrenar agentes en un entorno de aprendizaje basado en el pádel mediante aprendizaje por refuerzo, utilizando el toolkit de [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents).

Los directorios `Assets`, `Packages`, `Project Settings` y `User Settings` son los necesarios para abrir el proyecto en Unity.

El directorio `config` contiene los archivos de configuración del entrenamiento de agentes en el entorno virtual de pádel. Los modelos obtenidos del entrenamiento se encuentran en el directorio `results`.

El directorio `docs` contiene la memoria del trabajo de fin de grado (código fuente de LaTeX).

Vídeos de demostración:
- [Experimento 1. Entrenamiento mediante PPO](https://youtu.be/c01Wxk4V-j4)
- [Experimento 2. Efecto de Curiosity en el entorno virtual de pádel](https://youtu.be/9whYapjz-cY)
- [Experimento 3. Influencia en la recompensa de golpeo](https://youtu.be/A1_gc6cn3m0)
- [Experimento 4. Importancia del sistema de puntuación Elo](https://youtu.be/Mt8tv0s1uIw)
- [Experimento 5. Influencia de las posiciones clave](https://youtu.be/sc-13rTFV3E)
- [Demostración del modo de depuración](https://youtu.be/HECw2WBsCo4)

## Requerimientos

Este proyecto se ha probado únicamente en Windows 11. Para la ejecución del proyecto se requiere la versión 2021.3.22f1 de Unity y la versión 20 de ML-Agents.
Para el entrenamiento de agentes se requiere la versión 3.7.9 de Python (otras versiones compatibles: 3.9).


> [!NOTE]
> La guía de instalación oficial se puede consultar [aquí](https://github.com/Unity-Technologies/ml-agents/blob/develop/docs/Installation.md), pero se trata de una versión más reciente de ML-Agents.
> 
> A continuación se detallan los pasos a seguir específicos para este proyecto.


## Instalación del proyecto en Unity

Los pasos a seguir para la ejecución del entorno virtual de pádel desde Unity son los siguientes:
1. Instalar la [versión 2021.3.22f1](https://unity.com/releases/editor/whats-new/2021.3.22) de Unity, preferiblemente a través de Unity Hub.
2. Descargar la [versión 20](https://github.com/Unity-Technologies/ml-agents/releases/tag/release_20) de ML-Agents desde el repositorio oficial. La carpeta descargada `ml-agents-release-20` contiene el paquete de Unity necesario para la ejecución del entorno.
3. Clonar este repositorio y abrirlo desde Unity, en Modo Seguro.
4. Para añadir el paquete de Unity al proyecto:
   1. Navegar hasta el menú `Window` -> `Package Manager`.
   2. Hacer click al botón `+` (situado en esquina superior izquierda del menú)
   3. Seleccionar `Add package from disk...`
   4. Navegar hasta la carpeta de `com.unity.ml-agents` (dentro de la carpeta `ml-agents-release-20`)
   5. Seleccionar el archivo `package.json`.
5. En este punto, se deberían haber detectado todos los componentes procedentes de ML-Agents (`Agent`, `Behavior Parameters`, `Decision Requester`...) y se debería poder ejecutar la escena `Scenes\Padel2vs2`.

## Instalación del paquete de Python `mlagents`

Los pasos a seguir para entrenar agentes son los siguientes:
1. Instalar la versión [3.7.9](https://unity.com/releases/editor/whats-new/2021.3.22) de Python para Windows.
2. Crear y activar un entorno virtual de Python mediante [`pyenv`](https://github.com/pyenv/pyenv#getting-pyenv) (equivalente para [Anaconda](https://www.anaconda.com/download)):
```
python -m venv [nombre del entorno]
.\[nombre del entorno]\Scripts\activate
```
4. Desde el entorno virtual de Python, lo primero es instalar las dependencias de `mlagents`:
```
python -m pip install --upgrade pip
pip install torch torchvision torchaudio
pip install protobuf==3.20.3
pip install six
```
5. Instalar `mlagents` y comprobar que se haya instalado correctamente:
```
pip install mlagents
mlagents-learn --help
```
6. En caso de faltar alguna dependencia, descargar la dependencia correspondiente (indicada en el error al ejecutar `mlagents-learn --help`).
7. (Alternativa) También es posible instalar `mlagents` desde el repositorio clonado `ml-agents-release_20` (**requiere una versión de Python >= 3.8.13 y <= 3.10.8**):
```
cd /path/to/ml-agents-release_20
python -m pip install ./ml-agents-envs
python -m pip install ./ml-agents
```
8. Para entrenar agentes, el comando básico es:
```
mlagents-learn <trainer-config-file> --run-id=<run-identifier> --time-scale=1
```
La configuración utilizada durante el desarrollo del trabajo de fin de grado se encuentra en la carpeta `config`, donde hay información más detallada sobre cómo se han llevado a cabo los experimentos.

Una guía más detallada sobre cómo entrenar agentes se puede consultar [aquí](https://github.com/Unity-Technologies/ml-agents/blob/develop/docs/Training-ML-Agents.md).



