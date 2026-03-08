import { NavLink } from 'react-router-dom';

function Sidebar() {
    return (
        <aside className="w-64 bg-[#111827] text-white flex flex-col p-6 h-full border-r border-gray-800">
            <h2 className="text-2xl font-bold mb-10 text-[#00df9a]">TuFP</h2>
            {/* Lista de Navegación */}
            <nav className="flex flex-col gap-6">
                <NavLink to="/perfil" className={({ isActive }) => isActive ? "text-[#00df9a] font-bold flex items-center gap-3" : "text-gray-400 hover:text-white flex items-center gap-3"}>
                    <span>👤</span> Perfil
                </NavLink>
                <NavLink to="/partidos" className={({ isActive }) => isActive ? "text-[#00df9a] font-bold flex items-center gap-3" : "text-gray-400 hover:text-white flex items-center gap-3"}>
                    <span>⚽</span> Partidos
                </NavLink>
                <NavLink to="/canchas" className={({ isActive }) => isActive ? "text-[#00df9a] font-bold flex items-center gap-3" : "text-gray-400 hover:text-white flex items-center gap-3"}>
                    <span>🏟️</span> Canchas
                </NavLink>
                <NavLink to="/ranking" className={({ isActive }) => isActive ? "text-[#00df9a] font-bold flex items-center gap-3" : "text-gray-400 hover:text-white flex items-center gap-3"}>
                    <span>🏆</span> Ranking
                </NavLink>
            </nav>
        </aside>
    );
}
export default Sidebar;