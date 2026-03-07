import Registro from "../components/Registro.jsx";
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

function Login() {
  return <h2>Pantalla de Login</h2>
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/registro" />} />
        <Route path="/registro" element={<Registro />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>     
  )
}
export default App;