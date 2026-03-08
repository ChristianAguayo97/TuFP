import Registro from "../components/Registro.jsx";
import Estadisticas from "../components/IngresarEstadisticas.jsx";
import RutaProtegida from "../components/RutaProtegida.jsx";
import UsuarioLogueado from "../components/UsuarioLogueado.jsx";
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from '../components/Sidebar';
import { useState, useEffect } from 'react';

function App() {
  const [usuario, setUsuario] = useState(null);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    const verificarSesion = async () => {
      try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}usuario/usuario-logueado`, {
          method: 'GET',
          credentials: 'include', 
        });
        if (res.ok) {
          const data = await res.json();
          setUsuario(data);
        } else {
          setUsuario(null);
        }
      } catch (error) {
        console.error('Error al verificar la sesión:', error);
        setUsuario(null);
      } finally {
        setCargando(false);
      }
    };

    verificarSesion();
  }, []);

  if (cargando) return <div>Cargando aplicacion...</div>;

  return (
    <BrowserRouter>
      <div className="flex h-screen bg-[#0a1120] text-white overflow-hidden">
        {usuario && <Sidebar />}
        <main className="flex-1 overflow-y-auto p-8">
          <Routes>
            <Route path="/registro" element={<Registro setUsuario={setUsuario} />} />
            <Route path="/ingresar-estadisticas" element={
              <RutaProtegida usuario={usuario}>
                <Estadisticas />
              </RutaProtegida>
            } />
            <Route path="/usuario-logueado" element={
              <RutaProtegida usuario={usuario}>
                <UsuarioLogueado setUsuario={setUsuario} />
              </RutaProtegida>
            } />
            <Route path="/" element={<Navigate to={usuario ? "/usuario-logueado" : "/registro"} />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
