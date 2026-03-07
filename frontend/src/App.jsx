import Registro from "../components/Registro.jsx";
import Estadisticas from "../components/IngresarEstadisticas.jsx";
import RutaProtegida from "../components/RutaProtegida.jsx";
import UsuarioLogueado from "../components/UsuarioLogueado.jsx";
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/registro" />} />
        <Route path="/registro" element={<Registro />} />
        <Route path="/ingresar-estadisticas" element={
          <RutaProtegida>
            <Estadisticas />
          </RutaProtegida>
        } />
        <Route path="/usuario-logueado" element={
          <RutaProtegida>
            <UsuarioLogueado />
          </RutaProtegida>
        } /> 
      </Routes>
    </BrowserRouter>
  )
}
export default App;