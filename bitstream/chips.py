#!/usr/bin/python
#
# Copyright 2019 Steve White
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.
#

chips = []

from tiles import TileNamed

class Chip:
    name = None
    device_id = 0
    rows = 0
    columns = 0
    floorplan = []
    aliases = {}
    packages = {}
    
    def __init__(self, name, device_id, rows, columns, floorplan, aliases, packages):
        global chips
        self.name = name
        self.device_id = device_id
        self.rows = rows
        self.columns = columns
        self.floorplan = floorplan
        self.aliases = aliases
        self.packages = packages
        chips.append(self)
        
    def tile_at(self, x, y): 
        index = (y * self.columns) + x
        alias = self.floorplan[index]
        if alias is None:
            return None
        name = self.aliases[alias]
        return TileNamed(name)

    def column_width(self, column):
        size = 0
        for row in range(0, self.rows):
            tile = self.tile_at(column, row)
            if tile is not None:
                size = max(size, tile.columns)
        return size

    def max_row_height(self, row):
        result = 0
        for column in range(0, self.columns):
            tile = self.tile_at(column, row)
            if tile is not None:
                result = max(result, tile.rows)
        return result

    def max_row_width(self):
        result = 0
        for column in range(0, self.columns):
            result = result + self.column_width(column)
        return result

def ChipNamed(name):
    for chip in chips:
        if chip.name == name:
            return chip
    return None
    
def ChipWithID(id):
    for chip in chips:
        if chip.device_id == id:
            return chip
    return None

Chip('AG1KLP', 0x00120010, 10, 14, [
	None,     None,     None,     None,    None,     None,     None,     None,     None,       'IOS2',   None,    'IOS3',   'IOS3',   None,
	'IOS0',   'IOS0',   'IOS0',   None,    'IOS1',   'IOS1',   'IOS1',   'IOS1',   'BOOT_PLL', 'LOGIC0', 'BRAM1', 'LOGIC0', 'LOGIC0', 'ROGIC0',
	'LOGIC0', 'LOGIC0', 'LOGIC0', 'BRAM0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0',   'LOGIC0', 'BRAM1', 'LOGIC0', 'LOGIC0', 'ROGIC0',
	'LOGIC0', 'LOGIC0', 'LOGIC0', 'BRAM0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0',   'LOGIC0', 'BRAM1', 'LOGIC0', 'LOGIC0', 'ROGIC0',
	'LOGIC0', 'LOGIC0', 'LOGIC0', 'BRAM0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0',   'LOGIC0', 'BRAM1', 'LOGIC0', 'LOGIC0', 'ROGIC0',
	'LOGIC0', 'LOGIC0', 'LOGIC0', 'BRAM0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0',   'LOGIC0', 'BRAM1', 'LOGIC0', 'LOGIC0', 'ROGIC0',
	'LOGIC0', 'LOGIC0', 'LOGIC0', 'BRAM0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0',   'LOGIC0', 'BRAM1', 'LOGIC0', 'LOGIC0', 'ROGIC0',
	'LOGIC0', 'LOGIC0', 'LOGIC0', 'BRAM0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0',   'LOGIC0', 'BRAM1', 'LOGIC0', 'LOGIC0', 'ROGIC0',
	'LOGIC0', 'LOGIC0', 'LOGIC0', 'BRAM0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0', 'LOGIC0',   'LOGIC0', 'BRAM1', 'LOGIC0', 'LOGIC0', 'ROGIC0',
	'ION0',   'ION0',   'ION0',   None,    'ION1',   'ION1',   'ION1',   'ION1',   'ION1',     'ION1',   None,    'ION2',   'ION2',   None,
], {
	'BOOT_PLL': 'AG1200_IOTILE_BOOT_PLL',
	'LOGIC0':   'ALTA_TILE_SRAM_DIST',
	'ROGIC0':   'IOTILE_ROUTE',
	'BRAM0':    'ALTA_EMB4K5',
	'BRAM1':    'ALTA_EMB4K5',
	'IOS0':     'AG1200_IOTILE_S4',
	'IOS1':     'AG1200_IOTILE_S4_G1',
	'IOS2':     'AG1200_IOTILE_S4',
	'IOS3':     'AG1200_IOTILE_S4',
	'ION0':     'AG1200_IOTILE_N4',
	'ION1':     'AG1200_IOTILE_N4_G1',
	'ION2':     'AG1200_IOTILE_N4',
}, {
    'QFN48': [
        { 'name': 'PIN_1',    'type': 'IO', 'tile': (2,9),  'index': 0},
        { 'name': 'PIN_2',    'type': 'IO', 'tile': (1,9),  'index': 3},
        { 'name': 'PIN_3',    'type': 'IO', 'tile': (0,9),  'index': 2},
        { 'name': 'PIN_4',    'type': 'IO', 'tile': (0,9),  'index': 0},
        { 'name': 'PIN_5',    'type': 'IO', 'tile': (1,9),  'index': 1},
        { 'name': 'PIN_6',    'type': 'IO', 'tile': (6,9),  'index': 2},
        { 'name': 'VDDC',     'type': 'POWER'},
        { 'name': 'GND',      'type': 'POWER'},
        { 'name': 'PIN_9',    'type': 'IO', 'tile': (7,1),  'index': 0},
        { 'name': 'VDDC',     'type': 'POWER'},
        { 'name': 'PIN_11',   'type': 'IO', 'tile': (2,1),  'index': 2},
        { 'name': 'PIN_12',   'type': 'IO', 'tile': (2,1),  'index': 0},
        { 'name': 'PIN_13',   'type': 'IO', 'tile': (4,1),  'index': 2},
        { 'name': 'PIN_14',   'type': 'IO', 'tile': (4,1),  'index': 0},
        { 'name': 'PIN_15',   'type': 'IO', 'tile': (5,1),  'index': 0},
        { 'name': 'PIN_16',   'type': 'IO', 'tile': (5,1),  'index': 1},
        { 'name': 'PIN_17',   'type': 'IO', 'tile': (5,1),  'index': 2},
        { 'name': 'PIN_18',   'type': 'IO', 'tile': (5,1),  'index': 3},
        { 'name': 'PIN_19',   'type': 'IO', 'tile': (6,1),  'index': 0},
        { 'name': 'PIN_20',   'type': 'IO', 'tile': (6,1),  'index': 1},
        { 'name': 'VDDIO2',   'type': 'POWER'},
        { 'name': 'PIN_22',   'type': 'IO', 'tile': (6,1),  'index': 2},
        { 'name': 'PIN_23',   'type': 'IO', 'tile': (6,1),  'index': 3},
        { 'name': 'CDONE',    'type': 'CONFIG'},
        { 'name': 'PIN_25',   'type': 'IO', 'tile': (9,0),  'index': 1},
        { 'name': 'PIN_26',   'type': 'IO', 'tile': (9,0),  'index': 3},
        { 'name': 'PIN_27',   'type': 'IO', 'tile': (11,0), 'index': 1},
        { 'name': 'VDDSPI',   'type': 'POWER'},
        { 'name': 'PIN_29',   'type': 'IO', 'tile': (12,0), 'index': 0},
        { 'name': 'CRESET_B', 'type': 'CONFIG'},
        { 'name': 'PIN_31',   'type': 'IO', 'tile': (12,0), 'index': 2},
        { 'name': 'PIN_32',   'type': 'IO', 'tile': (11,0), 'index': 3},
        { 'name': 'PIN_33',   'type': 'IO', 'tile': (8,9),  'index': 0},
        { 'name': 'PIN_34',   'type': 'IO', 'tile': (11,9), 'index': 1},
        { 'name': 'PIN_35',   'type': 'IO', 'tile': (9,9),  'index': 3},
        { 'name': 'PIN_36',   'type': 'IO', 'tile': (9,9),  'index': 1},
        { 'name': 'PIN_37',   'type': 'IO', 'tile': (8,9),  'index': 3},
        { 'name': 'PIN_38',   'type': 'IO', 'tile': (7,9),  'index': 3},
        { 'name': 'PIN_39',   'type': 'IO', 'tile': (7,9),  'index': 0},
        { 'name': 'PIN_40',   'type': 'IO', 'tile': (6,9),  'index': 0},
        { 'name': 'PIN_41',   'type': 'IO', 'tile': (5,9),  'index': 3},
        { 'name': 'PIN_42',   'type': 'IO', 'tile': (5,9),  'index': 2},
        { 'name': 'PIN_43',   'type': 'IO', 'tile': (5,9),  'index': 1},
        { 'name': 'PIN_44',   'type': 'IO', 'tile': (5,9),  'index': 0},
        { 'name': 'PIN_45',   'type': 'IO', 'tile': (4,9),  'index': 2},
        { 'name': 'PIN_46',   'type': 'IO', 'tile': (4,9),  'index': 0},
        { 'name': 'VDDIO',    'type': 'POWER' },
        { 'name': 'PIN_48',   'type': 'IO', 'tile': (2,9),  'index': 2},
    ]
})