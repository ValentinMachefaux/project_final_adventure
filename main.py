from Character import *
from Monster import *

C=Character(json_class("Lancer"))
M=Monster(json_monster("4"))

# Test character
"""
print(

    C.get_accuracy(),
    C.get_attack(),
    C.get_hp(),
    C.get_defense(),
    C.get_exp(),
    C.get_level(),
    C.get_mp(),
    C.get_resitance_dark(),
    C.get_resitance_earth(),
    C.get_resitance_fire(),
    C.get_resitance_light(),
    C.get_resitance_thunder(),
    C.get_resitance_water(),
    C.get_resitance_wind(),
    C.get_speed(),
    )
print(
    C.get_ultimate().get_name(),
    "\n",
    C.get_ultimate().get_detail(),
    "\n",
    C.get_ultimate().get_rp(),
    "\n",
    C.get_ultimate().get_element(),
    "\n",
    C.get_ultimate().get_is_aoe(),
    "\n",
    C.get_ultimate().get_skill_type(),
    "\n",
    C.get_ultimate().get_value(),
    )
"""

# Test monster
"""
print(
    M.get_name(),
    "\n",
    M.get_hp(),
    "\n",
    M.get_attack(),
    "\n",
    M.get_defense(),
    "\n",
    M.get_spd(),
    "\n",
    M.get_accuracy(),
    "\n",
    M.get_weakness(),
    "\n",
    M.get_resistance(),
    "\n",
    M.get_skill_1().get_name(),
    M.get_skill_1().get_value(),
    "\n",
    M.get_detail(),
    "\n",
    M.get_loot1().get_name(),
    M.get_loot1().get_quantity(),
    M.get_loot1().get_rate(),
    "\n",
    M.get_exp(),
    "\n",
    M.get_gold(),
    )
"""
