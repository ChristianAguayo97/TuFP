import { useEffect, useState } from "react";
import { useNavigate } from 'react-router-dom';

function UsuarioLogueado({ setUsuario }) {
    const navigate = useNavigate();
    const [cargando, setCargando] = useState(true);
    const [datos, setDatos] = useState({
        nombre: '',
        apellido: '',
        email: '',
        username: '',
        foto_perfil: '',
        titulo: '',
        partidos_ganados: 0,
        partidos_perdidos: 0,
        partidos_empatados: 0,
        estadisticas: {}
    });

    const handleLogout = async () => {
        try {
            await fetch(`${import.meta.env.VITE_API_URL}auth/logout`, {
                method: 'POST',
                credentials: 'include',
            });
        } catch (error) {
            console.error("Error al cerrar sesión:", error);
        } finally {
            setUsuario(null); 
            navigate('/registro');
        }
    };

    useEffect(() => {
        const obtenerUsuario = async () => {
            try {
                const respuesta = await fetch(`${import.meta.env.VITE_API_URL}usuario/usuario-logueado`, {
                    method: 'GET',
                    credentials: 'include', 
                });
                if (respuesta.ok) {
                    const usuarioData = await respuesta.json();
                    setDatos(usuarioData);
                    setCargando(false);
                }
            } catch (error) {
                console.error("Error al obtener perfil:", error);
            }
        };
        obtenerUsuario();
    }, []);

    if (cargando) {
        return <p>Cargando...</p>;
    }

    return (
        <div className="p-8">
            <h1>Bienvenido a tu perfil, {datos.nombre}! ⚽</h1>
            <section className="mb-6">
                <h2>Información Personal 📋</h2>
                <p>Nombre: {datos.nombre}</p>
                <p>Apellido: {datos.apellido}</p>
                <p>Título: {datos.titulo}</p>
                <p>Email: {datos.email}</p>
                <p>Username: {datos.username}</p>
            </section>

            <section>
                <h2>Tus Estadísticas 📊</h2>
                <p>Partidos ganados: {datos.partidos_ganados}</p>
                <p>Partidos perdidos: {datos.partidos_perdidos}</p>
                <p>Partidos empatados: {datos.partidos_empatados}</p>
                <p>Ataque: {datos.estadisticas?.ataque}</p>
                <p>Defensa: {datos.estadisticas?.defensa}</p>
                <p>Creación: {datos.estadisticas?.creacion}</p>
                <p>Técnica: {datos.estadisticas?.tecnica}</p>
                <p>Físico: {datos.estadisticas?.fisico}</p>
            </section>

            <button
                onClick={handleLogout}
                className="mt-4 px-4 py-2 bg-red-500 text-white rounded"
            >
                Cerrar sesión
            </button>
        </div>
    );
}

export default UsuarioLogueado;
