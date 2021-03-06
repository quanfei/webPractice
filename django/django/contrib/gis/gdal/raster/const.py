"""
GDAL - Constant definitions
"""
from ctypes import (
    c_byte, c_double, c_float, c_int16, c_int32, c_uint16, c_uint32,
)

# See http://www.gdal.org/gdal_8h.html#a22e22ce0a55036a96f652765793fb7a4
GDAL_PIXEL_TYPES = {
    0: 'GDT_Unknown',  # Unknown or unspecified type
    1: 'GDT_Byte',  # Eight bit unsigned integer
    2: 'GDT_UInt16',  # Sixteen bit unsigned integer
    3: 'GDT_Int16',  # Sixteen bit signed integer
    4: 'GDT_UInt32',  # Thirty-two bit unsigned integer
    5: 'GDT_Int32',  # Thirty-two bit signed integer
    6: 'GDT_Float32',  # Thirty-two bit floating point
    7: 'GDT_Float64',  # Sixty-four bit floating point
    8: 'GDT_CInt16',  # Complex Int16
    9: 'GDT_CInt32',  # Complex Int32
    10: 'GDT_CFloat32',  # Complex Float32
    11: 'GDT_CFloat64',  # Complex Float64
}

# Lookup values to convert GDAL pixel type indices into ctypes objects.
# The GDAL band-io works with ctypes arrays to hold data to be written
# or to hold the space for data to be read into. The lookup below helps
# selecting the right ctypes object for a given gdal pixel type.
GDAL_TO_CTYPES = [
    None, c_byte, c_uint16, c_int16, c_uint32, c_int32,
    c_float, c_double, None, None, None, None
]
