# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

## [Unreleased]

- Añadido workflow de CI para C++ (`.github/workflows/cpp.yml`).
- Añadido workflow de pruebas Python & cobertura (`.github/workflows/python-tests.yml`).
- Añadido workflow de release (`.github/workflows/release.yml`).
- Añadido workflow de GitHub Pages (`.github/workflows/pages.yml`).
- Añadido `tests/test_quantum_bridge.py` (3 tests).
- Añadido `requirements.txt` con pytest y coverage.
- Añadido secciones en README: badges, release y semver.

## [1.0.0] - 2026-03-30

### Added

- Implementación completa de VOX-OMEGA QuantumFS en C++.
- Integración de hardware cuántico IBM (QuantumBridge y C++ shim).
- Visualización y persistencia contenidos.
- Documentación (README, LICENSE).
- Proceso de build + test + release automatizado en GitHub Actions.

### Fixed

- Varios warnings de Markdown MD022/MD031/MD032/MD040 resueltos.

### Notes

- El proyecto es educativo y de concepto; no es un producto de producción aún.
