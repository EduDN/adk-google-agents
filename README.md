# ADK (Agent Development Kit) - Google

Guía para crear y desplegar agentes de IA usando el Agent Development Kit de Google.

## Requisitos

- Python 3.10 o superior
- [uv](https://docs.astral.sh/uv/) — gestor de paquetes y entornos para Python
- [ADK de Google](https://google.github.io/adk-docs/)
- [API Key de Gemini](https://aistudio.google.com/api-keys)

## Instalación y configuración

### 1. Crear la carpeta del proyecto
```bash
mkdir nombre_de_tu_carpeta
cd nombre_de_tu_carpeta
```

### 2. Crear el entorno virtual de Python
```bash
uv venv
```

### 3. Instalar el ADK de Google
```bash
uv add google-adk
```

### 4. Configurar variables de entorno

> ⚠️ No olvides agregar `.env` a tu `.gitignore` para no exponer tu clave.


## Uso

### Crear un agente a través de un template
```bash
uvx --from google-adk adk create --type=config my_agent
```

### Ejecutar en interfaz web
```bash
adk web my_agent
```

### Ejecutar en terminal
```bash
adk run my_agent
```

### Resultado

![alt text](image.png)

## Recursos

- [Documentación oficial de ADK](https://google.github.io/adk-docs/)
- [Google AI Studio](https://aistudio.google.com/)