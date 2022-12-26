class alumno:

    def inicializar(self, nombre , nota):
        self.nombre =nombre
        self.nota =nota


    def _mostrar(self):
        print("nombre:",self.nombre)
        print("nota:", self.nota)

    def resultado(self):
        if self.nota>3:
           print("el alumno aprobo")
        else:
          print("el alumno no aprobo")


alumno1=alumno()
alumno1.inicializar("maria",3.5)
alumno1._mostrar()
alumno1.resultado()

alumno2=alumno()
alumno2.inicializar("juan",2)
alumno2._mostrar()
alumno2.resultado()