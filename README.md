# VOX-OMEGA QuantumFS

[![C++ CI](https://github.com/orionking12/vox-omega-quantumfs/actions/workflows/cpp.yml/badge.svg)](https://github.com/orionking12/vox-omega-quantumfs/actions/workflows/cpp.yml)
[![Python Tests](https://github.com/orionking12/vox-omega-quantumfs/actions/workflows/python-tests.yml/badge.svg)](https://github.com/orionking12/vox-omega-quantumfs/actions/workflows/python-tests.yml)
[![Pages build](https://github.com/orionking12/vox-omega-quantumfs/actions/workflows/pages.yml/badge.svg)](https://github.com/orionking12/vox-omega-quantumfs/actions/workflows/pages.yml)
[![Release](https://img.shields.io/github/v/release/orionking12/vox-omega-quantumfs)](https://github.com/orionking12/vox-omega-quantumfs/releases)
[![Coverage](https://img.shields.io/codecov/c/github/orionking12/vox-omega-quantumfs)](https://codecov.io/gh/orionking12/vox-omega-quantumfs)
[![License](https://img.shields.io/github/license/orionking12/vox-omega-quantumfs?color=blue)](LICENSE.md)

## Descripción

VOX-OMEGA QuantumFS es una simulación experimental de un sistema de archivos cuántico implementado en C++. Este proyecto demuestra conceptos de la mecánica cuántica aplicados a la gestión de archivos, incluyendo superposición de estados, colapso cuántico y múltiples timelines simultáneos.

## Características Principales

### 🧬 Superposición Cuántica

- Cada archivo existe en **8 estados simultáneos** (1 estado clásico + 7 superposiciones)
- Las superposiciones se generan mediante operaciones XOR aleatorias sobre los datos originales
- Simula el principio de incertidumbre cuántica donde múltiples realidades coexisten

### 🎭 Colapso Cuántico

- Al leer un archivo, el sistema "colapsa" a uno de los 8 timelines posibles
- La selección del timeline se basa en una máscara de coherencia (coherence_mask)
- Demuestra cómo la observación afecta el estado cuántico

### 💾 Persistencia en Disco

- Los archivos se almacenan en formato binario `.qfs`
- Se guardan tanto los datos clásicos como todas las superposiciones
- Los archivos se organizan en el directorio `./vox_omega_fs_nexus/`

### 🔬 Simulación Científica

- Implementa conceptos de computación cuántica aplicada a sistemas de archivos
- Usa máscaras de bits para representar estados de coherencia
- Incluye timestamps para rastrear la creación de archivos

## Arquitectura

### Archivos del Proyecto

- `vox_omega_quantum_fs.cpp` - Implementación principal del filesystem cuántico
- `quantum_hardware_integration.cpp` - Integración C++ con hardware cuántico
- `quantum_bridge.py` - Puente Python completo con Qiskit e IBM Quantum
- `requirements.txt` - Dependencias Python para integración cuántica
- `README.md` - Documentación completa del proyecto
- `LICENSE.md` - Licencia y términos de uso

### Estructura de Datos

```cpp
struct QuantumFile {
    std::string name;                           // Nombre del archivo
    std::vector<uint8_t> data;                  // Estado clásico
    std::vector<std::vector<uint8_t>> superpositions; // 7 estados cuánticos
    uint64_t coherence_mask{0xFF};              // Máscara de colapso (8 bits)
    std::chrono::system_clock::time_point created; // Timestamp de creación
    std::chrono::system_clock::time_point last_accessed; // Último acceso
    double coherence_level{1.0};                // Nivel de coherencia (0.0-1.0)
    std::vector<std::string> entangled_files;   // Archivos entrelazados
    bool is_quantum_network_node{false};        // Nodo de red cuántica
};
```

### Funcionalidades

- **create_file()**: Crea un archivo con 8 timelines simultáneos
- **read_file()**: Colapsa un timeline específico basado en coherencia
- **list_files()**: Muestra archivos con indicador de superposiciones activas
- **persist_to_disk()**: Guarda estado completo en formato binario
- **apply_temporal_decoherence()**: Simula pérdida de coherencia con el tiempo
- **entangle_files()**: Crea conexiones cuánticas entre archivos
- **quantum_teleport()**: Teletransporta estados cuánticos entre nodos
- **visualize_timelines()**: Muestra visualización completa de todos los timelines
- **enable_quantum_network_node()**: Activa un archivo como nodo de red cuántica

## Requisitos del Sistema

- **Compilador**: C++17 o superior (recomendado C++23)
- **Sistema Operativo**: Windows, Linux, macOS
- **Dependencias**: Biblioteca estándar de C++
- **Espacio**: Mínimo para archivos binarios generados

## Compilación

### Con g++ (Linux/macOS/Windows con MinGW)

```bash
g++ -std=c++17 -O3 -march=native vox_omega_quantum_fs.cpp -o vox_omega_fs.exe
```

### Con Visual Studio (Windows)

```cmd
cl /std=c++17 /EHsc vox_omega_quantum_fs.cpp
```

### Con CMake (Multiplataforma)

```cmake
cmake_minimum_required(VERSION 3.16)
project(VOX_OMEGA_QuantumFS)

set(CMAKE_CXX_STANDARD 17)
add_executable(vox_omega_fs vox_omega_quantum_fs.cpp)
```

## Uso

### Ejecución Básica

```bash
./vox_omega_fs.exe
```

### Comportamiento Esperado

1. **Inicialización**: Se crea el directorio `./vox_omega_fs_nexus/`
2. **Creación de archivos de ejemplo**:
   - `secret_project.txt`: Contiene texto de ejemplo
   - `intelligence_test.bin`: Datos binarios de prueba
   - `quantum_notes.txt`: Notas adicionales
3. **Activación de red cuántica**: Algunos archivos se convierten en nodos
4. **Entrelazamiento**: Archivos conectados cuánticamente
5. **Demostración completa**:
   - Visualización inicial de timelines
   - Lectura con decoherencia temporal
   - Teletransportación cuántica
   - Simulación de decoherencia
   - Visualización final
6. **Interacción**: Espera entrada del usuario antes de finalizar

### Salida de Ejemplo

```text
VOX-OMEGA QuantumFS 2026.03.27 inicializado.
Creado por: Jorge Humberto Dávalos González (orionchinnar@gmail.com)
Coherencia: 100% | Superposiciones activas: 8
Archivo 'secret_project.txt' creado en 8 timelines simultáneos.
Archivo 'intelligence_test.bin' creado en 8 timelines simultáneos.
Archivo 'quantum_notes.txt' creado en 8 timelines simultáneos.
Archivos en VOX-OMEGA QuantumFS:
  • secret_project.txt (8 superposiciones activas)
  • intelligence_test.bin (8 superposiciones activas)
  • quantum_notes.txt (8 superposiciones activas)

=== DEMOSTRACIÓN DE FUNCIONES AVANZADAS ===

🌌 VISUALIZACIÓN DE TIMELINES CUÁNTICOS
═══════════════════════════════════════
📁 secret_project.txt [Coherencia: 100%]
   📄 Timeline 0 (Clásico): Este es el filesystem...
   🌊 Timeline 1 (Cuántico) ✨: .....
   [... más timelines ...]

Colapsando timeline 5 para 'secret_project.txt'
Este es el filesystem cuántico auto-contenido creado por Jorge Humberto Dávalos González en Guadalajara 2026.

[... demostración completa ...]
```

## Conceptos Cuánticos Implementados

### 1. Superposición

Cada archivo existe en múltiples estados simultáneamente hasta ser observado.

### 2. Colapso

La lectura "colapsa" la función de onda, seleccionando un estado específico.

### 3. Coherencia

La máscara de coherencia determina qué timelines están disponibles.

### 4. Persistencia

Los estados cuánticos se mantienen entre ejecuciones del programa.

### 5. Decoherencia Temporal ⭐ NUEVO

Los estados cuánticos pierden coherencia con el tiempo, simulando el comportamiento real de sistemas cuánticos.

### 6. Entrelazamiento ⭐ NUEVO

Archivos pueden estar entrelazados, donde el estado de uno afecta al otro.

### 7. Red Cuántica ⭐ NUEVO

- **Nodos de red**: Archivos pueden actuar como nodos en una red cuántica
- **Teletransportación**: Transferencia instantánea de estados cuánticos entre nodos
- **Operaciones de red**: Simulación de protocolos cuánticos de comunicación

### 8. Visualización ⭐ NUEVO

Interfaz de consola avanzada para visualizar todos los timelines y estados cuánticos.

## Limitaciones

- **Simulación**: Es una simulación conceptual, no computación cuántica real
- **Rendimiento**: Las superposiciones duplican el uso de memoria
- **Escalabilidad**: Diseñado para demostración, no para uso en producción
- **Aleatoriedad**: Usa `std::rand()` para generar superposiciones

## Futuras Mejoras

- [x] Implementar decoherencia temporal
- [x] Agregar entrelazamiento entre archivos
- [x] Soporte para operaciones de red cuántica
- [x] Interfaz gráfica para visualización de timelines
- [x] Integración con hardware cuántico real (IBM Quantum, etc.)

## Integración con Hardware Cuántico Real

### Arquitectura de Integración

El proyecto incluye implementación dual para integración con hardware cuántico real:

#### C++ Integration Layer

```cpp
#include "quantum_hardware_integration.cpp"

// Inicializar integrador
IBM_Quantum_Integrator quantum_integrator("YOUR_API_TOKEN", "ibmq_manila");

// Generar números aleatorios cuánticos verdaderos
auto random_bytes = quantum_integrator.generate_quantum_random_bytes(16);

// Medir coherencia usando interferometría cuántica
double coherence = quantum_integrator.measure_coherence(file_data);

// Ejecutar teleportación cuántica
bool teleported_bit = quantum_integrator.quantum_teleport_bit(original_bit);
```

#### Python Bridge (Qiskit)

```python
from quantum_bridge import QuantumHardwareBridge

# Inicializar puente cuántico
quantum_bridge = QuantumHardwareBridge("YOUR_API_TOKEN", "ibmq_manila")

# Generar bits aleatorios cuánticos
random_bits = quantum_bridge.generate_quantum_random_bits(16)

# Teleportación cuántica
teleported_bit = quantum_bridge.quantum_teleportation(1)

# Medir coherencia
coherence = quantum_bridge.measure_coherence(b"test_data")
```

### Ejecución de la Integración

#### Demo en Python (Recomendado)

```bash
# Instalar dependencias
pip install qiskit qiskit-ibm-provider

# Ejecutar demo
python quantum_bridge.py
```

#### Compilación C++ (Avanzado)

```bash
# Nota: Requiere integración con Python/C API
g++ -std=c++17 quantum_hardware_integration.cpp -o quantum_integration
./quantum_integration
```

### Estado de Implementación

✅ **Completado**: Integración modular con IBM Quantum

- **C++ Layer**: `quantum_hardware_integration.cpp` - Interfaz de alto nivel
- **Python Bridge**: `quantum_bridge.py` - Implementación completa con Qiskit
- **Requirements**: `requirements.txt` - Dependencias Python
- **Modo Simulación**: Funciona sin hardware real para desarrollo
- **Modo Real**: Soporte completo para IBM Quantum backends

### Funcionalidades Implementadas

#### 🔀 Generación de Números Aleatorios Cuánticos

- Usa qubits reales para generar entropía verdadera
- Ideal para criptografía y simulaciones científicas
- Fallback a simulación local cuando no hay hardware

#### ⚡ Teletransportación Cuántica

- Implementa el protocolo de teleportación de Bennett (1993)
- Transfiere estados cuánticos entre nodos remotos
- Simulación completa del proceso cuántico

#### 📊 Medición de Coherencia

- Usa interferometría cuántica para medir coherencia
- Determina la "salud cuántica" de los datos
- Cálculos basados en distribución de probabilidad

### Modo Simulación vs Hardware Real

```cpp
// Modo simulación (sin API token)
IBM_Quantum_Integrator simulator; // Usa std::random_device

// Modo hardware real
IBM_Quantum_Integrator real_hardware("your_token", "ibmq_manila");
```

### Limitaciones Actuales

- **Híbrido C++/Python**: Requiere puente entre lenguajes
- **Latencia**: Hardware real tiene tiempos de cola
- **Costos**: Uso de hardware real puede tener límites diarios
- **Disponibilidad**: No todos los backends están siempre disponibles

### Futuras Extensiones

- Integración completa con Qiskit Runtime
- Soporte para otros proveedores (Rigetti, IonQ, etc.)
- Algoritmos cuánticos avanzados (Shor, Grover)
- Interfaz web para gestión de jobs cuánticos

Este proyecto es **código abierto** y se proporciona "tal cual" para fines educativos, de investigación y desarrollo personal.

**IMPORTANTE**: Este software fue creado por **Jorge Humberto Dávalos González** ([orionchinnar@gmail.com](mailto:orionchinnar@gmail.com)). Cualquier uso, modificación o distribución debe mantener visible y prominente el crédito al autor original.

### Condiciones de Uso

- ✅ Uso personal y educativo
- ✅ Modificaciones y mejoras personales
- ✅ Distribución no comercial con crédito al autor
- ❌ Uso comercial sin permiso expreso del autor
- ❌ Eliminación del crédito al creador

**Atribución requerida**: "Creado por Jorge Humberto Dávalos González - Todos los derechos reservados © 2026"

Ver [LICENSE.md](LICENSE.md) para detalles completos sobre la licencia.

No se garantiza su uso en entornos de producción sin modificaciones adicionales.

## Autor

**Jorge Humberto Dávalos González**  
📧 [orionchinnar@gmail.com](mailto:orionchinnar@gmail.com)  
📍 Guadalajara, México  
📅 2026

## Publicar una release

1. Asegúrate de estar en `main` y con los últimos cambios:

```bash
# Ejecutar el comando desde el directorio del proyecto
git checkout main
git pull origin main
```

1. Etiqueta la versión:

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
```

1. Empuja la etiqueta a GitHub:

```bash
git push origin v1.0.0
```

- Esto activará el workflow `.github/workflows/release.yml` y creará un release automático.
- Canary release: cambia `v1.0.0` por `v1.0.1`, `v1.1.0` según semver.

## Semver 2.0.0 (Versionado Semántico Avanzado)

Sigue esta guía cuando comiences a evolucionar el proyecto:

1. Cambios de parche (sin API breaking): `MAJOR.MINOR.PATCH` → `1.0.1`, `1.0.2`, etc.
2. Cambios de funcionalidad retrocompatible: `MAJOR.MINOR.PATCH` → `1.1.0`, `1.2.0`.
3. Cambios incompatibles (breaking): `MAJOR.MINOR.PATCH` → `2.0.0`, `3.0.0`.

Reglas clave:

- Usa `git commit` con mensajes claros: `fix:`, `feat:`, `refactor:`, `perf:`.
- Agrega un listado en `CHANGELOG.md` por versión.
- Genera tag al publicar y empuja:

  ```bash
  git tag -a v${VERSION} -m "Release ${VERSION}"
  git push origin v${VERSION}
  ```

- Si hay hotfix urgente, adopta branching `main` + `hotfix/x.y.z`.

## Generar y publicar GitHub Pages

1. Confirma que el workflow `.github/workflows/pages.yml` ejecuta build.

1. Sube cualquier cambio al branch `main`:

```bash
git add .
git commit -m "Update docs"
git push origin main
```

1. Verifica Pages en:

`https://orionking12.github.io/vox-omega-quantumfs/`

---

> "En un universo de infinitas posibilidades, cada archivo es una partícula en superposición hasta que decides observarlo."
> Creado por Jorge Humberto Dávalos González - Todos los derechos reservados © 2026
