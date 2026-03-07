import { use, useState } from "react";
import { useNavigate } from 'react-router-dom';

function Registro() {
    const navigate = useNavigate();
    const [datos, setDatos] = useState({
        nombre: '',
        apellido: '',
        email: '',
        username: '',
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
            const respuesta = await fetch(`${import.meta.env.VITE_API_URL}auth/registro`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(datos),
            });
            if(respuesta.ok){
                console.log("¡Usuario registrado exitosamente!");
                navigate('/login');
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
        <div className = "p-8">
            <h2>Registro de Usuario</h2>
            <form onSubmit = {handleSubmit}> 
                <input
                 type="text"
                 name="nombre"
                 placeholder="Escribe tu nombre..."
                 value={datos.nombre}
                 onChange={handleChange}
                 className="border p-2 rounded w-full mb-4"
                />
                <input
                 type="text"
                 name="apellido"
                 placeholder="Escribe tu apellido..."
                 value={datos.apellido}
                 onChange={handleChange}
                 className="border p-2 rounded w-full mb-4"
                />
                <input
                 type="email"
                 name="email"
                 placeholder="Escribe tu email..."
                 value={datos.email}
                 onChange={handleChange}
                 className="border p-2 rounded w-full mb-4"
                />
                <input
                 type="text"
                 name="username"
                 placeholder="Escribe tu username..."
                 value={datos.username}
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
                Registrarme
                </button>
            </form>
        </div>
    );
}
export default Registro;


