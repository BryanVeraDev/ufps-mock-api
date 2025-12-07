ESTUDIANTES = {
    "1234567": {
        "codigo": "1234567",
        "nombre": "Juan Pérez",
        "email": "juan.perez@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 5,
        "estado": "activo",
    },
    "2345678": {
        "codigo": "2345678",
        "nombre": "María García",
        "email": "maria.garcia@ufps.edu.co",
        "programa": "Ingeniería Civil",
        "semestre": 3,
        "estado": "activo",
    },
    "3456789": {
        "codigo": "3456789",
        "nombre": "Carlos López",
        "email": "carlos.lopez@ufps.edu.co",
        "programa": "Administración",
        "semestre": 7,
        "estado": "activo",
    },
    "1152263": {
        "codigo": "1152263",
        "nombre": "Omar David Jaimes Molina",
        "email": "omardavidjm@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 8,
        "estado": "activo",
    },
    "1152278": {
        "codigo": "1152278",
        "nombre": "Evelin Zharit Bermudez Guerrero",
        "email": "evelinzharitbg@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 8,
        "estado": "activo",
    },
    "1152277": {
        "codigo": "1152277",
        "nombre": "Bryan Alejandro Vera Osorio",
        "email": "bryanalejandrovo@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 8,
        "estado": "activo",
    },
    "1152280": {
        "codigo": "1152280",
        "nombre": "Saimer Adrian Saavedra Rojas",
        "email": "saimeradriansr@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 8,
        "estado": "activo",
    },
    "1152281": {
        "codigo": "1152281",
        "nombre": "Brayan Sebastian Gonzalez Gonzalez",
        "email": "brayansebastiangg@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 8,
        "estado": "activo",
    },
    "1152137": {
        "codigo": "1152137",
        "nombre": "Yohan Camilo Botello Maldonado",
        "email": "yohancamilobm@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 10,
        "estado": "activo",
    },
    "1152258": {
        "codigo": "1152258",
        "nombre": "Leydi Alejandra Durán Rozo",
        "email": "leydialejandradr@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 8,
        "estado": "activo",
    },
    "1152254": {
        "codigo": "1152254",
        "nombre": "Andres Felipe Lopez Triana",
        "email": "andresfelipelt@ufps.edu.co",
        "programa": "Ingeniería de Sistemas",
        "semestre": 8,
        "estado": "activo",
    },
}

PROFESORES = {
    "1000001": {
        "codigo": "1000001",
        "nombre": "Dr. Fernando Rodríguez",
        "email": "fernando.rodriguez@ufps.edu.co",
        "departamento": "Ingeniería de Sistemas",
        "estado": "activo",
    },
    "1000002": {
        "codigo": "1000002",
        "nombre": "Ing. Patricia Martínez",
        "email": "patricia.martinez@ufps.edu.co",
        "departamento": "Ingeniería Civil",
        "estado": "activo",
    },
}

DIRECTIVOS = {
    "2000001": {
        "codigo": "2000001",
        "nombre": "MSc. Roberto Díaz",
        "email": "roberto.diaz@ufps.edu.co",
        "cargo": "Decano",
        "facultad": "Ingeniería",
        "estado": "activo",
    }
}

CURSOS_ESTUDIANTE = {
    "1234567": [
        {
            "codigo": "1234567",
            "nombre": "Bases de Datos",
            "creditos": 3,
            "semestre": 5,
            "estado": "cursando",
        },
        {
            "codigo": "1234568",
            "nombre": "Programación Web",
            "creditos": 4,
            "semestre": 5,
            "estado": "cursando",
        },
        {
            "codigo": "1234569",
            "nombre": "Ingeniería de Software",
            "creditos": 4,
            "semestre": 5,
            "estado": "cursando",
        },
    ],
    "2345678": [
        {
            "codigo": "1234570",
            "nombre": "Análisis Estructural",
            "creditos": 4,
            "semestre": 3,
            "estado": "cursando",
        },
        {
            "codigo": "1234571",
            "nombre": "Resistencia de Materiales",
            "creditos": 3,
            "semestre": 3,
            "estado": "cursando",
        },
    ],
}

CURSOS_PROFESOR = {
    "1000001": [
        {
            "codigo": "1234567",
            "nombre": "Bases de Datos",
            "grupo": "A",
            "estudiantes": 30,
        },
        {
            "codigo": "1234568",
            "nombre": "Programación Web",
            "grupo": "B",
            "estudiantes": 25,
        },
    ]
}

ESTUDIANTES_CURSO = {
    "1234567A": [
        {
            "codigo": "1234567",
            "nombre": "Juan Pérez",
            "email": "juan.perez@ufps.edu.co",
            "calificacion": 4.2,
            "asistencia": 95,
            "riesgo": 5,
            "ac012": False,
        },
        {
            "codigo": "2345678",
            "nombre": "María García",
            "email": "maria.garcia@ufps.edu.co",
            "calificacion": 3.8,
            "asistencia": 87,
            "riesgo": 5,
            "ac012": False,
        },
        {
            "codigo": "3456789",
            "nombre": "Carlos López",
            "email": "carlos.lopez@ufps.edu.co",
            "calificacion": 2.1,
            "asistencia": 65,
            "riesgo": 1,
            "ac012": True,
        },
    ]
}
