import { useEffect, useState } from "react";
import { useNavigate } from 'react-router-dom';

function UsuarioLogueado() {
    const navigate = useNavigate();
    const handleLogout = () => {
        localStorage.removeItem('token');
        navigate('/login');
    };
    const [cargando, setCargando] = useState(true);
    const [usuario, setUsuario] = useState({
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

    useEffect(() => {
        const obtenerUsuario = async () => {
            try {
                const respuesta = await fetch(`${import.meta.env.VITE_API_URL}usuario/usuario-logueado`, {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token')}`
                    }
                });
                if (respuesta.ok) {
                    const usuarioData = await respuesta.json();
                    setUsuario(usuarioData);
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
            <h1>Bienvenido a tu perfil, {usuario.nombre}! ⚽</h1>
            <section className="mb-6">
                <h2>Información Personal 📋</h2>
                <p>Nombre: {usuario.nombre}</p>
                <p>Apellido: {usuario.apellido}</p>
                <p>Título: {usuario.titulo}</p>
                <p>Email: {usuario.email}</p>
                <p>Username: {usuario.username}</p>
            </section>

            <section>
                <h2>Tus Estadísticas 📊</h2>
                <p>Partidos ganados: {usuario.partidos_ganados}</p>
                <p>Partidos perdidos: {usuario.partidos_perdidos}</p>
                <p>Partidos empatados: {usuario.partidos_empatados}</p>
                <p>Ataque:{usuario.estadisticas?.ataque}</p>
                <p>Defensa:{usuario.estadisticas?.defensa}</p>
                <p>Creación:{usuario.estadisticas?.creacion}</p>
                <p>Técnica:{usuario.estadisticas?.tecnica}</p>
                <p>Físico:{usuario.estadisticas?.fisico}</p>
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

