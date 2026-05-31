import { useEffect, useState } from "react";
<<<<<<< HEAD
import "./index.css";

function App() {
  const [page, setPage] = useState("dashboard");
  const [apiStatus, setApiStatus] = useState("Verificando...");

  useEffect(() => {
    fetch("http://localhost:8000/api/health")
      .then((res) => res.json())
      .then((data) => {
        if (data.success) {
          setApiStatus("Conectado");
        } else {
          setApiStatus("Error");
        }
      })
      .catch(() => {
        setApiStatus("Sin conexión");
      });
  }, []);

  const renderPage = () => {
    if (page === "dashboard") return <Dashboard apiStatus={apiStatus} />;
    if (page === "productos") return <Productos />;
    if (page === "inventario") return <Inventario />;
    if (page === "movimientos") return <Movimientos />;
    if (page === "usuarios") return <Usuarios />;
    if (page === "reportes") return <Reportes />;
    if (page === "configuracion") return <Configuracion />;
  };

  return (
    <div className="layout">
      <header className="topbar">
        <div className="brand">
          <span>Inventario</span>
          <span className="cart-icon">▱</span>
        </div>
      </header>

      <aside className="sidebar">
        <div className="profile">
          <div className="avatar">👤</div>
          <h3>Juan Manuel Razo</h3>
          <p>admin@inventorypro.com</p>
        </div>

        <div className="menu-title">NAVEGACIÓN PRINCIPAL</div>

        <nav>
          <button className={page === "dashboard" ? "active" : ""} onClick={() => setPage("dashboard")}>
            <span>▦</span> Dashboard
          </button>

          <button className={page === "productos" ? "active" : ""} onClick={() => setPage("productos")}>
            <span>◼</span> Gestión de Productos
          </button>

          <button className={page === "inventario" ? "active" : ""} onClick={() => setPage("inventario")}>
            <span>▣</span> Gestión de Existencias
          </button>

          <button className={page === "movimientos" ? "active" : ""} onClick={() => setPage("movimientos")}>
            <span>↕</span> Movimientos
          </button>

          <button className={page === "usuarios" ? "active" : ""} onClick={() => setPage("usuarios")}>
            <span>☻</span> Gestión de Usuarios
          </button>

          <button className={page === "reportes" ? "active" : ""} onClick={() => setPage("reportes")}>
            <span>▤</span> Reportes
          </button>

          <button className={page === "configuracion" ? "active" : ""} onClick={() => setPage("configuracion")}>
            <span>⚙</span> Configuración
          </button>
        </nav>
      </aside>

      <main className="main-content">{renderPage()}</main>
    </div>
  );
}

function Dashboard({ apiStatus }) {
  const cards = [
    { title: "Clientes", value: "16", icon: "▣", color: "teal" },
    { title: "Proveedores", value: "10", icon: "👥", color: "orange" },
    { title: "Productos", value: "185", icon: "◼", color: "purple" },
    { title: "Facturas", value: "1", icon: "▤", color: "gray" },
    { title: "Existencia total", value: "149", icon: "▰", color: "blue" },
    { title: "Existencia vendida", value: "33", icon: "🚚", color: "pink" },
    { title: "Existencia actual", value: "115", icon: "▥", color: "sky" },
    { title: "Importe vendido", value: "$ 413", icon: "▱", color: "deeporange" },
    { title: "Importe pagado", value: "$ 413", icon: "$", color: "green" },
    { title: "Importe restante", value: "$ 0", icon: "$", color: "red" },
    { title: "Beneficio bruto", value: "$ 89", icon: "▰", color: "brown" },
    { title: "Estado API", value: apiStatus, icon: "⌁", color: "cyan" },
  ];

  return (
    <section>
      <h1 className="page-title">Dashboard</h1>

      <div className="dashboard-grid">
        {cards.map((card, index) => (
          <div className={`stat-card ${card.color}`} key={index}>
            <div className="stat-icon">{card.icon}</div>
            <div className="stat-info">
              <p>{card.title}</p>
              <h2>{card.value}</h2>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

function Productos() {
  return (
    <section>
      <h1 className="page-title">Gestión de Productos</h1>

      <div className="panel">
        <div className="panel-header">
          <h2>Productos registrados</h2>
          <button>Agregar producto</button>
        </div>

        <table>
          <thead>
            <tr>
              <th>Código</th>
              <th>Producto</th>
              <th>Categoría</th>
              <th>Proveedor</th>
              <th>Stock mínimo</th>
              <th>Estado</th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td>P-001</td>
              <td>Laptop Lenovo</td>
              <td>Electrónica</td>
              <td>TecnoMax</td>
              <td>5</td>
              <td><span className="badge success">Activo</span></td>
            </tr>

            <tr>
              <td>P-002</td>
              <td>Mouse Logitech</td>
              <td>Accesorios</td>
              <td>CompuCenter</td>
              <td>10</td>
              <td><span className="badge success">Activo</span></td>
            </tr>

            <tr>
              <td>P-003</td>
              <td>Teclado Mecánico</td>
              <td>Accesorios</td>
              <td>Digital Store</td>
              <td>7</td>
              <td><span className="badge success">Activo</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  );
}

function Inventario() {
  return (
    <section>
      <h1 className="page-title">Gestión de Existencias</h1>

      <div className="inventory-grid">
        <div className="inventory-card">
          <h3>Laptop Lenovo</h3>
          <p>Almacén principal</p>
          <strong>Stock actual: 12</strong>
          <span className="badge success">Disponible</span>
        </div>

        <div className="inventory-card">
          <h3>Mouse Logitech</h3>
          <p>Almacén principal</p>
          <strong>Stock actual: 4</strong>
          <span className="badge warning">Stock bajo</span>
        </div>

        <div className="inventory-card">
          <h3>Teclado Mecánico</h3>
          <p>Almacén secundario</p>
          <strong>Stock actual: 18</strong>
          <span className="badge success">Disponible</span>
        </div>
      </div>
    </section>
  );
}

function Movimientos() {
  return (
    <section>
      <h1 className="page-title">Movimientos de Inventario</h1>

      <div className="panel">
        <div className="panel-header">
          <h2>Historial de movimientos</h2>
          <button>Nuevo movimiento</button>
        </div>

        <table>
          <thead>
            <tr>
              <th>Tipo</th>
              <th>Producto</th>
              <th>Cantidad</th>
              <th>Usuario</th>
              <th>Fecha</th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td><span className="badge success">Entrada</span></td>
              <td>Laptop Lenovo</td>
              <td>10</td>
              <td>Juan Manuel</td>
              <td>21/05/2026</td>
            </tr>

            <tr>
              <td><span className="badge danger">Salida</span></td>
              <td>Mouse Logitech</td>
              <td>3</td>
              <td>Juan Manuel</td>
              <td>21/05/2026</td>
            </tr>

            <tr>
              <td><span className="badge success">Entrada</span></td>
              <td>Teclado Mecánico</td>
              <td>15</td>
              <td>Juan Manuel</td>
              <td>21/05/2026</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  );
}

function Usuarios() {
  return (
    <section>
      <h1 className="page-title">Gestión de Usuarios</h1>
      <div className="panel">
        <h2>Usuarios del sistema</h2>
        <p>En este módulo se administrarán los usuarios, roles y permisos del sistema.</p>
      </div>
    </section>
  );
}

function Reportes() {
  return (
    <section>
      <h1 className="page-title">Reportes</h1>
      <div className="panel">
        <h2>Reportes de inventario</h2>
        <p>Este módulo mostrará reportes de stock, movimientos, productos vendidos y existencias actuales.</p>
      </div>
    </section>
  );
}

function Configuracion() {
  return (
    <section>
      <h1 className="page-title">Configuración</h1>
      <div className="panel">
        <h2>Configuración general</h2>
        <p>Aquí se configurarán parámetros generales del sistema InventoryPro.</p>
      </div>
    </section>
  );
}

export default App;
=======

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function App() {
  const [txt, setTxt] = useState("cargando…");

  useEffect(() => {
    fetch(`${API}/api/avance`)
      .then((r) => r.json())
      .then((j) => setTxt(JSON.stringify(j, null, 2)))
      .catch((e) => setTxt("error: " + String(e)));
  }, []);

  return (
    <div style={{ fontFamily: "monospace", padding: 16 }}>
      <p>GET {API}/api/avance</p>
      <pre style={{ whiteSpace: "pre-wrap" }}>{txt}</pre>
    </div>
  );
}
>>>>>>> origin/gioauth-firebase
