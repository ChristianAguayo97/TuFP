import { Navigate } from 'react-router-dom';

function RutaProtegida({ children }) {
    const token = localStorage.getItem('token');
    if ( token === null) {
        return <Navigate to="/registro" />;
    }
    return children;
}
export default RutaProtegida;