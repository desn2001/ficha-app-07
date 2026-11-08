"""Genera la ficha de datos técnicos de una aplicación móvil."""
import sys
from decimal import ROUND_HALF_UP, Decimal
from typing import Final

# ---------------------------------------------------------------------------
# Datos de la aplicación. Sustituid los del ejemplo APP-00 por los vuestros.
# ---------------------------------------------------------------------------
CODIGO: Final[str] = "APP-00"
NOMBRE: Final[str] = "Agenda Escolar"
PAQUETE: Final[str] = "es.ieseuropa.agenda"
VERSION_MAYOR, VERSION_MENOR, VERSION_PARCHE = 2, 5, 13
TAMANO_APK: Final[int] = 48_734_208          # bytes
DESCARGAS: Final[int] = 12_500
PRECIO: Final[float] = 1.99                  # euros, IVA incluido
VALORACIONES: Final[int] = 400
ESTRELLAS: Final[int] = 1_700                # suma de todas las valoraciones
PERMISOS: Final[int] = 0b0001011
COLOR_ICONO: Final[int] = 0xFF3A7BD5         # ARGB

# ---------------------------------------------------------------------------
# Datos del programa. Solo hay que cambiar AUTORES.
# ---------------------------------------------------------------------------
VERSION_PROGRAMA: Final[str] = "1.0.0"
AUTORES: Final[str] = "[usuario] · [usuario]"
PENDIENTE: Final[str] = "  (opción pendiente de implementar)"

# ---------------------------------------------------------------------------
# Constantes de la pareja. Todo valor fijo del programa va aquí, con nombre.
# ---------------------------------------------------------------------------
ANCHO: Final[int] = 44
ANCHO_ETIQUETA: Final[int] = 18
ANCHO_VALOR: Final[int] = 14

COMISION: Final[float] = 0.15

BYTES_MB: Final[int] = 10 ** 6
BYTES_MIB: Final[int] = 2 ** 20
PORCENTAJE: Final[int] = 100

BITS_MENOR: Final[int] = 8
BITS_MAYOR: Final[int] = 16
MASCARA_8_BITS: Final[int] = 0xFF

PERMISO_INTERNET: Final[int] = 0b0000001
PERMISO_NOTIFICACIONES: Final[int] = 0b0000010
PERMISO_CAMARA: Final[int] = 0b0000100
PERMISO_UBICACION: Final[int] = 0b0001000
PERMISO_CONTACTOS: Final[int] = 0b0010000
PERMISO_MICROFONO: Final[int] = 0b0100000
PERMISO_ALMACENAMIENTO: Final[int] = 0b1000000
CIFRAS_PERMISOS: Final[int] = 7

DESPLAZ_ROJO: Final[int] = 16
DESPLAZ_VERDE: Final[int] = 8
DESPLAZ_ALFA: Final[int] = 24
OPACIDAD_MAXIMA: Final[int] = 255


# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------
def fila(etiqueta: str, valor: str) -> str:
    """Devuelve una fila con la etiqueta alineada y su valor."""
    return f"{etiqueta + ':':<{ANCHO_ETIQUETA}}{valor}"


def separador(caracter: str) -> str:
    """Devuelve una línea de ANCHO caracteres repitiendo el carácter."""
    return caracter * ANCHO


# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------
def opcion_1_identificacion() -> None:
    """Muestra la identificación de nuestra app móvil."""
    version = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    print(fila("Código", CODIGO))
    print(fila("Nombre", NOMBRE))
    print(fila("Paquete", PAQUETE))
    print(fila("Versión", version))


def opcion_2_tamano() -> None:
    """Muestra el tamaño del APK en B, MB, MiB y la diferencia"""
    megabytes = TAMANO_APK / BYTES_MB
    mebibytes = TAMANO_APK / BYTES_MIB
    diferencia = (megabytes - mebibytes) / megabytes * PORCENTAJE
    print(fila("Bytes", f"{TAMANO_APK:>{ANCHO_VALOR}} B"))
    print(fila("En la tienda", f"{megabytes:>{ANCHO_VALOR}.2f} MB"))
    print(fila("En el móvil", f"{mebibytes:>{ANCHO_VALOR}.2f} MiB"))
    print(fila("Diferencia", f"{diferencia:>{ANCHO_VALOR}.1f} %"))


def opcion_3_ingresos() -> None:
    """[Docstring: qué hace esta opción.]"""
    ingresos_brutos = DESCARGAS * PRECIO
    comision_tienda = ingresos_brutos * COMISION
    ingresos_netos = ingresos_brutos - COMISION
    print(fila("Descargas", f"{DESCARGAS:>{ANCHO_VALOR}} uds"))
    print(fila("Precio", f"{PRECIO:>{ANCHO_VALOR}.2f} €"))
    print(fila("Ingresos brutos", f"{ingresos_brutos:>{ANCHO_VALOR}.2f} €"))
    print(fila("Comisión tienda", f"{comision_tienda:>{ANCHO_VALOR}.2f} €"))
    print(fila("Ingresos netos", f"{ingresos_brutos:>{ANCHO_VALOR}.2f} €"))


def opcion_4_version() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_5_permisos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_6_color() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_7_tipos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_8_redondeo() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_9_ficha() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_10_acerca_de() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


# ---------------------------------------------------------------------------
# Función principal y punto de entrada. Vienen hechos: no los modifiquéis.
# ---------------------------------------------------------------------------
def main() -> None:
    """Ejecuta las diez opciones, una detrás de otra."""
    print("--- Opción 1. Identificación de la app ---")
    opcion_1_identificacion()
    print("\n--- Opción 2. Tamaño del APK ---")
    opcion_2_tamano()
    print("\n--- Opción 3. Ingresos ---")
    opcion_3_ingresos()
    print("\n--- Opción 4. versionCode ---")
    opcion_4_version()
    print("\n--- Opción 5. Permisos ---")
    opcion_5_permisos()
    print("\n--- Opción 6. Color del icono ---")
    opcion_6_color()
    print("\n--- Opción 7. Tipos de datos ---")
    opcion_7_tipos()
    print("\n--- Opción 8. Redondeo de la valoración ---")
    opcion_8_redondeo()
    print("\n--- Opción 9. Ficha completa ---")
    opcion_9_ficha()
    print("\n--- Opción 10. Acerca de ---")
    opcion_10_acerca_de()


if __name__ == "__main__":
    main()
