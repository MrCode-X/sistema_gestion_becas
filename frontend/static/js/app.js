let token = null;

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const response = await fetch('/api/token/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    if (response.ok) {
        const data = await response.json();
        token = data.access;
        document.getElementById('loginSection').style.display = 'none';
        document.getElementById('panelSection').style.display = 'block';
        cargarPostulaciones();
        cargarDashboard();
    } else {
        alert('Credenciales incorrectas');
    }
}

async function cargarPostulaciones() {
    const response = await fetch('/api/postulaciones/', {
        headers: { 'Authorization': `Bearer ${token}` }
    });
    const data = await response.json();
    const container = document.getElementById('postulacionesList');
    container.innerHTML = data.map(p => `
        <div class="card p-3">
            <b>${p.estudiante_nombre}</b> → ${p.programa_nombre} | Estado: ${p.estado} | Monto: Bs ${p.monto_asignado || 0}
            <div class="mt-2">
                <button class="btn btn-sm btn-warning" onclick="actualizarPostulacion(${p.id})">✏️ Editar</button>
                <button class="btn btn-sm btn-danger" onclick="eliminarPostulacion(${p.id})">🗑️ Eliminar</button>
            </div>
        </div>
    `).join('');
}

async function actualizarPostulacion(id) {
    const nuevoEstado = prompt('Nuevo estado (pendiente/aprobada/rechazada):');
    if (!nuevoEstado) return;
    await fetch(`/api/postulaciones/${id}/`, {
        method: 'PUT',
        headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({ estado: nuevoEstado })
    });
    cargarPostulaciones();
    cargarDashboard();
}

async function eliminarPostulacion(id) {
    if (!confirm('¿Eliminar esta postulación?')) return;
    await fetch(`/api/postulaciones/${id}/`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
    });
    cargarPostulaciones();
    cargarDashboard();
}

document.getElementById('postulacionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        estudiante: parseInt(document.getElementById('estudiante_id').value),
        programa: parseInt(document.getElementById('programa_id').value),
        estado: document.getElementById('estado').value,
        monto_asignado: parseFloat(document.getElementById('monto_asignado').value) || null
    };
    await fetch('/api/postulaciones/', {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    cargarPostulaciones();
    cargarDashboard();
});

async function cargarDashboard() {
    const response = await fetch('/api/programas/?activo=true', { headers: { 'Authorization': `Bearer ${token}` } });
    const programas = await response.json();
    document.getElementById('totalProgramas').innerText = programas.length;
    
    const postulaciones = await (await fetch('/api/postulaciones/', { headers: { 'Authorization': `Bearer ${token}` } })).json();
    document.getElementById('totalPostulaciones').innerText = postulaciones.length;
    document.getElementById('totalAprobadas').innerText = postulaciones.filter(p => p.estado === 'aprobada').length;
    
    const inversion = await (await fetch('/api/postulaciones/inversion_total/', { headers: { 'Authorization': `Bearer ${token}` } })).json();
    document.getElementById('totalInversion').innerText = `Bs ${inversion.total_invertido || 0}`;
}

async function consultarPorEstado() {
    const res = await fetch('/api/postulaciones/por_estado/?estado=pendiente', { headers: { 'Authorization': `Bearer ${token}` } });
    const data = await res.json();
    document.getElementById('resultadosConsulta').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}

async function resumenProgramas() {
    const res = await fetch('/api/postulaciones/resumen_por_programa/', { headers: { 'Authorization': `Bearer ${token}` } });
    const data = await res.json();
    document.getElementById('resultadosConsulta').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}

async function estudiantesDestacados() {
    const promedio = document.getElementById('promedio_min').value || 80;
    const res = await fetch(`/api/postulaciones/estudiantes_destacados/?promedio_min=${promedio}`, { headers: { 'Authorization': `Bearer ${token}` } });
    const data = await res.json();
    document.getElementById('resultadosConsulta').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}

async function rankingProgramas() {
    const res = await fetch('/api/postulaciones/ranking_programas/', { headers: { 'Authorization': `Bearer ${token}` } });
    const data = await res.json();
    document.getElementById('resultadosConsulta').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}