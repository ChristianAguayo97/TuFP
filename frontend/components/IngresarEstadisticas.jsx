import { useState } from "react";
import { useNavigate } from 'react-router-dom';

function Estadisticas() {
    const navigate = useNavigate();
    const [stats, setStats] = useState({
        ataque: 3,
        defensa: 3,
        creacion: 4,
        tecnica: 4,
        fisico: 4
    });
    const handleChange = (e) => {
        setStats({
            ...stats,
            [e.target.name]: Number(e.target.value),
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (stats.ataque + stats.defensa + stats.creacion + stats.tecnica + stats.fisico !== 18) {
            alert("La suma de tus estadisticas debe ser exactamente 18");
            return;
        }
        try {
            const respuesta = await fetch(`${import.meta.env.VITE_API_URL}auth/completar-estadisticas`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
                body: JSON.stringify(stats),
            });
            if (respuesta.ok) {
                console.log("¡Usuario registrado exitosamente!");
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
            <h2>Ingresa tus Estadísticas</h2>
            <p className="mb-4 text-gray-600">Recuerda: la suma de todos los atributos debe dar exactamente 18.</p>

            <form onSubmit={handleSubmit}>
                <label>Ataque:</label>
                <input type="number" name="ataque" min="1" max="5" value={stats.ataque} onChange={handleChange} className="border p-2 w-full mb-2" />

                <label>Defensa:</label>
                <input type="number" name="defensa" min="1" max="5" value={stats.defensa} onChange={handleChange} className="border p-2 w-full mb-2" />

                <label>Creación:</label>
                <input type="number" name="creacion" min="1" max="5" value={stats.creacion} onChange={handleChange} className="border p-2 w-full mb-2" />

                <label>Técnica:</label>
                <input type="number" name="tecnica" min="1" max="5" value={stats.tecnica} onChange={handleChange} className="border p-2 w-full mb-2" />

                <label>Físico:</label>
                <input type="number" name="fisico" min="1" max="5" value={stats.fisico} onChange={handleChange} className="border p-2 w-full mb-4" />

                <p className="font-bold mb-4">
                    Suma total actual: {stats.ataque + stats.defensa + stats.creacion + stats.tecnica + stats.fisico} / 18
                </p>

                <button type="submit" className="w-full bg-green-600 text-white p-2 rounded">
                    Guardar mis stats
                </button>
            </form>
        </div>
    );
}
export default Estadisticas;