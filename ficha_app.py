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
CIFRAS_HEX: Final[int] = 6

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

CIFRAS_ARGB: Final[int] = 8
CIFRAS_CANAL: Final[int] = 2
ANCHO_DECIMAL: Final[int] = 5
ANCHO_TIPO: Final[int] = 20
DECIMALES: Final[int] = 1
DECIMALES_EXTRA: Final[int] = 2
CUANTO_1_DEC: Final[Decimal] = Decimal("0.1")
CUANTO_2_DEC: Final[Decimal] = Decimal("0.2")


# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------
def fila(etiqueta: str, valor: str) -> str:
    """Devuelve una fila con la etiqueta alineada y su valor."""
    return f"{etiqueta + ':':<{ANCHO_ETIQUETA}}{valor}"


def separador(caracter: str) -> str:
    """Devuelve una línea de ANCHO caracteres repitiendo el carácter."""
    return caracter * ANCHO


def fila_canal(nombre: str, canal: int) -> str: 
    """ Devuelve una fila de canal de color: decimal, binario y hexadecimal"""
    decimal = f"{canal:<{ANCHO_ETIQUETA}}"
    binario = f"{canal:0{BITS_MENOR}b}"
    hexadecimal = f"{canal:0{CIFRAS_CANAL}x}"
    return fila(nombre, f"{decimal}{binario} {hexadecimal}")


def fila_tipo(nombre:str, valor:object) -> str: 
    """ Devuelve una fila con el nombre, el tipo (type) y el valor """
    tipo = str(type(valor))
    return f"{nombre + ':' :<{ANCHO_ETIQUETA}}{tipo:<{ANCHO_TIPO}}{valor}"


def valoracion_media() -> float:
    """ Devuelve la valoracion media --> Suma de estrellas entre las valoraciones """
    return ESTRELLAS / VALORACIONES


def redondeo_escolar(valor: Decimal, cuanto: Decimal) -> Decimal:
    """ Redondea con ROUND_HALF_UP: Los empates siempre suben """
    return valor.quantize(cuanto, rounding=ROUND_HALF_UP)


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
    """Muestra el tamaño del APK en B, MB, MiB y la diferencia."""
    megabytes = TAMANO_APK / BYTES_MB
    mebibytes = TAMANO_APK / BYTES_MIB
    diferencia = (megabytes - mebibytes) / megabytes * PORCENTAJE
    print(fila("Bytes", f"{TAMANO_APK:>{ANCHO_VALOR}} B"))
    print(fila("En la tienda", f"{megabytes:>{ANCHO_VALOR}.2f} MB"))
    print(fila("En el móvil", f"{mebibytes:>{ANCHO_VALOR}.2f} MiB"))
    print(fila("Diferencia", f"{diferencia:>{ANCHO_VALOR}.1f} %"))


def opcion_3_ingresos() -> None:
    """Muestra las descargas y la informacion economica de tienda."""
    ingresos_brutos = DESCARGAS * PRECIO
    comision_tienda = ingresos_brutos * COMISION
    ingresos_netos = ingresos_brutos - COMISION
    print(fila("Descargas", f"{DESCARGAS:>{ANCHO_VALOR}} uds"))
    print(fila("Precio", f"{PRECIO:>{ANCHO_VALOR}.2f} €"))
    print(fila("Ingresos brutos", f"{ingresos_brutos:>{ANCHO_VALOR}.2f} €"))
    print(fila("Comisión tienda", f"{comision_tienda:>{ANCHO_VALOR}.2f} €"))
    print(fila("Ingresos netos", f"{ingresos_brutos:>{ANCHO_VALOR}.2f} €"))


def opcion_4_version() -> None:
    """Empaqueta la versión en un entero y la desempaqueta."""
    version = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    mayor_movido = VERSION_MAYOR << BITS_MAYOR
    menor_movido = VERSION_MENOR << BITS_MENOR
    version_code = mayor_movido | menor_movido | VERSION_PARCHE
    hexadecimal = f"0x{version_code:0{CIFRAS_HEX}X}"
    parche = version_code & MASCARA_8_BITS
    menor = (version_code >> BITS_MENOR) & MASCARA_8_BITS
    mayor = (version_code >> BITS_MAYOR) & MASCARA_8_BITS
    desempaquetado = f"{mayor}.{menor}.{parche}"
    print(fila("Version", version))
    print(fila("VersionCode", f"{version_code:>{ANCHO_VALOR}}"))
    print(fila("En hexadecimal", f"{hexadecimal:>{ANCHO_VALOR}}"))
    print(fila("Desempaquetado", desempaquetado))


def opcion_5_permisos() -> None:
    """Muestra los permisos de la app y cómo queda sin el de ubicación."""
    binario = f"{PERMISOS:0{CIFRAS_PERMISOS}b}"
    pide_internet = (PERMISOS & PERMISO_INTERNET) != 0
    pide_notif = (PERMISOS & PERMISO_NOTIFICACIONES) != 0
    pide_camara = (PERMISOS & PERMISO_CAMARA) != 0
    pide_ubicacion = (PERMISOS & PERMISO_UBICACION) != 0
    pide_contactos = (PERMISOS & PERMISO_CONTACTOS) != 0
    pide_micro = (PERMISOS & PERMISO_MICROFONO) != 0
    pide_almacen = (PERMISOS & PERMISO_ALMACENAMIENTO) != 0
    sin_ubicacion = PERMISOS & ~PERMISO_UBICACION
    binario_sin = f"{sin_ubicacion:0{CIFRAS_PERMISOS}b}"
    print(fila("En binario", f"{binario:>{ANCHO_VALOR}}"))
    print(fila("Internet", f"{pide_internet:>{ANCHO_VALOR}}"))
    print(fila("Notificaciones", f"{pide_notif:>{ANCHO_VALOR}}"))
    print(fila("Cámara", f"{pide_camara:>{ANCHO_VALOR}}"))
    print(fila("Ubicación", f"{pide_ubicacion:>{ANCHO_VALOR}}"))
    print(fila("Contactos", f"{pide_contactos:>{ANCHO_VALOR}}"))
    print(fila("Micrófono", f"{pide_micro:>{ANCHO_VALOR}}"))
    print(fila("Almacenamiento", f"{pide_almacen:>{ANCHO_VALOR}}"))
    print(fila("Sin ubicación", f"{binario_sin:>{ANCHO_VALOR}}"))


def opcion_6_color() -> None:
    """ Descompone el color ARGB del icono en canales y lo da en formato CSS """
    alfa = (COLOR_ICONO >> DESPLAZ_ALFA) & MASCARA_8_BITS
    rojo = (COLOR_ICONO >> DESPLAZ_ROJO) & MASCARA_8_BITS
    verde = (COLOR_ICONO >> DESPLAZ_VERDE) & MASCARA_8_BITS
    azul = COLOR_ICONO & MASCARA_8_BITS
    opacidad = alfa / OPACIDAD_MAXIMA *PORCENTAJE
    css = f"#{rojo:0{CIFRAS_CANAL}X}{verde:0{CIFRAS_CANAL}X}" \
        f"{azul:0{CIFRAS_CANAL}X}"
    print("COLOR DEL ICONO")
    print(fila("ARGB", f"0x{COLOR_ICONO:0{CIFRAS_ARGB}X}"))
    print(fila_canal("Rojo", rojo))
    print(fila_canal("Verde", verde))
    print(fila_canal("Azul", azul))
    print(fila("Opacidad", f"{opacidad:.{DECIMALES}f} %"))
    print(fila("Para CSS", css))


def opcion_7_tipos() -> None:
    """ Muestra el tipo y el valor de ocho datos con conversiones """
    media = valoracion_media() # int/int da de resultado un float
    pide_camara = (PERMISOS & PERMISO_CAMARA) != 0  #devuelve boleano
    texto_descargas = str(DESCARGAS)  
    ingresos_brutos = DESCARGAS * PRECIO
    codigo = ((VERSION_MAYOR << BITS_MAYOR) | (VERSION_MENOR << BITS_MENOR) | VERSION_PARCHE)   
    print("TIPOS DE DATOS")
    print(fila_tipo("NOMBRE", NOMBRE))
    print(fila_tipo("DESCARGAS", DESCARGAS))
    print(fila_tipo("PRECIO", PRECIO))
    print(fila_tipo("media", media))
    print(fila_tipo("pide_camara", pide_camara))
    print(fila_tipo("texto_descargas", texto_descargas))
    print(fila_tipo("ingresos_brutos", ingresos_brutos))
    print(fila_tipo("codigo", codigo))


def opcion_8_redondeo() -> None:
    """ Compara round() con el redondeo escolar (Decimal y ROUND_HALF_UP) """
    media = valoracion_media()
    exacta = Decimal(str(media))
    escolar_1 = redondeo_escolar(exacta, CUANTO_1_DEC)
    escolar_2 = redondeo_escolar(exacta, CUANTO_2_DEC)
    print("REDONDEO DE LA VALORACION MEDIA")
    print(fila("Valor exacto", str(media)))
    print(fila("Round(), 1 dec", str(round(media, DECIMALES))))
    print(fila("Escolar, 1 dec", str(escolar_1)))
    print(fila("round(), 2 dec", str(round(media, DECIMALES_EXTRA))))
    print(fila("Escolar, 2d dec", str(escolar_2)))


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
