from .ToontownGlobals import *
import math
from . import TTLocalizer
BattleCamFaceOffFov = 30.0
BattleCamFaceOffPos = Point3(0, -10, 4)
BattleCamDefaultPos = Point3(0, -8.6, 16.5)
BattleCamDefaultHpr = Vec3(0, -61, 0)
BattleCamDefaultFov = 80.0
BattleCamMenuFov = 65.0
BattleCamJoinPos = Point3(0, -12, 13)
BattleCamJoinHpr = Vec3(0, -45, 0)
SkipMovie = 0
BaseHp = 15
Tracks = TTLocalizer.BattleGlobalTracks
NPCTracks = TTLocalizer.BattleGlobalNPCTracks
TrackColors = (
 (211 / 255.0, 148 / 255.0, 255 / 255.0),
 (249 / 255.0, 255 / 255.0, 93 / 255.0),
 (79 / 255.0, 190 / 255.0, 76 / 255.0),
 (255 / 255.0, 145 / 255.0, 66 / 255.0),
 (222 / 255.0, 255 / 255.0, 245 / 255.0),
 (245 / 255.0, 86 / 255.0, 86 / 255.0),
 (255 / 255.0, 65 / 255.0, 199 / 255.0),
 (93 / 255.0, 108 / 255.0, 239 / 255.0),
 (67 / 255.0, 243 / 255.0, 255 / 255.0)
)
HEAL_TRACK = 0
TRAP_TRACK = 1
LURE_TRACK = 2
THROW_TRACK = 3
BOUNCE_TRACK = 4
BURN_TRACK = 5
SQUIRT_TRACK = 6
SOUND_TRACK = 7
DROP_TRACK = 8
NPC_RESTOCK_GAGS = 9
NPC_TOONS_HIT = 10
NPC_COGS_MISS = 11
MIN_TRACK_INDEX = 0
MAX_TRACK_INDEX = 8
MIN_LEVEL_INDEX = 0
MAX_LEVEL_INDEX = 7
MAX_UNPAID_LEVEL_INDEX = 4
NUM_GAG_TRACKS = 9
AvLureRounds = (2, 2, 3, 3, 4, 4, 5, 6)
PropTypeToTrackBonus = {AnimPropTypes.Hydrant: SQUIRT_TRACK,
 AnimPropTypes.Mailbox: THROW_TRACK,
 AnimPropTypes.Trashcan: HEAL_TRACK}
TRACK_XP_LADDER = [0, 20, 100, 500, 2000, 5000, 10000, 20000]
Levels = [list(TRACK_XP_LADDER) for _ in range(NUM_GAG_TRACKS)]
MaxSkill = 20000
UnpaidMaxSkills = [Levels[track][1] - 1 for track in range(NUM_GAG_TRACKS)]
ExperienceCap = 500

def gagIsPaidOnly(track, level):
    return Levels[track][level] > UnpaidMaxSkills[track]


def gagIsVelvetRoped(track, level):
    if level > 0:
        if track in [4, 5]:
            if level > 3:
                return True
        else:
            return True
    return False


MaxToonAcc = 95
StartingLevel = 0
CARRY_LIMIT_PROGRESSION = (
 (10, 0, 0, 0, 0, 0, 0, 0),
 (10, 5, 0, 0, 0, 0, 0, 0),
 (15, 10, 5, 0, 0, 0, 0, 0),
 (20, 15, 10, 5, 0, 0, 0, 0),
 (25, 20, 15, 10, 3, 0, 0, 0),
 (30, 25, 20, 15, 7, 3, 0, 0),
 (30, 25, 20, 15, 7, 3, 1, 0),
 (30, 25, 20, 15, 7, 3, 2, 1)
)
CarryLimits =  tuple(CARRY_LIMIT_PROGRESSION for _ in range(NUM_GAG_TRACKS))
MaxProps = ((15, 40), (30, 60), (75, 80))
DLF_SKELECOG = 1
DLF_FOREMAN = 2
DLF_VP = 4
DLF_CFO = 8
DLF_SUPERVISOR = 16
DLF_VIRTUAL = 32
DLF_REVIVES = 64
pieNames = ['tart',
 'fruitpie-slice',
 'creampie-slice',
 'fruitpie',
 'creampie',
 'cheesecake',
 'birthday-cake',
 'wedding-cake',
 'lawbook']
AvProps = (
    ['feather', 'megaphone', 'lipstick', 'bamboo', 'pixie', 'juggle', 'tickle', 'dive'],
    ['banana', 'rake', 'mouse-trap', 'marbles', 'quicksand', 'trapdoor', 'portable-hole', 'tnt'],
    ['1dollar', 'small-magnet', '5dollar', 'big-magnet', '10dollar', 'hypno', 'paycheck', 'presentation'],
    ['tart', 'fruitpie-slice', 'creampie-slice', 'fruitpie', 'creampie', 'cheesecake', 'birthday-cake', 'wedding-cake'],
    ['rubber-band', 'pingpong', 'slinky', 'superball', 'jackbox', 'moon-boots', 'pogo', 'trampoline'],
    ['matchstick', 'hot-sauce', 'candle', 'sparkler', 'marshmallow', 'pepper-spray', 'ghost-pepper', 'body-spray'],
    ['squirt-flower', 'water-glass', 'squirtgun', 'balloon', 'seltzer', 'hose', 'cloud', 'geyser'],
    ['bike-horn', 'recorder', 'whistle', 'bugle', 'aoogah', 'elephant', 'foghorn', 'opera'],
    ['flower-pot', 'paint-can', 'sandbag', 'anvil', 'ton', 'safe', 'statue', 'piano']
)
AvPropsNew = (
    ['inventory_feather', 'inventory_megaphone', 'inventory_lipstick', 'inventory_bamboo_cane', 'inventory_pixiedust', 'inventory_juggling_cubes', 'inventory_', 'inventory_ladder'],
    ['inventory_bannana_peel', 'inventory_rake', 'inventory_', 'inventory_marbles', 'inventory_quicksand_icon', 'inventory_trapdoor', 'inventory_', 'inventory_tnt'],
    ['inventory_1dollarbill', 'inventory_small_magnet', 'inventory_5dollarbill', 'inventory_big_magnet', 'inventory_10dollarbill', 'inventory_hypno_goggles', 'inventory_', 'inventory_screen'],
    ['inventory_tart', 'inventory_fruit_pie_slice', 'inventory_cream_pie_slice', 'inventory_fruitpie', 'inventory_creampie', 'inventory_', 'inventory_cake', 'inventory_wedding'],
    ['inventory_', 'inventory_', 'inventory_', 'inventory_', 'inventory_', 'inventory_', 'inventory_', 'inventory_'],
    ['inventory_', 'inventory_', 'inventory_', 'inventory_', 'inventory_', 'inventory_', 'inventory_', 'inventory_'],
    ['inventory_squirt_flower', 'inventory_glass_of_water', 'inventory_water_gun', 'inventory_', 'inventory_seltzer_bottle', 'inventory_firehose', 'inventory_storm_cloud', 'inventory_geyser'],
    ['inventory_bikehorn', 'inventory_', 'inventory_whistle', 'inventory_bugle', 'inventory_aoogah', 'inventory_elephant', 'inventory_fog_horn', 'inventory_opera_singer'],
    ['inventory_flower_pot', 'inventory_', 'inventory_sandbag', 'inventory_anvil', 'inventory_weight', 'inventory_safe_box', 'inventory_', 'inventory_piano']
)
AvPropStrings = TTLocalizer.BattleGlobalAvPropStrings
AvPropStringsSingular = TTLocalizer.BattleGlobalAvPropStringsSingular
AvPropStringsPlural = TTLocalizer.BattleGlobalAvPropStringsPlural

ACCURACY_VALUES = {
    HEAL_TRACK: [100, 100, 100, 100, 100, 100, 100, 100],
    TRAP_TRACK: [0, 0, 0, 0, 0, 0, 0, 0],
    LURE_TRACK: [75, 70, 80, 75, 85, 80, 90, 85],
    THROW_TRACK: [75, 75, 75, 75, 75, 75, 75, 75],
    BOUNCE_TRACK: [95, 95, 95, 95, 95, 95, 95, 95],
    BURN_TRACK: [80, 80, 80, 80, 80, 80, 80, 80],
    SQUIRT_TRACK: [95, 95, 95, 95, 95, 95, 95, 95],
    SOUND_TRACK: [95, 95, 95, 95, 95, 95, 95, 95],
    DROP_TRACK: [60, 60, 60, 60, 60, 60, 60, 60]
}
AvPropAccuracy = tuple(tuple(ACCURACY_VALUES[track]) for track in range(NUM_GAG_TRACKS))
AvLureBonusAccuracy = (100, 100, 100, 100, 100, 100, 100, 100)
AvTrackAccStrings = TTLocalizer.BattleGlobalAvTrackAccStrings

DAMAGE_STEPS = {
    HEAL_TRACK: [(8,10), (15,18), (25,30), (39,45), (55,65), (78,90), (100,100), (135,135)],
    TRAP_TRACK: [(10,13), (19,26), (40,48), (56,75), (90,132), (156,185), (240,240), (310,310)],
    LURE_TRACK: [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
    THROW_TRACK: [(6,8), (10,12), (18,21), (32,38), (50,58), (80,95), (145,145), (195,195)],
    BOUNCE_TRACK: [(4,6), (6,8), (10,12), (20,23), (38,42), (60,75), (100,100), (140,140)],
    BURN_TRACK: [(5,7), (8,10), (14,17), (26,30), (42,48), (72,88), (140,140), (180,180)],
    SQUIRT_TRACK: [(3,5), (6,8), (12,14), (19,22), (26,30), (45,60), (90,90), (125,125)],
    SOUND_TRACK: [(3,4), (5,6), (8,10), (14,16), (28,30), (35,50), (75,75), (100,100)],
    DROP_TRACK: [(10,12), (15,20), (35,44), (52,65), (85,110), (130,160), (210,210), (280,280)]
}
AvPropDamage = []
for track in range(NUM_GAG_TRACKS):
    track_damage = []
    for level in range(MAX_LEVEL_INDEX + 1):
        min_e = Levels[track][level]
        max_e = Levels[track][level + 1] - 1 if level < MAX_LEVEL_INDEX else MaxSkill
        damage_pair = DAMAGE_STEPS[track][level]
        track_damage.append((damage_pair, (min_e, max_e)))
    track_damage = tuple(track_damage)
    AvPropDamage.append(track_damage)
AvPropDamage = tuple(AvPropDamage)

ATK_SINGLE_TARGET = 0
ATK_GROUP_TARGET = 1
SINGLE_TARGET_TRACK = (ATK_SINGLE_TARGET,) * (MAX_LEVEL_INDEX + 1)
GROUP_TARGET_TRACK = (ATK_GROUP_TARGET,) * (MAX_LEVEL_INDEX + 1)
ALTERNATING_TARGET_TRACK = tuple(
    ATK_GROUP_TARGET if level % 2 != 0 else ATK_SINGLE_TARGET
    for level in range(MAX_LEVEL_INDEX + 1)
)
AvPropTargetCat = (
    ALTERNATING_TARGET_TRACK,
    SINGLE_TARGET_TRACK,
    ALTERNATING_TARGET_TRACK,
    SINGLE_TARGET_TRACK,
    SINGLE_TARGET_TRACK,
    SINGLE_TARGET_TRACK,
    SINGLE_TARGET_TRACK,
    GROUP_TARGET_TRACK,
    SINGLE_TARGET_TRACK,
)
AvPropTarget = tuple(range(NUM_GAG_TRACKS))

def getAvPropDamage(attackTrack, attackLevel, exp, organicBonus = False, propBonus = False, propAndOrganicBonusStack = False):
    minD = AvPropDamage[attackTrack][attackLevel][0][0]
    maxD = AvPropDamage[attackTrack][attackLevel][0][1]
    minE = AvPropDamage[attackTrack][attackLevel][1][0]
    maxE = AvPropDamage[attackTrack][attackLevel][1][1]
    expVal = min(exp, maxE)
    expPerHp = float(maxE - minE + 1) / float(maxD - minD + 1)
    damage = math.floor((expVal - minE) / expPerHp) + minD
    if damage <= 0:
        damage = minD
    if propAndOrganicBonusStack:
        originalDamage = damage
        if organicBonus:
            damage += getDamageBonus(originalDamage)
        if propBonus:
            damage += getDamageBonus(originalDamage)
    elif organicBonus or propBonus:
        damage += getDamageBonus(damage)
    return damage


def getDamageBonus(normal):
    bonus = int(normal * 0.1)
    if bonus < 1 and normal > 0:
        bonus = 1
    return bonus


def isGroup(track, level):
    return AvPropTargetCat[AvPropTarget[track]][level]


def getCreditMultiplier(floorIndex):
    return 1 + floorIndex * 0.5


def getFactoryCreditMultiplier(factoryId):
    return 2.0


def getFactoryMeritMultiplier(factoryId):
    return 4.0


def getMintCreditMultiplier(mintId):
    return {CashbotMintIntA: 2.0,
     CashbotMintIntB: 2.5,
     CashbotMintIntC: 3.0}.get(mintId, 1.0)


def getStageCreditMultiplier(floor):
    return getCreditMultiplier(floor)


def getCountryClubCreditMultiplier(countryClubId):
    return {BossbotCountryClubIntA: 2.0,
     BossbotCountryClubIntB: 2.5,
     BossbotCountryClubIntC: 3.0}.get(countryClubId, 1.0)


def getBossBattleCreditMultiplier(battleNumber):
    return 1 + battleNumber


def getInvasionMultiplier():
    return 2.0


def getMoreXpHolidayMultiplier():
    return 2.0