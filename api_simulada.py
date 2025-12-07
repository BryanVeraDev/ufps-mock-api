from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
from data import (
    ESTUDIANTES,
    PROFESORES,
    DIRECTIVOS,
    CURSOS_ESTUDIANTE,
    CURSOS_PROFESOR,
    ESTUDIANTES_CURSO
)

# ==================== CONFIGURACIÓN ====================

app = FastAPI(
    title="API SAT SIA Simulada",
    description="Réplica exacta de la API SAT SIA con datos simulados",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== MODELOS ====================
class StandardResponse(BaseModel):
    """Estructura de respuesta estándar del proyecto"""
    ok: bool
    data: Optional[Any] = None
    msg: str

# ==================== FUNCIONES DE UTILIDAD ====================

def validate_code(code: str) -> bool:
    """Valida que el código tenga 5-7 dígitos numéricos (como el original)"""
    return code and code.isnumeric() and 5 <= len(code) <= 7

def validate_code_group(code: str, group: str) -> bool:
    """Valida código (5-7 dígitos) y grupo (1 carácter no numérico)"""
    return (code and code.isnumeric() and 5 <= len(code) <= 7 and 
            group and not group.isnumeric() and len(group) == 1)

# ==================== ENDPOINTS PÚBLICOS ====================

@app.get("/", tags=["Health"])
def ping():
    """Health check del API"""
    return {"message": "Hola, API SAT SIA Simulada está activa"}

@app.get("/test-connection", tags=["Health"])
def test_connection():
    """Test de conexión (simulado)"""
    return {"ok": True, "message": "Conexión exitosa"}

# ==================== ENDPOINTS ESTUDIANTE ====================

@app.get("/student/email/{email}", tags=["Estudiante"], response_model=StandardResponse)
def get_student_by_email(email: str):
    """
    ENDPOINT PÚBLICO - No requiere token
    Busca un estudiante por email
    """
    for codigo, estudiante in ESTUDIANTES.items():
        if estudiante["email"] == email:
            return {"ok": True, "data": estudiante, "msg": "Estudiante obtenido con éxito"}
    
    return {"ok": False, "data": None, "msg": "Estudiante no encontrado"}

@app.get("/student/code/{code}", tags=["Estudiante"], response_model=StandardResponse)
def get_student_by_code(code: str):
    """
    Busca un estudiante por código
    """
    if not validate_code(code):
        return {"ok": False, "data": None, "msg": "El código es incorrecto"}
    
    estudiante = ESTUDIANTES.get(code)
    if estudiante:
        return {"ok": True, "data": estudiante, "msg": "Estudiante obtenido con éxito"}
    
    return {"ok": False, "data": None, "msg": "Estudiante no encontrado"}

@app.get("/student/courses/{code}", tags=["Estudiante"], response_model=StandardResponse)
def get_student_courses(code: str):
    """
    Obtiene cursos de un estudiante
    """
    if not validate_code(code):
        return {"ok": False, "data": None, "msg": "El código es incorrecto"}
    
    cursos = CURSOS_ESTUDIANTE.get(code)
    if cursos:
        return {"ok": True, "data": cursos, "msg": "Cursos obtenidos con éxito"}
    
    return {"ok": False, "data": None, "msg": "No se obtuvieron resultados"}

@app.get("/student/courses/ac012/{code}", tags=["Estudiante AC012"], response_model=StandardResponse)
def get_student_courses_ac012(code: str):
    """
    Obtiene cursos AC012 de un estudiante
    """
    if not validate_code(code):
        return {"ok": False, "data": None, "msg": "El código es incorrecto"}
    
    cursos = CURSOS_ESTUDIANTE.get(code, [])
    cursos_ac012 = [c for c in cursos if c.get("ac012", False)]
    
    return {"ok": True, "data": cursos_ac012, "msg": "Cursos AC012 obtenidos con éxito"}

@app.get("/student/total_estudiantes/ac012", tags=["Estudiante AC012"], response_model=StandardResponse)
def get_total_estudiantes_ac012():
    """
    Obtiene total de estudiantes en AC012
    """
    total = sum(1 for estudiantes in ESTUDIANTES_CURSO.values() 
                for est in estudiantes if est.get("ac012", False))
    
    return {"ok": True, "data": {"type": "AC 012", "total": total}, "msg": "Total de estudiantes en el acuerdo AC012 obtenido con éxito"}

@app.get("/student/courses/students/ac012", tags=["Estudiante AC012"], response_model=StandardResponse)
def get_students_ac012():
    """
    Obtiene estudiantes en AC012
    """
    estudiantes_ac012 = []
    for codigo, estudiantes in ESTUDIANTES_CURSO.items():
        for est in estudiantes:
            if est.get("ac012", False):
                est_copy = est.copy()
                est_copy["ac012"] = True
                estudiantes_ac012.append(est_copy)
    
    if not estudiantes_ac012:
        return {"ok": False, "data": [], "msg": "No se obtuvieron resultados"}
    
    return {"ok": True, "data": estudiantes_ac012, "msg": "Estudiantes obtenidos con éxito"}

# ==================== ENDPOINTS PROFESOR ====================

@app.get("/teacher/code/{code}", tags=["Profesor"], response_model=StandardResponse)
def get_teacher_by_code(code: str):
    """
    Busca un profesor por código
    """
    if not validate_code(code):
        return {"ok": False, "data": None, "msg": "El código es incorrecto"}
    
    profesor = PROFESORES.get(code)
    if profesor:
        return {"ok": True, "data": profesor, "msg": "Profesor obtenido con éxito"}
    
    return {"ok": False, "data": None, "msg": "Profesor no encontrado"}

@app.get("/teacher/courses/{code}", tags=["Profesor"], response_model=StandardResponse)
def get_teacher_courses(code: str):
    """
    Obtiene cursos de un profesor
    """
    if not validate_code(code):
        return {"ok": False, "data": None, "msg": "El código es incorrecto"}
    
    cursos = CURSOS_PROFESOR.get(code)
    if cursos:
        return {"ok": True, "data": cursos, "msg": "Cursos obtenidos con éxito"}
    
    return {"ok": False, "data": None, "msg": "No se obtuvieron resultados"}

@app.get("/teacher/students-course/{code}/{group}", tags=["Profesor"], response_model=StandardResponse)
def get_students_of_course(
    code: str,
    group: str,
    page: int = Query(1),
    limit: int = Query(15),
    filter: str = Query("")
):
    
    if not validate_code_group(code, group):
        return {"ok": False, "data": None, "msg": "El código o el grupo es incorrecto"}
    
    course_key = f"{code}{group}"
    estudiantes = ESTUDIANTES_CURSO.get(course_key, [])
    
    # Paginación simulada
    page = max(1, page)
    limit = max(1, limit)
    nUntil = page * limit
    nFrom = nUntil - limit
    
    total_pages = (len(estudiantes) + limit - 1) // limit
    
    data = estudiantes[nFrom:nUntil]
    
    if not data:
        return {"ok": False, "data": None, "msg": "No se obtuvieron resultados"}
    
    info = {"students": data, "totalPages": total_pages}
    return {"ok": True, "data": info, "msg": "Cursos obtenidos con éxito"}

@app.get("/teacher/students-ac012/{code}/{group}", tags=["Profesor AC012"], response_model=StandardResponse)
def get_students_in_ac012(code: str, group: str):
    """
    Obtiene estudiantes en AC012 de un curso
    """
    if not validate_code_group(code, group):
        return {"ok": False, "data": None, "msg": "El código o el grupo es incorrecto"}
    
    course_key = f"{code}{group}"
    estudiantes = ESTUDIANTES_CURSO.get(course_key, [])
    
    estudiantes_ac012 = [
        {**est, "ac012": True} 
        for est in estudiantes if est.get("ac012", False)
    ]
    
    return {"ok": True, "data": estudiantes_ac012, "msg": "Estudiantes obtenidos con éxito"}

# ==================== ENDPOINTS DIRECTIVO ====================

@app.get("/boss/courses/{semester}/{program}", tags=["Directivo"], response_model=StandardResponse)
def get_courses_of_semester(
    semester: str,
    program: str
):
    """
    Obtiene cursos por semestre y programa
    """
    cursos = [
        {"codigo": "1234567", "nombre": "Bases de Datos", "creditos": 3},
        {"codigo": "1234568", "nombre": "Programación Web", "creditos": 4},
    ]
    return {"ok": True, "data": cursos, "msg": "Cursos obtenidos con éxito"}

@app.get("/boss/courses/groups/{program}/{course}", tags=["Directivo"], response_model=StandardResponse)
def get_groups_of_course(
    program: str,
    course: str
):
    """
    Obtiene grupos de un curso
    """
    grupos = ["A", "B", "C"]
    return {"ok": True, "data": grupos, "msg": "Grupos obtenidos con éxito"}

@app.get("/boss/courses/group/{program}/{course}/{group}", tags=["Directivo"], response_model=StandardResponse)
def get_group(
    program: str,
    course: str,
    group: str
):
    """
    Obtiene información de un grupo específico
    """
    grupo_info = {
        "programa": program,
        "curso": course,
        "grupo": group,
        "estudiantes": 25,
        "docente": "Dr. Fernando Rodríguez"
    }
    return {"ok": True, "data": grupo_info, "msg": "Grupo obtenido con éxito"}

@app.get("/boss/semesters/{program}", tags=["Directivo"], response_model=StandardResponse)
def get_semesters_of_program(
    program: str
):
    """
    Obtiene semestres de un programa
    """
    semesters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return {"ok": True, "data": semesters, "msg": "Semestres obtenidos con éxito"}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

