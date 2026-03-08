import { useState } from "react";
import { useNavigate } from 'react-router-dom';

function Login({ setUsuario }) {
    const navigate = useNavigate();
    const [datos, setDatos] = useState({
        emailOUsername: '',
        contrasena: ''
    });

    const handleChange = (e) => {
        setDatos({
            ...datos,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const respuesta = await fetch(`${import.meta.env.VITE_API_URL}auth/token`, {
                method: 'POST',
                credentials: 'include',
                body: new URLSearchParams({
                    username: datos.emailOUsername,
                    password: datos.contrasena
                }),
            });
            if (respuesta.ok) {
                const data = await respuesta.json();
                setUsuario(data);
                navigate('/usuario-logueado');
            } else {
                const errorData = await respuesta.json();
                console.error("Error del servidor:", errorData);
                alert("Hubo un error: " + errorData.detail);
            }
        } catch (error) {
            console.error("Error al conectar con el servidor:", error);
        }
    };

    return (
        <div className="p-8">
            <h2>Iniciar Sesión</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="emailOUsername"
                    placeholder="Email o username..."
                    value={datos.emailOUsername}
                    onChange={handleChange}
                    className="border p-2 rounded w-full mb-4"
                />
                <input
                    type="password"
                    name="contrasena"
                    placeholder="Contraseña"
                    value={datos.contrasena}
                    onChange={handleChange}
                    className="border p-2 rounded w-full mb-4"
                />
                <button
                    type="submit"
                    className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700 transition"
                >
                    Iniciar Sesión
                </button>
                <button
                    type="button"
                    onClick={() => navigate('/registro')}
                    className="mt-4 text-blue-400 hover:underline w-full text-center"
                >
                    ¿No tienes cuenta? Regístrate aquí
                </button>
            </form>
        </div>
    );
}

export default Login;



