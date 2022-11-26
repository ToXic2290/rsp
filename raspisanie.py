from .. import loader
import time

class raspisabie_Lib(loader.Library):
  developer = "@ToXicUse"
  version = (0, 0, 1)

  ponedelnik = f'''
☾☽ 𝙷𝚒𝚜𝚝𝚘𝚛𝚢 𝚘𝚏 𝙺𝚊𝚣𝚊𝚔𝚑𝚜𝚝𝚊𝚗
    ☞ {HisKz_dz} ☜

☾☽ 𝚁𝚞𝚜𝚜𝚒𝚊𝚗 𝚕𝚒𝚝𝚎𝚛𝚊𝚝𝚞𝚛𝚎
    ☞ {litra_dz} ☜

☾☽ 𝙰𝚕𝚐𝚎𝚋𝚛𝚊
    ☞ {algebra_dz} ☜

☾☽ 𝙱𝚒𝚘𝚕𝚘𝚐𝚢
    ☞ {biology_dz} ☜
'''

  vtornik = f"""
☾☽ 𝙴𝚗𝚐𝚕𝚒𝚜𝚑:
    ☞ {en_dz} ☜

☾☽ 𝙷𝚒𝚜𝚝𝚘𝚛𝚢 𝚘𝚏 𝙺𝚊𝚣𝚊𝚔𝚑𝚜𝚝𝚊𝚗
    ☞ {HisKz_dz} ☜

☾☽ 𝙶𝚎𝚘𝚐𝚛𝚊𝚙𝚑𝚢
    ☞ {geog_dz} ☜

☾☽ 𝙿𝚑𝚢𝚜𝚒𝚌𝚜
    ☞ {fizika_dz} ☜

☾☽ 𝙶𝚎𝚘𝚖𝚎𝚝𝚛𝚢
    ☞ {geom_dz} ☜

☾☽ 𝙺𝚊𝚣𝚊𝚔𝚑 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎
    ☞ {kz_dz} ☜
"""

  sreda = f"""
☾☽ 𝙴𝚗𝚐𝚕𝚒𝚜𝚑:
    ☞ {en_dz} ☜

☾☽ 𝙶𝚎𝚘𝚐𝚛𝚊𝚙𝚑𝚢
    ☞ {geog_dz} ☜

☾☽ 𝚁𝚞𝚜𝚜𝚒𝚊𝚗 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎
    ☞ {rus_dz} ☜

☾☽ 𝙲𝚑𝚎𝚖𝚎𝚜𝚝𝚛𝚢
    ☞ {himia_dz} ☜

☾☽ 𝙰𝚕𝚐𝚎𝚋𝚛𝚊
    ☞ {algebra_dz} ☜

☾☽ 𝙺𝚊𝚣𝚊𝚔𝚑 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎
    ☞ {kz_dz} ☜
"""

  chetverg = f"""
☾☽ 𝚁𝚞𝚜𝚜𝚒𝚊𝚗 𝚕𝚒𝚝𝚎𝚛𝚊𝚝𝚞𝚛𝚎
    ☞ {litra_dz} ☜

☾☽ 𝚆𝚘𝚛𝚕𝚍 𝚑𝚒𝚜𝚝𝚘𝚛𝚢
    ☞ {vsemirka_dz} ☜

☾☽ 𝙿𝚑𝚢𝚜𝚒𝚌𝚜
    ☞ {fizika_dz} ☜

☾☽ 𝙶𝚎𝚘𝚖𝚎𝚝𝚛𝚢
    ☞ {geom_dz} ☜

☾☽ 𝙺𝚊𝚣𝚊𝚔𝚑 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎
    ☞ {kz_dz} ☜
"""

  pytnica = f'''
☾☽ 𝙴𝚗𝚐𝚕𝚒𝚜𝚑:
    ☞ {en_dz} ☜

☾☽ 𝙲𝚑𝚎𝚖𝚎𝚜𝚝𝚛𝚢
    ☞ {himia_dz} ☜

☾☽ 𝙰𝚕𝚐𝚎𝚋𝚛𝚊
    ☞ {algebra_dz} ☜

☾☽ 𝙱𝚒𝚘𝚕𝚘𝚐𝚢
    ☞ {biology_dz} ☜

☾☽ 𝙺𝚊𝚣𝚊𝚔𝚑 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎
    ☞ {kz_dz} ☜

☾☽ 𝙻𝚊𝚠 𝚋𝚊𝚜𝚒𝚌𝚜
    ☞ {osnovi_dz} ☜
'''