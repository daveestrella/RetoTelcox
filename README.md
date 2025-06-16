# 📶 TelcoX - Plataforma de Autogestión de Consumo

Este proyecto es un módulo de visualización de consumo de servicios de telecomunicaciones para la empresa ficticia **TelcoX**. Permite a los clientes consultar su saldo, consumo de datos y minutos en tiempo real mediante una interfaz web moderna conectada a un backend RESTful.

---

## 🧩 Tecnologías utilizadas

### Frontend (Angular)
- Angular 17+
- Angular Material
- NGX Charts (gráficos)
- Bootstrap (opcional, para layout inicial)

### Backend (Flask)
- Python 3.10+
- Flask 2+
- CORS
- Simulación de un sistema BSS (Business Support System)

---

## 🚀 Funcionalidades principales

✅ Ingreso de ID de cliente  
✅ Visualización del nombre, saldo, datos y minutos  
✅ Gráfico tipo pastel con desglose de consumo  
✅ Llamada al backend REST (simulado)  
✅ Manejo de errores y mensajes amigables  
✅ Pruebas unitarias del frontend (componentes y servicios)  

---

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/telcox-consumo.git
cd telcox-consumo
```

### 2. Backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
python app.py
```
📡 Servidor Flask: http://localhost:5000

### 3. Frontend (Angular)

```bash
cd frontend
npm install
ng serve
```
🌐 Interfaz Angular: http://localhost:4200


### ✅ Pruebas
```bash
ng test
```


### 🧪 API REST simulada (Flask)
```bash
GET /api/consumo/<cliente_id>
Ejemplo: GET http://localhost:5000/api/consumo/12345

Respuesta esperada:
{
  "nombre": "Juan Pérez",
  "datos_consumidos_gb": 5.5,
  "minutos_consumidos": 120,
  "saldo_actual": 22.75
}
```
### 📁 Estructura del proyecto
```bash
/backend
  ├── app.py
  └── requirements.txt

/frontend
  ├── src/app/app.component.ts
  ├── src/app/services/consumo.service.ts
  ├── angular.json
  └── ...

README.md
```

### ✨ Autor
David Estrella
Reto de Desarrollo Fullstack para Empresa de Telecomunicaciones.
