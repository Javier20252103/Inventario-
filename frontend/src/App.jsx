import { useEffect, useState } from "react";
import "./index.css";

function App() {
  const [page, setPage] = useState("dashboard");
  const [apiStatus, setApiStatus] = useState("Verificando conexión...");

  useEffect(() => {
    fetch("http://localhost:8000/api/health")
      .then((res) => res.json())
      .then((data) => {
        if (data.success) {
          setApiStatus("Backend conectado correctamente");
        } else {
          setApiStatus("Backend respondió con error");
        }
      })
      .catch(() => {
        setApiStatus("Backend no conectado");
      });
  }, []);

  const renderPage = () => {
    if (page === "dashboard") return <Dashboard apiStatus={apiStatus} />;
    if (page === "products") return <Products />;
    if (page === "inventory") return <Inventory />;
    if (page === "movements") return <Movements />;
    if (page === "login") return <Login />;
  };

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>InventoryPro</h2>
        <p>Sistema de inventario</p>

        <button onClick={() => setPage("dashboard")}>Dashboard</button>
        <button onClick={() => setPage("products")}>Productos</button>
        <button onClick={() => setPage("inventory")}>Inventario</button>
        <button onClick={() => setPage("movements")}>Movimientos</button>
        <button onClick={() => setPage("login")}>Login</button>
      </aside>

      <main className="content">
        {renderPage()}
      </main>
    </div>
  );
}

function Dashboard({ apiStatus }) {
  return (
    <section>
      <h1>Dashboard</h1>
      <p className="subtitle">Resumen general del sistema InventoryPro</p>

      <div className="cards">
        <div className="card">
          <h3>Productos</h3>
          <p>24 registrados</p>
        </div>

        <div className="card">
          <h3>Categorías</h3>
          <p>6 activas</p>
        </div>

        <div className="card">
          <h3>Proveedores</h3>
          <p>8 registrados</p>
        </div>

        <div className="card">
          <h3>Estado API</h3>
          <p>{apiStatus}</p>
        </div>
      </div>
    </section>
  );
}

function Products() {
  return (
    <section>
      <h1>Productos</h1>
      <p className="subtitle">Listado base de productos del inventario</p>

      <table>
        <thead>
          <tr>
            <th>Producto</th>
            <th>Categoría</th>
            <th>Stock mínimo</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Laptop Lenovo</td>
            <td>Electrónica</td>
            <td>5</td>
            <td>Activo</td>
          </tr>
          <tr>
            <td>Mouse Logitech</td>
            <td>Accesorios</td>
            <td>10</td>
            <td>Activo</td>
          </tr>
          <tr>
            <td>Teclado Mecánico</td>
            <td>Accesorios</td>
            <td>7</td>
            <td>Activo</td>
          </tr>
        </tbody>
      </table>
    </section>
  );
}

function Inventory() {
  return (
    <section>
      <h1>Inventario</h1>
      <p className="subtitle">Consulta general de existencias</p>

      <div className="cards">
        <div className="card">
          <h3>Laptop Lenovo</h3>
          <p>Stock actual: 12</p>
          <span className="ok">Disponible</span>
        </div>

        <div className="card">
          <h3>Mouse Logitech</h3>
          <p>Stock actual: 4</p>
          <span className="warning">Stock bajo</span>
        </div>

        <div className="card">
          <h3>Teclado Mecánico</h3>
          <p>Stock actual: 18</p>
          <span className="ok">Disponible</span>
        </div>
      </div>
    </section>
  );
}

function Movements() {
  return (
    <section>
      <h1>Movimientos</h1>
      <p className="subtitle">Historial de entradas y salidas de inventario</p>

      <table>
        <thead>
          <tr>
            <th>Tipo</th>
            <th>Producto</th>
            <th>Cantidad</th>
            <th>Fecha</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Entrada</td>
            <td>Laptop Lenovo</td>
            <td>10</td>
            <td>21/05/2026</td>
          </tr>
          <tr>
            <td>Salida</td>
            <td>Mouse Logitech</td>
            <td>3</td>
            <td>21/05/2026</td>
          </tr>
          <tr>
            <td>Entrada</td>
            <td>Teclado Mecánico</td>
            <td>15</td>
            <td>21/05/2026</td>
          </tr>
        </tbody>
      </table>
    </section>
  );
}

function Login() {
  return (
    <section className="login-box">
      <h1>Inicio de sesión</h1>
      <p className="subtitle">Acceso al sistema InventoryPro</p>

      <form>
        <label>Correo electrónico</label>
        <input type="email" placeholder="admin@inventorypro.com" />

        <label>Contraseña</label>
        <input type="password" placeholder="********" />

        <button type="button">Iniciar sesión</button>
      </form>
    </section>
  );
}

export default App;