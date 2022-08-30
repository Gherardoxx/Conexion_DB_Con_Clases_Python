from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario


class UsuarioDAO:
    '''
    DAO - Data Access Object para la tabla de usuario
    CRUD - Create - Read - Update - Delete para la tabla de usuario
    '''
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    # Definimos las classmethod para llamar a las clases ya declaradas

    #  Declaramos la classmethod para seleccionar
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios') # Se usa la sentencia With para iniciar y finalizar el bloque
            cursor.execute(cls._SELECT) #Realiza las consultas llamando a SELECT en este caso, de esta manera
            # Se realizan las consultas  llamando a las clases indicadas y no colocandolas directamente
            registros = cursor.fetchall() # fetchall Con esta funcion se llaman todos los registros, se puede usar fechone para un solo registro
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password) #se realiza una tupla de valores en el mismo orden que se tienen que sustituir los valores
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount # Devuelve la cantidad de registros modificados

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount