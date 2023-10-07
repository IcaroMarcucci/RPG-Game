#SETUP
WIDTH = 1280
HEIGHT = 720
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

#Magic
magic_data = {
    'flame': {'stregth': 5, 'cost': 20, 'graphic': 'graphics/particles/flame/fire.png'},
    'heal': {'stregth': 20, 'cost': 10, 'graphic': 'graphics/particles/heal/heal.png'},
}

#Enemy
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': 'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': 'audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': 'audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': 'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},
}