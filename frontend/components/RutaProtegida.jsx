import { Navigate } from 'react-router-dom';

function RutaProtegida({ children, usuario }) {
    if (usuario === null) {
        return <Navigate to="/registro" />;
    }
    return children;
}

export default RutaProtegida;
