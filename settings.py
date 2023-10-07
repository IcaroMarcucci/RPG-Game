#SETUP
WIDTH = 1600
HEIGHT = 950
FPS = 60
TILESIZE = 64

#UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 150
ITEM_BOX_SIZE = 80
UI_FONT = 'graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

#GENERAL COLORS
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
UI_BORDER_COLOR_ACTIVE = 'gold'
TEXT_COLOR = '#EEEEEE'

#BAR COLORS
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'

#WEAPONS
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': 'graphics/weapons/sword/full.png'}, #DPS - 0,150
    'lance': {'cooldown': 400, 'damage': 45, 'graphic': 'graphics/weapons/lance/full.png'}, #DPS - 0,112
    'axe': {'cooldown': 300, 'damage': 25, 'graphic': 'graphics/weapons/axe/full.png'},     #DPS - 0,116
    'rapier': {'cooldown': 50, 'damage': 7, 'graphic': 'graphics/weapons/rapier/full.png'}, #DPS - 0,140
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': 'graphics/weapons/sai/full.png'}       #DPS - 0,125
}