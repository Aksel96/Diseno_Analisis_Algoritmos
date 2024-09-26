class Alumno:
    def __init__(self, num_cuenta,nombre,ap_p,ap_m,edad,correo,semestre,materias,promedio):
        self.num_cuenta = num_cuenta
        self.nombre = nombre
        self.ap_p = ap_p
        self.ap_m = ap_m
        self.edad = edad
        self.correo = correo
        self.semestre = semestre
        self.materias = materias
        self.promedio = promedio

    def get_num_cuenta(self):
        return self.num_cuenta

    def get_nombre(self):
        return self.nombre

    def get_ap_p(self):
        return self.ap_p

    def get_ap_m(self):
        return self.ap_m

    def get_edad(self):
        return self.edad

    def get_correo(self):
        return self.correo

    def get_semestre(self):
        return self.semestre

    def get_materias(self):
        return self.materias

    def get_promedio(self):
        return self.promedio

    def set_num_cuenta(self, num_cuenta):
        self.num_cuenta = num_cuenta

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_ap_p(self, ap_p):
        self.ap_p = ap_p

    def set_ap_m(self, ap_m):
        self.ap_m = ap_m

    def set_edad(self, edad):
        self.edad = edad

    def set_correo(self, correo):
        self.correo = correo

    def set_semestre(self, semestre):
        self.semestre = semestre

    def set_materias(self, materias):
        self.materias = materias

    def set_promedio(self, promedio):
        self.promedio = promedio

    def __str__(self):
        return (f"{self.nombre},"
                f"\n{self.ap_p},"
                f"\n{self.ap_m},"
                f"\n{self.edad} años,"
                f"\n{self.num_cuenta},"
                f"\n{self.correo},"
                f"\n{self.semestre},"
                f"\n{self.materias},"
                f"\n{self.promedio}")