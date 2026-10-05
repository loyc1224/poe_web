#===============================================================================================================

# NeverSink's Indepth Loot Filter - for Path of Exile

#===============================================================================================================

# VERSION:  8.20.1e.2026.256.23

# TYPE:     3-STRICT

# STYLE:    DEFAULT

# AUTHOR:   NeverSink

# BUILDNOTES: Filter generated with NeverSink's FilterpolishZ and the domainlanguage Exo.

#------------------------------------

# LINKS TO LATEST VERSION AND FILTER EDITOR

#------------------------------------

# CUSTOMIZE THE POE 1 FILTER ON: 	https://www.FilterBlade.xyz?game=Poe1

# GET THE LATEST VERSION ON: 	    https://www.FilterBlade.xyz or https://github.com/NeverSinkDev/NeverSink-Filter

#------------------------------------

# INSTALLATION / UPDATE :

#------------------------------------

# 0) It's recommended to check for updates once a month or at least before new leagues, to receive economy finetuning and new features!

# 1) Paste this file into the following folder: %userprofile%/Documents/My Games/Path of Exile

# 2) INGAME: Escape -> Options -> UI -> Scroll down -> Select the filter from the Dropdown box

#------------------------------------

# AUTO-UPDATER SERVICE AND SUPPORT THE DEVELOPMENT

#------------------------------------

# Patreon supporters get access to the FilterBlade Auto-Updater that combines 100% automated updates with custom styles and your customizations!

# It's a great way to support us and get something in return and it helps us on our journey of making our own company and potentially game. Thank you

# Learn more about the itemfilter-autoupdate feature here: https://www.youtube.com/watch?v=i8RJx0s0zsA

# PATREON:               		https://www.patreon.com/Neversink

# OTHER:                        https://www.filterblade.xyz/About

#------------------------------------

# CONTACT - if you want to get notifications about updates or just get in touch:

#------------------------------------

# For feedback, questions and suggestions please join our discord!

# DISCORD: https://discord.gg/zFEx92a

# TWITTER: @NeverSinkDev

# TWITCH:  https://www.twitch.tv/neversink

# BSKY:    @neversink.bsky.social

# FORUM:   https://goo.gl/oQn4EN

#===============================================================================================================

# [WELCOME] TABLE OF CONTENTS + QUICKJUMP TABLE

#===============================================================================================================

# [[0100]] OVERRIDE AREA 1 - Override ALL rules here

# [[0100]] Global overriding rules

# [[0200]] Gold

# [[0300]] Influenced Items

# [0301] Influenced Maps

# [0302] Influenced Gear

# [[0400]] ELDRITCH ITEMS

# [[0500]] Exotic Bases

# [[0600]] IDENTIFIED MOD FILTERING - COMBINATIONS

# [0601] Physical

# [0602] Elemental

# [0603] Blade Blast Daggers

# [0604] Gembased

# [0605] Caster

# [0606] Spellslinger

# [0607] Helmets

# [0608] Boots

# [0609] Gloves

# [0610] Shields

# [0611] Amulets

# [0612] Rings

# [0613] Quivers

# [0614] Body Armours

# [0615] Belts

# [0616] Jewels

# [0617] ID Mod exceptions - override id mod matching section

# [[0700]] IDENTIFIED MOD FILTERING - DUAL MODS

# [[0800]] IDENTIFIED MOD FILTERING - SINGLE MODS

# [0801] Top Value

# [0802] Uncorrupted Mods

# [0803] Flasks and Tinctures

# [[0900]] High Priority Equipment Properties

# [0901] Perfection and Overquality Filtering

# [0902] Memory Strand Gear

# [[1000]] IDENTIFIED MOD - CORRUPTED ITEMS

# [[1100]] Exotic Mods Filtering

# [1101] Veiled/Betrayal - low prio veiled items

# [1102] Incursion/Temple Mods

# [1103] Necropolis

# [1104] Bestiary

# [1105] Other

# [[1200]] Exotic Item Classes

# [1201] Relics

# [[1300]] Exotic Item Variations

# [1301] Double and Single Corruptions

# [1302] Abyss Jeweled Rares

# [1303] Fractured

# [1304] Enchanted

# [1305] Crucible

# [[1400]] Recipes and 5links

# [1401] Link Based

# [[1500]] High Level Crafting Bases

# [1501] Expensive Atlas 86 Bases - matched by economy

# [[1600]] Endgame - Rare - Gear

# [[1700]] Endgame - Rare - Decorators

# [[1800]] Endgame - Rare - Exotic Veiled

# [[1900]] Endgame - Rare - Exotic Corrupted

# [[2000]] Endgame - Rare - Conditional Hide Rules

# [[2100]] Endgame - Rare - Amulets, Rings, Boots

# [[2200]] Endgame - Rare - Gear - Droplevel Hiding

# [2201] Endgame - Rare - Gear

# [[2300]] Endgame - Crafting

# [2301] Early Endgame Crafting projects

# [2302] Crafting Matrix

# [[2400]] Chancing Bases

# [[2500]] Endgame Flasks & Tinctures

# [2501] Endgame Flasks

# [2502] Quality High

# [2503] Quality Low

# [2504] Utility flasks

# [2505] Early mapping life/mana/utility flasks

# [[2600]] Misc Rules

# [2601] RGB Endgame

# [2602] Remaining Rares

# [[2700]] Hide Layer 1 - Rare & Magic Gear

# [[2800]] Jewels

# [2801] Special Cases

# [2802] Leveling Exceptions

# [2803] Abyss Jewels

# [2804] Generic Jewels

# [2805] Cluster Jewels: Eco-Based-Large

# [2806] Cluster Jewels: Random

# [[2900]] Heist Gear

# [2901] Heist Cloak

# [2902] Heist Brooch

# [2903] Heist Gear

# [2904] Heist Tool

# [[3000]] Gem Tierlists

# [3001] Exceptional Gems - Awakened and AltQuality

# [3002] Economy based leveled, quality and vaal gem rules

# [3003] High Quality and Leveled Gems

# [[3100]] REPLICA AND FOULBORN UNIQUES

# [[3200]] Special Maps

# [3201] Unique Maps

# [3202] SpecialMaps

# [3203] Blighted maps

# [3204] Special Maps

# [[3300]] Normal Map Progression

# [3301] Generic Decorators

# [3302] Map progression

# [[3400]] Pseudo-Map-Items

# [[3500]] Misc Map Items

# [[3600]] Fragments

# [3601] Scarabs

# [3602] Regular Fragment Tiering

# [[3700]] Currency - Special

# [[3800]] Currency - Leveling Exceptions

# [[3900]] Currency - Exceptions - Stacked Currency

# [3901] Supplies: High Stacking

# [3902] Supplies: Low Stacking

# [3903] Supplies: Portal Stacking

# [3904] Supplies: Wisdom Stacking

# [3905] Stacked Currencies: 6x

# [3906] Stacked Currencies: 3x

# [3907] Heist Coins

# [[4000]] Currency - Regular Currency Tiering

# [[4100]] Currency - SPECIAL

# [4101] Incursion - Vials

# [4102] Delirum Orbs

# [4103] Delve - Fossils and Resonators

# [4104] Allflame - Ducats

# [4105] Blight - Oils

# [4106] Runes

# [4107] Corpses

# [4108] Essences

# [4109] Ritual

# [4110] Trial of the Ancestors

# [4111] Currency with a state - scrying orbs, lens, imprints

# [4112] Wombgifts

# [[4200]] Currency - Splinters

# [4201] Breach and Legion Splinters - stacked

# [4202] Breach and Legion Splinters - single

# [4203] Simulacrum Splinters

# [[4300]] Divination Cards

# [[4400]] Remaining Currency

# [[4500]] Questlike-Items1 (override uniques)

# [[4600]] Enshrouded Items

# [[4700]] Idols (Event Leagues Only)

# [[4800]] Uniques

# [4801] Exceptions #1

# [4802] Tier 1 and 2 uniques

# [4803] Exceptions #2

# [4804] Multi-Unique bases.

# [4805] Low tier exceptions

# [4806] Tier 3 uniques

# [4807] Tier 4 uniques

# [[4900]] Questlike-Items2

# [[5000]] Hide outdated leveling flasks

# [[5100]] Leveling - Utility Flasks and Tinctures

# [[5200]] Leveling - Life, Mana, Hybrid

# [5201] Hybrid Flasks

# [5202] Life flasks

# [5203] Mana flasks

# [[5300]] Leveling - Rules

# [5301] Links and Sockets

# [5302] Rares - Exotics

# [5303] Rares - Decorators

# [5304] Rares - Universal

# [5305] Rares - Caster

# [5306] Rares - Archer

# [5307] Rares - Melee

# [5308] Rares - Other

# [[5400]] Leveling - Useful magic and normal items

# [5401] Purpose Picked Items

# [5402] Normals

# [5403] Weapon Progression

# [5404] Attack Wand Progression

# [5405] Remaining Magics

# [5406] Hide All known Section

# [5407] Show All unknown Section

#===============================================================================================================

# [[0100]] Global overriding rules

#===============================================================================================================

# !! Waypoint c0.alpha : "All Rules - Highest priority - DANGER ZONE" : "Recipes and Linked Gear"

Show # %D8 $type->6l $tier->hightier
	Mirrored False
	Corrupted False
	LinkedSockets 6
	ItemLevel >= 75
	Rarity Normal Magic Rare
	BaseType == "Apex Cleaver" "Arcane Vestment" "Assassin's Garb" "Astral Leather" "Banishing Blade" "Battery Staff" "Carnal Armour" "Conquest Lamellar" "Despot Axe" "Destiny Leather" "Eventuality Rod" "Exquisite Leather" "Full Dragonscale" "Full Wyvernscale" "General's Brigandine" "Gladiator Plate" "Glorious Plate" "Grand Ringmail" "Grove Bow" "Harbinger Bow" "Impact Force Propagator" "Imperial Bow" "Ivory Bow" "Legion Plate" "Maraketh Bow" "Marshall's Brigandine" "Necrotic Armour" "Nightweave Robe" "Paladin's Hauberk" "Royal Plate" "Sacred Chainmail" "Sadist Garb" "Saint's Hauberk" "Saintly Chainmail" "Sanguine Raiment" "Short Bow" "Solarine Bow" "Spine Bow" "Supreme Leather" "Syndicate's Garb" "Thicket Bow" "Titan Plate" "Torturer Garb" "Triumphant Lamellar" "Twilight Regalia" "Vaal Regalia" "Zodiac Leather"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 200 0 0 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

Show # %D5 $type->6l $tier->others
	LinkedSockets 6
	Rarity Normal Magic Rare
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 200 0 0 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 1 Red Diamond

#===============================================================================================================

# [[0200]] Gold

#===============================================================================================================

# !! Waypoint c0.gold : "All Rules - Including Gold" : "Gold"

Show # %H7 $type->gold $tier->stack3
	StackSize >= 3001
	BaseType == "Gold"
	SetFontSize 45
	SetTextColor 235 200 110 255
	SetBorderColor 235 200 110 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 2 300
	PlayEffect Orange
	MinimapIcon 1 Yellow Cross

Show # %H6 $type->gold $tier->stack2
	StackSize >= 500
	BaseType == "Gold"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayEffect Orange Temp
	MinimapIcon 1 White Cross

Show # %H5 $type->gold $tier->stack1
	StackSize >= 150
	BaseType == "Gold"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	MinimapIcon 2 Grey Cross

Show # %H5 $type->gold $tier->stacklvl1
	StackSize >= 50
	BaseType == "Gold"
	AreaLevel <= 68
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	MinimapIcon 2 Grey Cross

Show # %H4 $type->gold $tier->anyother
	BaseType == "Gold"
	SetFontSize 35
	SetTextColor 180 180 180 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 20 20 0 180
	MinimapIcon 2 Grey Cross

#===============================================================================================================

# [[0300]] Influenced Items

#===============================================================================================================
#------------------------------------

# [0301] Influenced Maps

#------------------------------------

# !! Waypoint c1.infl.allplusmaps : "All rules - except gold and six-links" : "Maps"

#Hide # $type->maps->influenced $tier->zanacorrupthider

# ZanaMemory True

# Corrupted True

# Rarity Normal Magic

# Class == "Maps"

# SetFontSize 35

# SetBorderColor 0 0 0

Show # %H8 $type->maps->influenced $tier->zanamap
	ZanaMemory True
	MapTier >= 14
	Rarity Normal Magic Rare
	Class == "Maps"
	SetFontSize 45
	SetTextColor 100 0 122 255
	SetBorderColor 100 0 122 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

Show # %H6 $type->maps->influenced $tier->zanamaplow
	ZanaMemory True
	Rarity Normal Magic Rare
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 200 200 200 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 1 Purple Square

Show # %H7 $type->maps->influenced $tier->infelder
	HasInfluence Elder
	MapTier >= 14
	Rarity Normal Magic Rare
	Class == "Maps"
	SetFontSize 45
	SetTextColor 100 0 122 255
	SetBorderColor 100 0 122 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

Show # %H8 $type->maps->influenced $tier->infconquerors
	HasInfluence Crusader Hunter Redeemer Warlord
	Rarity Normal Magic Rare
	Class == "Maps"
	SetFontSize 45
	SetTextColor 100 0 122 255
	SetBorderColor 100 0 122 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

#------------------------------------

# [0302] Influenced Gear

#------------------------------------

# !! Waypoint c1.infl.all : "All rules - except 6links and influenced maps" : "Gear - Exotic"

# Selected exclusive bases

Show # %D9 $type->influenced->all $tier->t1exotic
	HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	Rarity Rare
	BaseType == "Apothecary's Gloves" "Bone Helmet" "Conquest Lamellar" "Divine Crown" "Fingerless Silk Gloves" "Fugitive Boots" "Giantslayer Helmet" "Gripped Gloves" "Haunted Bascinet" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Majestic Pelt" "Necrotic Armour" "Paladin Boots" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Royal Plate" "Sacred Chainmail" "Sacrificial Garb" "Spiked Gloves" "Syndicate's Garb" "Torturer's Mask" "Twilight Regalia" "Two-Toned Boots" "Velour Boots" "Velour Gloves" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 110 220
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

# Selected top tier bases

Show # %D5 $type->influenced->all $tier->t1top
	HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	Rarity Rare
	BaseType == "Agate Amulet" "Amber Amulet" "Amethyst Ring" "Archon Kite Shield" "Artillery Quiver" "Blue Pearl Amulet" "Bone Ring" "Broadhead Arrow Quiver" "Cardinal Round Shield" "Cerulean Ring" "Citrine Amulet" "Colossal Tower Shield" "Coral Ring" "Crystal Belt" "Diamond Ring" "Ezomyte Tower Shield" "Feathered Arrow Quiver" "Fossilised Spirit Shield" "Heavy Arrow Quiver" "Heavy Belt" "Iolite Ring" "Jade Amulet" "Lacquered Buckler" "Lapis Amulet" "Leather Belt" "Marble Amulet" "Moonstone Ring" "Onyx Amulet" "Opal Ring" "Primal Arrow Quiver" "Prismatic Ring" "Ruby Ring" "Sapphire Ring" "Steel Ring" "Stygian Vise" "Supreme Spiked Shield" "Titanium Spirit Shield" "Topaz Ring" "Turquoise Amulet" "Two-Stone Ring" "Unset Ring" "Vanguard Belt" "Vermillion Ring" "Vile Arrow Quiver"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 110 220
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D4 $type->influenced->all $tier->t1basescrusader
	HasInfluence Crusader
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Amethyst Ring" "Heat-attuned Tower Shield" "Iolite Ring" "Moonstone Ring" "Steel Ring" "Stygian Vise" "Synaptic Ring" "Transfer-attuned Spirit Shield" "Vaal Buckler" "Vermillion Ring"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 110 220
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D4 $type->influenced->all $tier->t1baseswarlord
	HasInfluence Warlord
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Amber Amulet" "Amethyst Ring" "Apothecary's Gloves" "Blizzard Crown" "Chimerascale Gauntlets" "Cryonic Ring" "Giantslayer Helmet" "Great Maw Talisman" "Harpyskin Gloves" "Hydrascale Gauntlets" "Jade Amulet" "Marble Amulet" "Onyx Amulet" "Paua Amulet" "Steel Ring" "Taurus Talisman" "Velour Gloves"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 110 220
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D4 $type->influenced->all $tier->t1basesredeemer
	HasInfluence Redeemer
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Cobra Talisman" "Cogwork Ring" "Crystal Belt" "Dusk Ring" "Fugitive Boots" "Opal Ring" "Spiked Gloves" "Stormrider Boots" "Vanguard Belt" "Vermillion Ring"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 110 220
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D4 $type->influenced->all $tier->t1baseshunter
	HasInfluence Hunter
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Enthalpic Ring" "Fugitive Boots" "Iolite Ring" "Leather Belt" "Organic Ring" "Pinnacle Tower Shield" "Scorpion Talisman" "Spiked Gloves" "Stormrider Boots" "Stygian Vise" "Synaptic Ring"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 110 220
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D4 $type->influenced->all $tier->t1basesshaper
	HasInfluence Shaper
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Anarchic Spiritblade" "Archdemon Crown" "Branded Kite Shield" "Cardinal Round Shield" "Ebony Tower Shield" "Enthalpic Ring" "Fugitive Ring" "Giantslayer Helmet" "Great Maw Talisman" "Imperial Claw" "Pinnacle Tower Shield" "Rhex Talisman" "Spike-Point Arrow Quiver" "Stygian Vise" "Supreme Spiked Shield" "Synaptic Ring" "Titanium Spirit Shield" "Transfer-attuned Spirit Shield"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 110 220
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D4 $type->influenced->all $tier->t1baseselder
	HasInfluence Elder
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Cord Belt" "Eclipse Staff" "Giantslayer Helmet" "Heat-attuned Tower Shield" "Sacrificial Garb"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 110 220
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D4 $type->influenced->all $tier->t2classescrusader
	HasInfluence Crusader
	ItemLevel >= 80
	Rarity Rare
	Class == "Amulets" "Belts" "Rings"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

Show # %D4 $type->influenced->all $tier->t2classeswarlord
	HasInfluence Warlord
	ItemLevel >= 80
	Rarity Rare
	Class == "Amulets" "Boots" "Gloves" "Rings"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

Show # %D4 $type->influenced->all $tier->t2classesredeemer
	HasInfluence Redeemer
	ItemLevel >= 80
	Rarity Rare
	Class == "Amulets" "Boots" "Rings" "Shields"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

Show # %D4 $type->influenced->all $tier->t2classeshunter
	HasInfluence Hunter
	ItemLevel >= 80
	Rarity Rare
	Class == "Amulets" "Belts" "Boots" "Gloves" "Quivers" "Rings" "Shields"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

Show # %D4 $type->influenced->all $tier->t2classesshaper
	HasInfluence Shaper
	ItemLevel >= 80
	Rarity Rare
	Class == "Amulets" "Bows" "Gloves" "Rings" "Wands"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

Show # %D4 $type->influenced->all $tier->t2classeselder
	HasInfluence Elder
	ItemLevel >= 80
	Rarity Rare
	Class == "Amulets" "Belts" "Rings"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

Show # %D4 $type->influenced->all $tier->t2classesinfluencedshared
	HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	ItemLevel >= 85
	Rarity Rare
	Class == "Amulets" "Body Armours" "Helmets" "Quivers" "Rings" "Sceptres" "Wands"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

# Second grade bases

Show # %D4 $type->influenced->all $tier->t2high
	HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	ItemLevel >= 84
	Rarity Rare
	BaseType == "Ancient Mask" "Arcanist Slippers" "Assassin's Boots" "Astral Leather" "Battered Foil" "Chimerascale Boots" "Chimerascale Gauntlets" "Conqueror's Helmet" "Conquest Helmet" "Convoking Wand" "Copper Kris" "Crusader Boots" "Crusader Gloves" "Deicide Mask" "Despot Axe" "Dire Pelt" "Dragonscale Boots" "Dragonscale Gauntlets" "Eternal Burgonet" "Faithful Helmet" "Full Wyvernscale" "Gemini Claw" "General's Helmet" "Golden Kris" "Goliath Gauntlets" "Goliath Greaves" "Grand Ringmail" "Grizzly Pelt" "Harmonic Spirit Shield" "Harpyskin Boots" "Harpyskin Gloves" "Hubris Circlet" "Hydrascale Boots" "Hydrascale Gauntlets" "Imperial Claw" "Imperial Skean" "Infiltrator Boots" "Infiltrator Mitts" "Jester Mask" "Jewelled Foil" "Kinetic Wand" "Knight Helm" "Lathi" "Legion Boots" "Legion Gloves" "Legion Plate" "Lion Pelt" "Marshall's Brigandine" "Martyr Boots" "Martyr Gloves" "Mind Cage" "Mirrored Spiked Shield" "Moonlit Circlet" "Murder Boots" "Murder Mitts" "Nightmare Bascinet" "Nightweave Robe" "Opal Sceptre" "Opal Wand" "Pagan Wand" "Paladin Crown" "Paladin's Hauberk" "Platinum Kris" "Praetor Crown" "Precursor Gauntlets" "Precursor Greaves" "Profane Wand" "Prophecy Wand" "Prophet Crown" "Reaver Axe" "Reaver Sword" "Reflex Bow" "Royal Burgonet" "Sage Gloves" "Sage Slippers" "Sanguine Raiment" "Short Bow" "Siege Axe" "Slink Boots" "Slink Gloves" "Soldier Boots" "Sorcerer Boots" "Sorcerer Gloves" "Spine Bow" "Stealth Boots" "Sunfire Circlet" "Supreme Leather" "Thicket Bow" "Titan Gauntlets" "Titan Greaves" "Titan Plate" "Tornado Wand" "Torturer Garb" "Vaal Axe" "Vaal Gauntlets" "Vaal Greaves" "Vaal Mask" "Void Sceptre" "Whalebone Rapier"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

# Low strictness 86 rule

Show # %D4 $type->influenced->all $tier->any86
	HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	ItemLevel >= 86
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

Show # %D3 $type->influenced->all $tier->any
	HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

#===============================================================================================================

# [[0400]] ELDRITCH ITEMS

#===============================================================================================================

# !! Waypoint c1.eldritch.all : "Eldritch Items - Exarch and Eater" : "Gear - Exotic"

Show # %D3 $type->rare->exarch $tier->anyhigh
	HasSearingExarchImplicit >= 1
	Rarity Normal Magic Rare
	BaseType == "Ambush Boots" "Ambush Mitts" "Ancient Gauntlets" "Ancient Greaves" "Ancient Mask" "Antique Gauntlets" "Antique Greaves" "Apothecary's Gloves" "Arcanist Gloves" "Arcanist Slippers" "Assassin's Boots" "Assassin's Mitts" "Bone Helmet" "Carnal Boots" "Carnal Mitts" "Chimerascale Boots" "Chimerascale Gauntlets" "Conjurer Boots" "Conjurer Gloves" "Conqueror's Helmet" "Conquest Helmet" "Crusader Boots" "Crusader Gloves" "Deicide Mask" "Dire Pelt" "Divine Crown" "Dragonscale Boots" "Dragonscale Gauntlets" "Eternal Burgonet" "Ezomyte Burgonet" "Faithful Helmet" "Fingerless Silk Gloves" "Fluted Bascinet" "Fugitive Boots" "General's Helmet" "Giantslayer Helmet" "Goliath Gauntlets" "Goliath Greaves" "Gripped Gloves" "Grizzly Pelt" "Harlequin Mask" "Harpyskin Boots" "Harpyskin Gloves" "Haunted Bascinet" "Hubris Circlet" "Hydrascale Boots" "Hydrascale Gauntlets" "Infiltrator Boots" "Infiltrator Mitts" "Jester Mask" "Knight Helm" "Legion Boots" "Legion Gloves" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Lion Pelt" "Magistrate Crown" "Majestic Pelt" "Martyr Boots" "Martyr Gloves" "Mind Cage" "Moonlit Circlet" "Murder Boots" "Murder Mitts" "Nightmare Bascinet" "Paladin Boots" "Paladin Crown" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Pig-Faced Bascinet" "Praetor Crown" "Precursor Gauntlets" "Precursor Greaves" "Prophet Crown" "Regicide Mask" "Riveted Boots" "Royal Burgonet" "Sage Gloves" "Sage Slippers" "Samite Slippers" "Samnite Helmet" "Serpentscale Boots" "Serpentscale Gauntlets" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Silken Hood" "Sinner Tricorne" "Slink Boots" "Slink Gloves" "Solaris Circlet" "Soldier Boots" "Soldier Gloves" "Sorcerer Boots" "Sorcerer Gloves" "Spiked Gloves" "Stealth Boots" "Stealth Gloves" "Sunfire Circlet" "Titan Gauntlets" "Titan Greaves" "Torturer's Mask" "Two-Toned Boots" "Vaal Gauntlets" "Vaal Greaves" "Vaal Mask" "Velour Boots" "Velour Gloves" "Warlock Boots" "Warlock Gloves" "Wyrmscale Boots" "Wyrmscale Gauntlets" "Wyvernscale Boots" "Wyvernscale Gauntlets" "Zealot Boots" "Zealot Gloves"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

#Show # %D0 $type->rare->exarch $tier->any

# HasSearingExarchImplicit >= 1

# Rarity Normal Magic Rare

# SetFontSize 40

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 50 130 165

# PlayEffect Blue Temp

Show # %D3 $type->rare->eater $tier->anyhigh
	HasEaterOfWorldsImplicit >= 1
	Rarity Normal Magic Rare
	BaseType == "Ambush Boots" "Ambush Mitts" "Ancient Gauntlets" "Ancient Greaves" "Ancient Mask" "Antique Gauntlets" "Antique Greaves" "Apothecary's Gloves" "Arcanist Gloves" "Arcanist Slippers" "Assassin's Boots" "Assassin's Mitts" "Bone Helmet" "Carnal Boots" "Carnal Mitts" "Chimerascale Boots" "Chimerascale Gauntlets" "Conjurer Boots" "Conjurer Gloves" "Conqueror's Helmet" "Conquest Helmet" "Crusader Boots" "Crusader Gloves" "Deicide Mask" "Dire Pelt" "Divine Crown" "Dragonscale Boots" "Dragonscale Gauntlets" "Eternal Burgonet" "Ezomyte Burgonet" "Faithful Helmet" "Fingerless Silk Gloves" "Fluted Bascinet" "Fugitive Boots" "General's Helmet" "Giantslayer Helmet" "Goliath Gauntlets" "Goliath Greaves" "Gripped Gloves" "Grizzly Pelt" "Harlequin Mask" "Harpyskin Boots" "Harpyskin Gloves" "Haunted Bascinet" "Hubris Circlet" "Hydrascale Boots" "Hydrascale Gauntlets" "Infiltrator Boots" "Infiltrator Mitts" "Jester Mask" "Knight Helm" "Legion Boots" "Legion Gloves" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Lion Pelt" "Magistrate Crown" "Majestic Pelt" "Martyr Boots" "Martyr Gloves" "Mind Cage" "Moonlit Circlet" "Murder Boots" "Murder Mitts" "Nightmare Bascinet" "Paladin Boots" "Paladin Crown" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Pig-Faced Bascinet" "Praetor Crown" "Precursor Gauntlets" "Precursor Greaves" "Prophet Crown" "Regicide Mask" "Riveted Boots" "Royal Burgonet" "Sage Gloves" "Sage Slippers" "Samite Slippers" "Samnite Helmet" "Serpentscale Boots" "Serpentscale Gauntlets" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Silken Hood" "Sinner Tricorne" "Slink Boots" "Slink Gloves" "Solaris Circlet" "Soldier Boots" "Soldier Gloves" "Sorcerer Boots" "Sorcerer Gloves" "Spiked Gloves" "Stealth Boots" "Stealth Gloves" "Sunfire Circlet" "Titan Gauntlets" "Titan Greaves" "Torturer's Mask" "Two-Toned Boots" "Vaal Gauntlets" "Vaal Greaves" "Vaal Mask" "Velour Boots" "Velour Gloves" "Warlock Boots" "Warlock Gloves" "Wyrmscale Boots" "Wyrmscale Gauntlets" "Wyvernscale Boots" "Wyvernscale Gauntlets" "Zealot Boots" "Zealot Gloves"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 50 130 165
	PlayEffect Blue Temp

#Show # %D0 $type->rare->eater $tier->any

# HasEaterOfWorldsImplicit >= 1

# Rarity Normal Magic Rare

# SetFontSize 40

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 50 130 165

# PlayEffect Blue Temp

#===============================================================================================================

# [[0500]] Exotic Bases

#===============================================================================================================

# !! Waypoint c1.exotic.all : "Exotic - Expedition, Ritual, Kalandra etc" : "Gear - Exotic"

# These bases don't usually drop during normal gameplay and are usually only acquired form certain sources

# These are bases such as heist and ritual bases.

Show # %D9 $type->exoticbases $tier->ecotinkbases84
	Mirrored False
	Corrupted False
	ItemLevel >= 84
	Rarity Normal Magic Rare
	BaseType == "Iron Flask"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %D9 $type->exoticbases $tier->ecotinkbases
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Iron Flask"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %D9 $type->exoticbases $tier->exoticheistbases
	Rarity Normal Magic Rare
	BaseType == "Accumulator Wand" "Alternating Sceptre" "Anarchic Spiritblade" "Apex Cleaver" "Astrolabe Amulet" "Banishing Blade" "Battery Staff" "Blasting Blade" "Boom Mace" "Capricious Spiritblade" "Cogwork Ring" "Cold-attuned Buckler" "Composite Ring" "Congregator Wand" "Crack Mace" "Crushing Force Magnifier" "Disapprobation Axe" "Eventuality Rod" "Flashfire Blade" "Focused Amulet" "Foundry Bow" "Geodesic Ring" "Heat-attuned Tower Shield" "Helical Ring" "Honed Cleaver" "Impact Force Propagator" "Infernal Blade" "Magmatic Tower Shield" "Malign Fangs" "Manifold Ring" "Mechalarm Belt" "Mechanical Belt" "Micro-Distillery Belt" "Oscillating Sceptre" "Pneumatic Dagger" "Polar Buckler" "Potentiality Rod" "Pressurised Dagger" "Psychotic Axe" "Ratcheting Ring" "Reciprocation Staff" "Simplex Amulet" "Solarine Bow" "Stabilising Sceptre" "Subsuming Spirit Shield" "Transfer-attuned Spirit Shield" "Void Fangs"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->exoticbases $tier->exoticritualbases
	Rarity Normal Magic Rare
	BaseType == "Aetherwind Gloves" "Apprentice Gloves" "Archdemon Crown" "Atonement Mask" "Basemetal Treads" "Blizzard Crown" "Brimstone Treads" "Cloudwhisper Boots" "Darksteel Treads" "Demon Crown" "Dreamquest Slippers" "Duskwalk Slippers" "Gale Crown" "Guarding Gauntlets" "Imp Crown" "Leyline Gloves" "Nexus Gloves" "Nightwind Slippers" "Penitent Mask" "Preserving Gauntlets" "Sorrow Mask" "Stormrider Boots" "Thwarting Gauntlets" "Tinker Gloves" "Trapsetter Gloves" "Windbreak Boots" "Winter Crown"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D9 $type->exoticbases $tier->exoticlakekala
	Rarity Normal Magic Rare
	BaseType == "Dusk Ring" "Gloam Ring" "Penumbra Ring" "Shadowed Ring" "Tenebrous Ring"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->exoticbases $tier->exoticexpeditionbases
	Rarity Normal Magic Rare
	BaseType == "Iron Flask" "Runic Crest" "Runic Crown" "Runic Gages" "Runic Gauntlets" "Runic Gloves" "Runic Greaves" "Runic Helm" "Runic Sabatons" "Runic Sollerets"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D9 $type->exoticbases $tier->exotictalismanbases $artefactex
	Rarity Normal Magic Rare
	BaseType == "Greatwolf Talisman"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D9 $type->exoticbases $tier->exoticbasesmisc
	Rarity Normal Magic Rare
	BaseType == "Grasping Mail"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->exoticbases $tier->exoticuniquebases
	Rarity Normal Magic Rare
	BaseType == "Ghostflame Blade" "Nameless Ring" "Ornate Quiver" "Prismatic Jewel" "Ring" "Ruby Amulet" "Unset Amulet"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

# !! Waypoint c1.exotic.exclusivebases : "Exotic - Stygian, Cord Belts, Sarificial Garbs" : "Gear - Exotic"

Show # %D9 $type->exoticbaseslower $tier->exoticmiragebases
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Cord Belt"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D9 $type->exoticbaseslower $tier->stygianmirage
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	BaseType == "Stygian Vise"
	HasExplicitMod "Abyssal"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->exoticbaseslower $tier->stygian86
	Mirrored False
	Corrupted False
	ItemLevel >= 86
	Rarity Normal Magic Rare
	BaseType == "Stygian Vise"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->exoticbaseslower $tier->stygian
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Stygian Vise"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D6 $type->exoticbaseslower $tier->exoticsacrificial
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Sacrificial Garb"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exoticbaseslower $tier->exoticpearl
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Pearlescent Amulet"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#===============================================================================================================

# [[0600]] IDENTIFIED MOD FILTERING - COMBINATIONS

#===============================================================================================================

# !! Waypoint c1.idmod.all : "Identified Mods - Best Veiled mods and combinations of expensive ID mods" : "Gear - Exotic"

#------------------------------------

# [0601] Physical

#------------------------------------

Show # %D5 $type->rareid $tier->weapon_phys
	Identified True
	DropLevel >= 50
	Rarity Rare
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	HasExplicitMod "Merciless" "Tyrannical" "Cruel" "of the Underground" "Subterranean" "of Many" "of Tacati" "Tacati's"
	HasExplicitMod >=3 "Merciless" "Tyrannical" "Flaring" "Dictator's" "Emperor's" "of Celebration" "of Incision" "of Dissolution" "of Destruction" "of the Underground" "Subterranean" "of Many" "of Tacati" "Tacati's" "Veil"
	HasExplicitMod =0 "Heavy" "Serrated" "Wicked" "Vicious" "Glinting" "Burnished" "Polished" "Honed" "of Needling" "of Skill"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->weapon_physpure
	Mirrored False
	Corrupted False
	Identified True
	DropLevel >= 50
	Rarity Rare
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	HasExplicitMod "Merciless" "Tyrannical" "Cruel" "of the Underground" "Subterranean" "of Many" "of Tacati" "Tacati's"
	HasExplicitMod >=2 "Merciless" "Tyrannical" "Flaring" "Dictator's" "Emperor's" "of Celebration" "of Incision" "of Dissolution" "of Destruction" "of the Underground" "Subterranean" "of Many" "of Tacati" "Tacati's" "Veil"
	HasExplicitMod =0 "Heavy" "Serrated" "Wicked" "Vicious" "Glinting" "Burnished" "Polished" "Honed" "of Needling" "of Skill"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0602] Elemental

#------------------------------------

Show # %D5 $type->rareid $tier->weapon_ele
	Identified True
	Rarity Rare
	BaseType == "Ambusher" "Blasting Wand" "Corsair Sword" "Dragonbone Rapier" "Eagle Claw" "Elegant Foil" "Eye Gouger" "Fancy Foil" "Gemini Claw" "Grove Bow" "Hellion's Paw" "Highborn Bow" "Imperial Bow" "Imperial Claw" "Imperial Skean" "Jewelled Foil" "Kinetic Wand" "Maraketh Bow" "Noble Claw" "Opal Wand" "Poignard" "Reflex Bow" "Serrated Foil" "Somatic Wand" "Spine Bow" "Spiraled Foil" "Steelwood Bow" "Stiletto" "Terror Claw" "Thicket Bow" "Throat Stabber" "Tornado Wand" "Twin Claw" "Wyrmbone Rapier"
	HasExplicitMod "Carbonising" "Cremating" "Blasting" "Crystalising" "Entombing" "Polar" "Vapourising" "Electrocuting" "Discharging" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many"
	HasExplicitMod >=4 "Carbonising" "Cremating" "Blasting" "Crystalising" "Entombing" "Polar" "Vapourising" "Electrocuting" "Discharging" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "of Celebration" "of Infamy" "of Fame" "of Incision" "of Penetrating" "of Puncturing" "of Destruction" "of Ferocity" "of Fury" "Devastating" "Overpowering" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Heated" "Smouldering" "Smoking" "Burning" "Frosted" "Chilled" "Icy" "Frigid" "Humming" "Buzzing" "Snapping" "Crackling" "of Needling" "of Skill" "Glinting" "Heavy"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->weapon_elepure
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	BaseType == "Ambusher" "Blasting Wand" "Corsair Sword" "Dragonbone Rapier" "Eagle Claw" "Elegant Foil" "Eye Gouger" "Fancy Foil" "Gemini Claw" "Grove Bow" "Hellion's Paw" "Highborn Bow" "Imperial Bow" "Imperial Claw" "Imperial Skean" "Jewelled Foil" "Kinetic Wand" "Maraketh Bow" "Noble Claw" "Opal Wand" "Poignard" "Reflex Bow" "Serrated Foil" "Somatic Wand" "Spine Bow" "Spiraled Foil" "Steelwood Bow" "Stiletto" "Terror Claw" "Thicket Bow" "Throat Stabber" "Tornado Wand" "Twin Claw" "Wyrmbone Rapier"
	HasExplicitMod "Carbonising" "Cremating" "Blasting" "Crystalising" "Entombing" "Polar" "Vapourising" "Electrocuting" "Discharging" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many"
	HasExplicitMod >=3 "Carbonising" "Cremating" "Blasting" "Crystalising" "Entombing" "Polar" "Vapourising" "Electrocuting" "Discharging" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "of Celebration" "of Infamy" "of Fame" "of Incision" "of Penetrating" "of Puncturing" "of Destruction" "of Ferocity" "of Fury" "Devastating" "Overpowering" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Heated" "Smouldering" "Smoking" "Burning" "Frosted" "Chilled" "Icy" "Frigid" "Humming" "Buzzing" "Snapping" "Crackling" "of Needling" "of Skill" "Glinting" "Heavy"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0603] Blade Blast Daggers

#------------------------------------

Show # %D4 $type->rareid $tier->bladeblast_2core
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	Class == "Daggers" "Rune Daggers"
	HasExplicitMod >=2 "of the Underground" "Subterranean" "of Many" "of Tacati" "Tacati's" "Matatl's" "Tacati" "Topotante's" "Carbonising" "Cremating" "Crystalising" "Entombing" "Vapourising" "Electrocuting" "Merciless" "Tyrannical"
	HasExplicitMod >=4 "of the Underground" "Subterranean" "of Many" "of Tacati" "Tacati's" "Matatl's" "Tacati" "Topotante's" "Carbonising" "Cremating" "Crystalising" "Entombing" "Vapourising" "Electrocuting" "Merciless" "Tyrannical" "Blasting" "Polar" "Discharging" "Flaring" "Runic" "Glyphic" "Incanter's" "Lithomancer's" "of Finesse" "of Sortilege" "of Prestidigitation" "of Unmaking" "of Ruin" "of Calamity" "of Destruction" "of Ferocity" "of Fury" "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0604] Gembased

#------------------------------------

Show # %D5 $type->rareid $tier->gem_bow
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	Class == "Bows"
	HasExplicitMod >=2 "Paragon's" "Sharpshooter's" "of Dissolution"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->gem_caster
	Identified True
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Wands"
	HasExplicitMod >=2 "of the Underground" "Subterranean" "of Many" "Martinet's" "Matatl's" "Tacati" "Topotante's" "Magister's" "Archon's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->gem_staves
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	Class == "Staves"
	HasExplicitMod >=2 "of the Underground" "Subterranean" "of Many" "Martinet's" "Matatl's" "Tacati" "Topotante's" "Typhoon Lord's" "Magmancer's" "Ice Shaper's" "Schismatist's" "Stone Singer's" "Lava Conjurer's" "Winter Beckoner's" "Tempest Master's" "Splintermind's" "Tecton's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0605] Caster

#------------------------------------

Show # %D5 $type->rareid $tier->caster_fireweapont2
	Identified True
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Wands"
	HasExplicitMod "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Xoph's" "Pyroclastic" "Magmatic" "Flame Shaper's" "Electrocuting" "Discharging" "Shocking" "Entombing" "Cremating"
	HasExplicitMod >=4 "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Xoph's" "Pyroclastic" "Magmatic" "Flame Shaper's" "Electrocuting" "Discharging" "Shocking" "Entombing" "Cremating" "of Unmaking" "of Ruin" "of Calamity" "of Finesse" "of Sortilege" "of Destruction" "of Ferocity" "of Fury" "Lich's" "Archmage's" "Mage's" "Zaffre" "Blue" "Polar" "Blasting" "Corrosive" "Dissolving" "of Ashes" "of Conflagrating" "of Combusting" "of the Fanatical" "of the Zealous" "of Dissolution" "of Melting" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Heated" "Smouldering" "Smoking" "Frosted" "Chilled" "Icy" "Humming" "Buzzing" "Snapping" "Apprentice's" "Adept's" "Scholar's" "Searing" "Sizzling" "Blistering" "Bitter" "Biting" "Alpine" "Charged" "Hissing" "Bolting" "of Talent"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->caster_coldweapont2
	Identified True
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Wands"
	HasExplicitMod "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Tul's" "Cryomancer's" "Crystalline" "Frost Singer's" "Electrocuting" "Entombing" "Polar" "Glaciated" "Cremating"
	HasExplicitMod >=4 "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Tul's" "Cryomancer's" "Crystalline" "Frost Singer's" "Electrocuting" "Entombing" "Polar" "Glaciated" "Cremating" "of Unmaking" "of Ruin" "of Calamity" "of Finesse" "of Sortilege" "of Destruction" "of Ferocity" "of Fury" "Lich's" "Archmage's" "Mage's" "Zaffre" "Blue" "Discharging" "Blasting" "Mortifying" "Festering" "of Glaciation" "of Heartstopping" "of the Gelid" "of Dissolution" "of Melting" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Heated" "Smouldering" "Smoking" "Frosted" "Chilled" "Icy" "Humming" "Buzzing" "Snapping" "Apprentice's" "Adept's" "Scholar's" "Searing" "Sizzling" "Blistering" "Bitter" "Biting" "Alpine" "Charged" "Hissing" "Bolting" "of Talent"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->caster_lightweapont2
	Identified True
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Wands"
	HasExplicitMod "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Esh's" "Ionising" "Smiting" "Thunderhand's" "Electrocuting" "Entombing" "Cremating" "Blasting" "Incinerating"
	HasExplicitMod >=4 "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Esh's" "Ionising" "Smiting" "Thunderhand's" "Electrocuting" "Entombing" "Cremating" "Blasting" "Incinerating" "of Unmaking" "of Ruin" "of Calamity" "of Finesse" "of Sortilege" "of Destruction" "of Ferocity" "of Fury" "Lich's" "Archmage's" "Mage's" "Zaffre" "Blue" "Discharging" "Polar" "Excruciating" "Harrowing" "of Arcing" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Heated" "Smouldering" "Smoking" "Frosted" "Chilled" "Icy" "Humming" "Buzzing" "Snapping" "Apprentice's" "Adept's" "Scholar's" "Searing" "Sizzling" "Blistering" "Bitter" "Biting" "Alpine" "Charged" "Hissing" "Bolting" "of Talent"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->caster_physweapont2
	Identified True
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Wands"
	HasExplicitMod "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Electrocuting" "Discharging" "Entombing" "Polar" "Cremating" "Blasting"
	HasExplicitMod >=4 "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Electrocuting" "Discharging" "Entombing" "Polar" "Cremating" "Blasting" "of Unmaking" "of Ruin" "of Calamity" "of Finesse" "of Sortilege" "of Destruction" "of Ferocity" "of Fury" "Lich's" "Archmage's" "Mage's" "Zaffre" "Blue" "of Exsanguinating" "of Hemorrhaging" "of Phlebotomising" "of Dissolution" "of Melting" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Heated" "Smouldering" "Smoking" "Frosted" "Chilled" "Icy" "Humming" "Buzzing" "Snapping" "Apprentice's" "Adept's" "Scholar's" "Searing" "Sizzling" "Blistering" "Bitter" "Biting" "Alpine" "Charged" "Hissing" "Bolting" "of Talent"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->caster_chaosweapont2
	Identified True
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Wands"
	HasExplicitMod "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Mad Lord's" "Electrocuting" "Entombing" "Cremating"
	HasExplicitMod >=4 "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "Runic" "Glyphic" "Incanter's" "Mad Lord's" "Electrocuting" "Entombing" "Cremating" "of Unmaking" "of Ruin" "of Calamity" "of Finesse" "of Sortilege" "of Destruction" "of Ferocity" "of Fury" "Lich's" "Archmage's" "Mage's" "Zaffre" "Blue" "Discharging" "Polar" "Blasting" "of Disintegrating" "of Atrophying" "of Deteriorating" "of Dissolution" "of Melting" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Heated" "Smouldering" "Smoking" "Frosted" "Chilled" "Icy" "Humming" "Buzzing" "Snapping" "Apprentice's" "Adept's" "Scholar's" "Searing" "Sizzling" "Blistering" "Bitter" "Biting" "Alpine" "Charged" "Hissing" "Bolting" "of Talent"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->minionwand
	Identified True
	Rarity Rare
	BaseType == "Calling Wand" "Convening Wand" "Convoking Wand"
	HasExplicitMod "Citaqualotl's" "Empress's" "Queen's" "Martinet's" "Magister's" "Archon's" "of Infuriation" "of Provocation" "of Destiny" "of the Monarch"
	HasExplicitMod >=4 "Martinet's" "Magister's" "Archon's" "Flame Shaper's" "Lithomancer's" "of Citaqualotl" "Veil" "Runic" "of Finesse" "of Sortilege" "Citaqualotl's" "Empress's" "Queen's" "of Infuriation" "of Provocation" "of Destiny" "of the Monarch" "King's" "Prince's" "Duke's" "Princess's" "Duchess's" "of Instigation" "of the Ruler" "of Determinism" "of Serendipity"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0606] Spellslinger

#------------------------------------

Show # %D5 $type->rareid $tier->caster_slingert2
	Identified True
	Rarity Rare
	Class == "Wands"
	HasExplicitMod "Carbonising" "Cremating" "Blasting" "Crystalising" "Entombing" "Polar" "Vapourising" "Electrocuting" "Discharging" "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "of Tacati" "Tacati's" "Runic" "Glyphic"
	HasExplicitMod >=4 "Carbonising" "Cremating" "Blasting" "Crystalising" "Entombing" "Polar" "Vapourising" "Electrocuting" "Discharging" "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "Empress's" "Queen's" "Lithomancer's" "of Tacati" "Tacati's" "Runic" "Glyphic" "of the Essence" "Essences" "of Puhuarte" "Veil" "of Celebration" "of Infamy" "of Destruction" "of Ferocity" "of Unmaking" "of Ruin" "Flame Shaper's" "Frost Singer's" "Thunderhand's" "Mad Lord's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0607] Helmets

#------------------------------------

Show # %D5 $type->rareid $tier->helmet_life_based
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	Class == "Helmets"
	HasExplicitMod "Fecund" "Athlete's" "Virile" "Overseer's" "of Everlasting" "of Youth" "of Nullification" "of Abjuration" "of Bameth"
	HasExplicitMod >=4 "Fecund" "Athlete's" "Virile" "Overseer's" "of Everlasting" "of Youth" "of Nullification" "of Abjuration" "of Bameth" "of Puhuarte" "of the Essence" "Essences" "of Tacati" "Veil" "of the Underground" "Subterranean" "Elevated " "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "Taskmaster's" "of Revoking" "of Lioneye" "of the Ranger" "of the Marksman" "of Vivification" "of Recuperation" "Impregnable" "Girded" "Mirage's" "Nightmare's" "Sturdy" "Durable" "Inspired" "Interpolated" "Illusory" "Unreal" "Enveloped" "Encased" "Elusory" "Vaporous" "Legend's" "Hero's" "Beatified" "Hallowed" "Spirit's" "Cherub's" "Abbot's" "Prior's" "Ram's" "Fawn's" "Nautilus's" "Urchin's"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D4 $type->rareid $tier->helmet_es_based
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	Class == "Helmets"
	HasExplicitMod >=2 "Unassailable" "Indomitable" "Blazing" "Seething" "Overseer's"
	HasExplicitMod >=4 "Unassailable" "Indomitable" "Blazing" "Seething" "Overseer's" "of Puhuarte" "of the Essence" "Essences" "of Tacati" "Veil" "of the Underground" "Subterranean" "Elevated " "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "Taskmaster's" "of Nullification" "of Abjuration" "of Revoking" "of Lioneye" "of the Ranger" "of the Marksman" "of Everlasting" "of Youth" "of Vivification" "of Recuperation" "Pulsing" "Priest's" "Abbot's" "Seraphim's" "Djinn's" "Fecund" "Athlete's"
	HasExplicitMod =0 "Hale" "Shining" "Glimmering" "Glittering" "Protective" "Strong-Willed" "Resolute"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0608] Boots

#------------------------------------

Show # %D5 $type->rareid $tier->boots_life_based
	Identified True
	Rarity Rare
	Class == "Boots"
	HasExplicitMod "Athlete's" "Hellion's" "Cheetah's" "of Nullification" "Matatl's" "of the Underground" "Subterranean" "Elevated "
	HasExplicitMod >=4 "Athlete's" "Hellion's" "Cheetah's" "of Nullification" "Matatl's" "of the Underground" "Subterranean" "Elevated " "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Abjuration" "of Revoking" "of Everlasting" "of Youth" "of Vivification" "Virile" "Rotund" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Abbot's" "Prior's" "Ram's" "Fawn's" "Nautilus's" "Urchin's"
	HasExplicitMod =0 "Runner's" "Sprinter's" "Stallion's" "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D4 $type->rareid $tier->boots_es_based
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	Class == "Boots"
	HasExplicitMod "Hellion's" "Cheetah's" "Matatl's" "of the Underground" "Subterranean" "Elevated "
	HasExplicitMod >=4 "Hellion's" "Cheetah's" "Matatl's" "of the Underground" "Subterranean" "Elevated " "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Nullification" "of Abjuration" "of Revoking" "of Everlasting" "of Youth" "of Vivification" "Blazing" "Seething" "Pulsing" "Unassailable" "Indomitable" "Priest's" "Abbot's" "Seraphim's" "Djinn's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Runner's" "Sprinter's" "Stallion's" "Shining" "Glimmering" "Glittering" "Protective" "Strong-Willed" "Resolute" "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0609] Gloves

#------------------------------------

Show # %D5 $type->rareid $tier->gloves_life_based
	Identified True
	Rarity Rare
	Class == "Gloves"
	HasExplicitMod "Athlete's" "Virile" "of Puhuarte" "of the Underground" "Subterranean" "Elevated " "of Nullification" "of Abjuration" "of Grandmastery" "of Bameth"
	HasExplicitMod >=4 "Athlete's" "Virile" "of Puhuarte" "of the Underground" "Subterranean" "Elevated " "of Nullification" "of Abjuration" "of Grandmastery" "of Bameth" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Revoking" "of Mastery" "of Lioneye" "of the Ranger" "Zaffre" "Rotund" "Abbot's" "Prior's" "Ram's" "Fawn's" "Nautilus's" "Urchin's" "of the Essence" "Essences" "of Tacati" "Veil"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->gloves_es_based
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	Class == "Gloves"
	HasExplicitMod >=2 "Blazing" "Seething" "Pulsing" "Unassailable" "Indomitable" "of Puhuarte" "of the Underground" "Subterranean" "Elevated "
	HasExplicitMod >=4 "Blazing" "Seething" "Pulsing" "Unassailable" "Indomitable" "of Puhuarte" "of the Underground" "Subterranean" "Elevated " "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Nullification" "of Abjuration" "of Revoking" "of Grandmastery" "of Mastery" "of Lioneye" "of the Ranger" "Zaffre" "Priest's" "Abbot's" "Seraphim's" "Djinn's" "of the Essence" "Essences" "of Tacati" "Veil"
	HasExplicitMod =0 "Runner's" "Sprinter's" "Stallion's" "Shining" "Glimmering" "Glittering" "Protective" "Strong-Willed" "Resolute" "Hale"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0610] Shields

#------------------------------------

Show # %D5 $type->rareid $tier->shield_esfocus
	Identified True
	Rarity Rare
	Class == "Shields"
	HasExplicitMod >=2 "of the Underground" "Subterranean" "Elevated " "Topotante's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of Nullification" "Vigorous" "Unyielding" "Lithomancer's" "Mad Lord's" "Thunderhand's" "Frost Singer's" "Flame Shaper's" "Runic" "Xoph's" "Tul's" "Esh's" "Incandescent" "Scintillating" "Blazing" "Unfaltering" "Unassailable"
	HasExplicitMod >=4 "of the Underground" "Subterranean" "Elevated " "Topotante's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of Nullification" "Vigorous" "Unyielding" "Lithomancer's" "Mad Lord's" "Thunderhand's" "Frost Singer's" "Flame Shaper's" "Runic" "Xoph's" "Tul's" "Esh's" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Convalescence" "of the Conservator" "of Abjuration" "of Revoking" "of Will" "of Fortitude" "Enduring" "Unwavering" "of the Bastion" "of Revitalization" "of Obstruction" "of Everlasting" "of Youth" "of the Deathless" "of Harmony" "of the Lightning Rod" "of the Mammoth" "of the Solar Storm" "of Unmaking" "Incandescent" "Scintillating" "Blazing" "Unfaltering" "Unassailable" "Priest's" "Abbot's" "Seraphim's" "Djinn's" "Glyphic" "Incanter's" "Pyroclastic" "Magmatic" "Cryomancer's" "Crystalline" "Ionising" "Smiting" "of Nirvana" "of Ruin" "of Calamity"
	HasExplicitMod =0 "Shining" "Glimmering" "Glittering" "Glowing" "Protective" "Strong-Willed" "Resolute" "Fearless"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->shield_defensefocus
	Identified True
	DropLevel >= 55
	Rarity Rare
	Class == "Shields"
	HasExplicitMod >=2 "of Nullification" "of the Underground" "Subterranean" "Elevated " "Topotante's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Vigorous" "Unyielding" "Lithomancer's" "Mad Lord's" "Thunderhand's" "Frost Singer's" "Flame Shaper's" "Runic" "Xoph's" "Tul's" "Esh's" "Unmoving" "Abating" "Lissome" "Adroit" "Adaptable" "Resilient" "Saintly" "Consecrated" "Apparition's" "Eidolon's" "Impenetrable" "Impregnable" "Illusion's" "Mirage's" "Victor's" "Sturdy" "Interpermeated" "Inspired" "Incorporeal" "Illusory" "Fecund" "of Bameth"
	HasExplicitMod >=4 "of the Underground" "Subterranean" "Elevated " "Topotante's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of Nullification" "Vigorous" "Unyielding" "Lithomancer's" "Mad Lord's" "Thunderhand's" "Frost Singer's" "Flame Shaper's" "Runic" "Xoph's" "Tul's" "Esh's" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Convalescence" "of the Conservator" "of Abjuration" "of Revoking" "of Will" "of Fortitude" "Enduring" "Unwavering" "of the Bastion" "of Revitalization" "of Obstruction" "of Everlasting" "of Youth" "of the Deathless" "of Harmony" "of the Lightning Rod" "of the Mammoth" "of the Solar Storm" "of Unmaking" "Fecund" "Athlete's" "of the Ranger" "of Mastery" "Impenetrable" "Impregnable" "Illusion's" "Mirage's" "Victor's" "Sturdy" "Interpermeated" "Inspired" "Incorporeal" "Illusory" "Unmoving" "Abating" "Lissome" "Adroit" "Adaptable" "Resilient" "Saintly" "Consecrated" "Apparition's" "Eidolon's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->shield_casterfocus
	Identified True
	Rarity Rare
	Class == "Shields"
	HasExplicitMod >=2 "of the Underground" "Subterranean" "Elevated " "Topotante's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of Nullification" "Vigorous" "Unyielding" "Lithomancer's" "Mad Lord's" "Thunderhand's" "Frost Singer's" "Flame Shaper's" "Runic" "Xoph's" "Tul's" "Esh's" "Glyphic" "Incanter's" "Pyroclastic" "Magmatic" "Cryomancer's" "Crystalline" "Ionising" "Smiting" "of Unmaking" "of Ruin" "Fecund"
	HasExplicitMod >=4 "of the Underground" "Subterranean" "Elevated " "Topotante's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of Nullification" "Vigorous" "Unyielding" "Lithomancer's" "Mad Lord's" "Thunderhand's" "Frost Singer's" "Flame Shaper's" "Runic" "Xoph's" "Tul's" "Esh's" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Convalescence" "of the Conservator" "of Abjuration" "of Revoking" "of Will" "of Fortitude" "Enduring" "Unwavering" "of the Bastion" "of Revitalization" "of Obstruction" "of Everlasting" "of Youth" "of the Deathless" "of Harmony" "of the Lightning Rod" "of the Mammoth" "of the Solar Storm" "of Unmaking" "Fecund" "Athlete's" "Glyphic" "Incanter's" "Pyroclastic" "Magmatic" "Cryomancer's" "Crystalline" "Ionising" "Smiting" "of Nirvana" "of Ruin" "of Calamity" "Incandescent" "Scintillating" "Unfaltering" "Unassailable"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->shield_lifefocus
	Identified True
	DropLevel >= 55
	Rarity Rare
	Class == "Shields"
	HasExplicitMod "of Nullification" "Vigorous"
	HasExplicitMod >=4 "of the Underground" "Subterranean" "Elevated " "Topotante's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of Nullification" "Vigorous" "Unyielding" "Lithomancer's" "Mad Lord's" "Thunderhand's" "Frost Singer's" "Flame Shaper's" "Runic" "Xoph's" "Tul's" "Esh's" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Convalescence" "of the Conservator" "of Abjuration" "of Revoking" "of Will" "of Fortitude" "Enduring" "Unwavering" "of the Bastion" "of Revitalization" "of Obstruction" "of Everlasting" "of Youth" "of the Deathless" "of Harmony" "of the Lightning Rod" "of the Mammoth" "of the Solar Storm" "of Unmaking" "Fecund" "Athlete's" "Glyphic" "Incanter's" "Pyroclastic" "Magmatic" "Cryomancer's" "Crystalline" "Ionising" "Smiting" "of Nirvana" "of Ruin" "of Calamity" "Unmoving" "Abating" "Lissome" "Adroit" "Adaptable" "Resilient" "Saintly" "Consecrated" "Apparition's" "Eidolon's" "Impenetrable" "Impregnable" "Illusion's" "Mirage's" "Victor's" "Sturdy" "Interpermeated" "Inspired" "Incorporeal" "Illusory" "Incandescent" "Scintillating" "Unfaltering" "Unassailable"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine" "Stalwart" "Stout"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0611] Amulets

#------------------------------------

Show # %D5 $type->rareid $tier->amu_exalter
	Identified True
	Rarity Rare
	Class == "Amulets"
	HasExplicitMod "Exalter's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->amu_1corecaster
	Identified True
	Rarity Rare
	Class == "Amulets"
	HasExplicitMod "Athlete's" "Virile" "Rotund" "Dazzling" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of Puhuarte" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Destruction" "of Dissolution" "of the Multiverse" "Unassailable"
	HasExplicitMod >=4 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of the Multiverse" "of the Infinite" "of the Universe" "of Nirvana" "of Euphoria" "Impregnable" "Vaporous" "Unassailable" "Athlete's" "Virile" "Rotund" "Ultramarine" "Dazzling" "Resplendent" "Perandus'" "of Legerdemain" "of Expertise" "Wizard's" "Thaumaturgist's" "Zaffre" "of Immolation" "of Flames" "of Floe" "of Rime" "of Discharge" "of Voltage" "of Dissolution" "of Melting" "of Destruction" "of Ferocity" "of Fury" "of Incision" "of Penetrating"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->amu_2corecaster
	Identified True
	Rarity Rare
	Class == "Amulets"
	HasExplicitMod >=2 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Athlete's" "Virile" "Rotund" "Robust" "Dazzling" "Resplendent" "Incandescent" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Destruction" "of Ferocity" "of Dissolution" "of Melting" "of the Multiverse" "of the Infinite" "Unassailable" "Indomitable" "of Bameth"
	HasExplicitMod >=4 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of the Multiverse" "of the Infinite" "of the Universe" "of Nirvana" "of Euphoria" "Impregnable" "Vaporous" "Unassailable" "Athlete's" "Virile" "Rotund" "Ultramarine" "Dazzling" "Resplendent" "Perandus'" "of Legerdemain" "of Expertise" "Wizard's" "Thaumaturgist's" "Zaffre" "of Immolation" "of Flames" "of Floe" "of Rime" "of Discharge" "of Voltage" "of Dissolution" "of Melting" "of Destruction" "of Ferocity" "of Fury" "of Incision" "of Penetrating"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->amu_1coredot
	Identified True
	Rarity Rare
	Class == "Amulets"
	HasExplicitMod "Athlete's" "Virile" "Rotund" "Dazzling" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of Puhuarte" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Destruction" "of Dissolution" "of the Multiverse" "Unassailable"
	HasExplicitMod >=4 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of the Multiverse" "of the Infinite" "of the Universe" "of Nirvana" "of Euphoria" "Impregnable" "Vaporous" "Unassailable" "Athlete's" "Virile" "Rotund" "Ultramarine" "Dazzling" "Resplendent" "Perandus'" "of Destruction" "of Legerdemain" "Wizard's" "Thaumaturgist's" "Devastating" "Overpowering" "of the Ranger" "of the Marksman" "of Immolation" "of Floe" "of Dissolution" "of Melting" "of Liquefaction"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->amu_2coredot
	Identified True
	Rarity Rare
	Class == "Amulets"
	HasExplicitMod >=2 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Athlete's" "Virile" "Rotund" "Robust" "Dazzling" "Resplendent" "Incandescent" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Destruction" "of Ferocity" "of Dissolution" "of Melting" "of the Multiverse" "of the Infinite" "Unassailable" "Indomitable" "of Bameth"
	HasExplicitMod >=4 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of the Multiverse" "of the Infinite" "of the Universe" "of Nirvana" "of Euphoria" "Impregnable" "Vaporous" "Unassailable" "Athlete's" "Virile" "Rotund" "Ultramarine" "Dazzling" "Resplendent" "Perandus'" "of Destruction" "of Legerdemain" "Wizard's" "Thaumaturgist's" "Devastating" "Overpowering" "of the Ranger" "of the Marksman" "of Immolation" "of Floe" "of Dissolution" "of Melting" "of Liquefaction"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->amu_1coreattack
	Identified True
	Rarity Rare
	Class == "Amulets"
	HasExplicitMod "Athlete's" "Virile" "Rotund" "Dazzling" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of Puhuarte" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Destruction" "of Dissolution" "of the Multiverse" "Unassailable"
	HasExplicitMod >=4 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of the Multiverse" "of the Infinite" "of the Universe" "of Nirvana" "of Euphoria" "Impregnable" "Vaporous" "Unassailable" "Athlete's" "Virile" "Rotund" "Ultramarine" "Dazzling" "Resplendent" "Perandus'" "of Destruction" "of Ferocity" "of Fury" "of Rage" "of Incision" "of Penetrating" "Cremating" "Entombing" "Electrocuting" "of the Ranger" "of the Marksman" "Devastating" "Overpowering" "Unleashed" "Flaring" "Tempered"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->amu_2coreattack
	Identified True
	Rarity Rare
	Class == "Amulets"
	HasExplicitMod >=2 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Athlete's" "Virile" "Rotund" "Robust" "Dazzling" "Resplendent" "Incandescent" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Destruction" "of Ferocity" "of Dissolution" "of Melting" "of the Multiverse" "of the Infinite" "Unassailable" "Indomitable" "of Bameth"
	HasExplicitMod >=4 "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of the Multiverse" "of the Infinite" "of the Universe" "of Nirvana" "of Euphoria" "Impregnable" "Vaporous" "Unassailable" "Athlete's" "Virile" "Rotund" "Ultramarine" "Dazzling" "Resplendent" "Perandus'" "of Destruction" "of Ferocity" "of Fury" "of Rage" "of Incision" "of Penetrating" "Cremating" "Entombing" "Electrocuting" "of the Ranger" "of the Marksman" "Devastating" "Overpowering" "Unleashed" "Flaring" "Tempered"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0612] Rings

#------------------------------------

Show # %D5 $type->rareid $tier->ring_caster
	Identified True
	Rarity Rare
	Class == "Rings"
	HasExplicitMod "of Bameth" "of Puhuarte" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of the Underground" "Subterranean" "Athlete's" "Virile" "Rotund" "Dazzling" "Resplendent"
	HasExplicitMod >=4 "of Bameth" "of Puhuarte" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of the Underground" "Subterranean" "Athlete's" "Virile" "Rotund" "Dazzling" "Resplendent" "Quintessential" "of the Essence" "Essences" "of Tacati" "Veil" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Nirvana" "of Euphoria" "of Fleshbinding" "of Suturing" "Perandus'" "of the Comet" "of Legerdemain" "of Expertise" "of Nimbleness" "of Flames" "of Rime" "of Voltage" "Ultramarine"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->ring_attack
	Identified True
	Rarity Rare
	Class == "Rings"
	HasExplicitMod "of Bameth" "of Puhuarte" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of the Underground" "Subterranean" "Athlete's" "Virile" "Rotund" "Dazzling" "Resplendent"
	HasExplicitMod >=4 "of Bameth" "of Puhuarte" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of the Underground" "Subterranean" "Athlete's" "Virile" "Rotund" "Dazzling" "Resplendent" "Quintessential" "of the Essence" "Essences" "of Tacati" "Veil" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Nirvana" "of Euphoria" "of Fleshbinding" "of Suturing" "Perandus'" "of the Comet" "Devastating" "Overpowering" "Unleashed" "of the Ranger" "of the Marksman" "Flaring" "Cremating" "Entombing" "Electrocuting" "of Skill" "of Flames" "of Rime" "of Voltage"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->ring_light
	Identified True
	Rarity Rare
	Class == "Rings"
	HasExplicitMod >=2 "of Bameth" "of Puhuarte" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of the Underground" "Subterranean" "Athlete's" "Virile" "Rotund" "of Radiance"
	HasExplicitMod >=4 "of Bameth" "of Puhuarte" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of the Underground" "Subterranean" "Athlete's" "Virile" "Rotund" "of Radiance" "Quintessential" "of the Essence" "Essences" "of Tacati" "Veil" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Nirvana" "of Euphoria" "of Fleshbinding" "of Legerdemain" "of Suturing" "of the Comet"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->ring_minion
	Identified True
	Rarity Rare
	Class == "Rings"
	BaseType == "Bone Ring"
	HasExplicitMod >=2 "Duchess's" "Countess's" "Marchioness's" "of Agitation" "of Incitation" "of Coercion" "of Harmony" "of Orchestration"
	HasExplicitMod >=4 "of Bameth" "of Puhuarte" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of the Underground" "Subterranean" "Athlete's" "Virile" "Rotund" "Dazzling" "Resplendent" "Quintessential" "of the Essence" "Essences" "of Tacati" "Veil" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of the Blur" "of the Wind" "of the Phantom" "of the Jaguar" "of the Polymath" "of the Genius" "of the Virtuoso" "of the Savant" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Nirvana" "of Euphoria" "of Fleshbinding" "of Suturing" "Perandus'" "of the Comet" "Duchess's" "Countess's" "Marchioness's" "of Agitation" "of Incitation" "of Coercion" "of Harmony" "of Orchestration" "of Metamorphosis" "of the Taskmaster"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0613] Quivers

#------------------------------------

Show # %D5 $type->rareid $tier->quiv_hit
	Identified True
	Rarity Rare
	Class == "Quivers"
	HasExplicitMod >=2 "Impaling" "of the Underground" "Subterranean" "Elevated " "of Splintering" "Fecund" "Athlete's" "of Destruction" "of Ferocity" "of Grandmastery" "of Dissolution" "of Melting" "of Rending" "Devastating"
	HasExplicitMod >=4 "Impaling" "Lacerating" "Incisive" "of the Underground" "Subterranean" "Elevated " "of Splintering" "Fecund" "Athlete's" "Virile" "of the Blur" "of the Wind" "of Tzteosh" "of the Magma" "of Haast" "of the Ice" "of Ephij" "of the Lightning" "of Bameth" "of Exile" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Flaring" "Cremating" "Entombing" "Electrocuting" "Devastating" "Overpowering" "of Grandmastery" "of Mastery" "of Ease" "of Lioneye" "of the Ranger" "of Dissolution" "of the Gale" "of Destruction" "of Ferocity" "of Fury" "of Rending" "of Incision" "of Penetrating"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareid $tier->quiv_dot
	Identified True
	Rarity Rare
	Class == "Quivers"
	HasExplicitMod >=2 "Impaling" "of the Underground" "Subterranean" "Elevated " "of Splintering" "Fecund" "Athlete's" "of Destruction" "of Ferocity" "of Grandmastery" "of Dissolution" "of Melting" "of Rending" "Devastating"
	HasExplicitMod >=4 "Impaling" "Lacerating" "Incisive" "of the Underground" "Subterranean" "Elevated " "of Splintering" "Fecund" "Athlete's" "Virile" "of the Blur" "of the Wind" "of Tzteosh" "of the Magma" "of Haast" "of the Ice" "of Ephij" "of the Lightning" "of Bameth" "of Exile" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Cremating" "Flaring" "Devastating" "of Grandmastery" "of Mastery" "of Ease" "of Lioneye" "of the Ranger" "of Dissolution" "of Melting" "of Liquefaction" "of the Gale" "of Destruction" "of Rending"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0614] Body Armours

#------------------------------------

Show # %D4 $type->rareid $tier->body_life
	Mirrored False
	Corrupted False
	Identified True
	DropLevel >= 55
	Rarity Rare
	Class == "Body Armours"
	HasExplicitMod "of Nullification" "Prime" "Rapturous" "Vigorous" "of the Underground" "Subterranean" "Elevated " "Guatelitzi's"
	HasExplicitMod >=5 "of Nullification" "Prime" "Rapturous" "Vigorous" "of the Underground" "Subterranean" "Elevated " "Guatelitzi's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Convalescence" "of the Conservator" "of the Protector" "of Abjuration" "Crocodile's" "Nautilus's" "Ibex's" "Ram's" "Exarch's" "Impervious" "Unmoving" "Fugitive" "Lissome" "Versatile" "Adaptable" "Phantasm's" "Apparition's" "Godly" "Saintly" "Interpermeated" "Inspired" "Interpolated" "Impenetrable" "Impregnable" "Girded" "Illusion's" "Mirage's" "Nightmare's" "Victor's" "Legend's" "Hero's" "Incorporeal" "Illusory" "Unreal"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine" "Stalwart" "Stout"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D4 $type->rareid $tier->body_defense
	Mirrored False
	Corrupted False
	Identified True
	DropLevel >= 55
	Rarity Rare
	Class == "Body Armours"
	HasExplicitMod >=2 "of Nullification" "Prime" "Rapturous" "Vigorous" "Impervious" "Unmoving" "Fugitive" "Lissome" "Versatile" "Adaptable" "Phantasm's" "Apparition's" "Godly" "Saintly" "Interpermeated" "Inspired" "Interpolated" "Impenetrable" "Impregnable" "Girded" "Illusion's" "Mirage's" "Nightmare's" "Victor's" "Legend's" "Hero's" "Incorporeal" "Illusory" "Unreal"
	HasExplicitMod >=4 "of Nullification" "Prime" "Rapturous" "Vigorous" "of the Underground" "Subterranean" "Elevated " "Guatelitzi's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Convalescence" "of the Conservator" "of the Protector" "of Abjuration" "Crocodile's" "Nautilus's" "Ibex's" "Ram's" "Exarch's" "Impervious" "Unmoving" "Fugitive" "Lissome" "Versatile" "Adaptable" "Phantasm's" "Apparition's" "Godly" "Saintly" "Interpermeated" "Inspired" "Interpolated" "Impenetrable" "Impregnable" "Girded" "Illusion's" "Mirage's" "Nightmare's" "Victor's" "Legend's" "Hero's" "Incorporeal" "Illusory" "Unreal"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D4 $type->rareid $tier->body_lifedefense
	Mirrored False
	Corrupted False
	Identified True
	DropLevel >= 55
	Rarity Rare
	Class == "Body Armours"
	HasExplicitMod >=2 "of Nullification" "Prime" "Rapturous" "Vigorous" "Impervious" "Unmoving" "Fugitive" "Lissome" "Versatile" "Adaptable" "Phantasm's" "Apparition's" "Godly" "Saintly" "Interpermeated" "Inspired" "Interpolated" "Impenetrable" "Impregnable" "Girded" "Illusion's" "Mirage's" "Nightmare's" "Victor's" "Legend's" "Hero's" "Incorporeal" "Illusory" "Unreal"
	HasExplicitMod "of Nullification" "Prime" "Rapturous" "Vigorous" "of the Underground" "Subterranean" "Elevated " "Guatelitzi's"
	HasExplicitMod >=4 "of Nullification" "Prime" "Rapturous" "Vigorous" "of the Underground" "Subterranean" "Elevated " "Guatelitzi's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Convalescence" "of the Conservator" "of the Protector" "of Abjuration" "Crocodile's" "Nautilus's" "Ibex's" "Ram's" "Exarch's" "Impervious" "Unmoving" "Fugitive" "Lissome" "Versatile" "Adaptable" "Phantasm's" "Apparition's" "Godly" "Saintly" "Interpermeated" "Inspired" "Interpolated" "Impenetrable" "Impregnable" "Girded" "Illusion's" "Mirage's" "Nightmare's" "Victor's" "Legend's" "Hero's" "Incorporeal" "Illusory" "Unreal"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D4 $type->rareid $tier->body_es
	Mirrored False
	Corrupted False
	Identified True
	DropLevel >= 55
	Rarity Rare
	Class == "Body Armours"
	HasExplicitMod >=2 "Resplendent" "Incandescent" "Unfaltering" "Unassailable" "Indomitable" "of the Underground" "Subterranean" "Elevated " "Guatelitzi's"
	HasExplicitMod >=4 "Resplendent" "Incandescent" "Unfaltering" "Unassailable" "Indomitable" "of the Underground" "Subterranean" "Elevated " "Guatelitzi's" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Convalescence" "of the Conservator" "of the Protector" "of Nullification" "of Abjuration" "Seraphim's" "Djinn's" "Bishop's" "Priest's" "Exarch's" "Abbot's" "Prime" "Rapturous"
	HasExplicitMod =0 "Shining" "Glimmering" "Glittering" "Glowing" "Protective" "Strong-Willed" "Resolute" "Fearless"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0615] Belts

#------------------------------------

Show # %D5 $type->rareid $tier->belt_general
	Identified True
	Rarity Rare
	Class == "Belts"
	HasExplicitMod "of the Underground" "Subterranean" "Guatelitzi's" "of Guatelitzi" "Fecund" "Athlete's" "Dazzling"
	HasExplicitMod >=4 "of the Underground" "Subterranean" "Guatelitzi's" "of Guatelitzi" "Fecund" "Athlete's" "Virile" "Dazzling" "of the Godslayer" "of the Gods" "of the Titan" "of the Leviathan" "of Tzteosh" "of the Magma" "of the Volcano" "of Haast" "of the Ice" "of the Polar Bear" "of Ephij" "of the Lightning" "of the Maelstrom" "of Bameth" "of Exile" "of Expulsion" "of Recuperation" "Enveloped" "Encased" "Carapaced" "Magnifying" "Condensing" "of Reveling" "of Relishing" "Devastating" "Overpowering" "Unleashed" "Blue" "Mazarine" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil"
	HasExplicitMod =0 "Hale" "Healthy" "Sanguine"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0616] Jewels

#------------------------------------

Show # %D7 $type->rareid $tier->idjewel_minion
	Identified True
	Rarity Rare
	Class == "Abyss Jewels" "Jewels"
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	HasExplicitMod >=2 "Vivid" "Shimmering" "Leadership" "Master's" "of Resilience" "Decrepifying"
	HasExplicitMod >=3 "Vivid" "Shimmering" "Leadership" "Master's" "of Resilience" "Decrepifying" "Expediting" "Prolonging" "Cerebral" "of the Phoenix" "of the Kraken" "of the Leviathan" "of Order" "of Resistance" "of Insulation" "of the Hearth" "of Shelter" "of Spirit" "of Athletics" "of Cunning" "of Adaption" "of Wounding" "Thwarting" "of Training" "Enlightened" "of Efficiency"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->idjewel_dot
	Identified True
	Rarity Rare
	Class == "Abyss Jewels" "Jewels"
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	HasExplicitMod >=1 "Vivid" "Shimmering" "of Acrimony" "Decrepifying"
	HasExplicitMod =1 "of Exsanguinating" "of Zealousness" "of Atrophy" "of Gelidity"
	HasExplicitMod >=3 "Vivid" "Shimmering" "Expediting" "Prolonging" "Cerebral" "of the Phoenix" "of the Kraken" "of the Leviathan" "of Order" "of Resistance" "of Insulation" "of the Hearth" "of Shelter" "of Spirit" "of Athletics" "of Cunning" "of Adaption" "of Wounding" "Thwarting" "of Entropy" "Decrepifying" "of Acrimony" "of Exsanguinating" "of Zealousness" "of Atrophy" "of Gelidity"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->idjewel_critattack
	Identified True
	Rarity Rare
	Class == "Abyss Jewels" "Jewels"
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	HasExplicitMod >=1 "of Potency" "of the Elements" "Vivid" "Shimmering" "of Demolishing"
	HasExplicitMod >=2 "of Potency" "of the Elements" "Vivid" "Shimmering" "of Demolishing" "Piercing" "Rupturing" "of Menace" "Arctic" "Surging" "Infernal" "Puncturing" "Expediting" "Prolonging" "Cerebral" "of the Phoenix" "of the Kraken" "of the Leviathan" "of Order" "of Resistance" "of Insulation" "of the Hearth" "of Shelter" "of Spirit" "of Athletics" "of Cunning" "of Adaption" "of Wounding" "Thwarting"
	HasExplicitMod >=3 "of Potency" "of the Elements" "Vivid" "Shimmering" "of Demolishing" "Piercing" "Rupturing" "of Menace" "Arctic" "Surging" "Infernal" "Puncturing" "Expediting" "Prolonging" "Cerebral" "of the Phoenix" "of the Kraken" "of the Leviathan" "of Order" "of Resistance" "of Insulation" "of the Hearth" "of Shelter" "of Spirit" "of Athletics" "of Cunning" "of Adaption" "of Wounding" "Thwarting" "of Berserking" "Sharpened" "Humming" "Chaotic" "Flaming" "Chilling" "of Zeal"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->idjewel_critspell
	Identified True
	Rarity Rare
	Class == "Abyss Jewels" "Jewels"
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	HasExplicitMod >=1 "of Potency" "of the Elements" "Vivid" "Shimmering" "of Unmaking"
	HasExplicitMod >=2 "of Potency" "of the Elements" "Vivid" "Shimmering" "of Unmaking" "of Menace" "Arctic" "Surging" "Infernal" "Puncturing" "Expediting" "Prolonging" "Cerebral" "of the Phoenix" "of the Kraken" "of the Leviathan" "of Order" "of Resistance" "of Insulation" "of the Hearth" "of Shelter" "of Spirit" "of Athletics" "of Cunning" "of Adaption" "of Wounding" "Thwarting"
	HasExplicitMod >=3 "of Potency" "of the Elements" "Vivid" "Shimmering" "of Unmaking" "of Menace" "Arctic" "Surging" "Infernal" "Puncturing" "Expediting" "Prolonging" "Cerebral" "of the Phoenix" "of the Kraken" "of the Leviathan" "of Order" "of Resistance" "of Insulation" "of the Hearth" "of Shelter" "of Spirit" "of Athletics" "of Cunning" "of Adaption" "of Wounding" "Thwarting" "of Mysticism" "of Blasting" "of Archery" "Chilling" "Trapping" "Sharpened" "Humming" "Chaotic" "Flaming" "Battlemage's" "Warding" "Sorcerer's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->idaj_attack
	Identified True
	Rarity Rare
	Class == "Abyss Jewels" "Jewels"
	BaseType == "Murderous Eye Jewel" "Searching Eye Jewel"
	HasExplicitMod >=1 "of the Lightning Rod" "Beclouded" "Sanguine" "Stalwart" "Healthy" "Resplendent" "Incandescent" "of the Deadeye" "Acuminate" "Flaring" "Electrocuting" "Discharging" "Cremating" "Blasting" "Entombing" "Polar" "Vile"
	HasExplicitMod >=3 "of the Lightning Rod" "Beclouded" "Sanguine" "Stalwart" "Healthy" "Resplendent" "Incandescent" "of the Deadeye" "Acuminate" "Flaring" "Electrocuting" "Discharging" "Cremating" "Blasting" "Entombing" "Polar" "Vile" "of the Dragon" "of Dexterity" "of Intelligence" "of Strength" "Fleet" "Seething" "Sapphire" "Carapaced" "Encased" "Vaporous" "Expediting" "of Athletics" "of Spirit" "of Cunning" "of Adaption" "of Shelter" "of Grounding" "of the Hearth" "of Resistance" "of Order" "of Potency" "of the Inquisitor" "of Menace" "of Blinding" "of the Assassin" "of Taunting" "of Phasing" "of Ashes" "of Glaciation" "of Arcing" "of Collision" "of the Inferno" "of Opportunity" "of Berserking" "of the Ranger" "Lancing" "of Unholy Might"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->idaj_caster
	Identified True
	Rarity Rare
	Class == "Abyss Jewels" "Jewels"
	BaseType == "Hypnotic Eye Jewel"
	HasExplicitMod >=1 "of the Lightning Rod" "Beclouded" "Sanguine" "Stalwart" "Healthy" "Resplendent" "Incandescent" "of the Deadeye" "Acuminate" "Flaring" "Electrocuting" "Discharging" "Cremating" "Blasting" "Entombing" "Polar" "Vile"
	HasExplicitMod >=3 "of the Lightning Rod" "Beclouded" "Sanguine" "Stalwart" "Healthy" "Resplendent" "Incandescent" "of the Deadeye" "Acuminate" "Flaring" "Electrocuting" "Discharging" "Cremating" "Blasting" "Entombing" "Polar" "Vile" "of the Dragon" "of Dexterity" "of Intelligence" "of Strength" "Fleet" "Seething" "Sapphire" "Carapaced" "Encased" "Vaporous" "Expediting" "of Athletics" "of Spirit" "of Cunning" "of Adaption" "of Shelter" "of Grounding" "of the Hearth" "of Resistance" "of Order" "of Potency" "of the Inquisitor" "of Menace" "of Blinding" "of the Assassin" "of Taunting" "of Phasing" "of Ashes" "of Glaciation" "of Arcing" "of Collision" "of the Inferno" "of Abuse" "of Enchanting" "of Hindering"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->idaj_minion
	Identified True
	Rarity Rare
	Class == "Abyss Jewels" "Jewels"
	BaseType == "Ghastly Eye Jewel"
	HasExplicitMod >=1 "of the Lightning Rod" "Beclouded" "Sanguine" "Stalwart" "Healthy" "Resplendent" "Incandescent" "of the Deadeye" "Acuminate" "Flaring" "Electrocuting" "Discharging" "Cremating" "Blasting" "Entombing" "Polar" "Vile" "Malicious"
	HasExplicitMod >=3 "of the Lightning Rod" "Beclouded" "Sanguine" "Stalwart" "Healthy" "Resplendent" "Incandescent" "of the Deadeye" "Acuminate" "Flaring" "Electrocuting" "Discharging" "Cremating" "Blasting" "Entombing" "Polar" "Vile" "of the Dragon" "of Dexterity" "of Intelligence" "of Strength" "Fleet" "Seething" "Sapphire" "Carapaced" "Encased" "Vaporous" "Expediting" "of Athletics" "of Spirit" "of Cunning" "of Adaption" "of Shelter" "of Grounding" "of the Hearth" "of Resistance" "of Order" "of Potency" "of the Inquisitor" "of Menace" "of Blinding" "of the Assassin" "of Taunting" "of Phasing" "of Ashes" "of Glaciation" "of Arcing" "of Collision" "of the Inferno" "of Venom" "of Stifling" "of Distraction" "of Delaying" "of Training" "of Vampirism" "of Command" "of Acclimatisation" "of Authority" "Malicious" "Tempered" "of Shocking" "of Chilling" "Resonating" "Motivating" "Foul-tongued"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D7 $type->rareid $tier->idaj_mixer
	Identified True
	Rarity Rare
	Class == "Abyss Jewels" "Jewels"
	BaseType == "Ghastly Eye Jewel" "Hypnotic Eye Jewel" "Murderous Eye Jewel" "Searching Eye Jewel"
	HasExplicitMod >=4 "of the Lightning Rod" "Beclouded" "Sanguine" "Stalwart" "Healthy" "Resplendent" "Incandescent" "of the Deadeye" "Acuminate" "Flaring" "Electrocuting" "Discharging" "Cremating" "Blasting" "Entombing" "Polar" "Vile" "of the Dragon" "of Dexterity" "of Intelligence" "of Strength" "Fleet" "Seething" "Sapphire" "Carapaced" "Encased" "Vaporous" "Expediting" "of Athletics" "of Spirit" "of Cunning" "of Adaption" "of Shelter" "of Grounding" "of the Hearth" "of Resistance" "of Order" "of Potency" "of the Inquisitor" "of Menace" "of Blinding" "of the Assassin" "of Taunting" "of Phasing" "of Ashes" "of Glaciation" "of Arcing" "of Collision" "of the Inferno" "of Opportunity" "of Berserking" "of the Ranger" "Lancing" "of Unholy Might" "of Abuse" "of Enchanting" "of Hindering" "of Venom" "of Stifling" "of Distraction" "of Delaying" "of Training" "of Vampirism" "of Command" "of Acclimatisation" "of Authority" "Malicious" "Tempered" "of Shocking" "of Chilling" "Resonating" "Motivating" "Foul-tongued" "of Insulating" "of Fireproofing" "of Heating" "of Poise" "of the Tourniquet"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0617] ID Mod exceptions - override id mod matching section

#------------------------------------

Show # %D3 $type->rareid $tier->t1veil
	Identified True
	Rarity Rare
	HasExplicitMod "Elreon's Veiled"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D0 $type->rareid $tier->t2veil

# Identified True

# Rarity Rare

# HasExplicitMod "Leo's Veiled" "Rin's Veiled" "Vagan's Veiled" "Vorici's Veiled" "Gravicius' Veiled" "Guff's Veiled" "Haku's" "It That Fled's Veiled" "Korell's Veiled" "of Aisling's Veil" "of Cameria's Veil" "of Hillock's Veil" "of Janus' Veil" "of Jorgin's Veil" "Riker" "Tora's Veiled"

# SetFontSize 45

# SetTextColor 0 240 190 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 47 0 74 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 2 Blue Diamond

#===============================================================================================================

# [[0700]] IDENTIFIED MOD FILTERING - DUAL MODS

#===============================================================================================================

# !! Waypoint c1.idmod.dualmod.all : "Identified Mods - Valuable Dual Mods" : "Gear - Exotic"

Show # %D5 $type->rareblendid $tier->wcastermin
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Rune Daggers" "Sceptres" "Shields" "Wands"
	HasExplicitMod >=3 "Runic" "Glyphic" "Flame Shaper's" "Frost Singer's" "Thunderhand's" "Mad Lord's" "Xoph's" "Tul's" "Esh's" "Martinet's" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "Magister's" "Archon's" "of Unmaking" "of Finesse" "of Destruction" "of Ferocity" "Lich's" "Carbonising" "Crystalising" "Vapourising"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareblendid $tier->wsmallarmorsblend
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Boots" "Gloves" "Helmets"
	HasExplicitMod >=3 "Overseer's" "Hellion's" "Cheetah's" "of Nullification" "of Abjuration" "Athlete's" "of the Godslayer" "of the Blur" "of the Polymath" "of Bameth" "of Exile" "of Tzteosh" "of the Magma" "of Haast" "of the Ice" "of Ephij" "of the Lightning" "of the Span" "of the Rainbow" "of Lioneye" "of Grandmastery" "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareblendid $tier->wringsblend
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Rings"
	HasExplicitMod >=3 "Athlete's" "Virile" "Ultramarine" "Dazzling" "of Fleshbinding" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Tzteosh" "of the Magma" "of Haast" "of the Ice" "of Ephij" "of the Lightning" "of the Span" "of Legerdemain" "of the Ranger" "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareblendid $tier->wamuletsblend
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Amulets"
	HasExplicitMod >=3 "Athlete's" "Virile" "Ultramarine" "Dazzling" "of the Multiverse" "of Fleshbinding" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Tzteosh" "of the Magma" "of Haast" "of the Ice" "of Ephij" "of the Lightning" "of the Span" "of Legerdemain" "of the Underground" "Subterranean" "Xopec's" "of Guatelitzi" "Guatelitzi's" "of Puhuarte" "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Destruction" "of Dissolution" "Unassailable" "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareblendid $tier->wbeltsblend
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Belts"
	HasExplicitMod >=3 "Fecund" "Blue" "Dazzling" "of Recuperation" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Bameth" "of Exile" "of Tzteosh" "of the Magma" "of Haast" "of the Ice" "of Ephij" "of the Lightning" "of the Span" "of Reveling" "Enveloped" "Devastating" "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->rareblendid $tier->weleattackblend
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Bows" "Claws" "Daggers" "Thrusting One Hand Swords" "Wands"
	HasExplicitMod >=3 "Carbonising" "Cremating" "Crystalising" "Entombing" "Vapourising" "Electrocuting" "Matatl's" "Tacati" "Topotante's" "of the Underground" "Subterranean" "of Many" "of Celebration" "of Incision" "of Destruction" "of Ferocity" "Devastating" "Merciless" "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#===============================================================================================================

# [[0800]] IDENTIFIED MOD FILTERING - SINGLE MODS

#===============================================================================================================

# !! Waypoint c1.idmod.singlemod.all : "Identified Mods - Single Mods and low priority combinations" : "Gear - Exotic"

#------------------------------------

# [0801] Top Value

#------------------------------------

Show # %D5 $type->magicid $tier->t1phys
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	HasExplicitMod >=1 "Merciless"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D4 $type->magicid $tier->t1caster
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Rune Daggers" "Sceptres" "Shields" "Wands"
	HasExplicitMod >=1 "Magister's" "Archon's" "Martinet's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->magicid $tier->t1proj
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Bows" "Wands"
	HasExplicitMod >=1 "of Many"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D8 $type->magicid $tier->t1amu
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Amulets"
	HasExplicitMod >=1 "Exalter's" "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Dissolution"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->magicid $tier->t1minionhelm
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Helmets"
	HasExplicitMod >=1 "Overseer's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#------------------------------------

# [0802] Uncorrupted Mods

#------------------------------------

Show # %D5 $type->magicid $tier->t2amu
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Amulets"
	HasExplicitMod >=1 "Vulcanist's" "Rimedweller's" "Stormbrewer's" "Behemoth's" "Provocateur's" "of Dissolution"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D5 $type->magicid $tier->t2quiver
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Quivers"
	HasExplicitMod >=1 "of Splintering"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D4 $type->magicid $tier->t2suppress
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Boots" "Gloves" "Helmets"
	HasExplicitMod >=1 "of Nullification"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#Show # %D4 $type->magicid $tier->t2caster

# Mirrored False

# Corrupted False

# Identified True

# Rarity Normal Magic Rare

# Class == "Rune Daggers" "Sceptres" "Shields" "Wands"

# HasExplicitMod >=1 "Lithomancer's" "Flame Shaper's" "Frost Singer's" "Thunderhand's" "Runic"

# SetFontSize 45

# SetTextColor 0 240 190 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 20 20 0 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Diamond

#Show # %D4 $type->magicid $tier->t2shield

# Mirrored False

# Corrupted False

# Identified True

# Rarity Normal Magic Rare

# Class == "Shields"

# HasExplicitMod >=1 "of the Deathless"

# SetFontSize 45

# SetTextColor 0 240 190 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 20 20 0 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Diamond

#Show # %D4 $type->magicid $tier->t2purephys

# Mirrored False

# Corrupted False

# Identified True

# Rarity Normal Magic Rare

# Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# HasExplicitMod >=1 "Merciless" "Dictator's"

# SetFontSize 45

# SetTextColor 0 240 190 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 20 20 0 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Diamond

#Show # %D4 $type->magicid $tier->t2dotwand

# Mirrored False

# Corrupted False

# Identified True

# Rarity Normal Magic Rare

# Class == "Rune Daggers" "Wands"

# HasExplicitMod >=1 "of Dissolution" "of Exsanguinating"

# SetFontSize 45

# SetTextColor 0 240 190 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 20 20 0 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Diamond

#Show # %D4 $type->magicid $tier->t2sceptre

# Mirrored False

# Corrupted False

# Identified True

# Rarity Normal Magic Rare

# Class == "Sceptres"

# HasExplicitMod >=1 "of the Fanatical" "of Dissolution"

# SetFontSize 45

# SetTextColor 0 240 190 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 20 20 0 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Diamond

#Show # %D4 $type->magicid $tier->t2eleweapons

# Mirrored False

# Corrupted False

# Identified True

# Rarity Normal Magic Rare

# Class == "Bows" "Claws" "Daggers" "Thrusting One Hand Swords" "Wands"

# HasExplicitMod >=1 "Carbonising" "Crystalising" "Vapourising"

# SetFontSize 45

# SetTextColor 0 240 190 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 20 20 0 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Diamond

#------------------------------------

# [0803] Flasks and Tinctures

#------------------------------------

Show # %D5 $type->magicid $tier->bleedlifeflask
	Mirrored False
	Corrupted False
	Identified True
	BaseType == "Divine Life Flask" "Eternal Life Flask"
	HasExplicitMod >=2 "of Assuaging" "of Allaying" "Catalysed" "Panicked" "Bubbling" "Cautious" "Flagellant's" "Perpetual"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D6 $type->magicid $tier->doublemodutilflask
	Mirrored False
	Corrupted False
	Identified True
	BaseType == "Amethyst Flask" "Basalt Flask" "Bismuth Flask" "Diamond Flask" "Gold Flask" "Granite Flask" "Iron Flask" "Jade Flask" "Quartz Flask" "Quicksilver Flask" "Ruby Flask" "Sapphire Flask" "Silver Flask" "Stibnite Flask" "Sulphur Flask" "Topaz Flask"
	HasExplicitMod >=2 "of the Owl" "of the Armadillo" "of the Impala" "of the Cheetah" "of the Sanderling" "of Incision" "of the Eel" "of the Penguin" "of the Starfish" "of the Iguana" "Perpetual" "Surgeon's" "Flagellant's" "Alchemist's" "Experimenter's" "Chemist's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D3 $type->magicid $tier->singlemodutilflask
	Mirrored False
	Corrupted False
	Identified True
	BaseType == "Amethyst Flask" "Basalt Flask" "Bismuth Flask" "Diamond Flask" "Gold Flask" "Granite Flask" "Iron Flask" "Jade Flask" "Quartz Flask" "Quicksilver Flask" "Ruby Flask" "Sapphire Flask" "Silver Flask" "Stibnite Flask" "Sulphur Flask" "Topaz Flask"
	HasExplicitMod >=1 "of the Owl" "of the Armadillo" "of the Impala" "of the Cheetah" "of the Sanderling" "of Incision" "of the Eel" "of the Penguin" "of the Starfish" "of the Iguana" "Perpetual" "Surgeon's" "Flagellant's" "Alchemist's" "Experimenter's" "Chemist's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D6 $type->magicid $tier->doublemodtincture
	Mirrored False
	Corrupted False
	Identified True
	BaseType == "Blood Sap Tincture" "Oakbranch Tincture" "Prismatic Tincture" "Rosethorn Tincture"
	HasExplicitMod >=2 "of Dissolution" "of Overpowering" "of Ferocity" "of Mastery" "Horticultural" "Enriched" "Persevering"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

Show # %D4 $type->magicid $tier->singlemodtincture
	Mirrored False
	Corrupted False
	Identified True
	BaseType == "Blood Sap Tincture" "Oakbranch Tincture" "Prismatic Tincture" "Rosethorn Tincture"
	HasExplicitMod >=1 "of Dissolution" "of Overpowering" "of Ferocity" "of Mastery" "Horticultural" "Enriched" "Persevering"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 1 Purple Diamond

#===============================================================================================================

# [[0900]] High Priority Equipment Properties

#===============================================================================================================
#------------------------------------

# [0901] Perfection and Overquality Filtering

#------------------------------------

# !! Waypoint c3.gear.perfectionbased.all : "Crafting Bases - Perfection & Quality filtering" : "Gear - Exotic"

Show # %D9 $type->crafting->qualityperfection $tier->qualchancing
	Mirrored False
	Corrupted False
	Quality >= 28
	BaseType == "Riveted Boots" "Steel Kite Shield"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D9 $type->crafting->qualityperfection $tier->armors1q1
	Mirrored False
	Corrupted False
	Quality >= 28
	Class == "Body Armours" "Boots" "Gloves" "Helmets" "Shields"
	BaseType == "Apothecary's Gloves" "Archon Kite Shield" "Bone Helmet" "Cardinal Round Shield" "Colossal Tower Shield" "Conquest Lamellar" "Divine Crown" "Ezomyte Tower Shield" "Fingerless Silk Gloves" "Fossilised Spirit Shield" "Fugitive Boots" "Giantslayer Helmet" "Gripped Gloves" "Haunted Bascinet" "Lacquered Buckler" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Majestic Pelt" "Necrotic Armour" "Paladin Boots" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Royal Plate" "Sacred Chainmail" "Sacrificial Garb" "Spiked Gloves" "Supreme Spiked Shield" "Syndicate's Garb" "Titanium Spirit Shield" "Torturer's Mask" "Twilight Regalia" "Two-Toned Boots" "Velour Boots" "Velour Gloves" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->crafting->qualityperfection $tier->armors1q2
	Mirrored False
	Corrupted False
	Quality >= 24
	Class == "Body Armours" "Boots" "Gloves" "Helmets" "Shields"
	BaseType == "Apothecary's Gloves" "Archon Kite Shield" "Bone Helmet" "Cardinal Round Shield" "Colossal Tower Shield" "Conquest Lamellar" "Divine Crown" "Ezomyte Tower Shield" "Fingerless Silk Gloves" "Fossilised Spirit Shield" "Fugitive Boots" "Giantslayer Helmet" "Gripped Gloves" "Haunted Bascinet" "Lacquered Buckler" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Majestic Pelt" "Necrotic Armour" "Paladin Boots" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Royal Plate" "Sacred Chainmail" "Sacrificial Garb" "Spiked Gloves" "Supreme Spiked Shield" "Syndicate's Garb" "Titanium Spirit Shield" "Torturer's Mask" "Twilight Regalia" "Two-Toned Boots" "Velour Boots" "Velour Gloves" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D9 $type->crafting->qualityperfection $tier->weapont1q1
	Mirrored False
	Corrupted False
	Quality >= 28
	ItemLevel >= 83
	BaseType == "Artillery Quiver" "Battered Foil" "Broadhead Arrow Quiver" "Convoking Wand" "Copper Kris" "Despot Axe" "Feathered Arrow Quiver" "Gemini Claw" "Golden Kris" "Imperial Claw" "Imperial Skean" "Jewelled Foil" "Kinetic Wand" "Opal Sceptre" "Opal Wand" "Pagan Wand" "Platinum Kris" "Primal Arrow Quiver" "Profane Wand" "Prophecy Wand" "Reaver Axe" "Reaver Sword" "Reflex Bow" "Short Bow" "Siege Axe" "Spine Bow" "Thicket Bow" "Vaal Axe" "Void Sceptre" "Whalebone Rapier"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->crafting->qualityperfection $tier->weapont2q1
	Mirrored False
	Corrupted False
	Quality >= 28
	ItemLevel >= 83
	BaseType == "Ambusher" "Basket Rapier" "Behemoth Mace" "Citadel Bow" "Convening Wand" "Corsair Sword" "Eclipse Staff" "Eternal Sword" "Exquisite Blade" "Ezomyte Blade" "Ezomyte Staff" "Fleshripper" "Grove Bow" "Harbinger Bow" "Heavy Arrow Quiver" "Imperial Bow" "Judgement Staff" "Karui Chopper" "Karui Sceptre" "Lathi" "Legion Hammer" "Maelström Staff" "Maraketh Bow" "Meatgrinder" "Piledriver" "Royal Axe" "Runic Hatchet" "Sai" "Sambar Sceptre" "Spiraled Foil" "Sundering Axe" "Vile Arrow Quiver"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D8 $type->crafting->qualityperfection $tier->weapont1q2
	Mirrored False
	Corrupted False
	Quality >= 24
	ItemLevel >= 83
	BaseType == "Artillery Quiver" "Battered Foil" "Broadhead Arrow Quiver" "Convoking Wand" "Copper Kris" "Despot Axe" "Feathered Arrow Quiver" "Gemini Claw" "Golden Kris" "Imperial Claw" "Imperial Skean" "Jewelled Foil" "Kinetic Wand" "Opal Sceptre" "Opal Wand" "Pagan Wand" "Platinum Kris" "Primal Arrow Quiver" "Profane Wand" "Prophecy Wand" "Reaver Axe" "Reaver Sword" "Reflex Bow" "Short Bow" "Siege Axe" "Spine Bow" "Thicket Bow" "Vaal Axe" "Void Sceptre" "Whalebone Rapier"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D7 $type->crafting->qualityperfection $tier->weapont2q2
	Mirrored False
	Corrupted False
	Quality >= 24
	ItemLevel >= 83
	BaseType == "Ambusher" "Basket Rapier" "Behemoth Mace" "Citadel Bow" "Convening Wand" "Corsair Sword" "Eclipse Staff" "Eternal Sword" "Exquisite Blade" "Ezomyte Blade" "Ezomyte Staff" "Fleshripper" "Grove Bow" "Harbinger Bow" "Heavy Arrow Quiver" "Imperial Bow" "Judgement Staff" "Karui Chopper" "Karui Sceptre" "Lathi" "Legion Hammer" "Maelström Staff" "Maraketh Bow" "Meatgrinder" "Piledriver" "Royal Axe" "Runic Hatchet" "Sai" "Sambar Sceptre" "Spiraled Foil" "Sundering Axe" "Vile Arrow Quiver"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->crafting->qualityperfection $tier->anyoverqualityperf
	Mirrored False
	Corrupted False
	Quality >= 30
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D3 $type->crafting->qualityperfection $tier->anyoverqualityhigh
	Mirrored False
	Corrupted False
	Quality >= 26
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#Show # %D0 $type->crafting->qualityperfection $tier->anyoverquality

# Mirrored False

# Corrupted False

# Quality >= 21

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# SetFontSize 45

# SetBorderColor 0 240 190 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 2 Blue Diamond

#Show # %D5 $type->crafting->qualityperfection $tier->perfectioncrafting

# Mirrored False

# Corrupted False

# ItemLevel >= 84

# BaseDefencePercentile >= 99

# Class == "Body Armours" "Boots" "Gloves" "Helmets" "Shields"

# BaseType == "Apothecary's Gloves" "Archon Kite Shield" "Bone Helmet" "Cardinal Round Shield" "Colossal Tower Shield" "Conquest Lamellar" "Divine Crown" "Ezomyte Tower Shield" "Fingerless Silk Gloves" "Fossilised Spirit Shield" "Fugitive Boots" "Giantslayer Helmet" "Gripped Gloves" "Haunted Bascinet" "Lacquered Buckler" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Majestic Pelt" "Necrotic Armour" "Paladin Boots" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Royal Plate" "Sacred Chainmail" "Sacrificial Garb" "Spiked Gloves" "Supreme Spiked Shield" "Syndicate's Garb" "Titanium Spirit Shield" "Torturer's Mask" "Twilight Regalia" "Two-Toned Boots" "Velour Boots" "Velour Gloves" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"

# SetFontSize 45

# SetTextColor 0 240 190 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 20 20 0 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 1 Blue Diamond

#------------------------------------

# [0902] Memory Strand Gear

#------------------------------------

# !! Waypoint c3.gear.memorystrand.all : "Crafting Bases - Memory Stranded" : "Gear - Memory Stranded"

Show # %D8 $type->gear->memorystrand $tier->strandedfractured
	FracturedItem True
	Mirrored False
	Corrupted False
	MemoryStrands >= 1
	Rarity Normal Magic Rare
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->gear->memorystrand $tier->strandedveiled
	Mirrored False
	Corrupted False
	Identified True
	MemoryStrands >= 1
	Rarity Normal Magic Rare
	HasExplicitMod "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->gear->memorystrand $tier->t1high
	Mirrored False
	Corrupted False
	MemoryStrands >= 60
	Rarity Normal Magic Rare
	BaseType == "Agate Amulet" "Amethyst Ring" "Citrine Amulet" "Conquest Lamellar" "Crystal Belt" "Divine Crown" "Giantslayer Helmet" "Haunted Bascinet" "Iolite Ring" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Majestic Pelt" "Necrotic Armour" "Onyx Amulet" "Opal Ring" "Paladin Boots" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Prismatic Ring" "Royal Plate" "Sacred Chainmail" "Sacrificial Garb" "Steel Ring" "Stygian Vise" "Syndicate's Garb" "Torturer's Mask" "Turquoise Amulet" "Twilight Regalia" "Two-Stone Ring" "Velour Boots" "Velour Gloves" "Vermillion Ring" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->gear->memorystrand $tier->t1
	Mirrored False
	Corrupted False
	MemoryStrands >= 15
	Rarity Normal Magic Rare
	BaseType == "Agate Amulet" "Amethyst Ring" "Citrine Amulet" "Conquest Lamellar" "Crystal Belt" "Divine Crown" "Giantslayer Helmet" "Haunted Bascinet" "Iolite Ring" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Majestic Pelt" "Necrotic Armour" "Onyx Amulet" "Opal Ring" "Paladin Boots" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Prismatic Ring" "Royal Plate" "Sacred Chainmail" "Sacrificial Garb" "Steel Ring" "Stygian Vise" "Syndicate's Garb" "Torturer's Mask" "Turquoise Amulet" "Twilight Regalia" "Two-Stone Ring" "Velour Boots" "Velour Gloves" "Vermillion Ring" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->gear->memorystrand $tier->t2high
	Mirrored False
	Corrupted False
	MemoryStrands >= 60
	Rarity Normal Magic Rare
	BaseType == "Amber Amulet" "Ancient Mask" "Apothecary's Gloves" "Arcanist Slippers" "Archon Kite Shield" "Artillery Quiver" "Assassin's Boots" "Astral Leather" "Battered Foil" "Blue Pearl Amulet" "Bone Helmet" "Bone Ring" "Broadhead Arrow Quiver" "Cardinal Round Shield" "Cerulean Ring" "Chimerascale Boots" "Chimerascale Gauntlets" "Colossal Tower Shield" "Conqueror's Helmet" "Conquest Helmet" "Convoking Wand" "Copper Kris" "Coral Ring" "Crusader Boots" "Crusader Gloves" "Deicide Mask" "Despot Axe" "Diamond Ring" "Dire Pelt" "Dragonscale Boots" "Dragonscale Gauntlets" "Eternal Burgonet" "Ezomyte Tower Shield" "Faithful Helmet" "Feathered Arrow Quiver" "Fingerless Silk Gloves" "Fossilised Spirit Shield" "Fugitive Boots" "Full Wyvernscale" "Gemini Claw" "General's Helmet" "Golden Kris" "Goliath Gauntlets" "Goliath Greaves" "Grand Ringmail" "Gripped Gloves" "Grizzly Pelt" "Harmonic Spirit Shield" "Harpyskin Boots" "Harpyskin Gloves" "Heavy Belt" "Hubris Circlet" "Hydrascale Boots" "Hydrascale Gauntlets" "Imperial Claw" "Imperial Skean" "Infiltrator Boots" "Infiltrator Mitts" "Jade Amulet" "Jester Mask" "Jewelled Foil" "Kinetic Wand" "Knight Helm" "Lacquered Buckler" "Lapis Amulet" "Lathi" "Leather Belt" "Legion Boots" "Legion Gloves" "Legion Plate" "Lion Pelt" "Marble Amulet" "Marshall's Brigandine" "Martyr Boots" "Martyr Gloves" "Mind Cage" "Mirrored Spiked Shield" "Moonlit Circlet" "Moonstone Ring" "Murder Boots" "Murder Mitts" "Nightmare Bascinet" "Nightweave Robe" "Opal Sceptre" "Opal Wand" "Pagan Wand" "Paladin Crown" "Paladin's Hauberk" "Platinum Kris" "Praetor Crown" "Precursor Gauntlets" "Precursor Greaves" "Primal Arrow Quiver" "Profane Wand" "Prophecy Wand" "Prophet Crown" "Reaver Axe" "Reaver Sword" "Reflex Bow" "Royal Burgonet" "Ruby Ring" "Sage Gloves" "Sage Slippers" "Sanguine Raiment" "Sapphire Ring" "Short Bow" "Siege Axe" "Slink Boots" "Slink Gloves" "Soldier Boots" "Sorcerer Boots" "Sorcerer Gloves" "Spiked Gloves" "Spine Bow" "Stealth Boots" "Sunfire Circlet" "Supreme Leather" "Supreme Spiked Shield" "Thicket Bow" "Titan Gauntlets" "Titan Greaves" "Titan Plate" "Titanium Spirit Shield" "Topaz Ring" "Tornado Wand" "Torturer Garb" "Two-Toned Boots" "Unset Ring" "Vaal Axe" "Vaal Gauntlets" "Vaal Greaves" "Vaal Mask" "Vanguard Belt" "Void Sceptre" "Whalebone Rapier"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->gear->memorystrand $tier->t2
	Mirrored False
	Corrupted False
	MemoryStrands >= 20
	Rarity Normal Magic Rare
	BaseType == "Amber Amulet" "Ancient Mask" "Apothecary's Gloves" "Arcanist Slippers" "Archon Kite Shield" "Artillery Quiver" "Assassin's Boots" "Astral Leather" "Battered Foil" "Blue Pearl Amulet" "Bone Helmet" "Bone Ring" "Broadhead Arrow Quiver" "Cardinal Round Shield" "Cerulean Ring" "Chimerascale Boots" "Chimerascale Gauntlets" "Colossal Tower Shield" "Conqueror's Helmet" "Conquest Helmet" "Convoking Wand" "Copper Kris" "Coral Ring" "Crusader Boots" "Crusader Gloves" "Deicide Mask" "Despot Axe" "Diamond Ring" "Dire Pelt" "Dragonscale Boots" "Dragonscale Gauntlets" "Eternal Burgonet" "Ezomyte Tower Shield" "Faithful Helmet" "Feathered Arrow Quiver" "Fingerless Silk Gloves" "Fossilised Spirit Shield" "Fugitive Boots" "Full Wyvernscale" "Gemini Claw" "General's Helmet" "Golden Kris" "Goliath Gauntlets" "Goliath Greaves" "Grand Ringmail" "Gripped Gloves" "Grizzly Pelt" "Harmonic Spirit Shield" "Harpyskin Boots" "Harpyskin Gloves" "Heavy Belt" "Hubris Circlet" "Hydrascale Boots" "Hydrascale Gauntlets" "Imperial Claw" "Imperial Skean" "Infiltrator Boots" "Infiltrator Mitts" "Jade Amulet" "Jester Mask" "Jewelled Foil" "Kinetic Wand" "Knight Helm" "Lacquered Buckler" "Lapis Amulet" "Lathi" "Leather Belt" "Legion Boots" "Legion Gloves" "Legion Plate" "Lion Pelt" "Marble Amulet" "Marshall's Brigandine" "Martyr Boots" "Martyr Gloves" "Mind Cage" "Mirrored Spiked Shield" "Moonlit Circlet" "Moonstone Ring" "Murder Boots" "Murder Mitts" "Nightmare Bascinet" "Nightweave Robe" "Opal Sceptre" "Opal Wand" "Pagan Wand" "Paladin Crown" "Paladin's Hauberk" "Platinum Kris" "Praetor Crown" "Precursor Gauntlets" "Precursor Greaves" "Primal Arrow Quiver" "Profane Wand" "Prophecy Wand" "Prophet Crown" "Reaver Axe" "Reaver Sword" "Reflex Bow" "Royal Burgonet" "Ruby Ring" "Sage Gloves" "Sage Slippers" "Sanguine Raiment" "Sapphire Ring" "Short Bow" "Siege Axe" "Slink Boots" "Slink Gloves" "Soldier Boots" "Sorcerer Boots" "Sorcerer Gloves" "Spiked Gloves" "Spine Bow" "Stealth Boots" "Sunfire Circlet" "Supreme Leather" "Supreme Spiked Shield" "Thicket Bow" "Titan Gauntlets" "Titan Greaves" "Titan Plate" "Titanium Spirit Shield" "Topaz Ring" "Tornado Wand" "Torturer Garb" "Two-Toned Boots" "Unset Ring" "Vaal Axe" "Vaal Gauntlets" "Vaal Greaves" "Vaal Mask" "Vanguard Belt" "Void Sceptre" "Whalebone Rapier"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show # %D4 $type->gear->memorystrand $tier->t3high
	Mirrored False
	Corrupted False
	MemoryStrands >= 60
	Rarity Normal Magic Rare
	BaseType == "Ambush Boots" "Ambush Mitts" "Ambusher" "Ancient Gauntlets" "Ancient Greaves" "Antique Gauntlets" "Antique Greaves" "Arcane Vestment" "Arcanist Gloves" "Assassin's Mitts" "Astral Plate" "Basket Rapier" "Behemoth Mace" "Blasting Wand" "Carnal Boots" "Carnal Mitts" "Carnal Sceptre" "Chain Belt" "Champion Kite Shield" "Citadel Bow" "Cloth Belt" "Conjurer Boots" "Conjurer Gloves" "Convening Wand" "Coral Amulet" "Corsair Sword" "Crusader Buckler" "Demon's Horn" "Eclipse Staff" "Elegant Round Shield" "Eternal Sword" "Exquisite Blade" "Ezomyte Axe" "Ezomyte Blade" "Ezomyte Burgonet" "Ezomyte Staff" "Fleshripper" "Fluted Bascinet" "Full Dragonscale" "Glorious Plate" "Gold Amulet" "Gold Ring" "Grove Bow" "Gutting Knife" "Harbinger Bow" "Harlequin Mask" "Heathen Wand" "Heavy Arrow Quiver" "Imperial Bow" "Imperial Buckler" "Imperial Staff" "Iron Ring" "Judgement Staff" "Karui Chopper" "Karui Sceptre" "Legion Hammer" "Maelström Staff" "Magistrate Crown" "Maraketh Bow" "Meatgrinder" "Mosaic Kite Shield" "Nightmare Mace" "Paua Amulet" "Paua Ring" "Pig-Faced Bascinet" "Piledriver" "Pinnacle Tower Shield" "Platinum Sceptre" "Regicide Mask" "Riveted Boots" "Royal Axe" "Runic Hatchet" "Rustic Sash" "Sadist Garb" "Sai" "Saint's Hauberk" "Saintly Chainmail" "Sambar Sceptre" "Samite Slippers" "Samnite Helmet" "Seaglass Amulet" "Serpentscale Boots" "Serpentscale Gauntlets" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Silken Hood" "Sinner Tricorne" "Solaris Circlet" "Soldier Gloves" "Spiraled Foil" "Stealth Gloves" "Studded Belt" "Sundering Axe" "Triumphant Lamellar" "Vaal Regalia" "Vaal Sceptre" "Vaal Spirit Shield" "Vile Arrow Quiver" "Wyrmscale Boots" "Wyrmscale Gauntlets" "Zealot Boots" "Zealot Gloves" "Zodiac Leather"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D2 $type->gear->memorystrand $tier->t3

# Mirrored False

# Corrupted False

# MemoryStrands >= 25

# Rarity Normal Magic Rare

# BaseType == "Ambush Boots" "Ambush Mitts" "Ambusher" "Ancient Gauntlets" "Ancient Greaves" "Antique Gauntlets" "Antique Greaves" "Arcane Vestment" "Arcanist Gloves" "Assassin's Mitts" "Astral Plate" "Basket Rapier" "Behemoth Mace" "Blasting Wand" "Carnal Boots" "Carnal Mitts" "Carnal Sceptre" "Chain Belt" "Champion Kite Shield" "Citadel Bow" "Cloth Belt" "Conjurer Boots" "Conjurer Gloves" "Convening Wand" "Coral Amulet" "Corsair Sword" "Crusader Buckler" "Demon's Horn" "Eclipse Staff" "Elegant Round Shield" "Eternal Sword" "Exquisite Blade" "Ezomyte Axe" "Ezomyte Blade" "Ezomyte Burgonet" "Ezomyte Staff" "Fleshripper" "Fluted Bascinet" "Full Dragonscale" "Glorious Plate" "Gold Amulet" "Gold Ring" "Grove Bow" "Gutting Knife" "Harbinger Bow" "Harlequin Mask" "Heathen Wand" "Heavy Arrow Quiver" "Imperial Bow" "Imperial Buckler" "Imperial Staff" "Iron Ring" "Judgement Staff" "Karui Chopper" "Karui Sceptre" "Legion Hammer" "Maelström Staff" "Magistrate Crown" "Maraketh Bow" "Meatgrinder" "Mosaic Kite Shield" "Nightmare Mace" "Paua Amulet" "Paua Ring" "Pig-Faced Bascinet" "Piledriver" "Pinnacle Tower Shield" "Platinum Sceptre" "Regicide Mask" "Riveted Boots" "Royal Axe" "Runic Hatchet" "Rustic Sash" "Sadist Garb" "Sai" "Saint's Hauberk" "Saintly Chainmail" "Sambar Sceptre" "Samite Slippers" "Samnite Helmet" "Seaglass Amulet" "Serpentscale Boots" "Serpentscale Gauntlets" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Silken Hood" "Sinner Tricorne" "Solaris Circlet" "Soldier Gloves" "Spiraled Foil" "Stealth Gloves" "Studded Belt" "Sundering Axe" "Triumphant Lamellar" "Vaal Regalia" "Vaal Sceptre" "Vaal Spirit Shield" "Vile Arrow Quiver" "Wyrmscale Boots" "Wyrmscale Gauntlets" "Zealot Boots" "Zealot Gloves" "Zodiac Leather"

# SetFontSize 45

# SetBorderColor 0 240 190 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 2 Blue Diamond

Show # %D3 $type->gear->memorystrand $tier->anyhigh
	Mirrored False
	Corrupted False
	MemoryStrands >= 70
	Rarity Normal Magic Rare
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D2 $type->gear->memorystrand $tier->any

# Mirrored False

# Corrupted False

# MemoryStrands >= 1

# Rarity Normal Magic Rare

# SetFontSize 40

# SetBorderColor 0 240 190 180

# PlayEffect Blue Temp

#===============================================================================================================

# [[1000]] IDENTIFIED MOD - CORRUPTED ITEMS

#===============================================================================================================

# !! Waypoint c1.idmod.corruptedmod : "Identified Mods - Items with corrupted implicits" : "Gear - Exotic"

Show # %D4 $type->corruptedid $tier->gloves_life_based
	Corrupted True
	Identified True
	CorruptedMods 1
	Class == "Gloves"
	HasExplicitMod >=1 "Athlete's" "Virile" "of Puhuarte" "of the Underground" "Subterranean" "Elevated " "of Nullification" "of Abjuration" "of Grandmastery" "of Bameth"
	HasExplicitMod >=3 "Athlete's" "Virile" "of Puhuarte" "of the Underground" "Subterranean" "Elevated " "of Nullification" "of Abjuration" "of Grandmastery" "of Bameth" "of the Godslayer" "of the Gods" "of the Blur" "of the Wind" "of the Polymath" "of the Genius" "of Exile" "of Expulsion" "of Eviction" "of Tzteosh" "of the Magma" "of the Volcano" "of the Furnace" "of Haast" "of the Ice" "of the Polar Bear" "of the Walrus" "of Ephij" "of the Lightning" "of the Maelstrom" "of the Tempest" "of the Span" "of the Rainbow" "of Variegation" "of Revoking" "of Mastery" "of Lioneye" "of the Ranger" "Zaffre" "Rotund" "Abbot's" "Prior's" "Ram's" "Fawn's" "Nautilus's" "Urchin's" "of the Essence" "Essences" "of Tacati" "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 250 0 0 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->corruptedid $tier->quiv_hit
	Corrupted True
	Identified True
	CorruptedMods 1
	ItemLevel >= 80
	Class == "Quivers"
	HasExplicitMod >=1 "Impaling" "of the Underground" "Subterranean" "Elevated " "of Splintering" "Fecund" "Athlete's" "of Destruction" "of Ferocity" "of Grandmastery" "of Dissolution" "of Melting" "of Rending" "Devastating"
	HasExplicitMod >=3 "Impaling" "Lacerating" "Incisive" "of the Underground" "Subterranean" "Elevated " "of Splintering" "Fecund" "Athlete's" "Virile" "of the Blur" "of the Wind" "of Tzteosh" "of the Magma" "of Haast" "of the Ice" "of Ephij" "of the Lightning" "of Bameth" "of Exile" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Flaring" "Cremating" "Entombing" "Electrocuting" "Devastating" "Overpowering" "of Grandmastery" "of Mastery" "of Ease" "of Lioneye" "of the Ranger" "of Dissolution" "of the Gale" "of Destruction" "of Ferocity" "of Fury" "of Rending" "of Incision" "of Penetrating"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 250 0 0 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->corruptedid $tier->quiv_dot
	Corrupted True
	Identified True
	CorruptedMods 1
	ItemLevel >= 80
	Class == "Quivers"
	HasExplicitMod >=1 "Impaling" "of the Underground" "Subterranean" "Elevated " "of Splintering" "Fecund" "Athlete's" "of Destruction" "of Ferocity" "of Grandmastery" "of Dissolution" "of Melting" "of Rending" "Devastating"
	HasExplicitMod >=3 "Impaling" "Lacerating" "Incisive" "of the Underground" "Subterranean" "Elevated " "of Splintering" "Fecund" "Athlete's" "Virile" "of the Blur" "of the Wind" "of Tzteosh" "of the Magma" "of Haast" "of the Ice" "of Ephij" "of the Lightning" "of Bameth" "of Exile" "of the Essence" "Essences" "of Tacati" "of Puhuarte" "Veil" "Cremating" "Flaring" "Devastating" "of Grandmastery" "of Mastery" "of Ease" "of Lioneye" "of the Ranger" "of Dissolution" "of Melting" "of Liquefaction" "of the Gale" "of Destruction" "of Rending"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 250 0 0 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#===============================================================================================================

# [[1100]] Exotic Mods Filtering

#===============================================================================================================

#------------------------------------

# [1101] Veiled/Betrayal - low prio veiled items

#------------------------------------

# !! Waypoint c1.idmod.veil.all : "Identified Mods - Low priority veiled items (not member specific)" : "Gear - Regular Rares"

Show # %D8 $type->exoticmods $tier->fracturedveiled
	FracturedItem True
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	HasExplicitMod "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D7 $type->exoticmods $tier->fracturedincursion
	FracturedItem True
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	HasExplicitMod "Citaqualotl" "Guatelitzi" "Matatl" "Puhuarte" "Tacati" "Topotante" "Xopec"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show # %D4 $type->exoticmods $tier->duoveil
	Mirrored False
	Corrupted False
	Identified True
	Rarity Rare
	HasExplicitMod "Veiled"
	HasExplicitMod "of the Veil"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#------------------------------------

# [1102] Incursion/Temple Mods

#------------------------------------

# !! Waypoint c1.idmod.league.all : "Identified Mods - Incursion mod filtering" : "Gear - Exotic"

Show # %D5 $type->exoticmods $tier->incursionspeedtraps
	Identified True
	Rarity Rare
	Class == "Boots"
	HasExplicitMod "Matatl's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exoticmods $tier->incursioncaster
	Identified True
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Shields" "Staves" "Wands"
	HasExplicitMod "Matatl's" "Tacati" "Topotante's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exoticmods $tier->incursionelemental
	Identified True
	Rarity Rare
	Class == "Bows" "Claws" "Daggers" "Thrusting One Hand Swords" "Wands"
	HasExplicitMod "Topotante's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exoticmods $tier->incursionjwlry
	Identified True
	Rarity Rare
	Class == "Amulets" "Belts" "Rings"
	HasExplicitMod "Citaqualotl" "Guatelitzi" "Matatl" "Puhuarte" "Tacati" "Topotante" "Xopec"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exoticmods $tier->incursionglovehelm
	Identified True
	Rarity Rare
	Class == "Gloves" "Helmets"
	HasExplicitMod "Puhuarte" "Topotante"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exoticmods $tier->incursionattack
	Identified True
	Rarity Rare
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	HasExplicitMod "of Tacati" "Tacati's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->exoticmods $tier->incursionlifechest
	Identified True
	Rarity Rare
	Class == "Body Armours"
	HasExplicitMod "Guatelitzi's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->exoticmods $tier->incursionminion
	Identified True
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Rune Daggers" "Sceptres" "Staves" "Thrusting One Hand Swords" "Wands"
	HasExplicitMod "Citaqualotl's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->exoticmods $tier->incursionmagic
	Identified True
	Rarity Magic
	HasExplicitMod "Citaqualotl" "Guatelitzi" "Matatl" "Puhuarte" "Tacati" "Topotante" "Xopec"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#Show # %D2 $type->exoticmods $tier->incursionrandom

# Identified True

# Rarity Rare

# HasExplicitMod "Citaqualotl" "Guatelitzi" "Matatl" "Puhuarte" "Tacati" "Topotante" "Xopec"

# SetFontSize 45

# SetBorderColor 0 240 190 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 2 Blue Diamond

#------------------------------------

# [1103] Necropolis

#------------------------------------

Show # %D8 $type->exoticmods $tier->necropoliscraft
	Identified True
	Rarity Rare
	HasExplicitMod "Haunted" "of Haunting"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#------------------------------------

# [1104] Bestiary

#------------------------------------

Show # %D5 $type->exoticmods $tier->bestiaryvaluable
	Identified True
	Rarity Rare
	HasExplicitMod "of Farrul" "of Fenumus"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->exoticmods $tier->bestiaryother
	Identified True
	Rarity Rare
	HasExplicitMod "of Craiceann" "of Saqawal"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#------------------------------------

# [1105] Other

#------------------------------------

Show # %D9 $type->exoticmods $tier->delvefractured
	FracturedItem True
	Identified True
	Rarity Normal Magic Rare
	HasExplicitMod "of the Underground" "Subterranean"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->exoticmods $tier->delve
	Identified True
	Rarity Normal Magic Rare
	HasExplicitMod "of the Underground" "Subterranean"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exoticmods $tier->mercenaryothers
	Identified True
	Rarity Normal Magic Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Gloves" "Helmets" "Quivers" "Rings" "Shields"
	HasExplicitMod "Infamous" "of Infamy"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exoticmods $tier->mercenaryweapons
	Identified True
	Rarity Normal Magic Rare
	Class == "Bows" "Staves" "Wands" "Warstaves"
	HasExplicitMod "Infamous"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D3 $type->exoticmods $tier->warband
	Identified True
	Rarity Normal Magic Rare
	HasExplicitMod "Betrayer's" "Brinerot" "Deceiver's" "Mutewind" "Redblade" "Turncoat's"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#Show # %D2 $type->exoticmods $tier->essence

# Identified True

# Rarity Rare

# HasExplicitMod "of the Essence" "Essences"

# SetFontSize 40

# SetBorderColor 0 240 190 180

# PlayEffect Blue Temp

#Show # %D1 $type->exoticmods $tier->crafting

# Identified True

# Rarity Rare

# HasExplicitMod "of Crafting" "of Spellcraft" "of Weaponcraft"

# SetFontSize 40

# SetBorderColor 0 240 190 180

# PlayEffect Blue Temp

#===============================================================================================================

# [[1200]] Exotic Item Classes

#===============================================================================================================

# !! Waypoint c2.exotic.artefacts.all : "Exotic - Voidstones, Quest Items, Trinkets, Fishing items, Pieces" : "Gear - Exotic"

Show # $type->artefact->misc $tier->anyimbued
	Imbued True
	SetFontSize 45
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # $type->artefact->misc $tier->anysynth
	SynthesisedItem True
	Rarity Normal Magic Rare
	SetFontSize 45
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # $type->artefact->misc $tier->voidstones
	BaseType == "Ceremonial Voidstone" "Decayed Voidstone" "Eldritch Voidstone" "Originator Voidstone"
	SetFontSize 45
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # $type->artefact->misc $tier->anytrinket
	Class == "Trinkets"
	SetFontSize 45
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # $type->artefact->misc $tier->fishingrods
	Class == "Fishing Rods"
	SetFontSize 45
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # $type->artefact->misc $tier->pieces
	Rarity Unique
	Class == "Pieces"
	SetFontSize 45
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # $type->questlikeexception $tier->questheist
	Class == "Quest Items"
	BaseType "Contract:"
	SetFontSize 45
	SetTextColor 74 230 58 255
	SetBorderColor 74 230 58 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 0 Green Pentagon

Show # $type->questlikeexception $tier->questitems
	Class == "Cursed Ducat" "Pantheon Souls" "Quest Items"
	SetFontSize 45
	SetTextColor 74 230 58 255
	SetBorderColor 74 230 58 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 0 Green Pentagon

#------------------------------------

# [1201] Relics

#------------------------------------

Show # %H9 $type->artefact->sanctifiedrelics $tier->selectedrelics
	Rarity Normal Magic Rare
	Class == "Relics"
	BaseType == "Candlestick Relic" "Censer Relic" "Coffer Relic" "Papyrus Relic" "Processional Relic" "Tome Relic" "Urn Relic"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %H6 $type->artefact->sanctifiedrelics $tier->anyrelic
	Rarity Normal Magic Rare
	Class == "Relics"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#===============================================================================================================

# [[1300]] Exotic Item Variations

#===============================================================================================================

# !! Waypoint c2.exotic.doublecorrupted.all : "SpecialGear - Double corrupted rare items" : "Gear - Exotic"

#------------------------------------

# [1301] Double and Single Corruptions

#------------------------------------

Show # %D8 $type->exotic->corruptions $tier->doublecorruptedjwlry
	Corrupted True
	CorruptedMods >= 2
	Rarity Rare
	Class == "Abyss Jewels" "Amulets" "Belts" "Gloves" "Jewels" "Quivers" "Rings"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 250 0 0 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->exotic->corruptions $tier->doublecorruptedany
	Corrupted True
	CorruptedMods >= 2
	Rarity Rare
	SetFontSize 45
	SetBorderColor 250 0 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

# !! Waypoint c2.exotic.singlecorrupted.all : "SpecialGear - Single corrupted rare items with implicits"

Show # %D3 $type->exotic->corruptions $tier->singlecorruptedquivers
	Corrupted True
	CorruptedMods >= 1
	ItemLevel >= 80
	Rarity Normal Magic Rare
	Class == "Quivers"
	SetFontSize 40
	SetBorderColor 250 0 0 255
	PlayEffect Blue Temp

Show # %D5 $type->exotic->corruptions $tier->singlecorrupteditems
	Corrupted True
	CorruptedMods >= 1
	ItemLevel >= 75
	Rarity Normal Magic Rare
	Class == "Rings"
	SetFontSize 40
	SetBorderColor 250 0 0 255
	PlayEffect Blue Temp

#------------------------------------

# [1302] Abyss Jeweled Rares

#------------------------------------

# !! Waypoint c2.exotic.abysssocketed : "SpecialGear - Rares with Abyss Sockets" : "Gear - Exotic"

Show # $type->exotic->sockets $tier->anynonbelt
	Rarity Normal Magic Rare
	SocketGroup "A"
	Class == "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#------------------------------------

# [1303] Fractured

#------------------------------------

# !! Waypoint c2.exotic.fractured.all : "SpecialGear - All fractured items" : "Gear - Fractured and Synthesised"

Show # %D5 $type->exotic->fractured $tier->fractt1
	FracturedItem True
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Agate Amulet" "Amethyst Ring" "Ancient Mask" "Arcane Vestment" "Assassin's Mitts" "Astral Leather" "Bone Ring" "Broadhead Arrow Quiver" "Chimerascale Boots" "Chimerascale Gauntlets" "Citrine Amulet" "Conqueror's Helmet" "Conquest Helmet" "Conquest Lamellar" "Convening Wand" "Convoking Wand" "Crusader Boots" "Crystal Belt" "Deicide Mask" "Despot Axe" "Dire Pelt" "Divine Crown" "Dragonscale Boots" "Dragonscale Gauntlets" "Eternal Burgonet" "Ezomyte Axe" "Faithful Helmet" "Feathered Arrow Quiver" "Fossilised Spirit Shield" "Full Wyvernscale" "Gemini Claw" "General's Helmet" "Giantslayer Helmet" "Grand Ringmail" "Grizzly Pelt" "Harpyskin Boots" "Harpyskin Gloves" "Haunted Bascinet" "Hubris Circlet" "Hydrascale Boots" "Hydrascale Gauntlets" "Imperial Claw" "Infiltrator Boots" "Infiltrator Mitts" "Jester Mask" "Kinetic Wand" "Knight Helm" "Legion Plate" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Lion Pelt" "Majestic Pelt" "Marshall's Brigandine" "Martyr Boots" "Martyr Gloves" "Moonlit Circlet" "Necrotic Armour" "Nightmare Bascinet" "Nightweave Robe" "Onyx Amulet" "Opal Sceptre" "Opal Wand" "Paladin Boots" "Paladin Crown" "Paladin Gloves" "Paladin's Hauberk" "Phantom Boots" "Phantom Mitts" "Pig-Faced Bascinet" "Precursor Gauntlets" "Precursor Greaves" "Profane Wand" "Prophecy Wand" "Reaver Axe" "Royal Burgonet" "Royal Plate" "Sacred Chainmail" "Sadist Garb" "Sage Gloves" "Sage Slippers" "Sanguine Raiment" "Short Bow" "Siege Axe" "Sinner Tricorne" "Slink Boots" "Slink Gloves" "Sorcerer Boots" "Sorcerer Gloves" "Spine Bow" "Stealth Boots" "Stealth Gloves" "Stygian Vise" "Sunfire Circlet" "Supreme Leather" "Syndicate's Garb" "Thicket Bow" "Titan Gauntlets" "Titan Plate" "Tornado Wand" "Torturer Garb" "Torturer's Mask" "Turquoise Amulet" "Twilight Regalia" "Two-Stone Ring" "Vaal Axe" "Vaal Gauntlets" "Velour Boots" "Velour Gloves" "Void Sceptre" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->exotic->fractured $tier->fractt2
	FracturedItem True
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Alder Spiked Shield" "Amber Amulet" "Ambush Boots" "Ambush Mitts" "Angelic Kite Shield" "Apothecary's Gloves" "Arcanist Gloves" "Arcanist Slippers" "Assassin's Boots" "Assassin's Garb" "Battered Foil" "Blood Raiment" "Blood Sceptre" "Blue Pearl Amulet" "Bone Helmet" "Callous Mask" "Cardinal Round Shield" "Carnal Armour" "Carnal Boots" "Carnal Mitts" "Carnal Sceptre" "Cerulean Ring" "Colossal Tower Shield" "Conjurer Gloves" "Copper Kris" "Coral Ring" "Crusader Buckler" "Crusader Gloves" "Crystal Sceptre" "Demon's Horn" "Diamond Ring" "Eelskin Boots" "Eelskin Gloves" "Eternal Sword" "Eye Gouger" "Ezomyte Burgonet" "Ezomyte Spiked Shield" "Ezomyte Staff" "Ezomyte Tower Shield" "Fencer Helm" "Fingerless Silk Gloves" "Fluted Bascinet" "Fugitive Boots" "Full Dragonscale" "General's Brigandine" "Glorious Plate" "Golden Kris" "Goliath Gauntlets" "Goliath Greaves" "Grinning Fetish" "Gripped Gloves" "Grove Bow" "Harlequin Mask" "Harmonic Spirit Shield" "Heathen Wand" "Heavy Arrow Quiver" "Heavy Belt" "Hellion's Paw" "Highborn Bow" "Horned Sceptre" "Imperial Bow" "Imperial Maul" "Imperial Skean" "Iolite Ring" "Ivory Bow" "Jade Amulet" "Jewelled Foil" "Lacquered Buckler" "Lacquered Helmet" "Lapis Amulet" "Lead Sceptre" "Leather Belt" "Legion Boots" "Legion Gloves" "Maelström Staff" "Maraketh Bow" "Marble Amulet" "Meatgrinder" "Mind Cage" "Mirrored Spiked Shield" "Moonstone Ring" "Murder Boots" "Murder Mitts" "Necromancer Circlet" "Noble Tricorne" "Nubuck Gloves" "Ochre Sceptre" "Omen Wand" "Opal Ring" "Piledriver" "Platinum Kris" "Praetor Crown" "Primal Arrow Quiver" "Prismatic Ring" "Prophet Crown" "Reaver Sword" "Regicide Mask" "Ritual Sceptre" "Royal Sceptre" "Ruby Ring" "Runic Hatchet" "Saintly Chainmail" "Samnite Helmet" "Sapphire Ring" "Seaglass Amulet" "Sekhem" "Serpentscale Boots" "Serpentscale Gauntlets" "Shadow Sceptre" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Sharkskin Gloves" "Sharktooth Arrow Quiver" "Siege Helmet" "Silken Hood" "Solaris Circlet" "Soldier Boots" "Soldier Gloves" "Sovereign Spiked Shield" "Spiked Gloves" "Spiny Round Shield" "Steel Ring" "Steelscale Gauntlets" "Sundering Axe" "Supreme Spiked Shield" "Thorium Spirit Shield" "Titan Greaves" "Titanium Spirit Shield" "Topaz Ring" "Triumphant Lamellar" "Two-Point Arrow Quiver" "Two-Toned Boots" "Unset Ring" "Ursine Pelt" "Vaal Greaves" "Vaal Hatchet" "Vaal Mask" "Vaal Regalia" "Vaal Sceptre" "Vaal Spirit Shield" "Vanguard Belt" "Vermillion Ring" "Void Axe" "Wyrmscale Boots" "Wyrmscale Gauntlets" "Zealot Boots" "Zodiac Leather"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#Show # %D2 $type->exotic->fractured $tier->fractt3

# FracturedItem True

# Mirrored False

# Corrupted False

# Rarity Normal Magic Rare

# BaseType == "Abyssal Sceptre" "Ambusher" "Ancient Gauntlets" "Ancient Greaves" "Ancient Spirit Shield" "Antique Gauntlets" "Antique Greaves" "Archon Kite Shield" "Artillery Quiver" "Assassin Bow" "Astral Plate" "Aventail Helmet" "Baroque Round Shield" "Battle Buckler" "Battle Lamellar" "Blazing Arrow Quiver" "Blunt Arrow Quiver" "Bone Bow" "Bone Circlet" "Branded Kite Shield" "Bronzescale Boots" "Bronzescale Gauntlets" "Butcher Knife" "Calling Wand" "Ceremonial Kite Shield" "Chain Belt" "Chain Boots" "Champion Kite Shield" "Chiming Spirit Shield" "Citadel Bow" "Clasped Boots" "Clasped Mitts" "Close Helmet" "Cloth Belt" "Coiled Wand" "Compound Spiked Shield" "Conjurer Boots" "Conquest Chainmail" "Coral Amulet" "Coronal Leather" "Coronal Maul" "Corsair Sword" "Crimson Raiment" "Crimson Round Shield" "Crusader Plate" "Crypt Armour" "Crystal Wand" "Cutthroat's Garb" "Deerskin Boots" "Deerskin Gloves" "Demon Dagger" "Desert Brigandine" "Destiny Leather" "Dragonscale Doublet" "Ebony Tower Shield" "Eclipse Staff" "Eelskin Tunic" "Elegant Ringmail" "Elegant Round Shield" "Etched Kite Shield" "Exquisite Blade" "Exquisite Leather" "Ezomyte Blade" "Ezomyte Dagger" "Faun's Horn" "Festival Mask" "Fiend Dagger" "Fire Arrow Quiver" "Fleshripper" "Frontier Leather" "Gilded Sallet" "Gladiator Helmet" "Gladiator Plate" "Glorious Leather" "Goathide Boots" "Goathide Gloves" "Gold Amulet" "Gold Ring" "Golden Buckler" "Golden Mask" "Golden Plate" "Great Crown" "Harbinger Bow" "Hunter Hood" "Imp Dagger" "Imperial Buckler" "Imperial Staff" "Iron Ring" "Ironscale Boots" "Ironscale Gauntlets" "Ironwood Buckler" "Ivory Spirit Shield" "Judgement Staff" "Karui Chopper" "Karui Maul" "Karui Sceptre" "Lacewood Spirit Shield" "Lacquered Garb" "Laminated Kite Shield" "Layered Kite Shield" "Leather Hood" "Lunaris Circlet" "Magistrate Crown" "Maple Round Shield" "Mesh Boots" "Mosaic Kite Shield" "Nightmare Mace" "Noble Axe" "Noble Claw" "Nubuck Boots" "Occultist's Vestment" "Ornate Spiked Shield" "Pagan Wand" "Paua Amulet" "Paua Ring" "Penetrating Arrow Quiver" "Pinnacle Tower Shield" "Plated Greaves" "Platinum Sceptre" "Polished Spiked Shield" "Quartz Wand" "Ranger Bow" "Raven Mask" "Reaver Helmet" "Reinforced Greaves" "Ringmail Boots" "Riveted Boots" "Riveted Gloves" "Royal Bow" "Royal Skean" "Rustic Sash" "Sage Wand" "Sai" "Saint's Hauberk" "Sambar Sceptre" "Samite Slippers" "Satin Slippers" "Scholar Boots" "Secutor Helm" "Sentinel Jacket" "Serrated Foil" "Shackled Boots" "Shagreen Tower Shield" "Sharkskin Tunic" "Slaughter Knife" "Sniper Bow" "Spike-Point Arrow Quiver" "Spiked Round Shield" "Spiraled Foil" "Spiraled Wand" "Splendid Round Shield" "Steel Circlet" "Steel Gauntlets" "Steel Kite Shield" "Steelscale Boots" "Steelwood Bow" "Strapped Boots" "Strapped Mitts" "Studded Belt" "Teak Round Shield" "Terror Claw" "Terror Maul" "Throat Stabber" "Trapper Boots" "Trapper Mitts" "Twin Claw" "Tyrant's Sekhem" "Vaal Buckler" "Varnished Coat" "Vile Arrow Quiver" "Widowsilk Robe" "Wolf Pelt" "Zealot Gloves" "Zealot Helmet"

# SetFontSize 45

# SetBorderColor 0 240 190 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 2 Blue Diamond

Show # %D6 $type->exotic->fractured $tier->fractspecial
	FracturedItem True
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	Class == "Abyss Jewels" "Heist Brooches" "Heist Cloaks" "Heist Gear" "Heist Tools" "Jewels" "Utility Flasks"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D2 $type->exotic->fractured $tier->fractothers

# FracturedItem True

# Mirrored False

# Corrupted False

# Rarity Normal Magic Rare

# SetFontSize 40

# SetBorderColor 0 240 190 180

# PlayEffect Blue Temp

#------------------------------------

# [1304] Enchanted

#------------------------------------

# !! Waypoint c2.exotic.enchanted.all : "SpecialGear - All enchanted items" : "Gear - Exotic"

Show # %D9 $type->exotic->enchanted $tier->exotic
	AnyEnchantment True
	Rarity Normal Magic Rare
	Class == "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D7 $type->exotic->enchanted $tier->anointedamulets
	AnyEnchantment True
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	Class == "Amulets"
	BaseType == "Agate Amulet" "Amber Amulet" "Blue Pearl Amulet" "Citrine Amulet" "Coral Amulet" "Gold Amulet" "Jade Amulet" "Lapis Amulet" "Marble Amulet" "Onyx Amulet" "Paua Amulet" "Seaglass Amulet" "Turquoise Amulet"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D3 $type->exotic->enchanted $tier->anointedrings
	AnyEnchantment True
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	Class == "Rings"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#------------------------------------

# [1305] Crucible

#------------------------------------

# !! Waypoint c2.exotic.others : "SpecialGear - Others exotic items" : "Gear - Exotic"

Show # %D3 $type->exotic->crucible $tier->crucibleany
	HasCruciblePassiveTree True
	Rarity Normal Magic Rare
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#===============================================================================================================

# [[1400]] Recipes and 5links

#===============================================================================================================

# !! Waypoint c3.gear.alllinks.all : "SpecialGear - 5-links and 6-socketed items" : "Recipes and Linked Gear"

#------------------------------------

# [1401] Link Based

#------------------------------------

Show # %D4 $type->socketslinks $tier->5linksleveling
	LinkedSockets >= 5
	Rarity Normal Magic Rare
	AreaLevel >= 2
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D4 $type->socketslinks $tier->5link6sockets
	LinkedSockets >= 5
	Sockets >= 6
	Rarity Normal Magic Rare
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 155 138 138 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 2 Blue Hexagon

Show # %D3 $type->socketslinks $tier->5links
	LinkedSockets >= 5
	Rarity Normal Magic Rare
	AreaLevel >= 68
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show # %D5 $type->socketslinks $tier->rgbsmall1
	Width 2
	Height 2
	Rarity Normal Magic Rare
	SocketGroup "RGB"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 155 138 138 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Hexagon

Show # %D5 $type->socketslinks $tier->rgbsmall2
	Width 1
	Height <= 4
	Rarity Normal Magic Rare
	SocketGroup "RGB"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 155 138 138 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Hexagon

Show # %D3 $type->socketslinks $tier->rgblarge
	Width 2
	Height 4
	Rarity Normal Magic Rare
	SocketGroup "RGB"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 155 138 138 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Hexagon

Show # %D4 $type->socketslinks $tier->rgbmedium
	Width 2
	Height 3
	Rarity Normal Magic Rare
	SocketGroup "RGB"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 155 138 138 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Hexagon

Show # %D3 $type->socketslinks $tier->6sockets4h
	Sockets >= 6
	Height 4
	Rarity Normal Magic Rare
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 155 138 138 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Hexagon

Show # %DS3 $type->socketslinks $tier->6sockets
	Sockets >= 6
	Height 3
	Rarity Normal Magic Rare
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 155 138 138 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Hexagon

#===============================================================================================================

# [[1500]] High Level Crafting Bases

#===============================================================================================================

# !! Waypoint c3.gear.valuableilvl86 : "Crafting Bases - ilvl86 crafting bases" : "Gear - Crafting Bases"

#------------------------------------

# [1501] Expensive Atlas 86 Bases - matched by economy

#------------------------------------

Show # %D5 $type->crafting->expensive $tier->any86
	Mirrored False
	Corrupted False
	ItemLevel >= 86
	Rarity Normal Magic Rare
	BaseType == "Archon Kite Shield" "Bone Helmet" "Cardinal Round Shield" "Carrion Queen Talisman" "Conquest Lamellar" "Crystal Belt" "Divine Crown" "Enthalpic Ring" "Ezomyte Tower Shield" "Fingerless Silk Gloves" "Gripped Gloves" "Haunted Bascinet" "Lacquered Buckler" "Marble Amulet" "Necrotic Armour" "Octopus Talisman" "Organic Ring" "Royal Plate" "Spiked Gloves" "Steel Ring" "Stygian Vise" "Synaptic Ring" "Syndicate's Garb" "Titanium Spirit Shield" "Torturer's Mask" "Twilight Regalia" "Two-Toned Boots" "Velour Boots" "Vermillion Ring" "Warlock Boots" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->crafting->expensive $tier->any85
	Mirrored False
	Corrupted False
	ItemLevel >= 85
	Rarity Normal Magic Rare
	BaseType == "Blood Viper Talisman" "Cardinal Round Shield" "Carrion Queen Talisman" "Cobra Talisman" "Colossal Tower Shield" "Craicic Talisman" "Croaker Talisman" "Ezomyte Tower Shield" "Fenumal Talisman" "Frost Hellion Talisman" "Fugitive Boots" "Fugitive Ring" "Ghastly Eye Jewel" "Great Maw Talisman" "Hybrid Arachnid Talisman" "Iolite Ring" "Lynx Talisman" "Marble Amulet" "Murderous Eye Jewel" "Plagued Arachnid Talisman" "Rhex Talisman" "Saqawine Talisman" "Scorpion Talisman" "Stygian Vise" "Synaptic Ring" "Taurus Talisman" "Tiger Talisman" "Twilight Regalia" "Two-Toned Boots" "Vermillion Ring"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->crafting->expensive $tier->any84
	Mirrored False
	Corrupted False
	ItemLevel >= 84
	Rarity Normal Magic Rare
	BaseType == "Carrion Queen Talisman" "Cobra Talisman" "Craicic Talisman" "Croaker Talisman" "Fenumal Talisman" "Frost Hellion Talisman" "Fugitive Ring" "Great Maw Talisman" "Hybrid Arachnid Talisman" "Lynx Talisman" "Plagued Arachnid Talisman" "Rhex Talisman" "Sacrificial Garb" "Saqawine Talisman" "Stygian Vise" "Synaptic Ring" "Taurus Talisman" "Tiger Talisman" "Twilight Regalia" "Vermillion Ring"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D4 $type->crafting->expensive $tier->any83
	Mirrored False
	Corrupted False
	ItemLevel >= 83
	Rarity Normal Magic Rare
	BaseType == "Carrion Queen Talisman" "Cobra Talisman" "Craicic Talisman" "Croaker Talisman" "Fenumal Talisman" "Frost Hellion Talisman" "Fugitive Ring" "Great Maw Talisman" "Hybrid Arachnid Talisman" "Lynx Talisman" "Plagued Arachnid Talisman" "Rhex Talisman" "Sacrificial Garb" "Saqawine Talisman" "Stygian Vise" "Synaptic Ring" "Taurus Talisman" "Tiger Talisman" "Twilight Regalia" "Vermillion Ring"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

#===============================================================================================================

# [[1600]] Endgame - Rare - Gear

#===============================================================================================================

# !! Waypoint c4.rare.decorator.all : "Rare Endgame Items - decorators"

#------------------------------------

# [[1700]] Endgame - Rare - Decorators

#------------------------------------

Show # $type->decorators->rareeg $tier->largerares
	Width >= 2
	Height >= 3
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetBorderColor 0 0 0 255
	Continue

Show # $type->decorators->rareeg $tier->mediumrares1
	Width 1
	Height >= 3
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetBorderColor 180 180 180 255
	Continue

Show # $type->decorators->rareeg $tier->mediumrares2
	Width 2
	Height 2
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetBorderColor 180 180 180 255
	Continue

Show # $type->decorators->rareeg $tier->tinyrares
	Width <= 2
	Height 1
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetBorderColor 50 200 50 255
	Continue

#Show # $type->decorators->rareeg $tier->ilvl68

# ItemLevel >= 68

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# Continue

#Show # $type->decorators->rareeg $tier->ilvl75

# ItemLevel >= 75

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# SetTextColor 245 190 0 255

# Continue

Show # $type->decorators->rareeg $tier->fourlinkedrares
	LinkedSockets >= 4
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetBorderColor 0 140 240 255
	Continue

Show # $type->decorators->rareeg $tier->topilvl83
	ItemLevel >= 83
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	SetTextColor 245 190 0 255
	Continue

Show # $type->decorators->rareeg $tier->topilvl84
	ItemLevel >= 84
	Rarity Rare
	Class == "Rings" "Rune Daggers" "Sceptres" "Staves" "Wands"
	SetTextColor 245 190 0 255
	Continue

Show # $type->decorators->rareeg $tier->topilvl85
	ItemLevel >= 85
	Rarity Rare
	Class == "Amulets" "Gloves" "Helmets"
	SetTextColor 245 190 0 255
	Continue

Show # $type->decorators->rareeg $tier->topilvl86
	ItemLevel >= 86
	Rarity Rare
	Class == "Belts" "Body Armours" "Boots" "Bows" "Quivers" "Shields"
	SetTextColor 245 190 0 255
	Continue

Show # $type->decorators->rareeg $tier->corruptedrares
	Corrupted True
	CorruptedMods 0
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetBorderColor 120 0 0 240
	Continue

Show # $type->decorators->rareeg $tier->corruptedraresimplicit
	Corrupted True
	CorruptedMods >= 1
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetBorderColor 250 0 0 255
	Continue

# !! Waypoint c4.rare.talisman.all : "Rare Endgame Items - Talismans" : "Gear - Exotic"

Show # %H5 $type->rare->exotic->talisman $tier->t1
	AnyEnchantment True
	ItemLevel >= 68
	Rarity Normal Magic Rare
	Class == "Amulets"
	BaseType == "Cobra Talisman" "Croaker Talisman" "Fenumal Talisman" "Great Maw Talisman" "Plagued Arachnid Talisman" "Retch Talisman" "Rhex Talisman" "Saqawine Talisman" "Scorpion Talisman" "Spider Crab Talisman" "Taurus Talisman" "Tiger Talisman" "Vulture Talisman" "Wolf Alpha Talisman"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %H5 $type->rare->exotic->talisman $tier->t2
	AnyEnchantment True
	ItemLevel >= 68
	Rarity Normal Magic Rare
	Class == "Amulets"
	BaseType == "Ape Talisman" "Black Widow Talisman" "Blood Viper Talisman" "Carrion Queen Talisman" "Chieftain Talisman" "Chimeral Talisman" "Craicic Talisman" "Devourer Talisman" "Farric Talisman" "Flame Hellion Talisman" "Frost Hellion Talisman" "Gargantuan Talisman" "Goatman Talisman" "Goliath Talisman" "Hybrid Arachnid Talisman" "Lynx Talisman" "Magma Hound Talisman" "Octopus Talisman" "Pitbull Talisman" "Rhoa Talisman" "Sand Spitter Talisman" "Savage Crab Talisman" "Scrabbler Talisman" "Shield Crab Talisman" "Squid Talisman" "Ursa Talisman" "Watcher Talisman"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show # %H5 $type->rare->exotic->talisman $tier->t3
	AnyEnchantment True
	ItemLevel >= 68
	Rarity Normal Magic Rare
	Class == "Amulets"
	BaseType == "Black Maw Talisman"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#Show # $type->rare->utility->droppeditems $tier->any

# Identified True

# ItemLevel >= 4

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# AreaLevel 1

# SetFontSize 45

# SetBorderColor 0 0 0

#------------------------------------

# [[1800]] Endgame - Rare - Exotic Veiled

#------------------------------------

# !! Waypoint c4.rare.veiled.generic : "Rare Endgame Items - Veiled" : "Gear - Veiled"

Show # %D4 $type->rare->exotic->veiled $tier->t1
	Identified True
	ItemLevel >= 68
	Rarity Rare
	BaseType == "Agate Amulet" "Amethyst Ring" "Citrine Amulet" "Conquest Lamellar" "Divine Crown" "Giantslayer Helmet" "Haunted Bascinet" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Majestic Pelt" "Necrotic Armour" "Onyx Amulet" "Paladin Boots" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Prismatic Ring" "Royal Plate" "Sacred Chainmail" "Stygian Vise" "Syndicate's Garb" "Torturer's Mask" "Turquoise Amulet" "Twilight Regalia" "Two-Stone Ring" "Velour Boots" "Velour Gloves" "Vermillion Ring" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	HasExplicitMod "Veil"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D3 $type->rare->exotic->veiled $tier->t2
	Identified True
	ItemLevel >= 68
	Rarity Rare
	BaseType == "Amber Amulet" "Ancient Mask" "Apothecary's Gloves" "Arcanist Slippers" "Archon Kite Shield" "Assassin's Boots" "Astral Leather" "Blue Pearl Amulet" "Bone Helmet" "Bone Ring" "Broadhead Arrow Quiver" "Cerulean Ring" "Chimerascale Boots" "Chimerascale Gauntlets" "Colossal Tower Shield" "Conqueror's Helmet" "Conquest Helmet" "Convoking Wand" "Copper Kris" "Coral Ring" "Crusader Boots" "Crusader Gloves" "Crystal Belt" "Deicide Mask" "Diamond Ring" "Dire Pelt" "Dragonscale Boots" "Dragonscale Gauntlets" "Eternal Burgonet" "Faithful Helmet" "Feathered Arrow Quiver" "Fugitive Boots" "Full Wyvernscale" "General's Helmet" "Golden Kris" "Goliath Gauntlets" "Goliath Greaves" "Grand Ringmail" "Gripped Gloves" "Grizzly Pelt" "Harmonic Spirit Shield" "Harpyskin Boots" "Harpyskin Gloves" "Heavy Belt" "Hubris Circlet" "Hydrascale Boots" "Hydrascale Gauntlets" "Imperial Claw" "Infiltrator Boots" "Infiltrator Mitts" "Iolite Ring" "Jade Amulet" "Jester Mask" "Kinetic Wand" "Knight Helm" "Lacquered Buckler" "Lapis Amulet" "Lathi" "Leather Belt" "Legion Boots" "Legion Gloves" "Legion Plate" "Lion Pelt" "Marble Amulet" "Marshall's Brigandine" "Martyr Boots" "Martyr Gloves" "Mind Cage" "Mirrored Spiked Shield" "Moonlit Circlet" "Moonstone Ring" "Murder Boots" "Murder Mitts" "Nightmare Bascinet" "Nightweave Robe" "Opal Ring" "Opal Sceptre" "Paladin Crown" "Paladin's Hauberk" "Platinum Kris" "Praetor Crown" "Precursor Gauntlets" "Precursor Greaves" "Profane Wand" "Prophecy Wand" "Prophet Crown" "Royal Burgonet" "Ruby Ring" "Sage Gloves" "Sage Slippers" "Sanguine Raiment" "Sapphire Ring" "Short Bow" "Slink Boots" "Slink Gloves" "Soldier Boots" "Sorcerer Boots" "Sorcerer Gloves" "Spiked Gloves" "Spine Bow" "Stealth Boots" "Steel Ring" "Sunfire Circlet" "Supreme Leather" "Titan Gauntlets" "Titan Greaves" "Titan Plate" "Titanium Spirit Shield" "Topaz Ring" "Tornado Wand" "Torturer Garb" "Two-Toned Boots" "Unset Ring" "Vaal Axe" "Vaal Gauntlets" "Vaal Greaves" "Vaal Mask" "Vanguard Belt" "Void Sceptre"
	HasExplicitMod "Veil"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show # %D3 $type->rare->exotic->veiled $tier->t3
	Identified True
	ItemLevel >= 68
	Rarity Rare
	BaseType == "Ambush Boots" "Ambush Mitts" "Ambusher" "Ancient Gauntlets" "Ancient Greaves" "Antique Gauntlets" "Antique Greaves" "Arcane Vestment" "Arcanist Gloves" "Assassin's Mitts" "Astral Plate" "Battered Foil" "Blasting Wand" "Cardinal Round Shield" "Carnal Boots" "Carnal Mitts" "Carnal Sceptre" "Chain Belt" "Champion Kite Shield" "Cloth Belt" "Conjurer Boots" "Conjurer Gloves" "Convening Wand" "Coral Amulet" "Corsair Sword" "Crusader Buckler" "Demon's Horn" "Despot Axe" "Eclipse Staff" "Elegant Round Shield" "Eternal Sword" "Ezomyte Axe" "Ezomyte Burgonet" "Ezomyte Staff" "Ezomyte Tower Shield" "Fingerless Silk Gloves" "Fluted Bascinet" "Fossilised Spirit Shield" "Full Dragonscale" "Gemini Claw" "Glorious Plate" "Gold Amulet" "Gold Ring" "Gutting Knife" "Harlequin Mask" "Heathen Wand" "Heavy Arrow Quiver" "Imperial Bow" "Imperial Buckler" "Imperial Skean" "Imperial Staff" "Iron Ring" "Jewelled Foil" "Karui Chopper" "Legion Hammer" "Maelström Staff" "Magistrate Crown" "Maraketh Bow" "Meatgrinder" "Mosaic Kite Shield" "Nightmare Mace" "Opal Wand" "Paua Amulet" "Paua Ring" "Pig-Faced Bascinet" "Piledriver" "Pinnacle Tower Shield" "Platinum Sceptre" "Primal Arrow Quiver" "Reaver Axe" "Reaver Sword" "Regicide Mask" "Riveted Boots" "Runic Hatchet" "Rustic Sash" "Sadist Garb" "Saint's Hauberk" "Saintly Chainmail" "Samite Slippers" "Samnite Helmet" "Seaglass Amulet" "Serpentscale Boots" "Serpentscale Gauntlets" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Siege Axe" "Silken Hood" "Sinner Tricorne" "Solaris Circlet" "Soldier Gloves" "Stealth Gloves" "Studded Belt" "Supreme Spiked Shield" "Thicket Bow" "Triumphant Lamellar" "Vaal Regalia" "Vaal Sceptre" "Vaal Spirit Shield" "Whalebone Rapier" "Wyrmscale Boots" "Wyrmscale Gauntlets" "Zealot Boots" "Zealot Gloves" "Zodiac Leather"
	HasExplicitMod "Veil"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#Show # %D2 $type->rare->exotic->veiled $tier->t4

# Identified True

# ItemLevel >= 68

# Rarity Rare

# BaseType == "Abyssal Sceptre" "Angelic Kite Shield" "Artillery Quiver" "Assassin's Garb" "Battle Buckler" "Behemoth Mace" "Blood Raiment" "Branded Kite Shield" "Bronze Gauntlets" "Bronze Tower Shield" "Bronzescale Boots" "Bronzescale Gauntlets" "Butcher Axe" "Calling Wand" "Callous Mask" "Carnal Armour" "Chiming Spirit Shield" "Citadel Bow" "Coiled Wand" "Colossus Mallet" "Coronal Maul" "Crystal Sceptre" "Crystal Wand" "Demon Dagger" "Ebony Tower Shield" "Eelskin Boots" "Eelskin Gloves" "Elegant Foil" "Elegant Ringmail" "Exquisite Blade" "Eye Gouger" "Ezomyte Blade" "Fencer Helm" "Fleshripper" "Foul Staff" "General's Brigandine" "Gladiator Plate" "Great Crown" "Grove Bow" "Harbinger Bow" "Hellion's Paw" "Imperial Maul" "Infernal Axe" "Ivory Bow" "Judgement Staff" "Karui Maul" "Karui Sceptre" "Lacewood Spirit Shield" "Lacquered Helmet" "Mesh Boots" "Mesh Gloves" "Midnight Blade" "Moon Staff" "Necromancer Circlet" "Nubuck Boots" "Omen Wand" "Pagan Wand" "Penetrating Arrow Quiver" "Plated Greaves" "Polished Spiked Shield" "Primordial Staff" "Ranger Bow" "Raven Mask" "Reaver Helmet" "Reinforced Greaves" "Ringmail Boots" "Riveted Gloves" "Royal Skean" "Sai" "Sambar Sceptre" "Samite Gloves" "Satin Gloves" "Satin Slippers" "Scholar Boots" "Serpentine Staff" "Serrated Foil" "Sharkskin Gloves" "Sharktooth Arrow Quiver" "Siege Helmet" "Silk Slippers" "Sovereign Spiked Shield" "Spike-Point Arrow Quiver" "Spiny Round Shield" "Spiraled Foil" "Steel Circlet" "Steel Gauntlets" "Steelscale Boots" "Steelscale Gauntlets" "Sundering Axe" "Teak Round Shield" "Terror Claw" "Thorium Spirit Shield" "Throat Stabber" "Trapper Boots" "Trapper Mitts" "Trisula" "Twin Claw" "Two-Point Arrow Quiver" "Tyrant's Sekhem" "Ursine Pelt" "Vaal Buckler" "Vaal Greatsword" "Vaal Hatchet" "Vile Arrow Quiver" "Void Axe" "Widowsilk Robe" "Zealot Helmet"

# HasExplicitMod "Veil"

# SetFontSize 40

# SetBorderColor 0 240 190 180

# PlayEffect Blue Temp

#Show # %D1 $type->rare->exotic->veiled $tier->any

# Identified True

# ItemLevel >= 68

# Rarity Rare

# HasExplicitMod "Veil"

# SetFontSize 40

# SetBorderColor 0 240 190 180

# PlayEffect Blue Temp

#------------------------------------

# [[1900]] Endgame - Rare - Exotic Corrupted

#------------------------------------

# !! Waypoint c4.rare.breach.all : "Rare Endgame Items - Breach rings" : "Gear - Exotic"

Show # %HS6 $type->rare->exotic->breachrings $tier->high
	ItemLevel >= 82
	Rarity Normal Magic Rare
	Class == "Rings"
	BaseType == "Cryonic Ring" "Enthalpic Ring" "Formless Ring" "Fugitive Ring" "Organic Ring" "Synaptic Ring"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %HS5 $type->rare->exotic->breachrings $tier->any
	ItemLevel >= 68
	Rarity Normal Magic Rare
	Class == "Rings"
	BaseType == "Cryonic Ring" "Enthalpic Ring" "Formless Ring" "Fugitive Ring" "Organic Ring" "Synaptic Ring"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#------------------------------------

# [[2000]] Endgame - Rare - Conditional Hide Rules

#------------------------------------

# !! Waypoint c4.rare.generic.all : "Rare Endgame Items - (Optional) Hiding identified rares"

#Hide # $type->rareoptional $tier->idhider

# Identified True

# ItemLevel >= 68

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# SetFontSize 35

# SetBorderColor 0 0 0

# !! Waypoint c4.rare.corrupthider : "Hide rare corrupted unidentified gear with no implicits"

Hide # $type->hidelayer $tier->corruptedrares
	Corrupted True
	Identified False
	CorruptedMods 0
	ItemLevel >= 68
	Rarity Rare
	Class == "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 35
	SetBorderColor 0 0 0

Hide # $type->hidelayer $tier->mirroredrares
	Mirrored True
	Identified False
	CorruptedMods 0
	ItemLevel >= 68
	Rarity Rare
	Class == "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 35
	SetBorderColor 0 0 0

#------------------------------------

# [[2100]] Endgame - Rare - Amulets, Rings, Boots

#------------------------------------

# !! Waypoint c4.rare.trinkets.all : "Rare Endgame Items - Amulets, Rings" : "Gear - Regular Rares"

Show # %D4 $type->rr->amuring $tier->t1
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Rings"
	BaseType == "Agate Amulet" "Amethyst Ring" "Citrine Amulet" "Onyx Amulet" "Prismatic Ring" "Turquoise Amulet" "Two-Stone Ring" "Vermillion Ring"
	SetFontSize 45
	SetBackgroundColor 0 80 30 255

Show # %D3 $type->rr->amuring $tier->t2
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Rings"
	BaseType == "Amber Amulet" "Blue Pearl Amulet" "Bone Ring" "Cerulean Ring" "Coral Ring" "Diamond Ring" "Iolite Ring" "Jade Amulet" "Lapis Amulet" "Marble Amulet" "Moonstone Ring" "Opal Ring" "Ruby Ring" "Sapphire Ring" "Steel Ring" "Topaz Ring" "Unset Ring"
	SetFontSize 45
	SetBackgroundColor 0 40 10 255

#Show # %D2 $type->rr->amuring $tier->t3

# ItemLevel >= 68

# Rarity Rare

# Class == "Amulets" "Rings"

# BaseType == "Coral Amulet" "Gold Amulet" "Gold Ring" "Iron Ring" "Paua Amulet" "Paua Ring" "Seaglass Amulet"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

# !! Waypoint c4.rare.belts.all : "Rare Endgame Items - Belts" : "Gear - Regular Rares"

Show # %D4 $type->rr->belts $tier->t1
	ItemLevel >= 68
	Rarity Rare
	Class == "Belts"
	BaseType == "Stygian Vise"
	SetFontSize 45
	SetBackgroundColor 0 80 30 255

Show # %D3 $type->rr->belts $tier->t2
	ItemLevel >= 68
	Rarity Rare
	Class == "Belts"
	BaseType == "Crystal Belt" "Heavy Belt" "Leather Belt" "Vanguard Belt"
	SetFontSize 45
	SetBackgroundColor 0 40 10 255

#Show # %D2 $type->rr->belts $tier->t3

# ItemLevel >= 68

# Rarity Rare

# Class == "Belts"

# BaseType == "Chain Belt" "Cloth Belt" "Rustic Sash" "Studded Belt"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#------------------------------------

# [[2200]] Endgame - Rare - Gear - Droplevel Hiding

#------------------------------------

# !! Waypoint c4.rare.drophiders : "Rare Endgame Items - Hide low items on high levels" : "Gear - Regular Rares"

#Hide # %RH3 $type->hidelayer $tier->rrihide1

# ItemLevel >= 68

# DropLevel < 75

# Rarity Rare

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

# AreaLevel >= 82

# SetFontSize 18

# SetBorderColor 0 0 0 0

# SetBackgroundColor 20 20 0 0

# DisableDropSound True

Hide # %RH2 $type->hidelayer $tier->rrihide2
	ItemLevel >= 68
	DropLevel < 60
	Rarity Rare
	Class == "Body Armours" "Boots" "Gloves" "Helmets"
	AreaLevel >= 80
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # %RH2 $type->hidelayer $tier->rrihide3
	ItemLevel >= 68
	DropLevel < 50
	Rarity Rare
	Class == "Body Armours" "Boots" "Gloves" "Helmets"
	AreaLevel >= 78
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # %RH1 $type->hidelayer $tier->rrihide4
	ItemLevel >= 68
	DropLevel < 40
	Rarity Rare
	Class == "Body Armours" "Boots" "Gloves" "Helmets"
	AreaLevel >= 73
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

#------------------------------------

# [2201] Endgame - Rare - Gear

#------------------------------------

# !! Waypoint c4.rare.t1.all : "Rare Endgame Items - T1" : "Gear - Regular Rares"

Show # %D4 $type->rr $tier->t1
	ItemLevel >= 68
	Rarity Rare
	BaseType == "Conquest Lamellar" "Divine Crown" "Giantslayer Helmet" "Haunted Bascinet" "Leviathan Gauntlets" "Leviathan Greaves" "Lich's Circlet" "Majestic Pelt" "Necrotic Armour" "Paladin Boots" "Paladin Gloves" "Phantom Boots" "Phantom Mitts" "Royal Plate" "Sacred Chainmail" "Syndicate's Garb" "Torturer's Mask" "Twilight Regalia" "Velour Boots" "Velour Gloves" "Warlock Boots" "Warlock Gloves" "Wyvernscale Boots" "Wyvernscale Gauntlets"
	SetFontSize 40
	SetBackgroundColor 20 20 0 255

# !! Waypoint c4.rare.t2.all : "Rare Endgame Items - T2" : "Gear - Regular Rares"

Show # %D3 $type->rr $tier->t2
	ItemLevel >= 68
	Rarity Rare
	BaseType == "Ancient Mask" "Apothecary's Gloves" "Arcanist Slippers" "Archon Kite Shield" "Assassin's Boots" "Astral Leather" "Bone Helmet" "Broadhead Arrow Quiver" "Chimerascale Boots" "Chimerascale Gauntlets" "Colossal Tower Shield" "Conqueror's Helmet" "Conquest Helmet" "Convoking Wand" "Copper Kris" "Crusader Boots" "Crusader Gloves" "Deicide Mask" "Dire Pelt" "Dragonscale Boots" "Dragonscale Gauntlets" "Eternal Burgonet" "Faithful Helmet" "Feathered Arrow Quiver" "Fugitive Boots" "Full Wyvernscale" "General's Helmet" "Golden Kris" "Goliath Gauntlets" "Goliath Greaves" "Grand Ringmail" "Gripped Gloves" "Grizzly Pelt" "Harmonic Spirit Shield" "Harpyskin Boots" "Harpyskin Gloves" "Hubris Circlet" "Hydrascale Boots" "Hydrascale Gauntlets" "Imperial Claw" "Infiltrator Boots" "Infiltrator Mitts" "Jester Mask" "Kinetic Wand" "Knight Helm" "Lacquered Buckler" "Lathi" "Legion Boots" "Legion Gloves" "Legion Plate" "Lion Pelt" "Marshall's Brigandine" "Martyr Boots" "Martyr Gloves" "Mind Cage" "Mirrored Spiked Shield" "Moonlit Circlet" "Murder Boots" "Murder Mitts" "Nightmare Bascinet" "Nightweave Robe" "Opal Sceptre" "Paladin Crown" "Paladin's Hauberk" "Platinum Kris" "Praetor Crown" "Precursor Gauntlets" "Precursor Greaves" "Profane Wand" "Prophecy Wand" "Prophet Crown" "Royal Burgonet" "Sage Gloves" "Sage Slippers" "Sanguine Raiment" "Short Bow" "Slink Boots" "Slink Gloves" "Soldier Boots" "Sorcerer Boots" "Sorcerer Gloves" "Spiked Gloves" "Spine Bow" "Stealth Boots" "Sunfire Circlet" "Supreme Leather" "Titan Gauntlets" "Titan Greaves" "Titan Plate" "Titanium Spirit Shield" "Tornado Wand" "Torturer Garb" "Two-Toned Boots" "Vaal Axe" "Vaal Gauntlets" "Vaal Greaves" "Vaal Mask" "Void Sceptre"
	SetFontSize 40
	SetBackgroundColor 20 20 0 255

# !! Waypoint c4.rare.idhandling.all :  "Rare Endgame Items - Identified Item Handling" : "Gear - Regular Rares"

#Show # %D0 $type->rr $tier->identifieditemhandling

# Mirrored False

# Corrupted False

# Identified True

# ItemLevel >= 68

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# SetFontSize 40

# SetBorderColor 0 240 190 180

# PlayEffect Blue Temp

# !! Waypoint c4.rare.t3.all : "Rare Endgame Items - t3" : "Gear - Regular Rares"

#Show # %D2 $type->rr $tier->t3

# ItemLevel >= 68

# Rarity Rare

# BaseType == "Ambush Boots" "Ambush Mitts" "Ambusher" "Ancient Gauntlets" "Ancient Greaves" "Antique Gauntlets" "Antique Greaves" "Arcane Vestment" "Arcanist Gloves" "Assassin's Mitts" "Astral Plate" "Battered Foil" "Blasting Wand" "Cardinal Round Shield" "Carnal Boots" "Carnal Mitts" "Carnal Sceptre" "Champion Kite Shield" "Conjurer Boots" "Conjurer Gloves" "Convening Wand" "Corsair Sword" "Crusader Buckler" "Demon's Horn" "Despot Axe" "Eclipse Staff" "Elegant Round Shield" "Eternal Sword" "Ezomyte Axe" "Ezomyte Burgonet" "Ezomyte Staff" "Ezomyte Tower Shield" "Fingerless Silk Gloves" "Fluted Bascinet" "Fossilised Spirit Shield" "Full Dragonscale" "Gemini Claw" "Glorious Plate" "Gutting Knife" "Harlequin Mask" "Heathen Wand" "Heavy Arrow Quiver" "Imperial Bow" "Imperial Buckler" "Imperial Skean" "Imperial Staff" "Jewelled Foil" "Karui Chopper" "Legion Hammer" "Maelström Staff" "Magistrate Crown" "Maraketh Bow" "Meatgrinder" "Mosaic Kite Shield" "Nightmare Mace" "Opal Wand" "Pig-Faced Bascinet" "Piledriver" "Pinnacle Tower Shield" "Platinum Sceptre" "Primal Arrow Quiver" "Reaver Axe" "Reaver Sword" "Regicide Mask" "Riveted Boots" "Runic Hatchet" "Sadist Garb" "Saint's Hauberk" "Saintly Chainmail" "Samite Slippers" "Samnite Helmet" "Serpentscale Boots" "Serpentscale Gauntlets" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Siege Axe" "Silken Hood" "Sinner Tricorne" "Solaris Circlet" "Soldier Gloves" "Stealth Gloves" "Supreme Spiked Shield" "Thicket Bow" "Triumphant Lamellar" "Vaal Regalia" "Vaal Sceptre" "Vaal Spirit Shield" "Whalebone Rapier" "Wyrmscale Boots" "Wyrmscale Gauntlets" "Zealot Boots" "Zealot Gloves" "Zodiac Leather"

# SetFontSize 40

# SetBackgroundColor 35 35 35 240

# !! Waypoint c4.rare.t4.all : "Rare Endgame Items - T4" : "Gear - Regular Rares"

#Show # %D1 $type->rr $tier->t4

# ItemLevel >= 68

# Rarity Rare

# BaseType == "Abyssal Sceptre" "Angelic Kite Shield" "Artillery Quiver" "Assassin's Garb" "Battle Buckler" "Behemoth Mace" "Blood Raiment" "Branded Kite Shield" "Bronze Gauntlets" "Bronze Tower Shield" "Bronzescale Boots" "Bronzescale Gauntlets" "Butcher Axe" "Calling Wand" "Callous Mask" "Carnal Armour" "Chiming Spirit Shield" "Citadel Bow" "Coiled Wand" "Colossus Mallet" "Coronal Maul" "Crystal Sceptre" "Crystal Wand" "Demon Dagger" "Ebony Tower Shield" "Eelskin Boots" "Eelskin Gloves" "Elegant Foil" "Elegant Ringmail" "Exquisite Blade" "Eye Gouger" "Ezomyte Blade" "Fencer Helm" "Fleshripper" "Foul Staff" "General's Brigandine" "Gladiator Plate" "Great Crown" "Grove Bow" "Harbinger Bow" "Hellion's Paw" "Imperial Maul" "Infernal Axe" "Ivory Bow" "Judgement Staff" "Karui Maul" "Karui Sceptre" "Lacewood Spirit Shield" "Lacquered Helmet" "Mesh Boots" "Mesh Gloves" "Midnight Blade" "Moon Staff" "Necromancer Circlet" "Nubuck Boots" "Omen Wand" "Pagan Wand" "Penetrating Arrow Quiver" "Plated Greaves" "Polished Spiked Shield" "Primordial Staff" "Ranger Bow" "Raven Mask" "Reaver Helmet" "Reinforced Greaves" "Ringmail Boots" "Riveted Gloves" "Royal Skean" "Sai" "Sambar Sceptre" "Samite Gloves" "Satin Gloves" "Satin Slippers" "Scholar Boots" "Serpentine Staff" "Serrated Foil" "Sharkskin Gloves" "Sharktooth Arrow Quiver" "Siege Helmet" "Silk Slippers" "Sovereign Spiked Shield" "Spike-Point Arrow Quiver" "Spiny Round Shield" "Spiraled Foil" "Steel Circlet" "Steel Gauntlets" "Steelscale Boots" "Steelscale Gauntlets" "Sundering Axe" "Teak Round Shield" "Terror Claw" "Thorium Spirit Shield" "Throat Stabber" "Trapper Boots" "Trapper Mitts" "Trisula" "Twin Claw" "Two-Point Arrow Quiver" "Tyrant's Sekhem" "Ursine Pelt" "Vaal Buckler" "Vaal Greatsword" "Vaal Hatchet" "Vile Arrow Quiver" "Void Axe" "Widowsilk Robe" "Zealot Helmet"

# SetFontSize 35

# SetBackgroundColor 80 80 80 190

#===============================================================================================================

# [[2300]] Endgame - Crafting

#===============================================================================================================
#------------------------------------

# [2301] Early Endgame Crafting projects

#------------------------------------

# Minimal list of bases crafting. This list is really not conclusive, but you can adjust it yourself on filterblade or here.

# Having this list too long will lead to being too flooded with these drops.

#Show # %D0 $type->normalcraft->extra $tier->earlycraftoptional

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# BaseType == "Amethyst Ring" "Kinetic Wand" "Two-Stone Ring"

# AreaLevel <= 75

# AreaLevel >= 68

# SetBorderColor 100 100 100 150

#Show # %D1 $type->normalcraft->extra $tier->earlyendgame4link

# Mirrored False

# Corrupted False

# LinkedSockets >= 4

# Rarity Normal Magic Rare

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

# AreaLevel <= 75

# AreaLevel >= 68

# SetBorderColor 100 100 100 150

# SetBackgroundColor 20 20 0 180

#------------------------------------

# [2302] Crafting Matrix

#------------------------------------

# !! Waypoint c5.gear.crafting86.all : "Crafting Bases - High level basetypes - ILVL86" : "Gear - Crafting Bases"

# Level 86 crafting bases

Show # %D5 $type->crafting->generalgear $tier->t1_86
	Mirrored False
	Corrupted False
	ItemLevel >= 86
	Rarity Normal Magic Rare
	BaseType == "Conquest Lamellar" "Crystal Belt" "Leviathan Greaves" "Necrotic Armour" "Paladin Boots" "Phantom Boots" "Royal Plate" "Sacred Chainmail" "Sacrificial Garb" "Syndicate's Garb" "Twilight Regalia" "Velour Boots" "Warlock Boots" "Wyvernscale Boots"
	SetBorderColor 200 200 0 255

Show # %D4 $type->crafting->generalgear $tier->t2_86
	Mirrored False
	Corrupted False
	ItemLevel >= 86
	Rarity Normal Magic Rare
	BaseType == "Archon Kite Shield" "Artillery Quiver" "Broadhead Arrow Quiver" "Cardinal Round Shield" "Colossal Tower Shield" "Ezomyte Tower Shield" "Feathered Arrow Quiver" "Fossilised Spirit Shield" "Fugitive Boots" "Lacquered Buckler" "Primal Arrow Quiver" "Reflex Bow" "Short Bow" "Spine Bow" "Supreme Spiked Shield" "Thicket Bow" "Titanium Spirit Shield" "Two-Toned Boots" "Vanguard Belt"
	SetBorderColor 200 200 0 185

Show # %D3 $type->crafting->generalgear $tier->t3_86
	Mirrored False
	Corrupted False
	ItemLevel >= 86
	Rarity Normal Magic Rare
	BaseType == "Champion Kite Shield" "Citadel Bow" "Crusader Buckler" "Elegant Round Shield" "Grove Bow" "Harbinger Bow" "Harmonic Spirit Shield" "Heavy Arrow Quiver" "Heavy Belt" "Imperial Bow" "Imperial Buckler" "Leather Belt" "Maraketh Bow" "Mirrored Spiked Shield" "Pinnacle Tower Shield" "Rustic Sash" "Vile Arrow Quiver"
	SetBorderColor 200 200 0 185

# Level 85 crafting bases

Show # %D4 $type->crafting->generalgear $tier->t1_85
	Mirrored False
	Corrupted False
	ItemLevel >= 85
	Rarity Normal Magic Rare
	BaseType == "Divine Crown" "Giantslayer Helmet" "Haunted Bascinet" "Leviathan Gauntlets" "Lich's Circlet" "Majestic Pelt" "Paladin Gloves" "Phantom Mitts" "Torturer's Mask" "Velour Gloves" "Warlock Gloves" "Wyvernscale Gauntlets"
	SetBorderColor 200 200 0 255

Show # %D3 $type->crafting->generalgear $tier->t2_85
	Mirrored False
	Corrupted False
	ItemLevel >= 85
	Rarity Normal Magic Rare
	BaseType == "Apothecary's Gloves" "Blue Pearl Amulet" "Bone Helmet" "Fingerless Silk Gloves" "Marble Amulet" "Onyx Amulet" "Spiked Gloves"
	SetBorderColor 200 200 0 185

#Show # %D2 $type->crafting->generalgear $tier->t3_85

# Mirrored False

# Corrupted False

# ItemLevel >= 85

# Rarity Normal Magic Rare

# BaseType == "Agate Amulet" "Citrine Amulet" "Seaglass Amulet" "Turquoise Amulet"

# SetBorderColor 200 200 0 185

# Level 84 crafting bases

Show # %D4 $type->crafting->generalgear $tier->t1_84
	Mirrored False
	Corrupted False
	ItemLevel >= 84
	Rarity Normal Magic Rare
	BaseType == "Iolite Ring" "Opal Ring" "Steel Ring" "Vermillion Ring"
	SetBorderColor 200 200 0 255

Show # %D3 $type->crafting->generalgear $tier->t2_84
	Mirrored False
	Corrupted False
	ItemLevel >= 84
	Rarity Normal Magic Rare
	BaseType == "Amethyst Ring" "Bone Ring" "Cerulean Ring" "Convoking Wand" "Copper Kris" "Diamond Ring" "Golden Kris" "Imperial Skean" "Kinetic Wand" "Moonstone Ring" "Opal Sceptre" "Opal Wand" "Pagan Wand" "Platinum Kris" "Prismatic Ring" "Profane Wand" "Prophecy Wand" "Two-Stone Ring" "Unset Ring" "Void Sceptre"
	SetBorderColor 200 200 0 185

#Show # %D2 $type->crafting->generalgear $tier->t3_84

# Mirrored False

# Corrupted False

# ItemLevel >= 84

# Rarity Normal Magic Rare

# BaseType == "Convening Wand" "Eclipse Staff" "Karui Sceptre" "Lathi" "Sambar Sceptre"

# SetBorderColor 200 200 0 185

# Level 83 crafting bases

#Show # %D4 $type->crafting->generalgear $tier->t1_83

# Mirrored False

# Corrupted False

# ItemLevel >= 83

# Rarity Normal Magic Rare

# SetBorderColor 200 200 0 255

Show # %D3 $type->crafting->generalgear $tier->t2_83
	Mirrored False
	Corrupted False
	ItemLevel >= 83
	Rarity Normal Magic Rare
	BaseType == "Battered Foil" "Despot Axe" "Gemini Claw" "Imperial Claw" "Jewelled Foil" "Reaver Axe" "Reaver Sword" "Siege Axe" "Vaal Axe" "Whalebone Rapier"
	SetBorderColor 200 200 0 185

#Show # %D2 $type->crafting->generalgear $tier->t3_83

# Mirrored False

# Corrupted False

# ItemLevel >= 83

# Rarity Normal Magic Rare

# BaseType == "Ambusher" "Basket Rapier" "Behemoth Mace" "Corsair Sword" "Eternal Sword" "Exquisite Blade" "Ezomyte Blade" "Ezomyte Staff" "Fleshripper" "Judgement Staff" "Karui Chopper" "Legion Hammer" "Maelström Staff" "Meatgrinder" "Piledriver" "Royal Axe" "Runic Hatchet" "Sai" "Spiraled Foil" "Sundering Axe"

# SetBorderColor 200 200 0 185

#===============================================================================================================

# [[2400]] Chancing Bases

#===============================================================================================================

# !! Waypoint c5.chancing : "Chancing bases" : "Recipes and Linked Gear"

#Show # %D1 $type->chancing $tier->hh

# Mirrored False

# Corrupted False

# Rarity Normal

# BaseType == "Heavy Belt" "Leather Belt"

# SetFontSize 35

# SetTextColor 255 255 255 255

# SetBorderColor 0 150 0 90

#Show # %D1 $type->chancing $tier->t2

# Mirrored False

# Corrupted False

# Rarity Normal

# BaseType == "Champion Kite Shield"

# SetFontSize 35

# SetTextColor 255 255 255 255

# SetBorderColor 0 150 0 90

#===============================================================================================================

# [[2500]] Endgame Flasks & Tinctures

#===============================================================================================================

# !! Waypoint c6.flasks.all : "Endgame Flasks - All non-unique" : "Flasks and Tinctures"

Show # %D9 $type->endgametinctures $tier->overqual1
	Mirrored False
	Corrupted False
	Quality >= 26
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Tinctures"
	AreaLevel >= 68
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->endgametinctures $tier->overqual2
	Mirrored False
	Corrupted False
	Quality >= 21
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Tinctures"
	AreaLevel >= 68
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->endgametinctures $tier->tinc85
	ItemLevel >= 85
	Rarity Normal Magic
	Class == "Tinctures"
	AreaLevel >= 68
	SetFontSize 45
	SetBorderColor 50 200 125
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

Show # %D4 $type->endgametinctures $tier->tinc82
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Tinctures"
	AreaLevel >= 68
	SetFontSize 45
	SetBorderColor 0 0 0 255
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

Show # %D3 $type->endgametinctures $tier->any
	Rarity Normal Magic
	Class == "Tinctures"
	AreaLevel >= 68
	SetFontSize 45
	SetBorderColor 0 0 0 255
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

#------------------------------------

# [2501] Endgame Flasks

#------------------------------------

Show # %D4 $type->endgameflasks $tier->overqualcorrupted
	Corrupted True
	Quality >= 30
	Rarity Magic
	Class == "Utility Flasks"
	BaseType == "Amethyst Flask" "Basalt Flask" "Bismuth Flask" "Diamond Flask" "Gold Flask" "Granite Flask" "Iron Flask" "Jade Flask" "Quartz Flask" "Quicksilver Flask" "Ruby Flask" "Sapphire Flask" "Silver Flask" "Stibnite Flask" "Sulphur Flask" "Topaz Flask"
	AreaLevel >= 68
	SetFontSize 45
	SetBorderColor 120 0 0 240
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

Show # %D9 $type->endgameflasks $tier->overqualutil1
	Mirrored False
	Corrupted False
	Quality >= 26
	ItemLevel >= 84
	Rarity Normal Magic
	Class == "Utility Flasks"
	AreaLevel >= 68
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->endgameflasks $tier->overqualutil2
	Mirrored False
	Corrupted False
	Quality >= 21
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Utility Flasks"
	BaseType == "Amethyst Flask" "Basalt Flask" "Bismuth Flask" "Diamond Flask" "Gold Flask" "Granite Flask" "Iron Flask" "Jade Flask" "Quartz Flask" "Quicksilver Flask" "Ruby Flask" "Sapphire Flask" "Silver Flask" "Stibnite Flask" "Sulphur Flask" "Topaz Flask"
	AreaLevel >= 68
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D6 $type->endgameflasks $tier->overquallife1
	Mirrored False
	Corrupted False
	Quality >= 30
	ItemLevel >= 82
	Rarity Normal Magic
	BaseType == "Divine Life Flask" "Divine Mana Flask" "Eternal Life Flask" "Eternal Mana Flask" "Hallowed Hybrid Flask"
	AreaLevel >= 68
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->endgameflasks $tier->overquallife2
	Mirrored False
	Corrupted False
	Quality >= 21
	ItemLevel >= 82
	Rarity Normal Magic
	BaseType == "Divine Life Flask" "Divine Mana Flask" "Eternal Life Flask" "Eternal Mana Flask" "Hallowed Hybrid Flask"
	AreaLevel >= 68
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

# !! Waypoint c6.flasks.eg : "Endgame Flasks - High level utility and life flasks" : "Flasks and Tinctures"

Show # %D5 $type->endgameflasks $tier->utility85
	Mirrored False
	Corrupted False
	ItemLevel >= 85
	Rarity Normal Magic
	Class == "Utility Flasks"
	BaseType == "Amethyst Flask" "Basalt Flask" "Bismuth Flask" "Diamond Flask" "Gold Flask" "Granite Flask" "Iron Flask" "Jade Flask" "Quartz Flask" "Quicksilver Flask" "Ruby Flask" "Sapphire Flask" "Silver Flask" "Stibnite Flask" "Sulphur Flask" "Topaz Flask"
	AreaLevel >= 68
	SetFontSize 45
	SetTextColor 50 200 125
	SetBorderColor 50 200 125
	SetBackgroundColor 25 100 75
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # %D4 $type->endgameflasks $tier->utility84
	Mirrored False
	Corrupted False
	ItemLevel >= 84
	Rarity Normal Magic
	Class == "Utility Flasks"
	BaseType == "Amethyst Flask" "Basalt Flask" "Bismuth Flask" "Diamond Flask" "Gold Flask" "Granite Flask" "Iron Flask" "Jade Flask" "Quartz Flask" "Quicksilver Flask" "Ruby Flask" "Sapphire Flask" "Silver Flask" "Stibnite Flask" "Sulphur Flask" "Topaz Flask"
	AreaLevel >= 68
	SetFontSize 45
	SetBorderColor 50 200 125
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

Show # %D4 $type->endgameflasks $tier->utility82
	Mirrored False
	Corrupted False
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Utility Flasks"
	AreaLevel >= 68
	SetFontSize 45
	SetBorderColor 0 0 0 255
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

Show # %D3 $type->endgameflasks $tier->lifemana82
	Mirrored False
	Corrupted False
	Quality >= 10
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Life Flasks" "Mana Flasks"
	BaseType == "Divine Life Flask" "Divine Mana Flask" "Eternal Life Flask" "Eternal Mana Flask" "Hallowed Hybrid Flask"
	AreaLevel >= 68
	SetFontSize 40
	SetTextColor 0 0 0 255
	SetBorderColor 200 200 200 255
	SetBackgroundColor 130 110 110 255

#------------------------------------

# [2502] Quality High

#------------------------------------

# !! Waypoint c6.flasks.others : "Endgame Flasks - Other flasks" : "Flasks and Tinctures"

#Show # %D2 $type->endgameflasks $tier->any20qualflask

# Quality >= 20

# Rarity Normal

# Class == "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Utility Flasks"

# AreaLevel >= 68

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayEffect Grey Temp

#------------------------------------

# [2503] Quality Low

#------------------------------------

#Show # %D1 $type->endgameflasks $tier->qualityhigh

# Quality >= 10

# Rarity Normal Magic

# Class == "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Tinctures" "Utility Flasks"

# AreaLevel >= 68

# AreaLevel <= 77

# SetFontSize 40

# SetTextColor 0 0 0 255

# SetBorderColor 200 200 200 255

# SetBackgroundColor 130 110 110 255

#Show # %D0 $type->endgameflasks $tier->qualitylow

# Quality >= 1

# Rarity Normal Magic

# Class == "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Tinctures" "Utility Flasks"

# AreaLevel >= 68

# AreaLevel <= 77

# SetFontSize 35

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 130 110 110 255

#------------------------------------

# [2504] Utility flasks

#------------------------------------

Show # %D4 $type->endgameflasks $tier->earlymappingflasks
	Mirrored False
	Corrupted False
	Rarity Normal Magic
	Class == "Utility Flasks"
	AreaLevel >= 68
	AreaLevel <= 75
	SetFontSize 45
	SetBorderColor 0 0 0 255
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

Show # %D3 $type->endgameflasks $tier->anyutility
	Mirrored False
	Corrupted False
	Rarity Normal Magic
	Class == "Utility Flasks"
	AreaLevel >= 68
	SetFontSize 40
	SetBorderColor 0 0 0 255
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

#------------------------------------

# [2505] Early mapping life/mana/utility flasks

#------------------------------------

#Show # %D2 $type->endgameflasks $tier->earlymappinglifemana

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# BaseType == "Divine Life Flask" "Divine Mana Flask" "Eternal Life Flask" "Eternal Mana Flask" "Hallowed Hybrid Flask"

# AreaLevel >= 68

# AreaLevel <= 70

# SetBorderColor 100 100 100 150

# SetBackgroundColor 20 20 0 180

#===============================================================================================================

# [[2600]] Misc Rules

#===============================================================================================================

# !! Waypoint c6.misc.others : "SpecialGear - Overquality items and optional animated weapon module" : "Gear - Exotic"

#Show # $type->animatedweapons $tier->normalmelee

# Rarity Normal

# Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"

# SetFontSize 18

# SetBorderColor 230 0 0 255

# SetBackgroundColor 20 20 0 100

#Show # $type->animatedweapons $tier->normalranged

# Rarity Normal

# Class == "Bows" "Wands"

# SetFontSize 18

# SetBorderColor 230 0 0 255

# SetBackgroundColor 20 20 0 100

#Show # $type->animatedweapons $tier->magicmelee

# Rarity Magic

# Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"

# SetFontSize 18

# SetBorderColor 230 0 0 255

# SetBackgroundColor 20 20 0 100

#Show # $type->animatedweapons $tier->magicranged

# Rarity Magic

# Class == "Bows" "Wands"

# SetFontSize 18

# SetBorderColor 230 0 0 255

# SetBackgroundColor 20 20 0 100

#------------------------------------

# [2601] RGB Endgame

#------------------------------------

# !! Waypoint c6.recipes.rgb.all : "Recipes - Endgame chromatic recipes (normal and magic RGBs)" : "Recipes and Linked Gear"

# Legacy RBG rules, will be deleted once confirmed no longer important

#Show # %D5 $type->endgamergb $tier->rgbsmall1

# Width 2

# Height 2

# Rarity Normal Magic Rare

# SocketGroup "RGB"

# AreaLevel >= 68

# AreaLevel <= 83

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Hexagon

#Show # %D5 $type->endgamergb $tier->rgbsmall2

# Width 1

# Height <= 4

# Rarity Normal Magic Rare

# SocketGroup "RGB"

# AreaLevel >= 68

# AreaLevel <= 83

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Hexagon

#Show # %D4 $type->endgamergb $tier->rgblarge

# Width 2

# Height 4

# Rarity Normal Magic Rare

# SocketGroup "RGB"

# AreaLevel >= 68

# AreaLevel <= 83

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Hexagon

#Show # %D4 $type->endgamergb $tier->rgbmedium

# Width 2

# Height 3

# Rarity Normal Magic Rare

# SocketGroup "RGB"

# AreaLevel >= 68

# AreaLevel <= 83

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Hexagon

#------------------------------------

# [2602] Remaining Rares

#------------------------------------

# !! Waypoint c6.rares.remaining : "Rares - lowest tier" : "Gear - Regular Rares"

#Show # %D1 $type->rr $tier->t5

# ItemLevel >= 68

# Rarity Rare

# Class == "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# SetFontSize 35

# SetBackgroundColor 80 80 80 100

#===============================================================================================================

# [[2700]] Hide Layer 1 - Rare & Magic Gear

#===============================================================================================================

# !! Waypoint c6.hidelayer.endgame : "HIDELAYER - all endgame and magic and normal items"

Hide # $type->hidelayer $tier->normalmagicendgame
	Rarity Normal Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Utility Flasks" "Wands" "Warstaves"
	AreaLevel >= 68
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # $type->hidelayer $tier->raresendgame
	ItemLevel >= 68
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

#===============================================================================================================

# [[2800]] Jewels

#===============================================================================================================

# !! Waypoint c7.jewels.identified : "Jewels - Identified with interesting mods" : "Jewels and Cluster Jewels"

#------------------------------------

# [2801] Special Cases

#------------------------------------

Show # %D4 $type->jewels->special $tier->1modcorrupted
	Corrupted True
	CorruptedMods >= 1
	Rarity Rare
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Ghastly Eye Jewel" "Hypnotic Eye Jewel" "Murderous Eye Jewel" "Searching Eye Jewel" "Viridian Jewel"
	SetFontSize 45
	SetTextColor 220 220 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 120 120 0 225
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show # %D4 $type->jewels->special $tier->1moduncorrupted
	Identified True
	Rarity Normal Magic Rare
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	HasExplicitMod "Shimmering" "Vivid" "Stalwart" "Resplendent" "Expediting"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show # %D3 $type->jewels->special $tier->any
	Corrupted True
	CorruptedMods >= 1
	Rarity Magic
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	SetFontSize 40
	SetTextColor 0 75 250 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 20 40 255
	PlayAlertSound 3 300
	PlayEffect Blue

#------------------------------------

# [2802] Leveling Exceptions

#------------------------------------

# !! Waypoint c7.jewels.leveling : "Jewels - Leveling Overrides" : "Jewels and Cluster Jewels"

Show # %D3 $type->jewels->leveling $tier->abyss
	ItemLevel <= 67
	Rarity Normal Magic
	BaseType == "Ghastly Eye Jewel" "Hypnotic Eye Jewel" "Murderous Eye Jewel" "Searching Eye Jewel"
	SetFontSize 45
	SetTextColor 0 75 250 255
	SetBorderColor 0 75 250 255
	SetBackgroundColor 0 20 40 255

Show # %D3 $type->jewels->leveling $tier->generic
	ItemLevel <= 67
	Rarity Normal Magic
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	SetFontSize 45
	SetTextColor 0 75 250 255
	SetBorderColor 0 75 250 255
	SetBackgroundColor 0 20 40 255

#------------------------------------

# [2803] Abyss Jewels

#------------------------------------

# !! Waypoint c7.jewels.abyss.all : "Jewels - Abyss Jewels" : "Jewels and Cluster Jewels"

Show # %H7 $type->jewels->abyss $tier->extramodcorruptedabyssjewel
	Corrupted True
	Rarity Rare
	Class == "Abyss Jewels"
	HasExplicitMod >=5 "a" "e" "i" "o" "u" "y"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %H5 $type->jewels->abyss $tier->corruptedabyssjewel
	Corrupted True
	Rarity Rare
	Class == "Abyss Jewels"
	SetFontSize 45
	SetTextColor 220 220 0 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 120 120 0 225
	PlayEffect Grey
	MinimapIcon 2 Grey Diamond

Show # %H5 $type->jewels->abyss $tier->veryhighrare
	ItemLevel >= 86
	Rarity Rare
	Class == "Abyss Jewels"
	SetFontSize 45
	SetTextColor 220 220 0 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 120 120 0 225
	PlayEffect Grey
	MinimapIcon 2 Grey Diamond

Show # %HS4 $type->jewels->abyss $tier->veryhighmagic
	ItemLevel >= 86
	Rarity Normal Magic
	Class == "Abyss Jewels"
	SetFontSize 40
	SetTextColor 0 75 250 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 0 20 40 255

Show # %HS4 $type->jewels->abyss $tier->highrare
	ItemLevel >= 82
	Rarity Rare
	Class == "Abyss Jewels"
	SetFontSize 45
	SetTextColor 220 220 0 255
	SetBorderColor 200 120 0 220
	SetBackgroundColor 120 120 0 225
	PlayEffect Grey
	MinimapIcon 2 Grey Diamond

Show # %HS3 $type->jewels->abyss $tier->highmagic
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Abyss Jewels"
	SetFontSize 40
	SetTextColor 0 75 250 255
	SetBorderColor 200 120 0 220
	SetBackgroundColor 0 20 40 255

Show # %HS3 $type->jewels->abyss $tier->anyrare
	Rarity Rare
	Class == "Abyss Jewels"
	SetFontSize 45
	SetTextColor 220 220 0 255
	SetBorderColor 220 220 0 255
	SetBackgroundColor 120 120 0 225
	PlayEffect Grey
	MinimapIcon 2 Grey Diamond

Hide # %H2 $type->jewels->abyss $tier->anymagic
	Rarity Normal Magic
	Class == "Abyss Jewels"
	SetFontSize 40
	SetTextColor 0 75 250 255
	SetBorderColor 0 75 250 255
	SetBackgroundColor 0 20 40 255

#------------------------------------

# [2804] Generic Jewels

#------------------------------------

# !! Waypoint c7.jewels.generic.all : "Jewels - Generic Jewels"

Show # %HS3 $type->jewels->generic $tier->anyrare
	Rarity Rare
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	SetFontSize 45
	SetTextColor 220 220 0 255
	SetBorderColor 220 220 0 255
	SetBackgroundColor 120 120 0 225
	PlayEffect Grey Temp
	MinimapIcon 2 Grey Diamond

Hide # %H2 $type->jewels->generic $tier->anymagic
	Rarity Normal Magic
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	SetFontSize 40
	SetTextColor 0 75 250 255
	SetBorderColor 0 75 250 255
	SetBackgroundColor 0 20 40 255

#------------------------------------

# [2805] Cluster Jewels: Eco-Based-Large

#------------------------------------

# !! Waypoint c7.jewels.cluster.all : "Jewels - Cluster - Economy-Based-Tiering" : "Jewels and Cluster Jewels"

Show # $type->jewels->clustereco $tier->n12_i84_t1
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 12
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while holding a Shield" "Chaos Damage" "Dagger and Claw Damage" "Fire Damage" "Lightning Damage" "Minion Damage" "Spell Damage" "Wand Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n12_i75_t1
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 12
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n12_i68_t1
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 12
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while Dual Wielding" "Elemental Damage" "Fire Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n11_i84_t1
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 11
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Chaos Damage" "Fire Damage" "Lightning Damage" "Minion Damage" "Physical Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n11_i75_t1
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 11
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while Dual Wielding" "Axe and Sword Damage" "Fire Damage" "Lightning Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

#Show # $type->jewels->clustereco $tier->n11_i68_t1

# ItemLevel >= 68

# ItemLevel <= 74

# Rarity Normal Magic Rare

# EnchantmentPassiveNum 11

# BaseType == "Large Cluster Jewel"

# SetFontSize 45

# SetTextColor 150 0 255 255

# SetBorderColor 240 100 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Star

#Show # $type->jewels->clustereco $tier->n10_i84_t1

# ItemLevel >= 84

# Rarity Normal Magic Rare

# EnchantmentPassiveNum 10

# BaseType == "Large Cluster Jewel"

# SetFontSize 45

# SetTextColor 150 0 255 255

# SetBorderColor 240 100 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n10_i75_t1
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 10
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Minion Damage" "Physical Damage" "Spell Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n10_i68_t1
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 10
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Elemental Damage" "Lightning Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

#Show # $type->jewels->clustereco $tier->n9_i84_t1

# ItemLevel >= 84

# Rarity Normal Magic Rare

# EnchantmentPassiveNum 9

# BaseType == "Large Cluster Jewel"

# SetFontSize 45

# SetTextColor 150 0 255 255

# SetBorderColor 240 100 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n9_i75_t1
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 9
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n9_i68_t1
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 9
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Physical Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n8_i84_t1
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 8
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Axe and Sword Damage" "Chaos Damage" "Damage with Two Handed Weapons" "Fire Damage" "Mace and Staff Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n8_i75_t1
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 8
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n8_i68_t1
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 8
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Attack Damage while holding a Shield" "Cold Damage" "Damage with Two Handed Weapons" "Elemental Damage" "Fire Damage" "Lightning Damage" "Physical Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n6_i84_t1
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 6
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Exerted Attack Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

#Show # $type->jewels->clustereco $tier->n6_i75_t1

# ItemLevel >= 75

# ItemLevel <= 83

# Rarity Normal Magic Rare

# EnchantmentPassiveNum 6

# BaseType == "Medium Cluster Jewel"

# SetFontSize 45

# SetTextColor 150 0 255 255

# SetBorderColor 240 100 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n6_i68_t1
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 6
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Totem Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n4_i84_t1
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 5
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Fire Damage over Time" "Projectile Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n4_i75_t1
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 5
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Brand Damage" "Life and Mana recovery from Flasks"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n4_i68_t1
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 5
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Damage over Time" "Effect of Non-Damaging Ailments" "Fire Damage over Time" "Minion Life" "Physical Damage over Time" "Totem Damage"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n3_i84_t1
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 3
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Lightning Resistance" "Mana"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n3_i75_t1
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 3
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Energy Shield" "Reservation Efficiency"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n3_i68_t1
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 3
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Armour" "Chance to Block Attack Damage" "Curse Effect" "Reservation Efficiency"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->jewels->clustereco $tier->n2_i84_t1
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 2
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Chance to Block Spell Damage" "Chaos Resistance" "Lightning Resistance" "Mana"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Star

#Show # $type->jewels->clustereco $tier->n2_i75_t1

# ItemLevel >= 75

# ItemLevel <= 83

# Rarity Normal Magic Rare

# EnchantmentPassiveNum 2

# BaseType == "Small Cluster Jewel"

# SetFontSize 45

# SetTextColor 150 0 255 255

# SetBorderColor 240 100 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Star

#Show # $type->jewels->clustereco $tier->n2_i68_t1

# ItemLevel >= 68

# ItemLevel <= 74

# Rarity Normal Magic Rare

# EnchantmentPassiveNum 2

# BaseType == "Small Cluster Jewel"

# SetFontSize 45

# SetTextColor 150 0 255 255

# SetBorderColor 240 100 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Star

Show # %D8 $type->jewels->clustereco $tier->n12_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 12
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Axe and Sword Damage" "Bow Damage" "Chaos Damage" "Cold Damage" "Dagger and Claw Damage" "Damage with Two Handed Weapons" "Elemental Damage" "Fire Damage" "Lightning Damage" "Mace and Staff Damage" "Minion Damage" "Physical Damage" "Spell Damage" "Wand Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n12_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 12
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Attack Damage while Dual Wielding" "Fire Damage" "Mace and Staff Damage" "Minion Damage" "Physical Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n12_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 12
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while Dual Wielding" "Elemental Damage" "Fire Damage" "Spell Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D8 $type->jewels->clustereco $tier->n11_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 11
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Bow Damage" "Chaos Damage" "Dagger and Claw Damage" "Elemental Damage" "Fire Damage" "Lightning Damage" "Mace and Staff Damage" "Minion Damage" "Physical Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n11_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 11
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Axe and Sword Damage" "Bow Damage" "Fire Damage" "Lightning Damage" "Mace and Staff Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n11_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 11
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Elemental Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D8 $type->jewels->clustereco $tier->n10_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 10
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while holding a Shield" "Bow Damage" "Chaos Damage" "Cold Damage" "Dagger and Claw Damage" "Fire Damage" "Lightning Damage" "Mace and Staff Damage" "Minion Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n10_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 10
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Cold Damage" "Lightning Damage" "Minion Damage" "Physical Damage" "Spell Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n10_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 10
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Elemental Damage" "Lightning Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D8 $type->jewels->clustereco $tier->n9_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 9
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Axe and Sword Damage" "Chaos Damage" "Cold Damage" "Dagger and Claw Damage" "Damage with Two Handed Weapons" "Elemental Damage" "Fire Damage" "Mace and Staff Damage" "Minion Damage" "Physical Damage" "Spell Damage" "Wand Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n9_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 9
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Lightning Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n9_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 9
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Axe and Sword Damage" "Damage with Two Handed Weapons" "Lightning Damage" "Physical Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D8 $type->jewels->clustereco $tier->n8_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 8
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Axe and Sword Damage" "Bow Damage" "Chaos Damage" "Cold Damage" "Dagger and Claw Damage" "Damage with Two Handed Weapons" "Elemental Damage" "Fire Damage" "Lightning Damage" "Mace and Staff Damage" "Minion Damage" "Physical Damage" "Spell Damage" "Wand Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n8_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 8
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Axe and Sword Damage" "Chaos Damage" "Cold Damage" "Fire Damage" "Mace and Staff Damage" "Spell Damage" "Wand Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n8_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 8
	BaseType == "Large Cluster Jewel"
	EnchantmentPassiveNode "Attack Damage" "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Bow Damage" "Chaos Damage" "Cold Damage" "Dagger and Claw Damage" "Damage with Two Handed Weapons" "Elemental Damage" "Fire Damage" "Lightning Damage" "Mace and Staff Damage" "Minion Damage" "Physical Damage" "Spell Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D8 $type->jewels->clustereco $tier->n6_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 6
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Brand Damage" "Cold Damage over Time" "Exerted Attack Damage" "Flask Duration" "Life and Mana recovery from Flasks" "Physical Damage over Time" "Totem Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n6_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 6
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Damage while you have a Herald" "Fire Damage over Time" "Flask Duration"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n6_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 6
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Cold Damage over Time" "Fire Damage over Time" "Totem Damage" "Trap and Mine Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D8 $type->jewels->clustereco $tier->n4_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 5
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Channelling Skill Damage" "Chaos Damage over Time" "Damage while you have a Herald" "Exerted Attack Damage" "Fire Damage over Time" "Flask Duration" "Projectile Damage" "Totem Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n4_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 5
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Brand Damage" "Chaos Damage over Time" "Cold Damage over Time" "Damage while you have a Herald" "Exerted Attack Damage" "Life and Mana recovery from Flasks" "Minion Damage while you have a Herald" "Minion Life" "Physical Damage over Time" "Projectile Damage" "Trap and Mine Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n4_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 5
	BaseType == "Medium Cluster Jewel"
	EnchantmentPassiveNode "Area Damage" "Brand Damage" "Chaos Damage over Time" "Critical Chance" "Damage over Time" "Damage while you have a Herald" "Effect of Non-Damaging Ailments" "Exerted Attack Damage" "Fire Damage over Time" "Minion Life" "Physical Damage over Time" "Totem Damage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D8 $type->jewels->clustereco $tier->n3_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 3
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Armour" "Chance to Block Attack Damage" "Chance to Block Spell Damage" "Chaos Resistance" "Cold Resistance" "Curse Effect" "Energy Shield" "Life" "Lightning Resistance" "Mana" "Suppres"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n3_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 3
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Chance to Block Attack Damage" "Chance to Block Spell Damage" "Energy Shield" "Reservation Efficiency"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n3_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 3
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Armour" "Chance to Block Attack Damage" "Curse Effect" "Life" "Mana" "Reservation Efficiency"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D8 $type->jewels->clustereco $tier->n2_i84_t2
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 2
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Armour" "Chance to Block Attack Damage" "Chance to Block Spell Damage" "Chaos Resistance" "Energy Shield" "Life" "Lightning Resistance" "Mana" "Reservation Efficiency" "Suppres"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n2_i75_t2
	ItemLevel >= 75
	ItemLevel <= 83
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 2
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Armour" "Energy Shield" "Evasion" "Lightning Resistance" "Reservation Efficiency"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D7 $type->jewels->clustereco $tier->n2_i68_t2
	ItemLevel >= 68
	ItemLevel <= 74
	Rarity Normal Magic Rare
	EnchantmentPassiveNum 2
	BaseType == "Small Cluster Jewel"
	EnchantmentPassiveNode "Armour" "Chance to Block Attack Damage" "Energy Shield"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 100 0 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

# !! Waypoint c7.jewels.cluster.good : "Jewels - Cluster - Others" : "Jewels and Cluster Jewels"

#------------------------------------

# [2806] Cluster Jewels: Random

#------------------------------------

Show # %D6 $type->jewels->cluster $tier->optimal1highlarge
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum >= 12
	BaseType == "Large Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D6 $type->jewels->cluster $tier->optimalhighlarge
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 8
	BaseType == "Large Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D4 $type->jewels->cluster $tier->highlarge
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 8
	BaseType == "Large Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Pentagon

Show # %H3 $type->jewels->cluster $tier->large
	Rarity Normal Magic Rare
	BaseType == "Large Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 150 0 255 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect Grey Temp
	MinimapIcon 2 Grey Pentagon

Show # %D6 $type->jewels->cluster $tier->optimalhighmedium
	ItemLevel >= 84
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 5
	BaseType == "Medium Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Pentagon

Show # %D4 $type->jewels->cluster $tier->highmedium
	Rarity Normal Magic Rare
	EnchantmentPassiveNum <= 5
	BaseType == "Medium Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Pentagon

Show # %H3 $type->jewels->cluster $tier->medium
	Rarity Normal Magic Rare
	BaseType == "Medium Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 150 0 255 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect Grey Temp
	MinimapIcon 2 Grey Pentagon

Show # %D6 $type->jewels->cluster $tier->highsmall
	ItemLevel >= 84
	Rarity Normal Magic Rare
	BaseType == "Small Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 240 100 0 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Pentagon

Show # %H3 $type->jewels->cluster $tier->small
	Rarity Normal Magic Rare
	BaseType == "Small Cluster Jewel"
	SetFontSize 45
	SetTextColor 150 0 255 255
	SetBorderColor 150 0 255 255
	SetBackgroundColor 34 0 67 255
	PlayAlertSound 2 300
	PlayEffect Grey Temp
	MinimapIcon 2 Grey Pentagon

#===============================================================================================================

# [[2900]] Heist Gear

#===============================================================================================================

# !! Waypoint c7.heist.all : "Heist Gear" : "Heist, Expedition, Sanctum"

#------------------------------------

# [2901] Heist Cloak

#------------------------------------

Show # %HS5 $type->heist->cloak $tier->t1highlevel
	ItemLevel >= 83
	Rarity Normal Magic Rare
	Class == "Heist Cloaks"
	BaseType == "Whisper-woven Cloak"
	SetFontSize 45
	SetTextColor 245 190 0 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Raindrop

Show # %H5 $type->heist->cloak $tier->t1
	Rarity Normal Magic Rare
	Class == "Heist Cloaks"
	BaseType == "Whisper-woven Cloak"
	SetFontSize 45
	SetBorderColor 255 85 85 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect White
	MinimapIcon 1 White Raindrop

Show # %H4 $type->heist->cloak $tier->t2
	Rarity Normal Magic Rare
	Class == "Heist Cloaks"
	BaseType == "Hooded Cloak" "Tattered Cloak"
	SetFontSize 45
	SetBorderColor 255 85 85 200
	SetBackgroundColor 35 35 35 240
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 1 Grey Raindrop

Show # %H3 $type->heist->cloak $tier->t3any
	Rarity Normal Magic Rare
	Class == "Heist Cloaks"
	SetFontSize 40
	SetBorderColor 255 85 85 200
	SetBackgroundColor 35 35 35 240
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 2 Grey Raindrop

#------------------------------------

# [2902] Heist Brooch

#------------------------------------

Show # %HS5 $type->heist->brooch $tier->t1highlevel
	ItemLevel >= 84
	Rarity Normal Magic Rare
	Class == "Heist Brooches"
	BaseType == "Foliate Brooch"
	SetFontSize 45
	SetTextColor 245 190 0 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Raindrop

Show # %H5 $type->heist->brooch $tier->t1
	Rarity Normal Magic Rare
	Class == "Heist Brooches"
	BaseType == "Foliate Brooch"
	SetFontSize 45
	SetBorderColor 255 85 85 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect White
	MinimapIcon 1 White Raindrop

Show # %H4 $type->heist->brooch $tier->t2
	Rarity Normal Magic Rare
	Class == "Heist Brooches"
	BaseType == "Enamel Brooch"
	SetFontSize 45
	SetBorderColor 255 85 85 200
	SetBackgroundColor 35 35 35 240
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 1 Grey Raindrop

Show # %H3 $type->heist->brooch $tier->t3any
	Rarity Normal Magic Rare
	Class == "Heist Brooches"
	SetFontSize 40
	SetBorderColor 255 85 85 200
	SetBackgroundColor 35 35 35 240
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 2 Grey Raindrop

#------------------------------------

# [2903] Heist Gear

#------------------------------------

Show # %HS5 $type->heist->gear $tier->t1highlevel
	ItemLevel >= 83
	Rarity Normal Magic Rare
	Class == "Heist Gear"
	BaseType == "Burst Band" "Fragmenting Arrowhead" "Obsidian Sharpening Stone" "Precise Arrowhead"
	SetFontSize 45
	SetTextColor 245 190 0 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Raindrop

Show # %H5 $type->heist->gear $tier->t1
	Rarity Normal Magic Rare
	Class == "Heist Gear"
	BaseType == "Burst Band" "Fragmenting Arrowhead" "Obsidian Sharpening Stone" "Precise Arrowhead"
	SetFontSize 45
	SetBorderColor 255 85 85 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect White
	MinimapIcon 1 White Raindrop

Show # %H4 $type->heist->gear $tier->t2
	Rarity Normal Magic Rare
	Class == "Heist Gear"
	BaseType == "Aggregator Charm" "Fine Sharpening Stone" "Hollowpoint Arrowhead"
	SetFontSize 45
	SetBorderColor 255 85 85 200
	SetBackgroundColor 35 35 35 240
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 1 Grey Raindrop

Show # %H3 $type->heist->gear $tier->t3any
	Rarity Normal Magic Rare
	Class == "Heist Gear"
	SetFontSize 40
	SetBorderColor 255 85 85 200
	SetBackgroundColor 35 35 35 240
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 2 Grey Raindrop

#------------------------------------

# [2904] Heist Tool

#------------------------------------

Show # %HS5 $type->heist->tool $tier->t1highlevel
	ItemLevel >= 83
	Rarity Normal Magic Rare
	Class == "Heist Tools"
	BaseType == "Grandmaster Keyring" "Master Lockpick" "Regicide Disguise Kit" "Silkweave Sole" "Steel Bracers" "Thaumaturgical Sensing Charm" "Thaumaturgical Ward" "Thaumetic Blowtorch" "Thaumetic Flashpowder"
	SetFontSize 45
	SetTextColor 245 190 0 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Raindrop

Show # %H5 $type->heist->tool $tier->t1
	Rarity Normal Magic Rare
	Class == "Heist Tools"
	BaseType == "Grandmaster Keyring" "Master Lockpick" "Regicide Disguise Kit" "Silkweave Sole" "Steel Bracers" "Thaumaturgical Sensing Charm" "Thaumaturgical Ward" "Thaumetic Blowtorch" "Thaumetic Flashpowder"
	SetFontSize 45
	SetBorderColor 255 85 85 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect White
	MinimapIcon 1 White Raindrop

Show # %H4 $type->heist->tool $tier->t2
	Rarity Normal Magic Rare
	Class == "Heist Tools"
	BaseType == "Azurite Flashpowder" "Espionage Disguise Kit" "Fine Lockpick" "Polished Sensing Charm" "Runed Bracers" "Shining Ward" "Skeleton Keyring" "Standard Lockpick" "Sulphur Blowtorch" "Winged Sole"
	SetFontSize 45
	SetBorderColor 255 85 85 200
	SetBackgroundColor 35 35 35 240
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 1 Grey Raindrop

Show # %H3 $type->heist->tool $tier->t3any
	Rarity Normal Magic Rare
	Class == "Heist Tools"
	SetFontSize 40
	SetBorderColor 255 85 85 200
	SetBackgroundColor 35 35 35 240
	PlayAlertSound 3 300
	PlayEffect Grey
	MinimapIcon 2 Grey Raindrop

#===============================================================================================================

# [[3000]] Gem Tierlists

#===============================================================================================================

# !! Waypoint c8.gems.all : "Gem Rules - Override All" : "Gems"

#------------------------------------

# [3001] Exceptional Gems - Awakened and AltQuality

#------------------------------------

# !! Waypoint c8.gems.empowerclass : "Gem Rules - Empower Class" : "Gems"

Show # $type->gems->exceptional $tier->highexceptionalbadcorrupt
	Corrupted True
	Quality <= 20
	GemLevel <= 3
	Class == "Skill Gems" "Support Gems"
	BaseType == "Annihilation Support" "Awakened Empower Support" "Awakened Enhance Support" "Awakened Enlighten Support" "Bloodsoaked Banner Support" "Cast on Ward Break Support" "Companionship Support" "Congregation Support" "Cooldown Recovery Support" "Crystalfall Support" "Eclipse Support" "Empower Support" "Enhance Support" "Enlighten Support" "Frostmage Support" "Gluttony Support" "Greater Ancestral Call Support" "Greater Chain Support" "Greater Fork Support" "Greater Multistrike Support" "Greater Spell Cascade Support" "Greater Spell Echo Support" "Greater Unleash Support" "Invert the Rules Support" "Item Quantity Support" "Overloaded Intensity Support" "Pact of Beidat" "Pact of Ghorr" "Pact of K'Tash" "Pact of Lycia" "Scornful Herald Support" "Vaal Temptation Support" "Void Shockwave Support"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # $type->gems->exceptional $tier->t1
	Class == "Skill Gems" "Support Gems"
	BaseType == "Annihilation Support" "Awakened Empower Support" "Awakened Enhance Support" "Awakened Enlighten Support" "Companionship Support" "Congregation Support" "Cooldown Recovery Support" "Eclipse Support" "Empower Support" "Enlighten Support" "Greater Ancestral Call Support" "Greater Multistrike Support" "Greater Spell Cascade Support" "Greater Spell Echo Support" "Item Quantity Support"
	SetFontSize 45
	SetTextColor 0 0 125 255
	SetBorderColor 0 0 125 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %D8 $type->gems->exceptional $tier->t2
	Class == "Skill Gems" "Support Gems"
	BaseType == "Bloodsoaked Banner Support" "Cast on Ward Break Support" "Crystalfall Support" "Enhance Support" "Frostmage Support" "Gluttony Support" "Greater Chain Support" "Greater Fork Support" "Greater Unleash Support" "Invert the Rules Support" "Overloaded Intensity Support" "Pact of Beidat" "Pact of Ghorr" "Pact of K'Tash" "Pact of Lycia" "Scornful Herald Support" "Vaal Temptation Support" "Void Shockwave Support"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # $type->gems->exceptional $tier->anyexceptionallvl
	GemLevel >= 2
	Class == "Skill Gems" "Support Gems"
	BaseType == "Annihilation Support" "Awakened Empower Support" "Awakened Enhance Support" "Awakened Enlighten Support" "Bloodsoaked Banner Support" "Bonespire Support" "Cast on Ward Break Support" "Communion Support" "Companionship Support" "Congregation Support" "Cooldown Recovery Support" "Coursing Current Support" "Crystalfall Support" "Cull the Weak Support" "Divine Sentinel Support" "Eclipse Support" "Eldritch Blasphemy Support" "Empower Support" "Enhance Support" "Enlighten Support" "Fissure Support" "Foulgrasp Support" "Frostmage Support" "Gluttony Support" "Greater Ancestral Call Support" "Greater Chain Support" "Greater Devour Support" "Greater Fork Support" "Greater Kinetic Instability Support" "Greater Multistrike Support" "Greater Spell Cascade Support" "Greater Spell Echo Support" "Greater Unleash Support" "Hexpass Support" "Hextoad Support" "Hiveborn Support" "Invention Support" "Invert the Rules Support" "Item Quantity Support" "Lethal Dose Support" "Machinations Support" "Overheat Support" "Overloaded Intensity Support" "Pacifism Support" "Pact of Beidat" "Pact of Ghorr" "Pact of K'Tash" "Pact of Lycia" "Pyre Support" "Scornful Herald Support" "Transfusion Support" "Unholy Trinity Support" "Vaal Sacrifice Support" "Vaal Temptation Support" "Void Shockwave Support" "Voidstorm Support"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # $type->gems->exceptional $tier->anyexceptionalqual
	Quality >= 10
	Class == "Skill Gems" "Support Gems"
	BaseType == "Annihilation Support" "Awakened Empower Support" "Awakened Enhance Support" "Awakened Enlighten Support" "Bloodsoaked Banner Support" "Bonespire Support" "Cast on Ward Break Support" "Communion Support" "Companionship Support" "Congregation Support" "Cooldown Recovery Support" "Coursing Current Support" "Crystalfall Support" "Cull the Weak Support" "Divine Sentinel Support" "Eclipse Support" "Eldritch Blasphemy Support" "Empower Support" "Enhance Support" "Enlighten Support" "Fissure Support" "Foulgrasp Support" "Frostmage Support" "Gluttony Support" "Greater Ancestral Call Support" "Greater Chain Support" "Greater Devour Support" "Greater Fork Support" "Greater Kinetic Instability Support" "Greater Multistrike Support" "Greater Spell Cascade Support" "Greater Spell Echo Support" "Greater Unleash Support" "Hexpass Support" "Hextoad Support" "Hiveborn Support" "Invention Support" "Invert the Rules Support" "Item Quantity Support" "Lethal Dose Support" "Machinations Support" "Overheat Support" "Overloaded Intensity Support" "Pacifism Support" "Pact of Beidat" "Pact of Ghorr" "Pact of K'Tash" "Pact of Lycia" "Pyre Support" "Scornful Herald Support" "Transfusion Support" "Unholy Trinity Support" "Vaal Sacrifice Support" "Vaal Temptation Support" "Void Shockwave Support" "Voidstorm Support"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %D6 $type->gems->exceptional $tier->t3
	Class == "Skill Gems" "Support Gems"
	BaseType == "Coursing Current Support" "Cull the Weak Support" "Eldritch Blasphemy Support" "Greater Devour Support" "Hexpass Support" "Machinations Support" "Unholy Trinity Support"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 20 240 240 255
	SetBackgroundColor 6 0 60 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Triangle

Show # %D5 $type->gems->exceptional $tier->t4
	Class == "Skill Gems" "Support Gems"
	BaseType == "Bonespire Support" "Communion Support" "Divine Sentinel Support" "Fissure Support" "Foulgrasp Support" "Greater Kinetic Instability Support" "Hextoad Support" "Hiveborn Support" "Invention Support" "Lethal Dose Support" "Overheat Support" "Pacifism Support" "Portal" "Pyre Support" "Transfusion Support" "Vaal Sacrifice Support" "Voidstorm Support"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 20 240 240 255
	SetBackgroundColor 6 0 60 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Triangle

#------------------------------------

# [3002] Economy based leveled, quality and vaal gem rules

#------------------------------------

Show # $type->gems->special $tier->altany
	TransfiguredGem True
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %D8 $type->gems->special $tier->2020z
	Corrupted False
	Quality >= 20
	GemLevel >= 20
	Class == "Skill Gems" "Support Gems"
	BaseType == "Absolution" "Ambush" "Anger" "Animate Guardian" "Arcane Surge Support" "Archmage Support" "Arrogance Support" "Assassin's Mark" "Autoexertion" "Awakened Added Chaos Damage Support" "Awakened Added Cold Damage Support" "Awakened Added Fire Damage Support" "Awakened Added Lightning Damage Support" "Awakened Ancestral Call Support" "Awakened Arrow Nova Support" "Awakened Blasphemy Support" "Awakened Brutality Support" "Awakened Burning Damage Support" "Awakened Cast On Critical Strike Support" "Awakened Cast While Channelling Support" "Awakened Chain Support" "Awakened Cold Penetration Support" "Awakened Controlled Destruction Support" "Awakened Deadly Ailments Support" "Awakened Elemental Damage with Attacks Support" "Awakened Elemental Focus Support" "Awakened Fire Penetration Support" "Awakened Fork Support" "Awakened Generosity Support" "Awakened Greater Multiple Projectiles Support" "Awakened Hextouch Support" "Awakened Lightning Penetration Support" "Awakened Melee Physical Damage Support" "Awakened Melee Splash Support" "Awakened Minion Damage Support" "Awakened Multistrike Support" "Awakened Spell Cascade Support" "Awakened Spell Echo Support" "Awakened Swift Affliction Support" "Awakened Unbound Ailments Support" "Awakened Unleash Support" "Awakened Vicious Projectiles Support" "Awakened Void Manipulation Support" "Blessed Call Support" "Block Chance Reduction Support" "Bone Offering" "Brutality Support" "Burning Damage Support" "Close Combat Support" "Combustion Support" "Controlled Destruction Support" "Deadly Ailments Support" "Despair" "Earthquake" "Earthshatter" "Efficacy Support" "Elemental Damage with Attacks Support" "Elemental Focus Support" "Elemental Penetration Support" "Elemental Weakness" "Enduring Cry" "Enfeeble" "Eternal Blessing Support" "Faster Attacks Support" "Faster Casting Support" "Flame Dash" "Flammability" "Freezing Pulse" "Frostblink" "Haste" "Hypothermia Support" "Immolate Support" "Incinerate" "Increased Critical Damage Support" "Increased Critical Strikes Support" "Inspiration Support" "Malevolence" "Meat Shield Support" "Melee Physical Damage Support" "Melee Splash Support" "Minefield Support" "Molten Shell" "Penance Brand" "Pierce Support" "Power Charge On Critical Support" "Precision" "Pyroclast Mine" "Raise Spectre" "Righteous Fire" "Seismic Cry" "Shield Charge" "Smite" "Static Strike" "Steelskin" "Storm Burst" "Stormblast Mine" "Summon Chaos Golem" "Summon Flame Golem" "Summon Phantasm Support" "Summon Skitterbots" "Summon Stone Golem" "Tempest Shield" "Trap and Mine Damage Support" "Unbound Ailments Support" "Urgent Orders Support" "Vitality" "Volatile Dead" "Volatility Support" "Winter Orb" "Withering Step"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %D8 $type->gems->special $tier->xx20z
	Corrupted False
	Quality >= 19
	Class == "Skill Gems" "Support Gems"
	BaseType == "Animate Guardian" "Arrogance Support" "Assassin's Mark" "Burning Damage Support" "Deadly Ailments Support" "Enduring Cry" "Eternal Blessing Support" "Faster Attacks Support" "Frostblink" "Haste" "Inspiration Support" "Meat Shield Support" "Molten Shell" "Power Charge On Critical Support" "Shield Charge" "Storm Burst" "Summon Flame Golem" "Tempest Shield" "Urgent Orders Support"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %D8 $type->gems->special $tier->2120
	Quality >= 20
	GemLevel >= 21
	Class == "Skill Gems" "Support Gems"
	BaseType == "Animate Guardian" "Arcane Cloak" "Arctic Armour" "Arrogance Support" "Awakened Added Chaos Damage Support" "Awakened Added Cold Damage Support" "Awakened Added Fire Damage Support" "Awakened Added Lightning Damage Support" "Awakened Ancestral Call Support" "Awakened Arrow Nova Support" "Awakened Blasphemy Support" "Awakened Brutality Support" "Awakened Burning Damage Support" "Awakened Cast On Critical Strike Support" "Awakened Cast While Channelling Support" "Awakened Chain Support" "Awakened Cold Penetration Support" "Awakened Controlled Destruction Support" "Awakened Deadly Ailments Support" "Awakened Elemental Damage with Attacks Support" "Awakened Elemental Focus Support" "Awakened Fire Penetration Support" "Awakened Fork Support" "Awakened Generosity Support" "Awakened Greater Multiple Projectiles Support" "Awakened Hextouch Support" "Awakened Lightning Penetration Support" "Awakened Melee Physical Damage Support" "Awakened Melee Splash Support" "Awakened Minion Damage Support" "Awakened Multistrike Support" "Awakened Spell Cascade Support" "Awakened Spell Echo Support" "Awakened Swift Affliction Support" "Awakened Unbound Ailments Support" "Awakened Unleash Support" "Awakened Vicious Projectiles Support" "Awakened Void Manipulation Support" "Battlemage's Cry" "Blade Flurry" "Block Chance Reduction Support" "Blood Rage" "Bone Offering" "Burning Damage Support" "Contagion" "Discharge" "Discipline" "Elemental Damage with Attacks Support" "Elemental Hit" "Enduring Cry" "Enfeeble" "Essence Drain" "Eternal Blessing Support" "Ethereal Knives" "Eviscerate" "Flame Dash" "Flame Link" "Flame Surge" "Flammability" "Forbidden Rite" "Fortify Support" "Frostblink" "Generosity Support" "Grace" "Haste" "Hatred" "Ice Crash" "Ice Spear" "Immortal Call" "Increased Critical Damage Support" "Inspiration Support" "Kinetic Bolt" "Life Leech Support" "Lightning Strike" "Malevolence" "Mana-Infused Staff" "Meat Shield Support" "Melee Physical Damage Support" "Minion Life Support" "Mirage Archer Support" "Molten Shell" "Molten Strike" "More Duration Support" "Penance Brand" "Phase Run" "Plague Bearer" "Precision" "Pulverise Support" "Punishment" "Raise Spectre" "Raise Zombie" "Rallying Cry" "Returning Projectiles Support" "Sacred Wisps Support" "Scorching Ray" "Shield Charge" "Siphoning Trap" "Smite" "Sniper's Mark" "Steelskin" "Summon Flame Golem" "Summon Lightning Golem" "Summon Raging Spirit" "Unbound Ailments Support" "Urgent Orders Support" "Vitality" "Voltaxic Burst" "Vulnerability" "Wrath"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %D8 $type->gems->special $tier->2023
	Quality >= 23
	GemLevel >= 20
	Class == "Skill Gems" "Support Gems"
	BaseType == "Arrogance Support" "Awakened Added Chaos Damage Support" "Awakened Added Cold Damage Support" "Awakened Added Fire Damage Support" "Awakened Added Lightning Damage Support" "Awakened Ancestral Call Support" "Awakened Arrow Nova Support" "Awakened Blasphemy Support" "Awakened Brutality Support" "Awakened Burning Damage Support" "Awakened Cast On Critical Strike Support" "Awakened Cast While Channelling Support" "Awakened Chain Support" "Awakened Cold Penetration Support" "Awakened Controlled Destruction Support" "Awakened Deadly Ailments Support" "Awakened Elemental Damage with Attacks Support" "Awakened Elemental Focus Support" "Awakened Fire Penetration Support" "Awakened Fork Support" "Awakened Generosity Support" "Awakened Greater Multiple Projectiles Support" "Awakened Hextouch Support" "Awakened Lightning Penetration Support" "Awakened Melee Physical Damage Support" "Awakened Melee Splash Support" "Awakened Minion Damage Support" "Awakened Multistrike Support" "Awakened Spell Cascade Support" "Awakened Spell Echo Support" "Awakened Swift Affliction Support" "Awakened Unbound Ailments Support" "Awakened Unleash Support" "Awakened Vicious Projectiles Support" "Awakened Void Manipulation Support" "Block Chance Reduction Support" "Blood Rage" "Controlled Destruction Support" "Despair" "Faster Attacks Support" "Flameblast" "Flammability" "Generosity Support" "Increased Critical Damage Support" "Inspiration Support" "Molten Shell" "More Duration Support" "Pulverise Support" "Sadism Support" "Scorching Ray" "Sniper's Mark" "Summon Chaos Golem" "Summon Flame Golem" "Urgent Orders Support"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %D9 $type->gems->special $tier->2123any
	Quality >= 23
	GemLevel >= 21
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %D8 $type->gems->special $tier->xx23
	Quality >= 23
	Class == "Skill Gems" "Support Gems"
	BaseType == "Awakened Added Chaos Damage Support" "Awakened Added Cold Damage Support" "Awakened Added Fire Damage Support" "Awakened Added Lightning Damage Support" "Awakened Ancestral Call Support" "Awakened Arrow Nova Support" "Awakened Blasphemy Support" "Awakened Brutality Support" "Awakened Burning Damage Support" "Awakened Cast On Critical Strike Support" "Awakened Cast While Channelling Support" "Awakened Chain Support" "Awakened Cold Penetration Support" "Awakened Controlled Destruction Support" "Awakened Deadly Ailments Support" "Awakened Elemental Damage with Attacks Support" "Awakened Elemental Focus Support" "Awakened Fire Penetration Support" "Awakened Fork Support" "Awakened Generosity Support" "Awakened Greater Multiple Projectiles Support" "Awakened Hextouch Support" "Awakened Lightning Penetration Support" "Awakened Melee Physical Damage Support" "Awakened Melee Splash Support" "Awakened Minion Damage Support" "Awakened Multistrike Support" "Awakened Spell Cascade Support" "Awakened Spell Echo Support" "Awakened Swift Affliction Support" "Awakened Unbound Ailments Support" "Awakened Unleash Support" "Awakened Vicious Projectiles Support" "Awakened Void Manipulation Support" "Controlled Destruction Support" "Despair" "Flameblast" "Sadism Support" "Scorching Ray"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %D8 $type->gems->special $tier->21xx
	GemLevel >= 21
	Class == "Skill Gems" "Support Gems"
	BaseType == "Animate Guardian" "Arctic Armour" "Discipline" "Elemental Damage with Attacks Support" "Grace" "Haste" "Hatred" "Immortal Call" "Malevolence" "Mana-Infused Staff" "Meat Shield Support" "Melee Physical Damage Support" "Minion Life Support" "Penance Brand" "Precision" "Raise Spectre" "Unbound Ailments Support" "Vitality" "Wrath"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

#Show # %D6 $type->gems->special $tier->vaal20

# Quality >= 20

# Class == "Skill Gems" "Support Gems"

# SetFontSize 45

# SetTextColor 20 240 240 255

# SetBorderColor 240 0 0 255

# SetBackgroundColor 70 0 20 255

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Triangle

#------------------------------------

# [3003] High Quality and Leveled Gems

#------------------------------------

# !! Waypoint c8.gems.qualityandlevel : "Gem Rules - Quality and Leveled versions" : "Gems"

Show # %D7 $type->gems->generic $tier->lt1
	GemLevel >= 21
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 20 240 240 255
	SetBackgroundColor 6 0 60 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Triangle

Show # %D7 $type->gems->generic $tier->qt1
	Quality >= 23
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 20 240 240 255
	SetBackgroundColor 6 0 60 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Triangle

Show # $type->gems->generic $tier->ex6lvlgems
	GemLevel >= 6
	Class == "Skill Gems" "Support Gems"
	BaseType == "Blood and Sand" "Brand Recall"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 20 240 240 255
	SetBackgroundColor 6 0 60 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Triangle

#Show # $type->gems->generic $tier->plusonegemcold

# Quality >= 5

# Class == "Skill Gems" "Support Gems"

# BaseType == "Added Cold Damage Support" "Arctic Armour" "Bonechill Support" "Cold Penetration Support" "Cold Snap" "Cold to Fire Support" "Creeping Frost" "Discharge" "Elemental Hit" "Elemental Proliferation Support" "Explosive Concoction" "Eye of Winter" "Freezing Pulse" "Frigid Bond Support" "Frost Blades" "Frost Bomb" "Frost Shield" "Frost Wall" "Frostbite" "Frostblink" "Frostbolt" "Frozen Legion" "Glacial Cascade" "Glacial Hammer" "Glacial Shield Swipe" "Hatred" "Herald of Ice" "Hydrosphere" "Hypothermia Support" "Ice Bite Support" "Ice Crash" "Ice Nova" "Ice Shot" "Ice Spear" "Ice Trap" "Icicle Mine" "Prismatic Burst Support" "Purity of Ice" "Siphoning Trap" "Summon Ice Golem" "Summon Skitterbots" "Vaal Arctic Armour" "Vaal Cold Snap" "Vaal Glacial Hammer" "Vaal Ice Nova" "Vaal Ice Shot" "Vaal Impurity of Ice" "Vortex" "Wild Strike" "Winter Orb" "Wintertide Brand"

# SetFontSize 45

# SetTextColor 30 190 190 255

# SetBorderColor 74 230 58 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 1 Green Triangle

#Show # $type->gems->generic $tier->plusonegemfire

# Quality >= 5

# Class == "Skill Gems" "Support Gems"

# BaseType == "Added Fire Damage Support" "Alchemist's Mark" "Anger" "Armageddon Brand" "Artillery Ballista" "Blast Rain" "Blazing Salvo" "Bodyswap" "Burning Arrow" "Burning Damage Support" "Cold to Fire Support" "Combustion Support" "Conflagration" "Consecrated Path" "Controlled Blaze Support" "Cremation" "Detonate Dead" "Discharge" "Divine Blast" "Elemental Hit" "Elemental Proliferation Support" "Excommunicate Support" "Explosive Arrow" "Explosive Concoction" "Explosive Trap" "Fire Penetration Support" "Fireball" "Firestorm" "Flame Dash" "Flame Link" "Flame Surge" "Flame Wall" "Flameblast" "Flamethrower Trap" "Flamewood Support" "Flammability" "Hallow Support" "Herald of Ash" "Holy Flame Totem" "Ignite Proliferation Support" "Immolate Support" "Incinerate" "Infernal Blow" "Infernal Cry" "Infernal Legion Support" "Molten Shell" "Molten Strike" "Prismatic Burst Support" "Purifying Flame" "Purity of Fire" "Pyroclast Mine" "Righteous Fire" "Rolling Magma" "Scorching Ray" "Searing Bond" "Summon Flame Golem" "Summon Raging Spirit" "Tectonic Slam" "Vaal Burning Arrow" "Vaal Fireball" "Vaal Firestorm" "Vaal Flameblast" "Vaal Impurity of Fire" "Vaal Molten Shell" "Vaal Molten Strike" "Vaal Righteous Fire" "Vaal Volcanic Fissure" "Volatile Dead" "Volcanic Fissure" "Wave of Conviction" "Wild Strike"

# SetFontSize 45

# SetTextColor 30 190 190 255

# SetBorderColor 74 230 58 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 1 Green Triangle

#Show # $type->gems->generic $tier->plusonegemlight

# Quality >= 5

# Class == "Skill Gems" "Support Gems"

# BaseType == "Absolution" "Added Lightning Damage Support" "Arc" "Arcane Cloak" "Archmage Support" "Ball Lightning" "Charged Dash" "Conductivity" "Crackling Lance" "Discharge" "Divine Ire" "Divine Retribution" "Elemental Hit" "Elemental Proliferation Support" "Energy Blade" "Excommunicate Support" "Explosive Concoction" "Galvanic Arrow" "Galvanic Field" "Herald of Thunder" "Holy Hammers" "Holy Strike" "Holy Sweep" "Hydrosphere" "Innervate Support" "Lightning Arrow" "Lightning Conduit" "Lightning Penetration Support" "Lightning Spire Trap" "Lightning Strike" "Lightning Tendrils" "Lightning Trap" "Lightning Warp" "Living Lightning Support" "Manabond" "Orb of Storms" "Overcharge Support" "Penance Brand" "Physical to Lightning Support" "Prismatic Burst Support" "Purity of Lightning" "Shield of Light" "Shock Nova" "Sigil of Power" "Smite" "Spark" "Static Strike" "Storm Brand" "Storm Burst" "Storm Call" "Storm Rain" "Stormbind" "Stormblast Mine" "Summon Lightning Golem" "Summon Skitterbots" "Tempest Shield" "Thunderstorm" "Vaal Absolution" "Vaal Arc" "Vaal Impurity of Lightning" "Vaal Lightning Arrow" "Vaal Lightning Strike" "Vaal Lightning Trap" "Vaal Lightning Warp" "Vaal Smite" "Vaal Spark" "Vaal Storm Call" "Voltaxic Burst" "Wave of Conviction" "Wild Strike" "Wrath"

# SetFontSize 45

# SetTextColor 30 190 190 255

# SetBorderColor 74 230 58 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 1 Green Triangle

#Show # $type->gems->generic $tier->plusonegemchaos

# Quality >= 5

# Class == "Skill Gems" "Support Gems"

# BaseType == "Added Chaos Damage Support" "Alchemist's Mark" "Bane" "Blight" "Caustic Arrow" "Chance to Poison Support" "Cobra Lash" "Contagion" "Dark Bargain" "Decay Support" "Desecrate" "Despair" "Essence Drain" "Forbidden Rite" "Herald of Agony" "Hexblast" "Impending Doom Support" "Pestilent Strike" "Plague Bearer" "Poisonous Concoction" "Sacrifice Support" "Scourge Arrow" "Summon Chaos Golem" "Toxic Rain" "Vaal Blight" "Vaal Caustic Arrow" "Vaal Venom Gyre" "Venom Gyre" "Vicious Projectiles Support" "Viper Strike" "Void Manipulation Support" "Void Sphere" "Voltaxic Burst" "Wither" "Withering Step" "Withering Touch Support"

# SetFontSize 45

# SetTextColor 30 190 190 255

# SetBorderColor 74 230 58 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 1 Green Triangle

#Show # $type->gems->generic $tier->plusonegemphys

# Quality >= 5

# Class == "Skill Gems" "Support Gems"

# BaseType == "Absolution" "Added Fire Damage Support" "Animate Weapon" "Bear Trap" "Blade Blast" "Bladefall" "Blood Rage" "Bloodlust Support" "Bloodthirst Support" "Boneshatter" "Brutality Support" "Chance to Bleed Support" "Corrupting Cry Support" "Corrupting Fever" "Determination" "Divine Blast" "Divine Ire" "Divine Retribution" "Double Strike" "Ethereal Knives" "Eviscerate" "Excommunicate Support" "Explosive Trap" "Exsanguinate" "Flesh and Stone" "Glacial Cascade" "Glacial Shield Swipe" "Hallow Support" "Herald of Agony" "Herald of Purity" "Holy Flame Totem" "Hydrosphere" "Impale Support" "Intimidating Cry" "Iron Grip Support" "Lacerate" "Lancing Steel" "Maim Support" "Melee Physical Damage Support" "Molten Shell" "Penance Brand" "Phase Run" "Physical to Lightning Support" "Pride" "Puncture" "Punishment" "Purifying Flame" "Reap" "Rupture Support" "Seismic Trap" "Shattering Steel" "Shield Charge" "Shield Crush" "Shield of Light" "Shockwave Totem" "Snipe" "Somatic Shell" "Spectral Shield Throw" "Splitting Steel" "Storm Burst" "Summon Carrion Golem" "Summon Reaper" "Summon Stone Golem" "Tornado" "Trauma Support" "Unearth" "Vaal Absolution" "Vaal Animate Weapon" "Vaal Blade Vortex" "Vaal Double Strike" "Vaal Molten Shell" "Vaal Reap" "Vicious Projectiles Support" "Void Sphere" "Vulnerability" "War Banner" "Wave of Conviction" "Withering Touch Support"

# SetFontSize 45

# SetTextColor 30 190 190 255

# SetBorderColor 74 230 58 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 1 Green Triangle

#Show # $type->gems->generic $tier->plusonegemminion

# Quality >= 5

# Class == "Skill Gems" "Support Gems"

# BaseType == "Absolution" "Animate Guardian" "Animate Weapon" "Blink Arrow" "Bone Offering" "Convocation" "Dark Bargain" "Dominating Blow" "Elemental Army Support" "Exemplar Support" "Feeding Frenzy Support" "Flesh Offering" "Fresh Meat Support" "Guardian's Blessing Support" "Herald of Agony" "Herald of Purity" "Holy Strike" "Infernal Legion Support" "Living Lightning Support" "Meat Shield Support" "Minion Damage Support" "Minion Life Support" "Minion Speed Support" "Mirror Arrow" "Predator Support" "Raise Spectre" "Raise Zombie" "Spirit Offering" "Summon Carrion Golem" "Summon Chaos Golem" "Summon Flame Golem" "Summon Holy Relic" "Summon Ice Golem" "Summon Lightning Golem" "Summon Phantasm Support" "Summon Raging Spirit" "Summon Reaper" "Summon Skeletons" "Summon Skitterbots" "Summon Stone Golem" "Vaal Summon Skeletons"

# SetFontSize 45

# SetTextColor 30 190 190 255

# SetBorderColor 74 230 58 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 1 Green Triangle

Show # $type->gems->generic $tier->decogemsvaalbgdrop
	Class == "Skill Gems" "Support Gems"
	BaseType "Vaal"
	SetFontSize 35
	SetBorderColor 0 0 0
	SetBackgroundColor 55 0 0 255
	Continue

Show # %D5 $type->gems->generic $tier->qt2
	Quality >= 20
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 20 240 240 255
	SetBorderColor 20 240 240 255
	SetBackgroundColor 6 0 60 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Triangle

Show # %D5 $type->gems->generic $tier->lt2
	GemLevel >= 20
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 30 190 190 255
	SetBorderColor 30 190 190 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 1 White Triangle

Show # %D4 $type->gems->generic $tier->qt3
	Quality >= 13
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 30 190 190 255
	SetBorderColor 30 190 190 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 1 White Triangle

Show # %D3 $type->gems->generic $tier->lt3
	GemLevel >= 18
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 30 190 190 255
	SetBorderColor 40 130 130 255
	PlayEffect Grey Temp
	MinimapIcon 1 Grey Triangle

Show # %D4 $type->gems->generic $tier->qt4lvl
	Quality >= 1
	Class == "Skill Gems" "Support Gems"
	AreaLevel >= 2
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 30 190 190 255
	SetBorderColor 30 190 190 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 1 White Triangle

Show # %D3 $type->gems->generic $tier->qt4
	Quality >= 1
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 30 190 190 255
	SetBorderColor 40 130 130 255
	PlayEffect Grey Temp
	MinimapIcon 1 Grey Triangle

#Show # %D0 $type->gems->generic $tier->lt4

# GemLevel >= 2

# Class == "Skill Gems" "Support Gems"

# SetFontSize 45

# SetTextColor 30 190 190 255

# SetBorderColor 40 130 130 255

# PlayEffect Grey Temp

# MinimapIcon 1 Grey Triangle

# !! Waypoint c8.gems.low : "Gem Rules - First Zones, Leveling, Vaal" : "Gems"

Show # $type->gems->generic $tier->firstzone
	Quality 0
	GemLevel 1
	Class == "Skill Gems" "Support Gems"
	BaseType == "Arcane Surge Support" "Burning Arrow" "Chance to Bleed Support" "Chance to Poison Support" "Double Strike" "Elemental Proliferation Support" "Fireball" "Hallow Support" "Heavy Strike" "Holy Strike" "Momentum Support" "Prismatic Burst Support" "Ruthless Support" "Spectral Throw" "Viper Strike"
	AreaLevel 1
	SetFontSize 45
	SetBorderColor 0 0 0

Show # %H4 $type->gems->generic $tier->levelingvaal
	Class == "Skill Gems" "Support Gems"
	BaseType "Vaal"
	AreaLevel >= 2
	AreaLevel <= 67
	SetFontSize 45
	SetBorderColor 0 0 0
	SetBackgroundColor 55 0 0 255
	MinimapIcon 2 White Triangle

Hide # %H2 $type->gems->generic $tier->leveling
	Class == "Skill Gems" "Support Gems"
	AreaLevel >= 2
	AreaLevel <= 67
	SetFontSize 40
	SetBorderColor 0 0 0

Show # %D3 $type->gems->generic $tier->corruptedvaalany
	Class == "Skill Gems" "Support Gems"
	BaseType "Vaal"
	SetFontSize 35
	SetBorderColor 0 0 0
	SetBackgroundColor 55 0 0 255

Hide # %H0 $type->gems->generic $tier->any
	Class == "Skill Gems" "Support Gems"
	SetFontSize 30
	SetTextColor 40 130 130 255
	SetBorderColor 0 0 0

#===============================================================================================================

# [[3100]] REPLICA AND FOULBORN UNIQUES

#===============================================================================================================

# !! Waypoint c9.replicas.all : "Tierlists - Replicas" : "Uniques"

Show # $type->uniques->replicas $tier->t1
	Replica True
	Rarity Unique
	BaseType == "Blood Raiment" "Carnal Armour" "Chain Belt" "Ebony Tower Shield" "Eternal Sword" "Granite Flask" "Great Crown" "Great Mallet" "Imperial Bow" "Karui Sceptre" "Leather Belt" "Maelström Staff" "Soldier Boots" "Terror Maul" "Triumphant Lamellar" "Turquoise Amulet" "Void Sceptre"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->uniques->replicas $tier->t2
	Replica True
	Rarity Unique
	BaseType == "Assassin's Boots" "Boot Knife" "Calling Wand" "Cloth Belt" "Diamond Ring" "Elegant Ringmail" "Ezomyte Burgonet" "Glorious Plate" "Great Helmet" "Gut Ripper" "Laminated Kite Shield" "Leather Hood" "Map (Tier 16)" "Nailed Fist" "Opal Wand" "Ornate Mace" "Ornate Quiver" "Paua Amulet" "Ruby Ring" "Rustic Sash" "Sage Wand" "Sapphire Ring" "Satin Gloves" "Shadow Sceptre" "Siege Axe" "Sinner Tricorne" "Sorcerer Gloves" "Spidersilk Robe" "Titan Greaves" "Tornado Wand" "Vaal Claw" "Vaal Gauntlets" "Vaal Rapier" "War Sword" "Zodiac Leather"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Star

Show # $type->uniques->replicas $tier->multi
	Replica True
	Rarity Unique
	BaseType == "Map (Tier 11)" "Map (Tier 12)" "Map (Tier 14)"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # %H6 $type->uniques->replicas $tier->t3
	Replica True
	Rarity Unique
	BaseType == "Arcanist Gloves" "Arcanist Slippers" "Blasting Wand" "Bronzescale Boots" "Cobalt Jewel" "Crimson Jewel" "Crusader Chainmail" "Death Bow" "Decimation Bow" "Elder Sword" "Ezomyte Axe" "Ezomyte Dagger" "Festival Mask" "Gnarled Branch" "Gold Amulet" "Grinning Fetish" "Heavy Belt" "Infernal Sword" "Jade Amulet" "Jasper Chopper" "Lacquered Buckler" "Murder Boots" "Onyx Amulet" "Paua Ring" "Royal Skean" "Samite Gloves" "Sanctified Mana Flask" "Shagreen Boots" "Short Bow" "Silk Slippers" "Spike-Point Arrow Quiver" "Stibnite Flask" "Stiletto" "Sulphur Flask" "Unset Ring" "Viridian Jewel" "Zealot Gloves"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 3 300
	PlayEffect White
	MinimapIcon 1 White Star

Show # $type->uniques->replicas $tier->restex
	Replica True
	Rarity Unique
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

# !! Waypoint c9.foulborn.all : "Tierlists - Foulborn" : "Uniques"

Show # $type->uniques->foulborn $tier->t1
	Foulborn True
	Rarity Unique
	BaseType == "Amethyst Ring" "Astral Plate" "Champion Kite Shield" "Desert Brigandine" "Devout Chainmail" "Dragonscale Boots" "Exquisite Leather" "Ezomyte Burgonet" "Fishing Rod" "Gladiator Plate" "Gold Ring" "Harlequin Mask" "Iron Circlet" "Karui Chopper" "Lunaris Circlet" "Midnight Blade" "Nubuck Boots" "Ornate Quiver" "Paua Amulet" "Prophecy Wand" "Raven Mask" "Rawhide Boots" "Sadist Garb" "Samite Gloves" "Silk Gloves" "Somatic Wand" "Steel Kite Shield" "Steelhead" "Terror Claw" "Terror Maul" "Titanium Spirit Shield" "Tomahawk" "Two-Point Arrow Quiver" "Vaal Gauntlets" "Vile Staff" "Widowsilk Robe" "Wyrmscale Doublet"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->uniques->foulborn $tier->t2
	Foulborn True
	Rarity Unique
	BaseType == "Abyssal Axe" "Agate Amulet" "Amber Amulet" "Archon Kite Shield" "Assassin's Garb" "Branded Kite Shield" "Bronzescale Gauntlets" "Cloth Belt" "Cobalt Jewel" "Coronal Maul" "Corrugated Buckler" "Crimson Jewel" "Crusader Chainmail" "Cutthroat's Garb" "Destiny Leather" "Etched Greatsword" "Eternal Sword" "Ezomyte Tower Shield" "Fiend Dagger" "Goat's Horn" "Goathide Boots" "Golden Mask" "Golden Plate" "Iron Ring" "Ironwood Buckler" "Lapis Amulet" "Lathi" "Legion Boots" "Lion Sword" "Majestic Plate" "Maraketh Bow" "Military Staff" "Mosaic Kite Shield" "Murder Mitts" "Nightmare Bascinet" "Plate Vest" "Platinum Sceptre" "Praetor Crown" "Ranger Bow" "Regicide Mask" "Reinforced Greaves" "Saintly Chainmail" "Sapphire Ring" "Short Bow" "Silken Hood" "Sinner Tricorne" "Sorcerer Boots" "Spiraled Wand" "Steel Gauntlets" "Strapped Mitts" "Studded Belt" "Topaz Ring" "Vaal Blade" "Wyrmscale Gauntlets"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Star

Show # $type->uniques->foulborn $tier->multi
	Foulborn True
	Rarity Unique
	BaseType == "Calling Wand" "Close Helmet" "Crusader Plate" "Cutlass" "Destroyer Regalia" "Diamond Ring" "Elegant Round Shield" "Gavel" "Heavy Belt" "Imperial Claw" "Jade Amulet" "Lacquered Garb" "Leather Belt" "Moonstone Ring" "Necromancer Silks" "Onyx Amulet" "Opal Wand" "Prismatic Ring" "Royal Burgonet" "Sage's Robe" "Scholar's Robe" "Silken Vest" "Spidersilk Robe" "Titan Greaves" "Turquoise Amulet" "Two-Stone Ring" "Vaal Sceptre" "Vaal Spirit Shield" "Viridian Jewel" "Zodiac Leather"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # %H6 $type->uniques->foulborn $tier->t3
	Foulborn True
	Rarity Unique
	BaseType == "Ancient Spirit Shield" "Assassin Bow" "Assassin's Mitts" "Blunt Arrow Quiver" "Buckskin Tunic" "Carnal Mitts" "Chain Belt" "Chain Gloves" "Citadel Bow" "Clasped Mitts" "Conjurer Gloves" "Copper Plate" "Crusader Gloves" "Crystal Belt" "Death Bow" "Deerskin Gloves" "Full Wyrmscale" "Gilded Sallet" "Great Helmet" "Harmonic Spirit Shield" "Holy Chainmail" "Hubris Circlet" "Ironscale Gauntlets" "Jasper Chopper" "Jewelled Foil" "Karui Sceptre" "Kinetic Wand" "Leather Cap" "Leather Hood" "Legion Gloves" "Mind Cage" "Occultist's Vestment" "Omen Wand" "Ornate Mace" "Penetrating Arrow Quiver" "Pinnacle Tower Shield" "Reaver Sword" "Royal Axe" "Royal Bow" "Ruby Ring" "Serpentine Staff" "Soldier Boots" "Spike-Point Arrow Quiver" "Steelscale Gauntlets" "Tarnished Spirit Shield" "Thresher Claw" "Timeworn Claw" "Titan Gauntlets" "Triumphant Lamellar" "Vaal Axe" "Varnished Coat" "War Buckler" "Wool Gloves" "Zealot Helmet"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 3 300
	PlayEffect White
	MinimapIcon 1 White Star

Show # $type->uniques->foulborn $tier->restex
	Foulborn True
	Rarity Unique
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#===============================================================================================================

# [[3200]] Special Maps

#===============================================================================================================

# !! Waypoint c9.maps.all : "Maps - All" : "Maps"

#------------------------------------

# [3201] Unique Maps

#------------------------------------

# !! Waypoint c9.maps.unique.all : "Maps - Unique Tierlists" : "Uniques"

Show # %H8 $type->uniques->maps $tier->multispecial
	Rarity Unique
	Class == "Maps"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # $type->uniques->maps $tier->restex
	Rarity Unique
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [3202] SpecialMaps

#------------------------------------

# !! Waypoint c9.maps.special.t17 : "Maps - Exceptional Types" : "Maps"

Show # %D8 $type->maps->nightmare $tier->valdomaps
	Class == "Maps"
	BaseType == "Valdo Map"
	SetFontSize 45
	SetTextColor 100 0 122 255
	SetBorderColor 100 0 122 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

Show # %D9 $type->maps->nightmare $tier->nightmaremaps
	Class == "Maps"
	BaseType == "Nightmare Map"
	SetFontSize 45
	SetTextColor 100 0 122 255
	SetBorderColor 100 0 122 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

Show # %D7 $type->maps->nightmare $tier->shaperguardianmaps
	Class == "Maps"
	BaseType == "Shaper Guardian Map"
	SetFontSize 45
	SetTextColor 100 0 122 255
	SetBorderColor 100 0 122 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

#------------------------------------

# [3203] Blighted maps

#------------------------------------

# !! Waypoint c9.maps.special.all : "Maps - Blighted, Enchanted, Delirium maps" : "Maps"

Show # $type->maps->blighted $tier->uber
	UberBlightedMap True
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square

Show # $type->maps->blighted $tier->t1
	BlightedMap True
	MapTier >= 13
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square

Show # %H5 $type->maps->blighted $tier->any
	BlightedMap True
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 200 200 200 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 1 Purple Square

#------------------------------------

# [3204] Special Maps

#------------------------------------

Show # $type->maps->vaaltemple $tier->any
	MapTier >= 16
	Class == "Maps"
	BaseType == "Vaal Temple Map"
	SetFontSize 45
	SetTextColor 100 0 122 255
	SetBorderColor 100 0 122 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

Show # $type->maps->corruptedspecial $tier->mod8
	Corrupted True
	Identified True
	Class == "Maps"
	HasExplicitMod >=8 "a" "e" "i" "o" "u" "y"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square

Show # %D6 $type->maps->enchanted $tier->t1
	AnyEnchantment True
	MapTier >= 14
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square

Show # %D5 $type->maps->enchanted $tier->any
	AnyEnchantment True
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 200 200 200 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 1 Purple Square

#Show # $type->maps->corruptedimplicit $tier->t1

# MapTier >= 14

# CorruptedMods >= 1

# Rarity Rare

# Class == "Maps"

# SetFontSize 45

# SetTextColor 145 30 220 255

# SetBorderColor 145 30 220 255

# SetBackgroundColor 235 220 245 255

# PlayAlertSound 5 300

# PlayEffect Purple

# MinimapIcon 0 Purple Square

#Show # %D6 $type->maps->corruptedimplicit $tier->any

# CorruptedMods >= 1

# Class == "Maps"

# SetFontSize 45

# SetTextColor 145 30 220 255

# SetBorderColor 145 30 220 255

# SetBackgroundColor 200 200 200 255

# PlayAlertSound 5 300

# PlayEffect Purple

# MinimapIcon 1 Purple Square

#Show # $type->maps->implicitmod $tier->t1

# HasImplicitMod True

# MapTier >= 14

# Class == "Maps"

# SetFontSize 45

# SetTextColor 145 30 220 255

# SetBorderColor 145 30 220 255

# SetBackgroundColor 235 220 245 255

# PlayAlertSound 5 300

# PlayEffect Purple

# MinimapIcon 0 Purple Square

#Show # %D6 $type->maps->implicitmod $tier->any

# HasImplicitMod True

# Class == "Maps"

# SetFontSize 45

# SetTextColor 145 30 220 255

# SetBorderColor 145 30 220 255

# SetBackgroundColor 200 200 200 255

# PlayAlertSound 5 300

# PlayEffect Purple

# MinimapIcon 1 Purple Square

#===============================================================================================================

# [[3300]] Normal Map Progression

#===============================================================================================================

# !! Waypoint c9.maps.generic.specialcases : "Maps - generic - optional special cases" : "Maps"

#Hide # $type->maphiders $tier->corruptedmaphider

# Corrupted True

# Rarity Normal Magic

# Class == "Maps"

# SetFontSize 35

# SetBorderColor 0 0 0

#Hide # $type->maphiders $tier->mirroredmaphider

# Mirrored True

# Rarity Normal Magic

# Class == "Maps"

# SetFontSize 35

# SetBorderColor 0 0 0

#------------------------------------

# [3301] Generic Decorators

#------------------------------------

# !! Waypoint c9.maps.decorators.all : "Maps - decorators" : "Maps"

Show # $type->maps $tier->deco_zone1general
	MapTier >= 14
	Class == "Maps"
	SetBorderColor 0 0 0 255
	Continue

Show # $type->maps $tier->deco_zone2general
	MapTier >= 11
	MapTier <= 13
	Class == "Maps"
	SetBorderColor 0 0 0 255
	Continue

Show # $type->maps $tier->deco_zone3general
	MapTier >= 6
	MapTier <= 10
	Class == "Maps"
	SetBorderColor 200 200 200 255
	Continue

Show # $type->maps $tier->deco_zone4general
	MapTier >= 1
	MapTier <= 5
	Class == "Maps"
	SetBorderColor 200 200 200 255
	Continue

Show # $type->maps $tier->deco_mapup_t16
	MapTier >= 16
	Class == "Maps"
	AreaLevel < 83
	SetBorderColor 220 50 0 255
	Continue

Show # $type->maps $tier->deco_mapup_t15
	MapTier >= 15
	Class == "Maps"
	AreaLevel < 82
	SetBorderColor 220 50 0 255
	Continue

Show # $type->maps $tier->deco_mapup_t14
	MapTier >= 14
	Class == "Maps"
	AreaLevel < 81
	SetBorderColor 220 50 0 255
	Continue

Show # %D4 $type->maps $tier->deco_mapup_t13
	MapTier >= 13
	Class == "Maps"
	AreaLevel < 80
	SetBorderColor 220 50 0 255
	Continue

Show # %D4 $type->maps $tier->deco_mapup_t12
	MapTier >= 12
	Class == "Maps"
	AreaLevel < 79
	SetBorderColor 220 50 0 255
	Continue

Show # %D4 $type->maps $tier->deco_mapup_t11
	MapTier >= 11
	Class == "Maps"
	AreaLevel < 78
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t10
	MapTier >= 10
	Class == "Maps"
	AreaLevel < 77
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t9
	MapTier >= 9
	Class == "Maps"
	AreaLevel < 76
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t8
	MapTier >= 8
	Class == "Maps"
	AreaLevel < 75
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t7
	MapTier >= 7
	Class == "Maps"
	AreaLevel < 74
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t6
	MapTier >= 6
	Class == "Maps"
	AreaLevel < 73
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t5
	MapTier >= 5
	Class == "Maps"
	AreaLevel < 72
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t4
	MapTier >= 4
	Class == "Maps"
	AreaLevel < 71
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t3
	MapTier >= 3
	Class == "Maps"
	AreaLevel < 70
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t2
	MapTier >= 2
	Class == "Maps"
	AreaLevel < 69
	SetBorderColor 220 50 0 255
	Continue

Show # %D3 $type->maps $tier->deco_mapup_t1
	MapTier >= 1
	Class == "Maps"
	AreaLevel < 68
	SetBorderColor 220 50 0 255
	Continue

Show # $type->maps $tier->decor_implicit
	HasImplicitMod True
	Class == "Maps"
	SetBorderColor 255 180 0 255
	Continue

Show # $type->maps $tier->deco_corruptedmod
	CorruptedMods >= 1
	Class == "Maps"
	SetBorderColor 255 180 0 255
	Continue

#------------------------------------

# [3302] Map progression

#------------------------------------

# !! Waypoint c9.maps.generic.t16 : "Maps - t14-t16 - high reds" : "Maps"

Show # $type->maps $tier->maps_a_t16
	MapTier >= 16
	Class == "Maps"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBackgroundColor 235 235 235 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Red Square

Show # %H5 $type->maps $tier->maps_a_t15
	MapTier 15
	Class == "Maps"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBackgroundColor 235 235 235 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Red Square

Show # %H5 $type->maps $tier->maps_a_t14
	MapTier 14
	Class == "Maps"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBackgroundColor 235 235 235 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Red Square

# !! Waypoint c9.maps.generic.t14 : "Maps - t11-t13 - low reds" : "Maps"

Show # %H4 $type->maps $tier->maps_b_t13
	MapTier 13
	Class == "Maps"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBackgroundColor 200 200 200 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Red Square

Show # %H4 $type->maps $tier->maps_b_t12
	MapTier 12
	Class == "Maps"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBackgroundColor 200 200 200 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Red Square

Show # %H4 $type->maps $tier->maps_b_t11
	MapTier 11
	Class == "Maps"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBackgroundColor 200 200 200 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Red Square

# !! Waypoint c9.maps.generic.t10 : "Maps - t6-t10 - yellow maps" : "Maps"

Show # %H4 $type->maps $tier->maps_c_t10
	MapTier 10
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 1 Yellow Square

Show # %H4 $type->maps $tier->maps_c_t9
	MapTier 9
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 1 Yellow Square

Show # %H4 $type->maps $tier->maps_c_t8
	MapTier 8
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 1 Yellow Square

Show # %H4 $type->maps $tier->maps_c_t7
	MapTier 7
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 1 Yellow Square

Show # %H4 $type->maps $tier->maps_c_t6
	MapTier 6
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 1 Yellow Square

# !! Waypoint c9.maps.generic.t5 : "maps - T1-T5 - white maps" : "Maps"

Show # %H4 $type->maps $tier->maps_d_t5
	MapTier 5
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 2 White Square

Show # %H4 $type->maps $tier->maps_d_t4
	MapTier 4
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 2 White Square

Show # %H4 $type->maps $tier->maps_d_t3
	MapTier 3
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 2 White Square

Show # %H4 $type->maps $tier->maps_d_t2
	MapTier 2
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 2 White Square

Show # %H4 $type->maps $tier->maps_d_t1
	MapTier 1
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 2 White Square

Show # $type->maps $tier->restex
	Class == "Maps"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#===============================================================================================================

# [[3400]] Pseudo-Map-Items

#===============================================================================================================

# !! Waypoint c9.maplike.all : "Maplike - contracts, logbooks, blueprints, memories" : "Heist, Expedition, Sanctum"

Show # $type->uniques->heist $tier->any
	Rarity Unique
	Class == "Blueprints" "Contracts"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Star

Show # $type->expedition->logbook $tier->any
	BaseType == "Expedition Logbook"
	SetFontSize 45
	SetTextColor 255 85 85 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 40 0 30 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow UpsideDownHouse

Show # $type->charts $tier->any
	Rarity Normal Magic Rare
	Class == "Chart"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 120 200 160 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Moon

Show # %H7 $type->heist->contract $tier->enchanted
	AnyEnchantment True
	Rarity Normal Magic Rare
	Class == "Contracts"
	BaseType == "Contract: Bunker" "Contract: Laboratory" "Contract: Mansion" "Contract: Prohibited Library" "Contract: Records Office" "Contract: Repository" "Contract: Smuggler's Den" "Contract: Tunnels" "Contract: Underbelly"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %H5 $type->heist->contract $tier->handpicked
	Rarity Normal Magic Rare
	Class == "Contracts"
	BaseType == "Contract: Bunker" "Contract: Laboratory" "Contract: Mansion" "Contract: Prohibited Library" "Contract: Records Office" "Contract: Repository" "Contract: Smuggler's Den" "Contract: Tunnels" "Contract: Underbelly"
	SetFontSize 45
	SetTextColor 220 60 60 255
	SetBorderColor 220 60 60 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 4 300
	PlayEffect White
	MinimapIcon 2 White UpsideDownHouse

Hide # $type->heist->contract $tier->exhide
	Class == "Contracts"
	SetFontSize 35
	SetBorderColor 0 0 0

Show # %H9 $type->heist->blueprint $tier->enchanted
	AnyEnchantment True
	Rarity Normal Magic Rare
	Class == "Blueprints"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->heist->blueprint $tier->handpicked
	Class == "Blueprints"
	BaseType == "Blueprint: Bunker" "Blueprint: Laboratory" "Blueprint: Mansion" "Blueprint: Prohibited Library" "Blueprint: Records Office" "Blueprint: Repository" "Blueprint: Smuggler's Den" "Blueprint: Tunnels" "Blueprint: Underbelly"
	SetFontSize 45
	SetTextColor 255 85 85 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 40 0 30 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow UpsideDownHouse

Show # %H8 $type->heist->blueprint $tier->any
	Class == "Blueprints"
	SetFontSize 45
	SetTextColor 255 85 85 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 40 0 30 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow UpsideDownHouse

Show # %H8 $type->exoticmap->sanctum $tier->ilvl83
	ItemLevel >= 83
	Class == "Sanctum Research"
	SetFontSize 45
	SetTextColor 255 85 85 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 40 0 30 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow UpsideDownHouse

Show # %H6 $type->exoticmap->sanctum $tier->any
	Class == "Sanctum Research"
	SetFontSize 45
	SetTextColor 255 85 85 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 40 0 30 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow UpsideDownHouse

#===============================================================================================================

# [[3500]] Misc Map Items

#===============================================================================================================

# !! Waypoint c10.relics.all : "Relic Keys, Itemized Leagues" : "Scarabs and Fragments"

Show # $type->miscmapitemsextra $tier->relickeys
	BaseType == "Ancient Reliquary Key" "Archive Reliquary Key" "Cosmic Reliquary Key" "Decaying Reliquary Key" "Forgotten Reliquary Key" "Lonely Reliquary Key" "Oubliette Reliquary Key" "Reverent Reliquary Key" "Shiny Reliquary Key" "Timeworn Reliquary Key" "Traumatic Reliquary Key" "Vaal Reliquary Key" "Visceral Reliquary Key" "Voidborn Reliquary Key"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->miscmapitemsextra $tier->relickeyssafe
	Class == "Vault Keys"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->miscmapitemsextra $tier->itemizedleaguesincursion
	BaseType == "Chronicle of Atzoatl"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 180 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

Show # $type->miscmapitemsextra $tier->itemizedleaguesultimatum
	BaseType == "Inscribed Ultimatum"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 180 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

#===============================================================================================================

# [[3600]] Fragments

#===============================================================================================================

# !! Waypoint c9.fragments.all : "Tierlist - Fragments" : "Scarabs and Fragments"

#------------------------------------

# [3601] Scarabs

#------------------------------------

Show # $type->fragments->scarabs $tier->t1
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Allflame Ember of Kulemak" "Essence Scarab of Calcification" "Harvest Scarab of Cornucopia" "Horned Scarab of Bloodlines" "Horned Scarab of Pandemonium" "Horned Scarab of Preservation" "Incursion Scarab of Timelines" "Ultimatum Scarab of Catalysing"
	SetFontSize 45
	SetTextColor 180 0 255 255
	SetBorderColor 180 0 255 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->fragments->scarabs $tier->t2
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Allflame Ember of the Ethereal" "Allflame Ember of the Gilded" "Ambush Scarab of Containment" "Blight Scarab of Blooming" "Cartography Scarab of Risk" "Divination Scarab of Pilfering" "Domination Scarab of Terrors" "Horned Scarab of Awakening" "Horned Scarab of Tradition" "Kalguuran Scarab of Refinement" "Legion Scarab of Eternal Conflict" "Trarthan Scarab of Renown" "Trarthan Scarab of Surprising Alliances"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 180 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

Show # %D7 $type->fragments->scarabs $tier->t3stackedex
	StackSize >= 3
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Abyss Scarab of Crystals" "Abyss Scarab of Descending" "Abyss Scarab of the Consort" "Allflame Ember of Flesh" "Allflame Ember of Resplendence" "Allflame Ember of the Wildwood" "Allflame Ember of Toads" "Ambush Scarab" "Ambush Scarab of Discernment" "Ambush Scarab of Potency" "Anarchy Scarab" "Anarchy Scarab of Gigantification" "Anarchy Scarab of Partnership" "Anarchy Scarab of the Exceptional" "Bestiary Scarab" "Bestiary Scarab of Duplicating" "Bestiary Scarab of the Herd" "Betrayal Scarab" "Betrayal Scarab of Reinforcements" "Betrayal Scarab of the Allflame" "Betrayal Scarab of Unbreaking" "Beyond Scarab" "Beyond Scarab of Haemophilia" "Beyond Scarab of Resurgence" "Beyond Scarab of the Invasion" "Blight Scarab" "Blight Scarab of the Blightheart" "Breach Scarab of the Hive" "Breach Scarab of the Incensed Swarm" "Cartography Scarab of Corruption" "Cartography Scarab of Escalation" "Cartography Scarab of the Multitude" "Delirium Scarab" "Delirium Scarab of Delusions" "Delirium Scarab of Mania" "Delirium Scarab of Neuroses" "Delirium Scarab of Paranoia" "Divination Scarab of Plenty" "Domination Scarab" "Domination Scarab of Apparitions" "Domination Scarab of Evolution" "Essence Scarab" "Essence Scarab of Ascent" "Essence Scarab of Stability" "Expedition Scarab" "Expedition Scarab of Archaeology" "Expedition Scarab of Infusion" "Expedition Scarab of Runefinding" "Expedition Scarab of Verisium Powder" "Harvest Scarab" "Horned Scarab of Glittering" "Horned Scarab of Nemeses" "Incursion Scarab" "Incursion Scarab of Champions" "Incursion Scarab of Invasion" "Influencing Scarab of Hordes" "Influencing Scarab of Interference" "Influencing Scarab of the Elder" "Influencing Scarab of the Shaper" "Kalguuran Scarab" "Kalguuran Scarab of Enriching" "Kalguuran Scarab of Guarded Riches" "Legion Scarab" "Legion Scarab of Officers" "Legion Scarab of Treasures" "Ritual Scarab of Corpses" "Ritual Scarab of Selectiveness" "Ritual Scarab of Wisps" "Scarab of Adversaries" "Scarab of Divinity" "Scarab of Stability" "Scarab of the Dextral" "Scarab of the Sinistral" "Scarab of Wisps" "Sulphite Scarab" "Sulphite Scarab of Fumes" "Titanic Scarab" "Titanic Scarab of Legend" "Titanic Scarab of Treasures" "Torment Scarab" "Torment Scarab of Peculiarity" "Torment Scarab of Possession" "Trarthan Scarab" "Ultimatum Scarab" "Ultimatum Scarab of Bribing" "Ultimatum Scarab of Dueling" "Ultimatum Scarab of Inscription"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 0 255 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Hexagon

Show # %HS6 $type->fragments->scarabs $tier->t3
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Abyss Scarab" "Abyss Scarab of Multitudes" "Allflame Ember of Propagation" "Ambush Scarab of Hidden Compartments" "Blight Scarab of Invigoration" "Breach Scarab of Instability" "Breach Scarab of Resonant Cascade" "Breach Scarab of the Marshal" "Divination Scarab of The Cloister" "Essence Scarab of Adaptation" "Harvest Scarab of Doubling" "Ritual Scarab of Abundance" "Scarab of Monstrous Lineage" "Scarab of Radiant Storms" "Trarthan Scarab of Infamy"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 0 255 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Hexagon

Show # %H5 $type->fragments->scarabs $tier->t4
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Abyss Scarab of Descending" "Abyss Scarab of the Consort" "Ambush Scarab" "Ambush Scarab of Discernment" "Bestiary Scarab of Duplicating" "Beyond Scarab of Haemophilia" "Beyond Scarab of Resurgence" "Breach Scarab of the Incensed Swarm" "Cartography Scarab of Corruption" "Cartography Scarab of the Multitude" "Delirium Scarab of Neuroses" "Delirium Scarab of Paranoia" "Divination Scarab of Plenty" "Domination Scarab" "Essence Scarab of Ascent" "Horned Scarab of Glittering" "Horned Scarab of Nemeses" "Incursion Scarab of Invasion" "Influencing Scarab of Hordes" "Influencing Scarab of Interference" "Kalguuran Scarab" "Legion Scarab of Treasures" "Scarab of the Sinistral" "Scarab of Wisps" "Ultimatum Scarab of Bribing" "Ultimatum Scarab of Dueling" "Ultimatum Scarab of Inscription"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 120 230 240
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Hexagon

Show # %HS4 $type->fragments->scarabs $tier->t5
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Abyss Scarab of Crystals" "Allflame Ember of the Wildwood" "Ambush Scarab of Potency" "Anarchy Scarab" "Anarchy Scarab of Partnership" "Bestiary Scarab" "Bestiary Scarab of the Herd" "Betrayal Scarab" "Betrayal Scarab of Reinforcements" "Betrayal Scarab of Unbreaking" "Beyond Scarab" "Beyond Scarab of the Invasion" "Blight Scarab" "Blight Scarab of the Blightheart" "Breach Scarab of the Hive" "Cartography Scarab of Escalation" "Delirium Scarab" "Delirium Scarab of Delusions" "Delirium Scarab of Mania" "Domination Scarab of Evolution" "Essence Scarab" "Essence Scarab of Stability" "Expedition Scarab of Runefinding" "Harvest Scarab" "Incursion Scarab" "Incursion Scarab of Champions" "Influencing Scarab of the Elder" "Influencing Scarab of the Shaper" "Kalguuran Scarab of Enriching" "Kalguuran Scarab of Guarded Riches" "Legion Scarab" "Legion Scarab of Officers" "Ritual Scarab of Corpses" "Ritual Scarab of Selectiveness" "Ritual Scarab of Wisps" "Scarab of Adversaries" "Scarab of Divinity" "Scarab of Stability" "Scarab of the Dextral" "Sulphite Scarab" "Sulphite Scarab of Fumes" "Titanic Scarab" "Titanic Scarab of Legend" "Titanic Scarab of Treasures" "Torment Scarab" "Torment Scarab of Peculiarity" "Trarthan Scarab" "Ultimatum Scarab"
	SetFontSize 45
	SetTextColor 175 120 230 240
	SetBorderColor 175 120 230 240
	PlayEffect Grey Temp
	MinimapIcon 2 White Hexagon

Show # %HS3 $type->fragments->scarabs $tier->t6
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Allflame Ember of Flesh" "Allflame Ember of Resplendence" "Allflame Ember of Toads" "Anarchy Scarab of Gigantification" "Anarchy Scarab of the Exceptional" "Betrayal Scarab of the Allflame" "Domination Scarab of Apparitions" "Expedition Scarab" "Expedition Scarab of Archaeology" "Expedition Scarab of Infusion" "Expedition Scarab of Verisium Powder" "Torment Scarab of Possession"
	SetFontSize 45
	SetTextColor 175 120 230 240
	SetBorderColor 0 0 0

Show # $type->fragments->scarabs $tier->restex
	Class == "Map Fragments" "Misc Map Items"
	BaseType "Scarab"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [3602] Regular Fragment Tiering

#------------------------------------

Show # $type->fragments $tier->t1
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "An Audience With The King" "Cosmic Fragment" "Decaying Fragment" "Devouring Fragment" "Echo of Loneliness" "Echo of Reverence" "Echo of Trauma" "Incandescent Invitation" "Reality Fragment" "Reverent Fragment" "Sacred Blossom" "Screaming Invitation" "Simulacrum" "Syndicate Medallion" "The Black Barya" "Timeless Maraketh Emblem" "Timeless Vaal Emblem" "Zorath's Eye of the Endless" "Zorath's Eye of the Inevitable"
	SetFontSize 45
	SetTextColor 180 0 255 255
	SetBorderColor 180 0 255 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %DS3 $type->fragments $tier->t3stackedex
	StackSize >= 3
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Divine Vessel" "Sacrifice at Dawn" "Sacrifice at Dusk" "Sacrifice at Midnight" "Sacrifice at Noon"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 0 255 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Hexagon

Show # %H8 $type->fragments $tier->t2
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Al-Hezmin's Crest" "Blazing Fragment" "Fragment of Constriction" "Fragment of Emptiness" "Fragment of Enslavement" "Fragment of Eradication" "Fragment of Knowledge" "Fragment of Purification" "Fragment of Shape" "Fragment of Terror" "Hivebrain Gland" "Lonely Fragment" "Mercenary Warrant" "The Maven's Writ" "Timeless Eternal Emblem" "Timeless Karui Emblem" "Timeless Templar Emblem" "Traumatic Fragment"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 180 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

Show # %H7 $type->fragments $tier->t4
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Awakening Fragment" "Baran's Crest" "Blood-filled Vessel" "Dedication to the Goddess" "Drox's Crest" "Fragment of the Chimera" "Fragment of the Hydra" "Fragment of the Minotaur" "Fragment of the Phoenix" "Gift to the Goddess" "Mortal Grief" "Mortal Hope" "Mortal Ignorance" "Mortal Rage" "Offering to the Goddess" "Polaric Invitation" "Synthesising Fragment" "Tribute to the Goddess" "Veritania's Crest" "Writhing Invitation" "Zorath's Eye of Authority" "Zorath's Eye of Malevolence"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 120 230 240
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Hexagon

Show # %HS3 $type->fragments $tier->t5
	Class == "Map Fragments" "Misc Map Items"
	BaseType == "Divine Vessel" "Sacrifice at Dawn" "Sacrifice at Dusk" "Sacrifice at Midnight" "Sacrifice at Noon"
	SetFontSize 45
	SetTextColor 175 120 230 240
	SetBorderColor 175 120 230 240
	PlayEffect Grey Temp
	MinimapIcon 2 White Hexagon

Show # $type->fragments $tier->restex
	Class == "Map Fragments" "Misc Map Items"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

Show # $type->miscmapitems $tier->restex
	Class == "Misc Map Items"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#===============================================================================================================

# [[3700]] Currency - Special

#===============================================================================================================

# !! Waypoint c9.currency.lifeforce : "Tierlist - Currency - Lifeforce" : "Currency and Currency-Likes"

Show # %D9 $type->currency->harvest $tier->t1lifeforce
	StackSize >= 4000
	Class == "Stackable Currency"
	BaseType == "Primal Crystallised Lifeforce" "Vivid Crystallised Lifeforce" "Wild Crystallised Lifeforce"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %D8 $type->currency->harvest $tier->t2lifeforce
	StackSize >= 500
	Class == "Stackable Currency"
	BaseType == "Primal Crystallised Lifeforce" "Vivid Crystallised Lifeforce" "Wild Crystallised Lifeforce"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %D7 $type->currency->harvest $tier->t3lifeforce
	StackSize >= 250
	Class == "Stackable Currency"
	BaseType == "Primal Crystallised Lifeforce" "Vivid Crystallised Lifeforce" "Wild Crystallised Lifeforce"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %D6 $type->currency->harvest $tier->t4lifeforce
	StackSize >= 45
	Class == "Stackable Currency"
	BaseType == "Primal Crystallised Lifeforce" "Vivid Crystallised Lifeforce" "Wild Crystallised Lifeforce"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %D6 $type->currency->harvest $tier->t5lifeforce
	StackSize >= 20
	Class == "Stackable Currency"
	BaseType == "Primal Crystallised Lifeforce" "Vivid Crystallised Lifeforce" "Wild Crystallised Lifeforce"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %H5 $type->currency->harvest $tier->t6lifeforce
	Class == "Stackable Currency"
	BaseType == "Primal Crystallised Lifeforce" "Vivid Crystallised Lifeforce" "Wild Crystallised Lifeforce"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Hide # $type->currency->harvest $tier->exhide
	Class == "Stackable Currency"
	BaseType == "Primal Crystallised Lifeforce" "Vivid Crystallised Lifeforce" "Wild Crystallised Lifeforce"
	BaseType == "Primal Crystallised Lifeforce" "Vivid Crystallised Lifeforce" "Wild Crystallised Lifeforce"
	SetFontSize 35
	SetBorderColor 0 0 0

Show # $type->currency->deadmansulphur $tier->t1
	StackSize >= 20000
	Class == "Stackable Currency"
	BaseType == "Dead Man's Sulphur"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %D8 $type->currency->deadmansulphur $tier->t2
	StackSize >= 5000
	Class == "Stackable Currency"
	BaseType == "Dead Man's Sulphur"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %D7 $type->currency->deadmansulphur $tier->t3
	StackSize >= 1500
	Class == "Stackable Currency"
	BaseType == "Dead Man's Sulphur"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %D6 $type->currency->deadmansulphur $tier->t4
	StackSize >= 200
	Class == "Stackable Currency"
	BaseType == "Dead Man's Sulphur"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %D6 $type->currency->deadmansulphur $tier->t5
	StackSize >= 100
	Class == "Stackable Currency"
	BaseType == "Dead Man's Sulphur"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %H5 $type->currency->deadmansulphur $tier->t6
	Class == "Stackable Currency"
	BaseType == "Dead Man's Sulphur"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

#===============================================================================================================

# [[3800]] Currency - Leveling Exceptions

#===============================================================================================================

# !! Waypoint c9.currency.leveling.all : "Tierlist - Currency - Leveling Stacked Currency" : "Leveling"

Show # %D4 $type->currency->levelingstacked $tier->t2chance
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Orb of Chance"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Grey Circle

Show # %D4 $type->currency->levelingstacked $tier->t3trans
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Orb of Alteration" "Orb of Transmutation"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # %D4 $type->currency->levelingstacked $tier->t4misc
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Armourer's Scrap" "Blacksmith's Whetstone"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # %D4 $type->currency->levelingstacked $tier->t5aug
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Orb of Augmentation"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 190 178 135 255
	SetBorderColor 190 178 135 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->currency->levelingstacked $tier->portal
	StackSize >= 2
	Class == "Stackable Currency"
	BaseType == "Portal Scroll"
	AreaLevel <= 67
	SetFontSize 45
	SetBorderColor 60 100 200 255
	SetBackgroundColor 5 8 40 255

Show # %D3 $type->currency->levelingstacked $tier->wisdom
	StackSize >= 2
	Class == "Stackable Currency"
	BaseType == "Scroll of Wisdom"
	AreaLevel <= 67
	SetFontSize 45
	SetBorderColor 200 100 60 255
	SetBackgroundColor 30 5 5 255

# !! Waypoint c9.currency.leveling.nonstacked : "Tierlist - Currency - Leveling Currency" : "Leveling"

Show # %D5 $type->currency->leveling $tier->essences
	Class == "Stackable Currency"
	BaseType "Muttering Essence of" "Wailing Essence of" "Weeping Essence of" "Whispering Essence of"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 Grey Circle

Show # %D5 $type->currency->leveling $tier->t1binding
	Class == "Stackable Currency"
	BaseType == "Orb of Binding"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Grey Circle

Show # %D4 $type->currency->leveling $tier->t2chance
	Class == "Stackable Currency"
	BaseType == "Orb of Chance"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Grey Circle

Show # %D4 $type->currency->leveling $tier->t3transearly
	Class == "Stackable Currency"
	BaseType == "Orb of Alteration" "Orb of Transmutation"
	AreaLevel <= 34
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # %D4 $type->currency->leveling $tier->t3trans
	Class == "Stackable Currency"
	BaseType == "Orb of Alteration" "Orb of Transmutation"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 190 178 135 255
	SetBorderColor 190 178 135 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->currency->leveling $tier->t4misc
	Class == "Stackable Currency"
	BaseType == "Armourer's Scrap" "Blacksmith's Whetstone"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # %D4 $type->currency->leveling $tier->t5aug
	Class == "Stackable Currency"
	BaseType == "Orb of Augmentation"
	AreaLevel <= 67
	SetFontSize 45
	SetTextColor 190 178 135 255
	SetBorderColor 190 178 135 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->currency->leveling $tier->portal
	Class == "Stackable Currency"
	BaseType == "Portal Scroll"
	AreaLevel <= 67
	SetFontSize 45
	SetBorderColor 30 50 100 255
	SetBackgroundColor 20 20 0 255

Show # %D3 $type->currency->leveling $tier->wisdom
	Class == "Stackable Currency"
	BaseType == "Scroll of Wisdom"
	AreaLevel <= 67
	SetFontSize 45
	SetBorderColor 100 50 30 255
	SetBackgroundColor 20 20 0 255

#===============================================================================================================

# [[3900]] Currency - Exceptions - Stacked Currency

#===============================================================================================================
#------------------------------------

# [3901] Supplies: High Stacking

#------------------------------------

# !! Waypoint c9.currency.stacked.all : "Tierlist - Currency - Endgame Stacked" : "Currency and Currency-Likes"

Show # %DS4 $type->currency->stackedsupplieshigh $tier->t1
	StackSize >= 10
	Class == "Stackable Currency"
	BaseType == "Orb of Transmutation"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %DS3 $type->currency->stackedsupplieshigh $tier->t2
	StackSize >= 5
	Class == "Stackable Currency"
	BaseType == "Orb of Transmutation"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255

Show # %D3 $type->currency->stackedsupplieshigh $tier->t3
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Orb of Transmutation"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255

#------------------------------------

# [3902] Supplies: Low Stacking

#------------------------------------

Show # %DS4 $type->currency->stackedsupplieslow $tier->t1
	StackSize >= 10
	Class == "Stackable Currency"
	BaseType == "Orb of Augmentation"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # %DS3 $type->currency->stackedsupplieslow $tier->t2
	StackSize >= 5
	Class == "Stackable Currency"
	BaseType == "Orb of Augmentation"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255

Show # %D3 $type->currency->stackedsupplieslow $tier->t3
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Orb of Augmentation"
	SetFontSize 45
	SetTextColor 190 178 135 255
	SetBorderColor 190 178 135 255
	SetBackgroundColor 20 20 0 255

#------------------------------------

# [3903] Supplies: Portal Stacking

#------------------------------------

Show # %DS4 $type->currency->stackedsuppliesportal $tier->t1
	StackSize >= 10
	Class == "Stackable Currency"
	BaseType == "Portal Scroll"
	SetFontSize 45
	SetBorderColor 60 100 200 255
	SetBackgroundColor 5 8 40 255

Show # %D3 $type->currency->stackedsuppliesportal $tier->t2
	StackSize >= 5
	Class == "Stackable Currency"
	BaseType == "Portal Scroll"
	SetFontSize 45
	SetBorderColor 60 100 200 255
	SetBackgroundColor 5 8 40 255

#Show # %D2 $type->currency->stackedsuppliesportal $tier->t3

# StackSize >= 3

# Class == "Stackable Currency"

# BaseType == "Portal Scroll"

# SetFontSize 40

# SetBorderColor 30 50 100 255

# SetBackgroundColor 20 20 0 255

#------------------------------------

# [3904] Supplies: Wisdom Stacking

#------------------------------------

Show # %DS4 $type->currency->stackedsupplieswisdom $tier->t1
	StackSize >= 10
	Class == "Stackable Currency"
	BaseType == "Scroll of Wisdom"
	SetFontSize 45
	SetBorderColor 200 100 60 255
	SetBackgroundColor 30 5 5 255

Show # %D3 $type->currency->stackedsupplieswisdom $tier->t2
	StackSize >= 5
	Class == "Stackable Currency"
	BaseType == "Scroll of Wisdom"
	SetFontSize 45
	SetBorderColor 200 100 60 255
	SetBackgroundColor 30 5 5 255

#Show # %D2 $type->currency->stackedsupplieswisdom $tier->t3

# StackSize >= 3

# Class == "Stackable Currency"

# BaseType == "Scroll of Wisdom"

# SetFontSize 40

# SetBorderColor 100 50 30 255

# SetBackgroundColor 20 20 0 255

#------------------------------------

# [3905] Stacked Currencies: 6x

#------------------------------------

Show # %D9 $type->currency->stackedsix $tier->t1
	StackSize >= 6
	Class == "Stackable Currency"
	BaseType == "Dextral Catalyst" "Fertile Catalyst" "Fracturing Shard" "Grand Eldritch Ember" "Orb of Annulment" "Prismatic Catalyst" "Sinistral Catalyst" "Tempering Catalyst"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %D8 $type->currency->stackedsix $tier->t2
	StackSize >= 6
	Class == "Stackable Currency"
	BaseType == "Accelerating Catalyst" "Ancient Orb" "Burial Medallion" "Chaos Orb" "Chromatic Orb" "Exotic Coinage" "Grand Eldritch Ichor" "Greater Eldritch Ember" "Greater Eldritch Ichor" "Imbued Catalyst" "Intrinsic Catalyst" "Noxious Catalyst" "Stacked Deck" "Unstable Catalyst"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %D7 $type->currency->stackedsix $tier->t3
	StackSize >= 6
	Class == "Stackable Currency"
	BaseType == "Abrasive Catalyst" "Enkindling Orb" "Exalted Orb" "Gemcutter's Prism" "Glassblower's Bauble" "Instilling Orb" "Lesser Eldritch Ember" "Lesser Eldritch Ichor" "Orb of Regret" "Orb of Scouring" "Scrap Metal" "Turbulent Catalyst" "Vaal Orb"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %D6 $type->currency->stackedsix $tier->t4
	StackSize >= 6
	Class == "Stackable Currency"
	BaseType == "Blacksmith's Whetstone" "Blessed Orb" "Orb of Alchemy" "Orb of Alteration" "Orb of Fusing" "Orb of Unmaking" "Regal Orb"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %DS4 $type->currency->stackedsix $tier->t5
	StackSize >= 6
	Class == "Stackable Currency"
	BaseType == "Armourer's Scrap" "Astragali" "Jeweller's Orb" "Orb of Binding" "Orb of Chance"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

#Show # %DS3 $type->currency->stackedsix $tier->t6

# StackSize >= 6

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 210 178 135 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Circle

Show # %DS2 $type->currency->stackedsix $tier->t7
	StackSize >= 6
	Class == "Stackable Currency"
	BaseType == "Alchemy Shard" "Alteration Shard"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255

#------------------------------------

# [3906] Stacked Currencies: 3x

#------------------------------------

Show # %D9 $type->currency->stackedthree $tier->t1
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Dextral Catalyst" "Fertile Catalyst" "Orb of Annulment" "Sinistral Catalyst"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %D8 $type->currency->stackedthree $tier->t2
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Accelerating Catalyst" "Ancient Orb" "Fracturing Shard" "Grand Eldritch Ember" "Imbued Catalyst" "Noxious Catalyst" "Prismatic Catalyst" "Tempering Catalyst" "Unstable Catalyst"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %D7 $type->currency->stackedthree $tier->t3
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Abrasive Catalyst" "Burial Medallion" "Chaos Orb" "Chromatic Orb" "Exalted Orb" "Exotic Coinage" "Gemcutter's Prism" "Grand Eldritch Ichor" "Greater Eldritch Ember" "Greater Eldritch Ichor" "Instilling Orb" "Intrinsic Catalyst" "Orb of Regret" "Stacked Deck" "Turbulent Catalyst"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %D6 $type->currency->stackedthree $tier->t4
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Enkindling Orb" "Glassblower's Bauble" "Lesser Eldritch Ember" "Lesser Eldritch Ichor" "Orb of Scouring" "Orb of Unmaking" "Regal Orb" "Scrap Metal" "Vaal Orb"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %DS4 $type->currency->stackedthree $tier->t5
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Blacksmith's Whetstone" "Blessed Orb" "Jeweller's Orb" "Orb of Alchemy" "Orb of Alteration" "Orb of Binding" "Orb of Chance" "Orb of Fusing"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %DS3 $type->currency->stackedthree $tier->t6
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Armourer's Scrap" "Astragali"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

#Show # %DS2 $type->currency->stackedthree $tier->t7

# StackSize >= 3

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 210 178 135 255

# !! Waypoint c9.currency.heistcoins : "Tierlist - Currency - Heist Coins" : "Heist, Expedition, Sanctum"

#------------------------------------

# [3907] Heist Coins

#------------------------------------

Show # %H5 $type->currency->heist $tier->highstack
	StackSize >= 400
	Class == "Stackable Currency"
	BaseType == "Rogue's Marker"
	SetFontSize 45
	SetTextColor 255 178 135 255
	SetBorderColor 255 178 135 255
	SetBackgroundColor 150 90 70 255
	PlayEffect Orange

Show # %H4 $type->currency->heist $tier->any
	Class == "Stackable Currency"
	BaseType == "Rogue's Marker"
	SetFontSize 45
	SetTextColor 255 178 135 255
	SetBorderColor 255 178 135 255
	SetBackgroundColor 20 20 0 255
	PlayEffect Orange Temp

Hide # $type->currency->heist $tier->exhide
	Class == "Stackable Currency"
	BaseType == "Rogue's Marker"
	SetFontSize 35
	SetBorderColor 0 0 0

Show # $type->currency->leagueexclusive $tier->silvercoin
	BaseType == "Silver Coin"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 120 200 160 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Moon

#===============================================================================================================

# [[4000]] Currency - Regular Currency Tiering

#===============================================================================================================

# !! Waypoint c9.currency.single : "Tierlist - Currency - General" : "Currency and Currency-Likes"

Show # $type->currency $tier->t1exalted
	Class == "Stackable Currency"
	BaseType == "Albino Rhoa Feather" "Awakener's Orb" "Chaotic Astrolabe" "Crusader's Exalted Orb" "Crystallised Rancour" "Deceptive Astrolabe" "Dextral Catalyst" "Divine Orb" "Elder's Exalted Orb" "Eldritch Orb of Annulment" "Eternal Orb" "Flesh of Xesht" "Foulborn Exalted Orb" "Fracturing Orb" "Fruiting Astrolabe" "Fungal Astrolabe" "Grasping Astrolabe" "Hinekora's Lock" "Hunter's Exalted Orb" "Lightless Astrolabe" "Maraketh Enshrouding Crystal" "Mirror of Kalandra" "Mirror Shard" "Orb of Conflict" "Orb of Dominance" "Orb of Remembrance" "Redeemer's Exalted Orb" "Reflecting Mist" "Runic Astrolabe" "Sacred Crystallised Lifeforce" "Shaper's Exalted Orb" "Tainted Divine Teardrop" "Tempering Orb" "Timeless Astrolabe" "Valdo's Puzzle Box" "Veiled Chaos Orb" "Veiled Exalted Orb" "Volatile Vaal Orb" "Warlord's Exalted Orb"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency $tier->t2divine
	Class == "Stackable Currency"
	BaseType == "Coin of Knowledge" "Coin of Power" "Coin of Skill" "Eldritch Chaos Orb" "Exceptional Eldritch Ember" "Exceptional Eldritch Ichor" "Fertile Catalyst" "Foulborn Regal Orb" "Fracturing Shard" "Grand Eldritch Ember" "Karui Enshrouding Crystal" "Maven's Chisel of Avarice" "Maven's Chisel of Divination" "Maven's Chisel of Procurement" "Maven's Chisel of Proliferation" "Memory of Reverence" "Memory of Trauma" "Message in a Bottle" "Orb of Annulment" "Orb of Unravelling" "Prismatic Catalyst" "Refracting Fog" "Ritual Vessel" "Sacred Orb" "Sinistral Catalyst" "Tailoring Orb" "Tainted Catalyst" "Tainted Exalted Orb" "Tainted Orb of Fusing" "Tempering Catalyst" "Templar Astrolabe" "Templar Enshrouding Crystal"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency $tier->t3annul
	Class == "Stackable Currency"
	BaseType == "Accelerating Catalyst" "Ancient Orb" "Burial Medallion" "Crescent Splinter" "Eldritch Exalted Orb" "Exotic Coinage" "Foulborn Orb of Augmentation" "Imbued Catalyst" "Intrinsic Catalyst" "Maven's Chisel of Scarabs" "Memory of Loneliness" "Nameless Astrolabe" "Noxious Catalyst" "Stacked Deck" "Tainted Chaos Orb" "Tainted Chromatic Orb" "Tainted Mythic Orb" "Unstable Catalyst" "Vaal Enshrouding Crystal"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->currency $tier->t4chaos
	Class == "Stackable Currency"
	BaseType == "Abrasive Catalyst" "Chaos Orb" "Chromatic Orb" "Coin of Desecration" "Exalted Orb" "Gemcutter's Prism" "Grand Eldritch Ichor" "Greater Eldritch Ember" "Greater Eldritch Ichor" "Imperial Enshrouding Crystal" "Lesser Eldritch Ichor" "Orb of Intention" "Orb of Regret" "Ritual Splinter" "Scrap Metal" "Tainted Armourer's Scrap" "Tainted Jeweller's Orb" "Turbulent Catalyst" "Vaal Orb" "Veiled Scarab"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %HS4 $type->currency $tier->t5alchemy
	Class == "Stackable Currency"
	BaseType == "Astragali" "Coin of Restoration" "Enkindling Orb" "Glassblower's Bauble" "Instilling Orb" "Lesser Eldritch Ember" "Orb of Alchemy" "Orb of Alteration" "Orb of Scouring" "Orb of Unmaking" "Regal Orb" "Tainted Blacksmith's Whetstone"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %HS3 $type->currency $tier->t6chrom
	Class == "Stackable Currency"
	BaseType == "Blacksmith's Whetstone" "Blessed Orb" "Orb of Fusing"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # %HS2 $type->currency $tier->t7chance
	Class == "Stackable Currency"
	BaseType == "Armourer's Scrap" "Jeweller's Orb" "Orb of Binding" "Orb of Chance"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255

Hide # %HS1 $type->currency $tier->t8trans
	Class == "Stackable Currency"
	BaseType == "Alchemy Shard" "Alteration Shard" "Orb of Transmutation"
	SetFontSize 45
	SetTextColor 190 178 135 255
	SetBorderColor 190 178 135 255
	SetBackgroundColor 20 20 0 255

Hide # %H1 $type->currency $tier->t9armour
	Class == "Stackable Currency"
	BaseType == "Orb of Augmentation" "Transmutation Shard"
	SetFontSize 40
	SetTextColor 170 158 130 255
	SetBorderColor 170 158 130 255
	SetBackgroundColor 20 20 0 255

Hide # %H1 $type->currency $tier->tportal
	Class == "Stackable Currency"
	BaseType == "Portal Scroll"
	SetFontSize 40
	SetBorderColor 30 50 100 255
	SetBackgroundColor 20 20 0 255

Hide # %H1 $type->currency $tier->twisdom
	Class == "Stackable Currency"
	BaseType == "Scroll of Wisdom"
	SetFontSize 40
	SetBorderColor 100 50 30 255
	SetBackgroundColor 20 20 0 255

#===============================================================================================================

# [[4100]] Currency - SPECIAL

#===============================================================================================================
#------------------------------------

# [4101] Incursion - Vials

#------------------------------------

# !! Waypoint c9.currency.vials.all : "Tierlist - Currency - Vials" : "Currency and Currency-Likes"

Show # $type->vials $tier->t1
	Class == "Stackable Currency"
	BaseType == "Vial of Sacrifice" "Vial of the Ghost" "Vial of the Ritual"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->vials $tier->t2
	Class == "Stackable Currency"
	BaseType == "Vial of Summoning" "Vial of Transcendence"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %HS4 $type->vials $tier->t3
	Class == "Stackable Currency"
	BaseType == "Vial of Awakening" "Vial of Consequence" "Vial of Dominance" "Vial of Fate"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # $type->vials $tier->restex
	Class == "Stackable Currency"
	BaseType "Vial of"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4102] Delirum Orbs

#------------------------------------

# !! Waypoint c9.currency.delirium.all : "Tierlist - Currency - Delirium Orbs" : "Currency and Currency-Likes"

#Show # $type->currency->deliriumorbs $tier->t1

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 255 0 0 255

# SetBorderColor 255 0 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 6 300

# PlayEffect Red

# MinimapIcon 0 Red Star

Show # %H8 $type->currency->deliriumorbs $tier->t2
	Class == "Stackable Currency"
	BaseType == "Diviner's Delirium Orb" "Skittering Delirium Orb"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency->deliriumorbs $tier->t3
	Class == "Stackable Currency"
	BaseType == "Armoursmith's Delirium Orb" "Blacksmith's Delirium Orb" "Blighted Delirium Orb" "Cartographer's Delirium Orb" "Fine Delirium Orb" "Fragmented Delirium Orb" "Jeweller's Delirium Orb" "Singular Delirium Orb" "Thaumaturge's Delirium Orb" "Whispering Delirium Orb"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # $type->currency->deliriumorbs $tier->restex
	Class == "Stackable Currency"
	BaseType "Delirium Orb"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4103] Delve - Fossils and Resonators

#------------------------------------

# !! Waypoint c9.currency.fossils.all : "Tierlist - Fossils and Resonators" : "Currency and Currency-Likes"

Show # $type->currency->fossil $tier->t1
	Class == "Delve Stackable Socketable Currency" "Stackable Currency"
	BaseType == "Faceted Fossil" "Fractured Fossil" "Hollow Fossil" "Prime Chaotic Resonator"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency->fossil $tier->t2
	Class == "Delve Stackable Socketable Currency" "Stackable Currency"
	BaseType == "Dense Fossil" "Gilded Fossil" "Glyphic Fossil" "Sanctified Fossil"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %HS5 $type->currency->fossil $tier->t3
	Class == "Delve Stackable Socketable Currency" "Stackable Currency"
	BaseType == "Aberrant Fossil" "Aetheric Fossil" "Bound Fossil" "Corroded Fossil" "Deft Fossil" "Frigid Fossil" "Fundamental Fossil" "Jagged Fossil" "Lucent Fossil" "Metallic Fossil" "Opulent Fossil" "Prismatic Fossil" "Pristine Fossil" "Serrated Fossil" "Shuddering Fossil"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %HS4 $type->currency->fossil $tier->t4
	Class == "Delve Stackable Socketable Currency" "Stackable Currency"
	BaseType == "Bloodstained Fossil" "Potent Chaotic Resonator" "Powerful Chaotic Resonator" "Primitive Chaotic Resonator" "Tangled Fossil"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %HS3 $type->currency->fossil $tier->t5
	Class == "Delve Stackable Socketable Currency" "Stackable Currency"
	BaseType == "Scorched Fossil"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Hide # $type->currency->fossil $tier->exhide
	Class == "Delve Stackable Socketable Currency" "Stackable Currency"
	BaseType == "Aberrant Fossil" "Aetheric Fossil" "Bloodstained Fossil" "Bound Fossil" "Corroded Fossil" "Deft Fossil" "Dense Fossil" "Faceted Fossil" "Fractured Fossil" "Frigid Fossil" "Fundamental Fossil" "Gilded Fossil" "Glyphic Fossil" "Hollow Fossil" "Jagged Fossil" "Lucent Fossil" "Metallic Fossil" "Opulent Fossil" "Potent Chaotic Resonator" "Powerful Chaotic Resonator" "Prime Chaotic Resonator" "Primitive Chaotic Resonator" "Prismatic Fossil" "Pristine Fossil" "Sanctified Fossil" "Scorched Fossil" "Serrated Fossil" "Shuddering Fossil" "Tangled Fossil"
	SetFontSize 35
	SetBorderColor 0 0 0

Show # $type->currency->fossil $tier->restex
	Class == "Delve Stackable Socketable Currency" "Stackable Currency"
	BaseType "Fossil" "Resonator"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4104] Allflame - Ducats

#------------------------------------

# !! Waypoint c9.currency.ducats.all : "Tierlist - Allflame Ducats" : "Currency and Currency-Likes"

#Show # $type->currency->ducats $tier->t1

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 255 0 0 255

# SetBorderColor 255 0 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 6 300

# PlayEffect Red

# MinimapIcon 0 Red Star

Show # %H9 $type->currency->ducats $tier->t2
	Class == "Stackable Currency"
	BaseType == "Brinehook's Ducat" "Tzamoto's Ducat" "Ukatoa's Ducat"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H8 $type->currency->ducats $tier->t3
	Class == "Stackable Currency"
	BaseType == "Kishara's Ducat" "The Genteel's Ducat"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H7 $type->currency->ducats $tier->t4
	Class == "Stackable Currency"
	BaseType == "Cyaxan's Ducat" "Katakohi's Ducat" "Merrick's Ducat" "Rotmother's Ducat" "Telesia's Ducat" "The Changeling's Ducat"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

#Show # %H5 $type->currency->ducats $tier->t5

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 210 178 135 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Circle

Hide # $type->currency->ducats $tier->exhide
	Class == "Stackable Currency"
	BaseType == "Brinehook's Ducat" "Cyaxan's Ducat" "Katakohi's Ducat" "Kishara's Ducat" "Merrick's Ducat" "Rotmother's Ducat" "Telesia's Ducat" "The Changeling's Ducat" "The Genteel's Ducat" "Tzamoto's Ducat" "Ukatoa's Ducat"
	SetFontSize 35
	SetBorderColor 0 0 0

Show # $type->currency->ducats $tier->restex
	Class == "Stackable Currency"
	BaseType "Ducat"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4105] Blight - Oils

#------------------------------------

# !! Waypoint c9.currency.oils.all : "Tierlist - Oils" : "Currency and Currency-Likes"

Show # $type->currency->oil $tier->t1
	Class == "Stackable Currency"
	BaseType == "Golden Oil" "Opalescent Oil" "Prismatic Oil" "Reflective Oil" "Silver Oil" "Tainted Oil"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency->oil $tier->t2
	Class == "Stackable Currency"
	BaseType == "Black Oil"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %HS5 $type->currency->oil $tier->t3
	Class == "Stackable Currency"
	BaseType == "Crimson Oil"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %HS4 $type->currency->oil $tier->t4
	Class == "Stackable Currency"
	BaseType == "Amber Oil" "Azure Oil" "Teal Oil" "Verdant Oil" "Violet Oil"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %HS3 $type->currency->oil $tier->t5
	Class == "Stackable Currency"
	BaseType == "Clear Oil" "Indigo Oil" "Sepia Oil"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Hide # $type->currency->oil $tier->exhide
	Class == "Stackable Currency"
	BaseType == "Amber Oil" "Azure Oil" "Black Oil" "Clear Oil" "Crimson Oil" "Golden Oil" "Indigo Oil" "Opalescent Oil" "Prismatic Oil" "Reflective Oil" "Sepia Oil" "Silver Oil" "Tainted Oil" "Teal Oil" "Verdant Oil" "Violet Oil"
	SetFontSize 35
	SetBorderColor 0 0 0

Show # $type->currency->oil $tier->restex
	Class == "Stackable Currency"
	BaseType "Oil"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4106] Runes

#------------------------------------

# !! Waypoint c9.runes.all : "Tierlist - Runes and Corpses" : "Currency and Currency-Likes"

Show # $type->runesgrafts $tier->t1
	Class == "Stackable Currency"
	BaseType == "Runegraft of Gemcraft" "Runegraft of the Angler" "Runegraft of the Fortress" "Runegraft of the Soulwick" "Runegraft of the Warp"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->runesgrafts $tier->t2
	Class == "Stackable Currency"
	BaseType == "Runegraft of Bellows" "Runegraft of Blasphemy" "Runegraft of Connection" "Runegraft of Consecration" "Runegraft of Fury" "Runegraft of Loyalty" "Runegraft of Quaffing" "Runegraft of Rallying" "Runegraft of Restitching" "Runegraft of Rotblood" "Runegraft of Stability" "Runegraft of Suffering" "Runegraft of the Agile" "Runegraft of the Bound" "Runegraft of the Combatant" "Runegraft of the Imbued" "Runegraft of the Jeweller" "Runegraft of the Novamark" "Runegraft of the River" "Runegraft of the Sinistral" "Runegraft of the Spellbound" "Runegraft of the Witchmark" "Runegraft of Time" "Runegraft of Treachery"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %HS6 $type->runesgrafts $tier->t3
	Class == "Stackable Currency"
	BaseType == "Runegraft of Refraction" "Runegraft of Resurgence"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

#Show # %HS5 $type->runesgrafts $tier->t4

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 249 150 25 255

# PlayAlertSound 2 300

# PlayEffect White

# MinimapIcon 2 White Circle

#Show # %HS3 $type->runesgrafts $tier->t5

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 210 178 135 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Circle

Show # $type->runesgrafts $tier->restex
	Class == "Stackable Currency"
	BaseType "Runegraft"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4107] Corpses

#------------------------------------

Show # $type->corpses $tier->t1
	Class == "Corpses"
	BaseType == "Perfect Forest Tiger" "Perfect Warlord"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->corpses $tier->t2
	Class == "Corpses"
	BaseType == "Perfect Adherent of Zarokh" "Perfect Astral Lich" "Perfect Blasphemer" "Perfect Blood Demon" "Perfect Conjuror of Rot" "Perfect Dancing Sword" "Perfect Dark Marionette" "Perfect Dark Reaper" "Perfect Druidic Alchemist" "Perfect Eldritch Eye" "Perfect Fiery Cannibal" "Perfect Forest Warrior" "Perfect Frozen Cannibal" "Perfect Guardian Turtle" "Perfect Half-remembered Goliath" "Perfect Hulking Miscreation" "Perfect Hydra" "Perfect Judgemental Spirit" "Perfect Meatsack" "Perfect Naval Officer" "Perfect Needle Horror" "Perfect Pain Artist" "Perfect Primal Demiurge" "Perfect Primal Thunderbird" "Perfect Runic Skeleton" "Perfect Sanguimancer Demon" "Perfect Sawblade Horror" "Perfect Serpent Warrior" "Perfect Shadow Construct" "Perfect Slashing Horror" "Perfect Spider Matriarch" "Perfect Spirit of Fortune"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %HS5 $type->corpses $tier->t3
	Class == "Corpses"
	BaseType == "Adherent of Zarokh" "Astral Lich" "Blasphemer" "Blood Demon" "Conjuror of Rot" "Dancing Sword" "Dark Marionette" "Dark Reaper" "Druidic Alchemist" "Eldritch Eye" "Fiery Cannibal" "Forest Tiger" "Forest Warrior" "Frozen Cannibal" "Guardian Turtle" "Half-remembered Goliath" "Hulking Miscreation" "Hydra" "Imperfect Adherent of Zarokh" "Imperfect Astral Lich" "Imperfect Conjuror of Rot" "Judgemental Spirit" "Meatsack" "Naval Officer" "Needle Horror" "Pain Artist" "Primal Demiurge" "Primal Thunderbird" "Runic Skeleton" "Sanguimancer Demon" "Sawblade Horror" "Serpent Warrior" "Shadow Construct" "Slashing Horror" "Spider Matriarch" "Spirit of Fortune" "Warlord"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %HS4 $type->corpses $tier->t4
	Class == "Corpses"
	BaseType == "Imperfect Blasphemer" "Imperfect Blood Demon" "Imperfect Dancing Sword" "Imperfect Dark Marionette" "Imperfect Dark Reaper" "Imperfect Druidic Alchemist" "Imperfect Eldritch Eye" "Imperfect Fiery Cannibal" "Imperfect Forest Tiger" "Imperfect Forest Warrior" "Imperfect Frozen Cannibal" "Imperfect Guardian Turtle" "Imperfect Half-remembered Goliath" "Imperfect Hulking Miscreation" "Imperfect Hydra" "Imperfect Judgemental Spirit" "Imperfect Meatsack" "Imperfect Naval Officer" "Imperfect Needle Horror" "Imperfect Pain Artist" "Imperfect Primal Demiurge" "Imperfect Primal Thunderbird" "Imperfect Runic Skeleton" "Imperfect Sanguimancer Demon" "Imperfect Sawblade Horror" "Imperfect Serpent Warrior" "Imperfect Shadow Construct" "Imperfect Slashing Horror" "Imperfect Spider Matriarch" "Imperfect Spirit of Fortune" "Imperfect Warlord"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

#Show # %HS3 $type->corpses $tier->t5

# Class == "Corpses"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 210 178 135 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Circle

Show # $type->corpses $tier->restex
	Class == "Corpses"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4108] Essences

#------------------------------------

# !! Waypoint c9.currency.essences.all : "Tierlist - Essences, Omen, Tattoos" : "Currency and Currency-Likes"

Show # $type->currency->essence $tier->t1
	Class == "Stackable Currency"
	BaseType == "Essence of Horror"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency->essence $tier->t2
	Class == "Stackable Currency"
	BaseType == "Deafening Essence of Contempt" "Deafening Essence of Doubt" "Deafening Essence of Envy" "Deafening Essence of Greed" "Deafening Essence of Loathing" "Deafening Essence of Scorn" "Deafening Essence of Spite" "Deafening Essence of Suffering" "Deafening Essence of Zeal" "Essence of Delirium" "Essence of Desolation" "Essence of Hysteria" "Essence of Insanity"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %HS5 $type->currency->essence $tier->t3
	Class == "Stackable Currency"
	BaseType == "Deafening Essence of Anger" "Deafening Essence of Anguish" "Deafening Essence of Dread" "Deafening Essence of Fear" "Deafening Essence of Hatred" "Deafening Essence of Rage" "Deafening Essence of Sorrow" "Deafening Essence of Torment" "Deafening Essence of Woe" "Deafening Essence of Wrath" "Shrieking Essence of Anger" "Shrieking Essence of Anguish" "Shrieking Essence of Contempt" "Shrieking Essence of Doubt" "Shrieking Essence of Dread" "Shrieking Essence of Envy" "Shrieking Essence of Fear" "Shrieking Essence of Greed" "Shrieking Essence of Hatred" "Shrieking Essence of Loathing" "Shrieking Essence of Misery" "Shrieking Essence of Rage" "Shrieking Essence of Scorn" "Shrieking Essence of Sorrow" "Shrieking Essence of Spite" "Shrieking Essence of Suffering" "Shrieking Essence of Torment" "Shrieking Essence of Woe" "Shrieking Essence of Wrath" "Shrieking Essence of Zeal"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %HS4 $type->currency->essence $tier->t4
	Class == "Stackable Currency"
	BaseType == "Deafening Essence of Misery" "Screaming Essence of Anger" "Screaming Essence of Anguish" "Screaming Essence of Contempt" "Screaming Essence of Doubt" "Screaming Essence of Dread" "Screaming Essence of Envy" "Screaming Essence of Fear" "Screaming Essence of Greed" "Screaming Essence of Hatred" "Screaming Essence of Loathing" "Screaming Essence of Misery" "Screaming Essence of Rage" "Screaming Essence of Scorn" "Screaming Essence of Sorrow" "Screaming Essence of Spite" "Screaming Essence of Suffering" "Screaming Essence of Torment" "Screaming Essence of Woe" "Screaming Essence of Wrath" "Screaming Essence of Zeal"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %HS3 $type->currency->essence $tier->t5
	Class == "Stackable Currency"
	BaseType == "Wailing Essence of Anger" "Wailing Essence of Anguish" "Wailing Essence of Contempt" "Wailing Essence of Doubt" "Wailing Essence of Fear" "Wailing Essence of Greed" "Wailing Essence of Hatred" "Wailing Essence of Loathing" "Wailing Essence of Rage" "Wailing Essence of Sorrow" "Wailing Essence of Spite" "Wailing Essence of Suffering" "Wailing Essence of Torment" "Wailing Essence of Woe" "Wailing Essence of Wrath" "Wailing Essence of Zeal"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # %HS2 $type->currency->essence $tier->t6
	Class == "Stackable Currency"
	BaseType == "Muttering Essence of Anger" "Muttering Essence of Contempt" "Muttering Essence of Fear" "Muttering Essence of Greed" "Muttering Essence of Hatred" "Muttering Essence of Sorrow" "Muttering Essence of Torment" "Muttering Essence of Woe" "Weeping Essence of Anger" "Weeping Essence of Contempt" "Weeping Essence of Doubt" "Weeping Essence of Fear" "Weeping Essence of Greed" "Weeping Essence of Hatred" "Weeping Essence of Rage" "Weeping Essence of Sorrow" "Weeping Essence of Suffering" "Weeping Essence of Torment" "Weeping Essence of Woe" "Weeping Essence of Wrath" "Whispering Essence of Contempt" "Whispering Essence of Greed" "Whispering Essence of Hatred" "Whispering Essence of Woe"
	SetFontSize 45
	SetTextColor 190 178 135 255
	SetBorderColor 190 178 135 255
	SetBackgroundColor 20 20 0 255

Hide # $type->currency->essence $tier->exhide
	Class == "Stackable Currency"
	BaseType == "Deafening Essence of Anger" "Deafening Essence of Anguish" "Deafening Essence of Contempt" "Deafening Essence of Doubt" "Deafening Essence of Dread" "Deafening Essence of Envy" "Deafening Essence of Fear" "Deafening Essence of Greed" "Deafening Essence of Hatred" "Deafening Essence of Loathing" "Deafening Essence of Misery" "Deafening Essence of Rage" "Deafening Essence of Scorn" "Deafening Essence of Sorrow" "Deafening Essence of Spite" "Deafening Essence of Suffering" "Deafening Essence of Torment" "Deafening Essence of Woe" "Deafening Essence of Wrath" "Deafening Essence of Zeal" "Essence of Delirium" "Essence of Desolation" "Essence of Horror" "Essence of Hysteria" "Essence of Insanity" "Muttering Essence of Anger" "Muttering Essence of Contempt" "Muttering Essence of Fear" "Muttering Essence of Greed" "Muttering Essence of Hatred" "Muttering Essence of Sorrow" "Muttering Essence of Torment" "Muttering Essence of Woe" "Screaming Essence of Anger" "Screaming Essence of Anguish" "Screaming Essence of Contempt" "Screaming Essence of Doubt" "Screaming Essence of Dread" "Screaming Essence of Envy" "Screaming Essence of Fear" "Screaming Essence of Greed" "Screaming Essence of Hatred" "Screaming Essence of Loathing" "Screaming Essence of Misery" "Screaming Essence of Rage" "Screaming Essence of Scorn" "Screaming Essence of Sorrow" "Screaming Essence of Spite" "Screaming Essence of Suffering" "Screaming Essence of Torment" "Screaming Essence of Woe" "Screaming Essence of Wrath" "Screaming Essence of Zeal" "Shrieking Essence of Anger" "Shrieking Essence of Anguish" "Shrieking Essence of Contempt" "Shrieking Essence of Doubt" "Shrieking Essence of Dread" "Shrieking Essence of Envy" "Shrieking Essence of Fear" "Shrieking Essence of Greed" "Shrieking Essence of Hatred" "Shrieking Essence of Loathing" "Shrieking Essence of Misery" "Shrieking Essence of Rage" "Shrieking Essence of Scorn" "Shrieking Essence of Sorrow" "Shrieking Essence of Spite" "Shrieking Essence of Suffering" "Shrieking Essence of Torment" "Shrieking Essence of Woe" "Shrieking Essence of Wrath" "Shrieking Essence of Zeal" "Wailing Essence of Anger" "Wailing Essence of Anguish" "Wailing Essence of Contempt" "Wailing Essence of Doubt" "Wailing Essence of Fear" "Wailing Essence of Greed" "Wailing Essence of Hatred" "Wailing Essence of Loathing" "Wailing Essence of Rage" "Wailing Essence of Sorrow" "Wailing Essence of Spite" "Wailing Essence of Suffering" "Wailing Essence of Torment" "Wailing Essence of Woe" "Wailing Essence of Wrath" "Wailing Essence of Zeal" "Weeping Essence of Anger" "Weeping Essence of Contempt" "Weeping Essence of Doubt" "Weeping Essence of Fear" "Weeping Essence of Greed" "Weeping Essence of Hatred" "Weeping Essence of Rage" "Weeping Essence of Sorrow" "Weeping Essence of Suffering" "Weeping Essence of Torment" "Weeping Essence of Woe" "Weeping Essence of Wrath" "Whispering Essence of Contempt" "Whispering Essence of Greed" "Whispering Essence of Hatred" "Whispering Essence of Woe"
	SetFontSize 35
	SetBorderColor 0 0 0

Show # $type->currency->essence $tier->restex
	Class == "Stackable Currency"
	BaseType "Essence of"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4109] Ritual

#------------------------------------

Show # $type->currency->trial->omen $tier->t1
	Class == "Stackable Currency"
	BaseType == "Omen of Connections" "Omen of Fortune"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency->trial->omen $tier->t2
	Class == "Stackable Currency"
	BaseType == "Omen of Amelioration" "Omen of Death-dancing" "Omen of Death's Door" "Omen of the Jeweller" "Omen of Trichromatism"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency->trial->omen $tier->t3
	Class == "Stackable Currency"
	BaseType == "Omen of Brilliance"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H5 $type->currency->trial->omen $tier->t4
	Class == "Stackable Currency"
	BaseType == "Omen of Adrenaline" "Omen of Return"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %HS3 $type->currency->trial->omen $tier->t5
	Class == "Stackable Currency"
	BaseType == "Omen of Refreshment" "Omen of the Soul Devourer"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 210 178 135 255
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Circle

Show # $type->currency->trial->omen $tier->restex
	Class == "Stackable Currency"
	BaseType "Omen of"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4110] Trial of the Ancestors

#------------------------------------

Show # $type->currency->trial->tattoo $tier->t1
	Class == "Stackable Currency"
	BaseType == "Journey Tattoo of the Body" "Journey Tattoo of the Mind" "Journey Tattoo of the Soul" "Tattoo of the Arohongui Shaman" "Tattoo of the Ngamahu Warmonger" "Tattoo of the Ramako Shaman" "Tattoo of the Rongokurai Turtle" "Tattoo of the Valako Shieldbearer"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency->trial->tattoo $tier->t2
	Class == "Stackable Currency"
	BaseType == "Tattoo of the Arohongui Scout" "Tattoo of the Arohongui Warmonger" "Tattoo of the Arohongui Warrior" "Tattoo of the Hinekora Warrior" "Tattoo of the Ngamahu Firewalker" "Tattoo of the Ramako Fleetfoot" "Tattoo of the Tukohama Shaman"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency->trial->tattoo $tier->t3
	Class == "Stackable Currency"
	BaseType == "Tattoo of the Arohongui Moonwarden" "Tattoo of the Hinekora Deathwarden" "Tattoo of the Hinekora Shaman" "Tattoo of the Hinekora Storyteller" "Tattoo of the Hinekora Warmonger" "Tattoo of the Kitava Shaman" "Tattoo of the Ngamahu Shaman" "Tattoo of the Ngamahu Warrior" "Tattoo of the Ngamahu Woodcarver" "Tattoo of the Ramako Archer" "Tattoo of the Ramako Sniper" "Tattoo of the Tukohama Warcaller" "Tattoo of the Valako Scout" "Tattoo of the Valako Shaman" "Tattoo of the Valako Stormrider" "Tattoo of the Valako Warrior"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->currency->trial->tattoo $tier->t4
	Class == "Stackable Currency"
	BaseType == "Tattoo of the Kitava Blood Drinker" "Tattoo of the Kitava Heart Eater" "Tattoo of the Kitava Rebel" "Tattoo of the Kitava Warrior" "Tattoo of the Ramako Scout" "Tattoo of the Rongokurai Brute" "Tattoo of the Rongokurai Goliath" "Tattoo of the Rongokurai Guard" "Tattoo of the Rongokurai Warrior" "Tattoo of the Tasalio Bladedancer" "Tattoo of the Tasalio Scout" "Tattoo of the Tasalio Shaman" "Tattoo of the Tasalio Tideshifter" "Tattoo of the Tasalio Warrior" "Tattoo of the Tawhoa Herbalist" "Tattoo of the Tawhoa Naturalist" "Tattoo of the Tawhoa Scout" "Tattoo of the Tawhoa Shaman" "Tattoo of the Tawhoa Warrior" "Tattoo of the Tukohama Brawler" "Tattoo of the Tukohama Warmonger" "Tattoo of the Tukohama Warrior"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # $type->currency->trial->tattoo $tier->restex
	Class == "Stackable Currency"
	BaseType "Tattoo of"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#------------------------------------

# [4111] Currency with a state - scrying orbs, lens, imprints

#------------------------------------

Show # $type->currency->others $tier->mischigh
	Class == "Stackable Currency"
	BaseType == "Imprint" "Scrying Orb" "Unshaping Orb"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # $type->currency->others $tier->misclow
	Class == "Stackable Currency"
	BaseType == "Facetor's Lens"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

#------------------------------------

# [4112] Wombgifts

#------------------------------------

#Show # $type->exotic->wombgifts $tier->exgiftshigh

# ItemLevel >= 82

# Class == "Wombgifts"

# BaseType == "Ancient Wombgift" "Lavish Wombgift" "Mysterious Wombgift" "Provisioning Wombgift"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 240 90 35 255

# PlayAlertSound 2 300

# PlayEffect Yellow

# MinimapIcon 1 Yellow Circle

#Show # $type->exotic->wombgifts $tier->t2

# Class == "Wombgifts"

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 240 90 35 255

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Circle

Show # %H8 $type->exotic->wombgifts $tier->t3
	Class == "Wombgifts"
	BaseType == "Ancient Wombgift"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->exotic->wombgifts $tier->t4
	Class == "Wombgifts"
	BaseType == "Lavish Wombgift" "Mysterious Wombgift" "Provisioning Wombgift"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

#Show # %H4 $type->exotic->wombgifts $tier->t5

# Class == "Wombgifts"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 210 178 135 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Circle

#===============================================================================================================

# [[4200]] Currency - Splinters

#===============================================================================================================
#------------------------------------

# [4201] Breach and Legion Splinters - stacked

#------------------------------------

# !! Waypoint c9.splinters.all : "Tierlist - Splinters" : "Scarabs and Fragments"

Show # %D6 $type->currency->stackedsplintershigh $tier->t1
	StackSize >= 80
	Class == "Stackable Currency"
	BaseType == "Timeless Eternal Empire Splinter" "Timeless Karui Splinter" "Timeless Maraketh Splinter" "Timeless Templar Splinter" "Timeless Vaal Splinter"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %D6 $type->currency->stackedsplintershigh $tier->t2
	StackSize >= 25
	Class == "Stackable Currency"
	BaseType == "Timeless Eternal Empire Splinter" "Timeless Karui Splinter" "Timeless Maraketh Splinter" "Timeless Templar Splinter" "Timeless Vaal Splinter"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %D6 $type->currency->stackedsplintershigh $tier->t3
	StackSize >= 10
	Class == "Stackable Currency"
	BaseType == "Timeless Eternal Empire Splinter" "Timeless Karui Splinter" "Timeless Maraketh Splinter" "Timeless Templar Splinter" "Timeless Vaal Splinter"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %DS6 $type->currency->stackedsplintershigh $tier->t4
	StackSize >= 5
	Class == "Stackable Currency"
	BaseType == "Timeless Eternal Empire Splinter" "Timeless Karui Splinter" "Timeless Maraketh Splinter" "Timeless Templar Splinter" "Timeless Vaal Splinter"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Show # %DS5 $type->currency->stackedsplintershigh $tier->t5
	StackSize >= 2
	Class == "Stackable Currency"
	BaseType == "Timeless Eternal Empire Splinter" "Timeless Karui Splinter" "Timeless Maraketh Splinter" "Timeless Templar Splinter" "Timeless Vaal Splinter"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 213 159 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

#Show # %D5 $type->currency->stackedsplinterslow $tier->t1

# StackSize >= 66

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 240 90 35 255

# PlayAlertSound 2 300

# PlayEffect Yellow

# MinimapIcon 1 Yellow Circle

#Show # %D5 $type->currency->stackedsplinterslow $tier->t2

# StackSize >= 25

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 249 150 25 255

# PlayAlertSound 2 300

# PlayEffect White

# MinimapIcon 2 White Circle

#Show # %D5 $type->currency->stackedsplinterslow $tier->t3

# StackSize >= 10

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 249 150 25 255

# PlayAlertSound 2 300

# PlayEffect White

# MinimapIcon 2 White Circle

#Show # %DS5 $type->currency->stackedsplinterslow $tier->t4

# StackSize >= 5

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 213 159 0 255

# PlayAlertSound 2 300

# PlayEffect White

# MinimapIcon 2 White Circle

#Show # %DS4 $type->currency->stackedsplinterslow $tier->t5

# StackSize >= 2

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 213 159 0 255

# PlayAlertSound 2 300

# PlayEffect White

# MinimapIcon 2 White Circle

#------------------------------------

# [4202] Breach and Legion Splinters - single

#------------------------------------

Show # %HS4 $type->currency->splinter $tier->t1
	Class == "Stackable Currency"
	BaseType == "Timeless Eternal Empire Splinter" "Timeless Karui Splinter" "Timeless Maraketh Splinter" "Timeless Templar Splinter" "Timeless Vaal Splinter"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 210 20 210 255
	SetBackgroundColor 65 20 80
	PlayAlertSound 2 300
	PlayEffect Purple Temp
	MinimapIcon 1 Grey Kite

#Show # %HS3 $type->currency->splinter $tier->t3

# Class == "Stackable Currency"

# SetFontSize 40

# SetTextColor 255 255 255 255

# SetBorderColor 115 115 115 255

# SetBackgroundColor 65 20 80

# PlayEffect Purple Temp

# MinimapIcon 2 Grey Kite

#------------------------------------

# [4203] Simulacrum Splinters

#------------------------------------

Show # %D6 $type->currency->splinter->simulacrum $tier->t1
	StackSize >= 150
	Class == "Stackable Currency"
	BaseType == "Simulacrum Splinter"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Kite

Show # %D6 $type->currency->splinter->simulacrum $tier->t2
	StackSize >= 60
	Class == "Stackable Currency"
	BaseType == "Simulacrum Splinter"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Kite

Show # %D6 $type->currency->splinter->simulacrum $tier->t3
	StackSize >= 20
	Class == "Stackable Currency"
	BaseType == "Simulacrum Splinter"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 90 35 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Kite

Show # %D6 $type->currency->splinter->simulacrum $tier->t4
	StackSize >= 3
	Class == "Stackable Currency"
	BaseType == "Simulacrum Splinter"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Kite

Show # %H4 $type->currency->splinter->simulacrum $tier->t5
	Class == "Stackable Currency"
	BaseType == "Simulacrum Splinter"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 130 15 255 255
	SetBackgroundColor 65 20 80
	PlayAlertSound 2 300
	PlayEffect Purple Temp
	MinimapIcon 2 Grey Kite

#===============================================================================================================

# [[4300]] Divination Cards

#===============================================================================================================

# !! Waypoint c9.divination.all : "Tierlist - Cards - All" : "Divination Cards"

Show # $type->divination $tier->excustomstack
	StackSize >= 3
	Class == "Divination Cards"
	BaseType == "The Fortunate"
	SetFontSize 45
	SetTextColor 0 0 255 255
	SetBorderColor 0 0 255 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->divination $tier->t1
	Class == "Divination Cards"
	BaseType == "Apocalypse" "Brother's Gift" "Choking Guilt" "Damnation" "Darker Half" "Desecrated Virtue" "Divine Beauty" "Divine Justice" "Father's Love" "Fire Of Unknown Origin" "Gemcutter's Mercy" "History" "House of Mirrors" "I See Brothers" "Last Stand" "Lethean Temptation" "Lonely Warrior" "Love Through Ice" "Lucky Bastion" "Luminous Trove" "Outfoxed" "Pearls Before Swine" "Reflection of the Heart" "Seven Years Bad Luck" "Succor of the Sinless" "The Apothecary" "The Chosen" "The Damned" "The Demon" "The Doctor" "The Dragon's Heart" "The Endless Darkness" "The Enlightened" "The Eye of Terror" "The Fiend" "The Gulf" "The Immortal" "The Insane Cat" "The Mad King" "The Mayor" "The Miracle" "The Nurse" "The Price of Devotion" "The Price of Loyalty" "The Progeny of Lunaris" "The Samurai's Eye" "The Sephirot" "The Slumbering Beast" "The Soul" "Unrequited Love" "Wealth and Power"
	SetFontSize 45
	SetTextColor 0 0 255 255
	SetBorderColor 0 0 255 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->divination $tier->t2
	Class == "Divination Cards"
	BaseType == "Azyran's Reward" "Doryani's Epiphany" "Duality" "Energy Sword" "Friendship" "Home" "Imperfect Memories" "Matryoshka" "Misery in Darkness" "Monochrome" "One Last Score" "Peaceful Moments" "Pride Before the Fall" "Reckless Ambition" "Silence and Frost" "Squandered Prosperity" "The Artist" "The Astromancer" "The Destination" "The Eternal War" "The Everlasting" "The Forbidden Fruit" "The Fortunate" "The Greatest Intentions" "The Heroic Shot" "The Hook" "The Journey" "The Last One Standing" "The Last Supper" "The Leviathan" "The Life Thief" "The Long Con" "The Patient" "The Prince of Darkness" "The Rabbit's Foot" "The Sacrifice" "The Shieldbearer" "The Silly Boy" "The World Eater" "Winter's Embrace"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 0 20 180 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show # %HS6 $type->divination $tier->t3
	Class == "Divination Cards"
	BaseType == "A Fate Worse Than Death" "A Modest Request" "A Stone Perfected" "Altered Perception" "Ambitious Obsession" "Assassin's Gift" "Auspicious Ambitions" "Avian Pursuit" "Beauty Through Death" "Bijoux" "Broken Promises" "Brother's Stash" "Brush, Paint and Palette" "Burning Blood" "Chaotic Disposition" "Costly Curio" "Council of Cats" "Deadly Joy" "Draped in Dreams" "Eternal Bonds" "Fateful Meeting" "Guardian's Challenge" "Hunter's Reward" "Judging Voices" "Keeper's Corruption" "Lachrymal Necrosis" "Lingering Remnants" "Magnum Opus" "Mawr Blaidd" "Merciless Armament" "Pride of the First Ones" "Rebirth and Renewal" "Remembrance" "Something Dark" "Temperance" "Terrible Secret of Space" "The Academic" "The Admirer" "The Aspirant" "The Bitter Blossom" "The Brawny Battle Mage" "The Breach" "The Dreamer" "The Eldritch Decay" "The Enforcer" "The Escape" "The Eye of the Dragon" "The Finishing Touch" "The Fishmonger" "The Formless Sea" "The Garish Power" "The Lake" "The Last Laugh" "The Magma Crab" "The Old Man" "The Poet" "The Polymath" "The Price of Prescience" "The Shepherd's Sandals" "The Shortcut" "The Side Quest" "The Strategist" "The Tumbleweed" "The Vast" "The Void" "The Wedding Gift" "Tranquillity" "Underground Forest" "Who Asked"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 0 220 240 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Triangle

#Show # $type->divination $tier->tnew

# Class == "Divination Cards"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 40 255 217

# PlayAlertSound 2 300

# PlayEffect Yellow

# MinimapIcon 1 Yellow Triangle

# !! Waypoint c9.divination.t4 : "Tierlist - Cards - T4, T4c and lower" : "Divination Cards"

Show # %HS4 $type->divination $tier->t4c
	Class == "Divination Cards"
	BaseType == "A Sea of Blue" "Abandoned Wealth" "Acclimatisation" "Alluring Bounty" "Boon of Justice" "Buried Treasure" "Cameria's Cut" "Checkmate" "Coveted Possession" "Dementophobia" "Demigod's Wager" "Disdain" "Divine Shard" "Emperor's Luck" "Ever-Changing" "Harmony of Souls" "Humility" "Immortal Resolve" "Last Hope" "Lucky Connections" "Lucky Deck" "Man With Bear" "More is Never Enough" "No Traces" "Rebirth" "Sambodhi's Vow" "Society's Remorse" "The Cacophony" "The Card Sharp" "The Doppelganger" "The Ethereal" "The Fool" "The Gemcutter" "The Hoarder" "The Innocent" "The Inventor" "The Price of Protection" "The Rusted Bard" "The Scout" "The Seeker" "The Survivalist" "The Tinkerer's Table" "The Transformation" "The Union" "The White Knight" "The Wrath" "Three Faces in the Dark" "Vanity" "Vinia's Token"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 39 141 192 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Triangle

Show # %D4 $type->divination $tier->exstack
	StackSize >= 3
	Class == "Divination Cards"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 39 141 192 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Triangle

Show # %HS2 $type->divination $tier->t5c
	Class == "Divination Cards"
	BaseType == "Gemcutter's Promise" "Her Mask" "Loyalty" "Rain of Chaos" "Runic Luck" "The Catalyst" "The Deal" "The Flora's Gift" "The Gambler" "The Master Artisan" "The Saint's Treasure" "The Scholar" "The Tireless Extractor" "Three Voices"
	SetFontSize 45
	SetTextColor 39 141 192 255
	SetBorderColor 39 141 192 255
	SetBackgroundColor 20 20 0 255

Show # %HS3 $type->divination $tier->t4
	Class == "Divination Cards"
	BaseType == "A Chilling Wind" "A Dab of Ink" "A Dusty Memory" "A Familiar Call" "Akil's Prophecy" "Anarchy's Price" "Arrogance of the Vaal" "Assassin's Favour" "Astral Protection" "Atziri's Arsenal" "Baited Expectations" "Blind Venture" "Boon of the First Ones" "Bowyer's Dream" "Broken Truce" "Brotherhood in Exile" "Chasing Risk" "Dark Dreams" "Deathly Designs" "Desperate Crusade" "Doedre's Madness" "Dying Anguish" "Dying Light" "Earth Drinker" "Eldritch Perfection" "Emperor of Purity" "Endless Night" "Etched in Blood" "From Bone to Ashes" "Further Invention" "Gift of Asenath" "Gift of the Gemling Queen" "Glimmer of Hope" "Haunting Shadows" "Heterochromia" "Hope" "Hubris" "Hunter's Resolve" "Jack in the Box" "Justified Ambition" "Left to Fate" "Light and Truth" "Lysah's Respite" "Mitts" "Nook's Crown" "Parasitic Passengers" "Perfection" "Poisoned Faith" "Prejudice" "Prometheus' Armoury" "Sambodhi's Wisdom" "Scholar of the Seas" "Shard of Fate" "The Aesthete" "The Archmage's Right Hand" "The Awakened" "The Battle Born" "The Bear Woman" "The Blessing of Moosh" "The Body" "The Bones" "The Brittle Emperor" "The Cache" "The Cataclysm" "The Catch" "The Celestial Justicar" "The Celestial Stone" "The Chains that Bind" "The Coming Storm" "The Craving" "The Cursed King" "The Dapper Prodigy" "The Dark Mage" "The Darkest Dream" "The Deep Ones" "The Dragon" "The Dungeon Master" "The Easy Stroll" "The Encroaching Darkness" "The Endurance" "The Enthusiasts" "The Forgotten Treasure" "The Forward Gaze" "The Fox" "The Gentleman" "The Hale Heart" "The Hive of Knowledge" "The Hunger" "The Jester" "The Jeweller's Boon" "The King's Heart" "The Lion" "The Long Watch" "The Mercenary" "The Messenger" "The Mind's Eyes" "The Mountain" "The Offering" "The Offspring" "The One That Got Away" "The One With All" "The Opulent" "The Pact" "The Penitent" "The Porcupine" "The Primordial" "The Professor" "The Queen" "The Realm" "The Risk" "The Rite of Elements" "The Road to Power" "The Spark and the Flame" "The Stormcaller" "The Thaumaturgist" "The Throne" "The Tower" "The Traitor" "The Twilight Moon" "The Tyrant" "The Undaunted" "The Undisputed" "The Unexpected Prize" "The Valkyrie" "The Warlord" "The Whiteout" "The Wilted Rose" "The Wolf" "The Wolf's Legacy" "The Wolven King's Bite" "The Wolverine" "The Wretched" "Time-Lost Relic" "Toxic Tidings" "Triskaidekaphobia" "Unchained" "Void of the Elements" "When Currents Blaze"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 39 141 192 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Triangle

Hide # %H0 $type->divination $tier->t5
	Class == "Divination Cards"
	BaseType == "A Mother's Parting Gift" "A Note in the Wind" "Alivia's Grace" "Alone in the Darkness" "Audacity" "Azure Rage" "Bound by Flame" "Boundless Realms" "Call to the First Ones" "Cartographer's Delight" "Cursed Words" "Dark Temptation" "Death" "Destined to Crumble" "Dialla's Subjugation" "Echoes of Love" "Forbidden Power" "Grave Knowledge" "Imperial Legacy" "Lantador's Lost Love" "Lost Worlds" "Might is Right" "Prosperity" "Rain Tempter" "Rats" "Struck by Lightning" "The Adventuring Spirit" "The Arena Champion" "The Army of Blood" "The Avenger" "The Beast" "The Betrayal" "The Blazing Fire" "The Calling" "The Carrion Crow" "The Conduit" "The Deceiver" "The Demoness" "The Dreamland" "The Drunken Aristocrat" "The Explorer" "The Fathomless Depths" "The Feast" "The Fletcher" "The Forsaken" "The Fox in the Brambles" "The Gladiator" "The Golden Era" "The Harvester" "The Hermit" "The Incantation" "The Inoculated" "The Insatiable" "The Journalist" "The King's Blade" "The Lich" "The Lord in Black" "The Lord of Celebration" "The Lover" "The Lunaris Priestess" "The Metalsmith's Gift" "The Oath" "The Pack Leader" "The Rabid Rhoa" "The Return of the Rat" "The Ruthless Ceinture" "The Scarred Meadow" "The Scavenger" "The Sigil" "The Siren" "The Skeleton" "The Spoiled Prince" "The Standoff" "The Summoner" "The Sun" "The Surgeon" "The Surveyor" "The Sword King's Salute" "The Trial" "The Twins" "The Visionary" "The Warden" "The Watcher" "The Web" "The Wind" "The Witch" "The Wolf's Shadow" "Thirst for Knowledge" "Thunderous Skies" "Treasure Hunter" "Turn the Other Cheek" "Vile Power" "Volatile Power"
	SetFontSize 35
	SetTextColor 39 141 192 255
	SetBorderColor 39 141 192 255
	SetBackgroundColor 20 20 0 255

Show # $type->divination $tier->restex
	Class == "Divination Cards"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#===============================================================================================================

# [[4400]] Remaining Currency

#===============================================================================================================

#Hide # $type->currency $tier->untiereditems

# Class == "Stackable Currency"

# SetFontSize 35

# SetBorderColor 0 0 0

Hide # $type->currency $tier->scrollfragments
	Class == "Stackable Currency"
	BaseType == "Scroll Fragment"
	SetFontSize 35
	SetBorderColor 0 0 0

Show # $type->currency $tier->restex
	Class == "Stackable Currency"
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#===============================================================================================================

# [[4500]] Questlike-Items1 (override uniques)

#===============================================================================================================

# !! Waypoint c9.metamorph.all : "Heist Targets"

Show # $type->heisttarget $tier->any
	Class == "Heist Targets"
	SetFontSize 45
	SetTextColor 74 230 58 255
	SetBorderColor 74 230 58 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 0 Green Pentagon

#===============================================================================================================

# [[4600]] Enshrouded Items

#===============================================================================================================

Show # $type->enshrouded $tier->enshroudedgear
	BaseType == "Enshrouded Body Armour" "Enshrouded Boots" "Enshrouded Gloves" "Enshrouded Helmet" "Enshrouded Shield"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

#===============================================================================================================

# [[4700]] Idols (Event Leagues Only)

#===============================================================================================================

# 1x3 Idols

Show # %H6 $type->event->idols $tier->minorrare
	Rarity Rare
	BaseType == "Minor Idol"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 120 200 160 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Moon

Show # %H4 $type->event->idols $tier->minormagic
	Rarity Magic
	BaseType == "Minor Idol"
	SetFontSize 45
	SetTextColor 120 200 160 255
	SetBorderColor 120 200 160 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Moon

# 1x2 Idols

Show # %H6 $type->event->idols $tier->kamasanrare
	Rarity Rare
	BaseType == "Kamasan Idol"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 120 200 160 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Moon

Show # %H4 $type->event->idols $tier->kamasanmagic
	Rarity Magic
	BaseType == "Kamasan Idol"
	SetFontSize 45
	SetTextColor 120 200 160 255
	SetBorderColor 120 200 160 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Moon

# 1x3 Idols

Show # %H6 $type->event->idols $tier->totemicrare
	Rarity Rare
	BaseType == "Totemic Idol"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 120 200 160 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Moon

Show # %H4 $type->event->idols $tier->totemicmagic
	Rarity Magic
	BaseType == "Totemic Idol"
	SetFontSize 45
	SetTextColor 120 200 160 255
	SetBorderColor 120 200 160 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Moon

# 2x1 Idols

Show # %H6 $type->event->idols $tier->noblerare
	Rarity Rare
	BaseType == "Noble Idol"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 120 200 160 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Moon

Show # %H4 $type->event->idols $tier->noblemagic
	Rarity Magic
	BaseType == "Noble Idol"
	SetFontSize 45
	SetTextColor 120 200 160 255
	SetBorderColor 120 200 160 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Moon

# 3x1 Idols

Show # %H6 $type->event->idols $tier->burialrare
	Rarity Rare
	BaseType == "Burial Idol"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 120 200 160 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Moon

Show # %H5 $type->event->idols $tier->burialmagic
	Rarity Magic
	BaseType == "Burial Idol"
	SetFontSize 45
	SetTextColor 120 200 160 255
	SetBorderColor 120 200 160 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Moon

# 2x2 Idols

Show # %H6 $type->event->idols $tier->conquerorrare
	Rarity Rare
	BaseType == "Conqueror Idol"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 120 200 160 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Moon

Show # %H5 $type->event->idols $tier->conquerormagic
	Rarity Magic
	BaseType == "Conqueror Idol"
	SetFontSize 45
	SetTextColor 120 200 160 255
	SetBorderColor 120 200 160 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Moon

# These should not exist

Show # $type->event->idols $tier->normalidols
	Rarity Normal
	Class == "Idols"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#===============================================================================================================

# [[4800]] Uniques

#===============================================================================================================

# !! Waypoint c10.uniques.all : "Tierlist - Uniques - All Tiering + Exceptions" : "Uniques"

#------------------------------------

# [4801] Exceptions #1

#------------------------------------

Show # $type->uniques $tier->exuberimpresence
	HasInfluence "Shaper"
	HasInfluence "Elder"
	Rarity Unique
	BaseType == "Onyx Amulet"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->uniques $tier->exkaom
	Sockets < 1
	Rarity Unique
	BaseType == "Glorious Plate"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

Show # $type->uniques $tier->extabula
	LinkedSockets 6
	Rarity Unique
	BaseType == "Simple Robe"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

Show # $type->uniques $tier->exforgesword
	HasInfluence "Elder" "Shaper"
	Rarity Unique
	BaseType == "Infernal Sword"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->uniques $tier->exrationaljewel
	SynthesisedItem True
	Rarity Unique
	BaseType == "Cobalt Jewel"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->uniques $tier->exsynth
	SynthesisedItem True
	Rarity Unique
	BaseType == "Amethyst Ring" "Iron Ring" "Prismatic Ring" "Ruby Ring" "Sapphire Ring" "Topaz Ring"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

Show # $type->uniques $tier->ex6link
	LinkedSockets 6
	Rarity Unique
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

Show # $type->uniques $tier->4xabysshelmet
	Sockets >= AAAA
	Rarity Unique
	BaseType == "Bone Circlet"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->uniques $tier->3xabyss
	Sockets >= AAA
	Rarity Unique
	BaseType == "Carnal Armour"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

#------------------------------------

# [4802] Tier 1 and 2 uniques

#------------------------------------

# !! Waypoint c10.uniques.t1 : "Tierlist - Uniques - All tiering" : "Uniques"

Show # $type->uniques $tier->t1
	Rarity Unique
	BaseType == "Assembled Eye Jewel" "Astrolabe Amulet" "Blood Sceptre" "Cabalist Regalia" "Candlestick Relic" "Censer Relic" "Champion Kite Shield" "Crusader Boots" "Desert Brigandine" "Dusk Blade" "Engraved Greatsword" "Faithful Helmet" "Faun's Horn" "Fishing Rod" "Fleshripper" "Fluted Bascinet" "Formless Ring" "Foul Staff" "Fugitive Ring" "Ghastly Eye Jewel" "Girded Tower Shield" "Gold Flask" "Golden Buckler" "Greatwolf Talisman" "Imperial Maul" "Iron Flask" "Jingling Spirit Shield" "Karui Maul" "Lacewood Spirit Shield" "Large Cluster Jewel" "Maple Round Shield" "Murderous Eye Jewel" "Painted Tower Shield" "Papyrus Relic" "Pearlescent Amulet" "Prismatic Jewel" "Processional Relic" "Rawhide Boots" "Rhex Talisman" "Ring" "Riveted Boots" "Ruby Flask" "Runic Gages" "Runic Helm" "Savant's Robe" "Seaglass Amulet" "Siege Axe" "Siege Helmet" "Slaughter Knife" "Steel Kite Shield" "Unset Amulet" "Vaal Rapier" "Vermillion Ring" "Void Axe" "Wyrmscale Doublet"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->uniques $tier->t2
	Rarity Unique
	BaseType == "Antique Gauntlets" "Assassin's Garb" "Black Maw Talisman" "Blood Raiment" "Butcher Axe" "Carnal Boots" "Colosseum Plate" "Coronal Maul" "Crimson Round Shield" "Deicide Mask" "Devout Chainmail" "Exquisite Blade" "Ezomyte Spiked Shield" "Fingerless Silk Gloves" "Full Wyrmscale" "General's Brigandine" "Gladiator Plate" "Goliath Greaves" "Highborn Staff" "Hydrascale Gauntlets" "Imperial Bow" "Jewelled Foil" "Karui Chopper" "Leviathan Greaves" "Lich's Circlet" "Magistrate Crown" "Maraketh Bow" "Martyr Gloves" "Medium Cluster Jewel" "Murder Mitts" "Occultist's Vestment" "Ornate Quiver" "Paladin Crown" "Pig-Faced Bascinet" "Piledriver" "Prophecy Wand" "Quarterstaff" "Raven Mask" "Reaver Helmet" "Reinforced Greaves" "Riveted Gloves" "Royal Burgonet" "Runic Crown" "Runic Gauntlets" "Runic Sabatons" "Runic Sollerets" "Sacrificial Garb" "Scholar's Robe" "Silk Gloves" "Simple Robe" "Slink Boots" "Somatic Wand" "Sorcerer Boots" "Spectral Axe" "Steel Circlet" "Steel Ring" "Synaptic Ring" "Timeless Jewel" "Titanium Spirit Shield" "Torturer Garb" "Trapper Boots" "Vaal Gauntlets" "Vaal Hatchet" "Vaal Spirit Shield" "Velour Boots" "Visored Sallet" "Warlock Boots" "Waxed Garb" "Wolf Alpha Talisman" "Wyrmscale Boots" "Zodiac Leather"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

#------------------------------------

# [4803] Exceptions #2

#------------------------------------

# !! Waypoint c10.uniques.undert1t2 : "Tierlist - Uniques - All tiering, except T1 and T2" : "Uniques"

Show # %D9 $type->uniques $tier->vestige
	Vestigial True
	Rarity Unique
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 210 20 210 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Purple
	MinimapIcon 1 Purple Star

Show # $type->uniques $tier->exuniqueidols
	Rarity Unique
	Class == "Idols"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # $type->uniques $tier->2xcorrupteduniques
	Corrupted True
	CorruptedMods >= 2
	Rarity Unique
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 120 0 0 240
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Blue
	MinimapIcon 0 Blue Star

Show # $type->uniques $tier->2xabyss
	Sockets >= AA
	Rarity Unique
	BaseType == "Great Crown" "Mind Cage" "Murder Boots" "Riveted Gloves" "Steelscale Gauntlets"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

Show # $type->uniques $tier->excrucibleunique
	HasCruciblePassiveTree True
	Rarity Unique
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

#------------------------------------

# [4804] Multi-Unique bases.

#------------------------------------

Show # $type->uniques $tier->multispecialhigh
	Rarity Unique
	BaseType == "Amethyst Flask" "Assassin's Boots" "Cloth Belt" "Coffer Relic" "Elegant Round Shield" "Heavy Belt" "Hellion's Paw" "Hypnotic Eye Jewel" "Imperial Skean" "Imperial Staff" "Leather Belt" "Paua Amulet" "Searching Eye Jewel" "Small Cluster Jewel" "Spine Bow" "Vaal Blade" "Vaal Claw"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

#Show # $type->uniques $tier->exdust1

# Rarity Unique

# BaseType == "Arcanist Gloves" "Arcanist Slippers" "Crystal Belt" "Deerskin Gloves" "Deicide Mask" "Demon Dagger" "Diamond Ring" "Eternal Sword" "Ezomyte Dagger" "Fiend Dagger" "Glorious Plate" "Harlequin Mask" "Jewelled Foil" "Lacquered Buckler" "Lion Pelt" "Marble Amulet" "Mind Cage" "Omen Wand" "Ornate Quiver" "Prismatic Ring" "Sadist Garb" "Sinner Tricorne" "Sorcerer Boots" "Titanium Spirit Shield" "Two-Point Arrow Quiver" "Two-Toned Boots" "Vaal Gauntlets" "Widowsilk Robe"

# SetFontSize 45

# SetTextColor 175 96 37 255

# SetBorderColor 175 96 37 255

# SetBackgroundColor 10 30 45 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Star

#Show # $type->uniques $tier->exdust2

# Rarity Unique

# BaseType == "Ambusher" "Archon Kite Shield" "Assassin's Garb" "Baroque Round Shield" "Black Maw Talisman" "Branded Kite Shield" "Carnal Sceptre" "Conjurer Boots" "Conjurer Gloves" "Corsair Sword" "Desert Brigandine" "Destiny Leather" "Dragonscale Gauntlets" "Eelskin Gloves" "Elegant Round Shield" "Embroidered Gloves" "Enameled Buckler" "Exquisite Leather" "Full Dragonscale" "Full Wyrmscale" "Gilded Sallet" "Gold Amulet" "Infernal Axe" "Ironwood Buckler" "Lathi" "Legion Gloves" "Lion Sword" "Meatgrinder" "Midnight Blade" "Mosaic Kite Shield" "Necromancer Silks" "Nightmare Bascinet" "Nubuck Gloves" "Platinum Sceptre" "Primal Arrow Quiver" "Ranger Bow" "Reaver Helmet" "Regicide Mask" "Royal Axe" "Royal Sceptre" "Royal Skean" "Serpentscale Boots" "Serpentscale Gauntlets" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Sharkskin Tunic" "Slink Gloves" "Soldier Boots" "Spike-Point Arrow Quiver" "Steel Circlet" "Steel Gauntlets" "Supreme Spiked Shield" "Terror Claw" "Throat Stabber" "Titan Gauntlets" "Tomahawk" "Trapper Boots" "Two-Stone Ring" "Vaal Buckler" "Vaal Hatchet" "Wyrmscale Gauntlets"

# SetFontSize 45

# SetTextColor 175 96 37 255

# SetBorderColor 175 96 37 255

# SetBackgroundColor 10 30 45 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Star

#Show # $type->uniques $tier->exdust3

# Rarity Unique

# BaseType == "Abyssal Axe" "Ancient Greaves" "Ancient Spirit Shield" "Antique Greaves" "Auric Mace" "Aventail Helmet" "Boot Blade" "Brass Spirit Shield" "Bronzescale Boots" "Chain Belt" "Chiming Spirit Shield" "Citadel Bow" "Clasped Mitts" "Close Helmet" "Compound Spiked Shield" "Conquest Chainmail" "Corrugated Buckler" "Crusader Chainmail" "Cutthroat's Garb" "Destroyer Regalia" "Dread Maul" "Eelskin Boots" "Elder Sword" "Estoc" "Ezomyte Axe" "Ezomyte Blade" "Flaying Knife" "Fright Claw" "Golden Mask" "Graceful Sword" "Gut Ripper" "Harbinger Bow" "Heavy Arrow Quiver" "Holy Chainmail" "Karui Chopper" "Laminated Kite Shield" "Leather Cap" "Lunaris Circlet" "Maple Round Shield" "Mesh Gloves" "Military Staff" "Nubuck Boots" "Opal Sceptre" "Ornate Mace" "Ornate Ringmail" "Platinum Kris" "Polished Spiked Shield" "Reaver Sword" "Ritual Sceptre" "Samite Gloves" "Samnite Helmet" "Satin Gloves" "Scholar Boots" "Secutor Helm" "Shackled Boots" "Spiraled Wand" "Tarnished Spirit Shield" "Teak Round Shield" "Terror Maul" "Thresher Claw" "Timeworn Claw" "Tricorne" "Twilight Blade" "Tyrant's Sekhem" "Ursine Pelt" "Vile Arrow Quiver" "Vile Staff" "War Buckler"

# SetFontSize 45

# SetTextColor 175 96 37 255

# SetBorderColor 175 96 37 255

# SetBackgroundColor 10 30 45 255

# PlayAlertSound 3 300

# PlayEffect Purple

# MinimapIcon 1 Purple Star

Show # %D9 $type->uniques $tier->foulborn
	Foulborn True
	Rarity Unique
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 210 20 210 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Purple
	MinimapIcon 1 Purple Star

Show # %H7 $type->uniques $tier->multispecial
	Rarity Unique
	BaseType == "Abyssal Axe" "Agate Amulet" "Amethyst Ring" "Ancient Gauntlets" "Ancient Greaves" "Archon Kite Shield" "Assassin Bow" "Blunt Arrow Quiver" "Callous Mask" "Coral Amulet" "Coral Ring" "Crusader Plate" "Crystal Sceptre" "Ebony Tower Shield" "Eternal Sword" "Exquisite Leather" "Fiend Dagger" "Gavel" "Goathide Boots" "Gold Ring" "Golden Mask" "Granite Flask" "Iron Circlet" "Karui Sceptre" "Lacquered Buckler" "Lacquered Garb" "Legion Sword" "Midnight Blade" "Moonstone Ring" "Necromancer Silks" "Nightmare Bascinet" "Onyx Amulet" "Prophet Crown" "Quartz Flask" "Sadist Garb" "Sage Wand" "Saint's Hauberk" "Shadow Sceptre" "Solaris Circlet" "Spidersilk Robe" "Stealth Boots" "Stibnite Flask" "Studded Belt" "Terror Claw" "Topaz Ring" "Turquoise Amulet" "Two-Point Arrow Quiver" "Two-Stone Ring" "Unset Ring" "Vanguard Belt" "Widowsilk Robe" "Zealot Gloves"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # %D5 $type->uniques $tier->overqual
	Quality >= 27
	Rarity Unique
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # %D4 $type->uniques $tier->5link
	LinkedSockets 5
	Rarity Unique
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # %D4 $type->uniques $tier->6s
	Sockets >= 6
	Rarity Unique
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Star

#------------------------------------

# [4805] Low tier exceptions

#------------------------------------

# !! Waypoint c10.uniques.low : "Tierlist - Uniques - C Tier, Boss-Tier and lower" : "Uniques"

#Show # %H5 $type->uniques $tier->earlyleague

# Rarity Unique

# SetFontSize 45

# SetTextColor 175 96 37 255

# SetBorderColor 175 96 37 255

# SetBackgroundColor 10 30 45 255

# PlayAlertSound 3 300

# PlayEffect Brown

# MinimapIcon 2 Brown Star

#Show # $type->uniques $tier->recipeuniquerings

# Rarity Unique

# Class == "Rings"

# SetFontSize 45

# SetTextColor 175 96 37 255

# SetBorderColor 0 240 190 255

# SetBackgroundColor 53 13 13 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 2 Blue Star

Show # $type->uniques $tier->exjewelscorrupted
	Corrupted True
	CorruptedMods 0
	Rarity Unique
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # $type->uniques $tier->exjewels
	Rarity Unique
	BaseType == "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 175 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

#Show # $type->uniques $tier->highvinktar

# ItemLevel >= 82

# Rarity Unique

# BaseType == "Imperial Staff"

# SetFontSize 45

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 175 96 37 255

# PlayAlertSound 2 300

# PlayEffect Yellow

# MinimapIcon 1 Brown Star

Show # %D5 $type->uniques $tier->corrupteduniques
	Corrupted True
	CorruptedMods >= 1
	Rarity Unique
	Class == "Amulets" "Belts" "Boots" "Gloves" "Helmets" "Quivers" "Rings" "Shields"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 120 0 0 240
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Star

#------------------------------------

# [4806] Tier 3 uniques

#------------------------------------

Show # %H5 $type->uniques $tier->t3boss
	Rarity Unique
	BaseType == "Amber Amulet" "Ambush Mitts" "Ancient Spirit Shield" "Assassin's Mitts" "Bismuth Flask" "Bone Circlet" "Broadhead Arrow Quiver" "Cardinal Round Shield" "Carnal Armour" "Carnal Mitts" "Citadel Bow" "Coiled Staff" "Colossal Mana Flask" "Colossal Tower Shield" "Crusader Gloves" "Cryonic Ring" "Cutlass" "Dragonscale Boots" "Enthalpic Ring" "Ezomyte Burgonet" "Ezomyte Staff" "Ezomyte Tower Shield" "Fugitive Boots" "Gladius" "Golden Plate" "Goliath Gauntlets" "Great Crown" "Harlequin Mask" "Hubris Circlet" "Hydrascale Boots" "Infernal Sword" "Jade Amulet" "Judgement Staff" "Lacquered Helmet" "Lapis Amulet" "Legion Gloves" "Lion Sword" "Maelström Staff" "Marble Amulet" "Mind Cage" "Mirrored Spiked Shield" "Murder Boots" "Necromancer Circlet" "Nightmare Mace" "Opal Ring" "Opal Wand" "Organic Ring" "Praetor Crown" "Primordial Staff" "Prismatic Ring" "Ranger Bow" "Ruby Ring" "Sapphire Flask" "Sapphire Ring" "Sentinel Jacket" "Serpentine Staff" "Silken Hood" "Silver Flask" "Soldier Gloves" "Spiked Gloves" "Spiny Round Shield" "Steelscale Gauntlets" "Steelwood Bow" "Stygian Vise" "Sulphur Flask" "Tome Relic" "Topaz Flask" "Tornado Wand" "Triumphant Lamellar" "Urn Relic" "Vaal Axe" "Vaal Greaves" "Vaal Mask" "Vaal Regalia" "Vaal Sceptre" "Varnished Coat" "Vile Arrow Quiver" "Void Sceptre"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Star

Show # %H4 $type->uniques $tier->t3
	Rarity Unique
	BaseType == "Astral Plate" "Baroque Round Shield" "Blue Pearl Amulet" "Bone Helmet" "Branded Kite Shield" "Citrine Amulet" "Conjurer Boots" "Crude Bow" "Crystal Belt" "Deerskin Gloves" "Demon Dagger" "Embroidered Gloves" "Festival Mask" "Ghostflame Blade" "Glorious Plate" "Goat's Horn" "Graceful Sword" "Great Mallet" "Hallowed Hybrid Flask" "Harmonic Spirit Shield" "Iron Ring" "Lathi" "Leather Cap" "Leather Hood" "Legion Boots" "Majestic Plate" "Meatgrinder" "Mesh Gloves" "Mosaic Kite Shield" "Nailed Fist" "Omen Wand" "Pagan Wand" "Paua Ring" "Pinnacle Tower Shield" "Prismatic Tincture" "Rawhide Tower Shield" "Regicide Mask" "Ritual Sceptre" "Saintly Chainmail" "Satin Gloves" "Serpentscale Gauntlets" "Sharktooth Arrow Quiver" "Shield Crab Talisman" "Short Bow" "Sinner Tricorne" "Two-Toned Boots" "Wool Shoes" "Zealot Helmet"
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 2 Brown Star

#------------------------------------

# [4807] Tier 4 uniques

#------------------------------------

Show # %H3 $type->uniques $tier->hideable2
	Rarity Unique
	BaseType == "Despot Axe" "Elegant Ringmail" "Elegant Sword" "Nameless Ring" "Platinum Sceptre" "Rustic Sash" "Sovereign Spiked Shield" "Tyrant's Sekhem"
	SetFontSize 40
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 2 Brown Star

Show # %H3 $type->uniques $tier->hideable
	Rarity Unique
	BaseType == "Ambusher" "Antique Greaves" "Antique Rapier" "Arcanist Gloves" "Arcanist Slippers" "Ashbark Tincture" "Auric Mace" "Aventail Helmet" "Awl" "Barbute Helmet" "Basket Rapier" "Bastard Sword" "Blasting Wand" "Blazing Arrow Quiver" "Bone Armour" "Boot Blade" "Boot Knife" "Brass Maul" "Brass Spirit Shield" "Bronze Gauntlets" "Bronze Sceptre" "Bronzescale Boots" "Bronzescale Gauntlets" "Buckskin Tunic" "Calling Wand" "Carnal Sceptre" "Cedar Tower Shield" "Chain Belt" "Chain Gloves" "Chiming Spirit Shield" "Clasped Boots" "Clasped Mitts" "Cleaver" "Close Helmet" "Compound Spiked Shield" "Conjurer Gloves" "Conquest Chainmail" "Copper Plate" "Corrugated Buckler" "Corsair Sword" "Crusader Chainmail" "Cutthroat's Garb" "Death Bow" "Decimation Bow" "Decorative Axe" "Deerskin Boots" "Destiny Leather" "Destroyer Regalia" "Diamond Flask" "Diamond Ring" "Dragonscale Gauntlets" "Dread Maul" "Dream Mace" "Driftwood Wand" "Eelskin Boots" "Eelskin Gloves" "Elder Sword" "Enameled Buckler" "Estoc" "Etched Greatsword" "Eternal Burgonet" "Ezomyte Axe" "Ezomyte Blade" "Ezomyte Dagger" "Feathered Arrow Quiver" "Flaying Knife" "Fright Claw" "Full Dragonscale" "Gemstone Sword" "Gilded Sallet" "Gnarled Branch" "Goathide Gloves" "Gold Amulet" "Grand Mana Flask" "Great Helmet" "Greater Mana Flask" "Grinning Fetish" "Gut Ripper" "Harbinger Bow" "Headsman Axe" "Heavy Arrow Quiver" "Highland Blade" "Holy Chainmail" "Imperial Claw" "Infernal Axe" "Iron Gauntlets" "Iron Hat" "Iron Mask" "Iron Staff" "Ironscale Boots" "Ironscale Gauntlets" "Ironwood Buckler" "Ironwood Tincture" "Jade Hatchet" "Jagged Foil" "Jagged Maul" "Jasper Chopper" "Kinetic Wand" "Laminated Kite Shield" "Large Hybrid Flask" "Latticed Ringmail" "Lion Pelt" "Long Bow" "Lunaris Circlet" "Mesh Boots" "Military Staff" "Nubuck Boots" "Nubuck Gloves" "Oakbranch Tincture" "Opal Sceptre" "Ornate Mace" "Ornate Ringmail" "Ornate Sword" "Painted Buckler" "Penetrating Arrow Quiver" "Pine Buckler" "Plague Mask" "Plank Kite Shield" "Plate Vest" "Plated Greaves" "Platinum Kris" "Poleaxe" "Polished Spiked Shield" "Primal Arrow Quiver" "Quicksilver Flask" "Reaver Sword" "Recurve Bow" "Reinforced Tower Shield" "Rock Breaker" "Rotted Round Shield" "Royal Axe" "Royal Bow" "Royal Sceptre" "Royal Skean" "Royal Staff" "Rusted Sword" "Sabre" "Sage's Robe" "Samite Gloves" "Samnite Helmet" "Sanctified Life Flask" "Sanctified Mana Flask" "Satin Slippers" "Scholar Boots" "Secutor Helm" "Serpentscale Boots" "Serrated Arrow Quiver" "Shackled Boots" "Shadow Axe" "Shagreen Boots" "Shagreen Gloves" "Sharkskin Boots" "Sharkskin Tunic" "Silk Slippers" "Silken Vest" "Skinning Knife" "Sledgehammer" "Slink Gloves" "Soldier Boots" "Soldier Helmet" "Spike-Point Arrow Quiver" "Spiked Club" "Spiraled Wand" "Sporebloom Tincture" "Steel Gauntlets" "Steelhead" "Stiletto" "Strapped Boots" "Strapped Mitts" "Studded Round Shield" "Sun Leather" "Supreme Spiked Shield" "Tarnished Spirit Shield" "Teak Round Shield" "Terror Maul" "Thresher Claw" "Throat Stabber" "Tiger Sword" "Timeworn Claw" "Titan Gauntlets" "Titan Greaves" "Tomahawk" "Tribal Circlet" "Tricorne" "Twilight Blade" "Ursine Pelt" "Vaal Buckler" "Velvet Gloves" "Velvet Slippers" "Vile Staff" "Vine Circlet" "War Buckler" "War Hammer" "War Sword" "Whalebone Rapier" "Wild Leather" "Wolf Pelt" "Woodsplitter" "Wool Gloves" "Wrapped Mitts" "Wyrmscale Gauntlets"
	SetFontSize 40
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 2 Brown Star

Show # $type->uniques $tier->restex
	Rarity Unique
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle

#===============================================================================================================

# [[4900]] Questlike-Items2

#===============================================================================================================

Show # $type->questlike $tier->invitations
	BaseType "Maven's"
	SetFontSize 45
	SetTextColor 74 230 58 255
	SetBorderColor 74 230 58 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 0 Green Pentagon

Show # $type->questlike $tier->labyrinthconsumable
	Class == "Labyrinth Items" "Labyrinth Trinkets"
	SetFontSize 45
	SetTextColor 74 230 58 255
	SetBorderColor 74 230 58 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 0 Green Pentagon

Show # $type->questlike $tier->incursionconsumable
	Class == "Incursion Items"
	SetFontSize 45
	SetTextColor 74 230 58 255
	SetBorderColor 74 230 58 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 0 Green Pentagon

#===============================================================================================================

# [[5000]] Hide outdated leveling flasks

#===============================================================================================================

# !! Waypoint c11.leveling.all : "Leveling - ALL rules" : "Leveling"

Hide # $type->hidelayer $tier->outdatedlevelflaska
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Large" "Medium" "Small"
	AreaLevel >= 15
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # $type->hidelayer $tier->outdatedlevelflaskb
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Grand" "Greater"
	AreaLevel >= 30
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # $type->hidelayer $tier->outdatedlevelflaskc
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Colossal" "Giant" "Sacred"
	AreaLevel >= 48
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # $type->hidelayer $tier->outdatedlevelflaskd
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Hallowed" "Sanctified"
	AreaLevel >= 60
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

#===============================================================================================================

# [[5100]] Leveling - Utility Flasks and Tinctures

#===============================================================================================================

# !! Waypoint c11.leveling.utilflasks : "Leveling - Utility flasks and Quality Flasks" : "Leveling"

Show # $type->leveling->flasks->utility $tier->quicksilver
	BaseType == "Quicksilver Flask"
	SetFontSize 45
	SetTextColor 50 200 125
	SetBorderColor 50 200 125
	SetBackgroundColor 25 100 75
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 1 Yellow Raindrop

Show # $type->leveling->flasks->utility $tier->asortedutility
	BaseType == "Amethyst Flask" "Basalt Flask" "Bismuth Flask" "Diamond Flask" "Gold Flask" "Granite Flask" "Iron Flask" "Jade Flask" "Quartz Flask" "Quicksilver Flask" "Ruby Flask" "Sapphire Flask" "Silver Flask" "Stibnite Flask" "Sulphur Flask" "Topaz Flask"
	SetFontSize 45
	SetBorderColor 50 200 125
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp
	MinimapIcon 2 Grey Raindrop

Show # %H3 $type->leveling->flasks->utility $tier->any
	Class == "Utility Flasks"
	SetFontSize 40
	SetBorderColor 0 0 0 255
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp

Show # %D3 $type->leveling->flasks->quality $tier->max
	Quality >= 20
	Rarity Normal
	Class == "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Tinctures" "Utility Flasks"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 155 138 138 255
	PlayEffect Grey Temp

#Show # %D1 $type->leveling->flasks->quality $tier->high

# Quality >= 14

# Rarity Normal Magic

# Class == "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Tinctures" "Utility Flasks"

# SetFontSize 40

# SetTextColor 0 0 0 255

# SetBorderColor 200 200 200 255

# SetBackgroundColor 130 110 110 255

#Show # %D0 $type->leveling->flasks->quality $tier->any

# Quality >= 1

# Rarity Normal Magic

# Class == "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Tinctures" "Utility Flasks"

# SetFontSize 35

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 130 110 110 255

Show # $type->leveling->tincture $tier->any
	ItemLevel <= 67
	Class == "Tinctures"
	SetFontSize 45
	SetBorderColor 50 200 125
	SetBackgroundColor 25 100 75
	PlayEffect Grey Temp
	MinimapIcon 2 Grey Raindrop

#===============================================================================================================

# [[5200]] Leveling - Life, Mana, Hybrid

#===============================================================================================================
#------------------------------------

# [5201] Hybrid Flasks

#------------------------------------

# !! Waypoint c11.leveling.lifeflasks : "Leveling - life and mana flasks" : "Leveling"

Hide # %H2 $type->leveling->flasks->hybrid $tier->t1
	Class == "Hybrid Flasks"
	BaseType "Small"
	AreaLevel <= 20
	SetFontSize 40
	SetBorderColor 100 0 100

Hide # %H2 $type->leveling->flasks->hybrid $tier->t2
	Class == "Hybrid Flasks"
	BaseType "Medium"
	AreaLevel <= 30
	SetFontSize 40
	SetBorderColor 100 0 100

Hide # %H2 $type->leveling->flasks->hybrid $tier->t3
	Class == "Hybrid Flasks"
	BaseType "Large"
	AreaLevel <= 40
	SetFontSize 40
	SetBorderColor 100 0 100

Hide # %H2 $type->leveling->flasks->hybrid $tier->t4
	Class == "Hybrid Flasks"
	BaseType "Colossal"
	AreaLevel <= 50
	SetFontSize 40
	SetBorderColor 100 0 100

Hide # %H2 $type->leveling->flasks->hybrid $tier->t5
	Class == "Hybrid Flasks"
	BaseType "Sacred"
	AreaLevel <= 60
	SetFontSize 40
	SetBorderColor 100 0 100

Hide # %H2 $type->leveling->flasks->hybrid $tier->t6
	Class == "Hybrid Flasks"
	BaseType "Hallowed"
	AreaLevel <= 67
	SetFontSize 40
	SetBorderColor 100 0 100

#------------------------------------

# [5202] Life flasks

#------------------------------------

Show # $type->leveling->flasks->life $tier->t1
	Class == "Life Flasks"
	BaseType "Small"
	AreaLevel <= 9
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t2
	Class == "Life Flasks"
	BaseType "Medium"
	AreaLevel <= 13
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t3
	Class == "Life Flasks"
	BaseType "Large"
	AreaLevel <= 17
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t4
	Class == "Life Flasks"
	BaseType "Greater"
	AreaLevel <= 19
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t5
	Class == "Life Flasks"
	BaseType "Grand"
	AreaLevel <= 25
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t6
	Class == "Life Flasks"
	BaseType "Giant"
	AreaLevel <= 31
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t7
	Class == "Life Flasks"
	BaseType "Colossal"
	AreaLevel <= 37
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t8
	Class == "Life Flasks"
	BaseType "Sacred"
	AreaLevel <= 43
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t9
	Class == "Life Flasks"
	BaseType "Hallowed"
	AreaLevel <= 51
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t10
	Class == "Life Flasks"
	BaseType "Sanctified"
	AreaLevel <= 60
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t11
	Class == "Life Flasks"
	BaseType "Divine"
	AreaLevel <= 68
	SetFontSize 40
	SetBorderColor 120 0 0

Show # $type->leveling->flasks->life $tier->t12
	Class == "Life Flasks"
	BaseType "Eternal"
	AreaLevel <= 68
	SetFontSize 40
	SetBorderColor 120 0 0

#------------------------------------

# [5203] Mana flasks

#------------------------------------

Show # $type->leveling->flasks->mana $tier->t1
	Class == "Mana Flasks"
	BaseType "Small"
	AreaLevel <= 9
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t2
	Class == "Mana Flasks"
	BaseType "Medium"
	AreaLevel <= 13
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t3
	Class == "Mana Flasks"
	BaseType "Large"
	AreaLevel <= 17
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t4
	Class == "Mana Flasks"
	BaseType "Greater"
	AreaLevel <= 19
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t5
	Class == "Mana Flasks"
	BaseType "Grand"
	AreaLevel <= 25
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t6
	Class == "Mana Flasks"
	BaseType "Giant"
	AreaLevel <= 31
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t7
	Class == "Mana Flasks"
	BaseType "Colossal"
	AreaLevel <= 37
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t8
	Class == "Mana Flasks"
	BaseType "Sacred"
	AreaLevel <= 43
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t9
	Class == "Mana Flasks"
	BaseType "Hallowed"
	AreaLevel <= 51
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t10
	Class == "Mana Flasks"
	BaseType "Sanctified"
	AreaLevel <= 60
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t11
	Class == "Mana Flasks"
	BaseType "Divine"
	AreaLevel <= 68
	SetFontSize 40
	SetBorderColor 0 0 120

Show # $type->leveling->flasks->mana $tier->t12
	Class == "Mana Flasks"
	BaseType "Eternal"
	AreaLevel <= 68
	SetFontSize 40
	SetBorderColor 0 0 120

#===============================================================================================================

# [[5300]] Leveling - Rules

#===============================================================================================================

# !! Waypoint c11.leveling.gear.all : "Leveling - Gear - All non-unique" : "Leveling"

#------------------------------------

# [5301] Links and Sockets

#------------------------------------

Show # %D4 $type->leveling->rare->socketslinks $tier->4linkrares
	LinkedSockets >= 4
	ItemLevel <= 67
	Rarity Rare
	SetFontSize 45
	SetBorderColor 0 140 240 255
	SetBackgroundColor 20 20 0 255
	PlayEffect Grey
	MinimapIcon 2 Grey Diamond

#------------------------------------

# [5302] Rares - Exotics

#------------------------------------

Show # %D5 $type->leveling->rare->exotics $tier->movementbootshigh
	ItemLevel <= 67
	Rarity Normal Magic Rare
	Class == "Boots"
	HasExplicitMod "Cheetah's" "Gazelle's" "Stallion's"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->leveling->rare->exotics $tier->movementbootslow
	ItemLevel <= 67
	Rarity Normal Magic Rare
	Class == "Boots"
	HasExplicitMod "Sprinter's" "Runner's"
	AreaLevel <= 40
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D4 $type->leveling->rare->exotics $tier->anyveiled
	Identified True
	ItemLevel <= 67
	Rarity Normal Magic Rare
	HasExplicitMod "Veil"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

#------------------------------------

# [5303] Rares - Decorators

#------------------------------------

# !! Waypoint c11.leveling.decorators.all : "Leveling - Rares - Decorators" : "Leveling"

Show # $type->decorators->leveling->rare $tier->largerares
	Width >= 2
	Height >= 3
	ItemLevel <= 67
	Rarity Rare
	SetBorderColor 0 0 0 255
	Continue

Show # $type->decorators->leveling->rare $tier->mediumrares1
	Width 1
	Height >= 3
	ItemLevel <= 67
	Rarity Rare
	SetBorderColor 180 180 180 255
	Continue

Show # $type->decorators->leveling->rare $tier->mediumrares2
	Width 2
	Height 2
	ItemLevel <= 67
	Rarity Rare
	SetBorderColor 180 180 180 255
	Continue

Show # $type->decorators->leveling->rare $tier->tinyrares
	Width <= 2
	Height 1
	ItemLevel <= 67
	Rarity Rare
	SetBorderColor 50 200 50 255
	Continue

#------------------------------------

# [5304] Rares - Universal

#------------------------------------

# !! Waypoint c11.leveling.rares.minions : "Leveling - Rares - Minion Items" : "Leveling"

Show # %D4 $type->leveling->rare->minion $tier->general
	Rarity Rare
	BaseType == "Bone Ring" "Bone Spirit Shield" "Calling Wand" "Convening Wand" "Fossilised Spirit Shield" "Ivory Spirit Shield"
	SetFontSize 40
	SetBorderColor 150 50 150 255
	SetBackgroundColor 111 67 117 210

# !! Waypoint c11.leveling.rares.trinkets : "Leveling - Rares - Belts, Rings, Amulets" : "Leveling"

Show # %D5 $type->leveling->rare->universal $tier->jewellery
	Rarity Rare
	Class == "Amulets" "Belts" "Rings"
	SetFontSize 45
	SetBackgroundColor 0 80 30 255

# !! Waypoint c11.leveling.rares.armors : "Leveling - Rares - Armour Pieces" : "Leveling"

Show # %D4 $type->leveling->rare->armours $tier->bootsfocus
	Rarity Rare
	Class == "Boots"
	SetFontSize 45
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->leveling->rare->armours $tier->general
	Rarity Rare
	Class == "Boots" "Gloves" "Helmets"
	SetFontSize 40
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->leveling->rare->armours $tier->bodyarmours
	Rarity Rare
	Class == "Body Armours"
	SetFontSize 40
	SetBackgroundColor 35 35 35 240

Show # %D4 $type->leveling->rare->armours $tier->shields
	Rarity Rare
	Class == "Shields"
	SetFontSize 40
	SetBackgroundColor 35 35 35 240

Show # %D4 $type->leveling->rare->armours $tier->quivers
	Rarity Rare
	Class == "Quivers"
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

#------------------------------------

# [5305] Rares - Caster

#------------------------------------

# !! Waypoint c11.leveling.rares.caster : "Leveling - Rares - Caster" : "Leveling"

Show # %D4 $type->leveling->rare->caster $tier->earlylevels
	ItemLevel <= 16
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Staves" "Wands"
	SetFontSize 40
	SetBorderColor 50 50 150 255
	SetBackgroundColor 43 43 100 210

Show # %D4 $type->leveling->rare->caster $tier->general
	Rarity Rare
	Class == "Rune Daggers" "Sceptres" "Staves" "Wands"
	SetFontSize 40
	SetBorderColor 50 50 150 255
	SetBackgroundColor 43 43 100 210

#------------------------------------

# [5306] Rares - Archer

#------------------------------------

# !! Waypoint c11.leveling.rares.archer : "Leveling - Gear - Archer" : "Leveling"

Show # %D4 $type->leveling->rare->archer $tier->l1
	Rarity Rare
	Class == "Bows"
	AreaLevel <= 25
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

Show # %D4 $type->leveling->rare->archer $tier->l2
	DropLevel >= 10
	Rarity Rare
	Class == "Bows"
	AreaLevel <= 30
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

Show # %D4 $type->leveling->rare->archer $tier->l3
	DropLevel >= 15
	Rarity Rare
	Class == "Bows"
	AreaLevel <= 35
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

Show # %D4 $type->leveling->rare->archer $tier->l4
	DropLevel >= 20
	Rarity Rare
	Class == "Bows"
	AreaLevel <= 45
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

Show # %D4 $type->leveling->rare->archer $tier->l5
	DropLevel >= 25
	Rarity Rare
	Class == "Bows"
	AreaLevel <= 55
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

Show # %D4 $type->leveling->rare->archer $tier->l6
	DropLevel >= 30
	Rarity Rare
	Class == "Bows"
	AreaLevel <= 60
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

Show # %D4 $type->leveling->rare->archer $tier->l7
	DropLevel >= 35
	Rarity Rare
	Class == "Bows"
	AreaLevel <= 65
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

Show # %D4 $type->leveling->rare->archer $tier->l8
	DropLevel >= 40
	Rarity Rare
	Class == "Bows"
	AreaLevel <= 70
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

#------------------------------------

# [5307] Rares - Melee

#------------------------------------

# !! Waypoint c11.leveling.rares.melee : "Leveling - Gear - Melee" : "Leveling"

Show # %D4 $type->leveling->rare->melee2h $tier->l1
	Rarity Rare
	Class == "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	AreaLevel <= 25
	SetFontSize 40
	SetBorderColor 150 50 50 255
	SetBackgroundColor 100 43 43 210

Show # %D4 $type->leveling->rare->melee2h $tier->l2
	DropLevel >= 10
	Rarity Rare
	Class == "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	AreaLevel <= 30
	SetFontSize 40
	SetBorderColor 150 50 50 255
	SetBackgroundColor 100 43 43 210

Show # %D4 $type->leveling->rare->melee2h $tier->l3
	DropLevel >= 15
	Rarity Rare
	Class == "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	AreaLevel <= 35
	SetFontSize 40
	SetBorderColor 150 50 50 255
	SetBackgroundColor 100 43 43 210

Show # %D4 $type->leveling->rare->melee2h $tier->l4
	DropLevel >= 20
	Rarity Rare
	Class == "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	AreaLevel <= 45
	SetFontSize 40
	SetBorderColor 150 50 50 255
	SetBackgroundColor 100 43 43 210

Show # %D4 $type->leveling->rare->melee2h $tier->l5
	DropLevel >= 25
	Rarity Rare
	Class == "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	AreaLevel <= 55
	SetFontSize 40
	SetBorderColor 150 50 50 255
	SetBackgroundColor 100 43 43 210

Show # %D4 $type->leveling->rare->melee2h $tier->l6
	DropLevel >= 30
	Rarity Rare
	Class == "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	AreaLevel <= 60
	SetFontSize 40
	SetBorderColor 150 50 50 255
	SetBackgroundColor 100 43 43 210

Show # %D4 $type->leveling->rare->melee2h $tier->l7
	DropLevel >= 35
	Rarity Rare
	Class == "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	AreaLevel <= 65
	SetFontSize 40
	SetBorderColor 150 50 50 255
	SetBackgroundColor 100 43 43 210

Show # %D4 $type->leveling->rare->melee2h $tier->l8
	DropLevel >= 40
	Rarity Rare
	Class == "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Warstaves"
	AreaLevel <= 70
	SetFontSize 40
	SetBorderColor 150 50 50 255
	SetBackgroundColor 100 43 43 210

Show # %D4 $type->leveling->rare->melee1h $tier->l1
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords"
	AreaLevel <= 25
	SetFontSize 40
	SetBorderColor 180 180 0 255
	SetBackgroundColor 150 90 0 210

Show # %D4 $type->leveling->rare->melee1h $tier->l2
	DropLevel >= 10
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords"
	AreaLevel <= 30
	SetFontSize 40
	SetBorderColor 180 180 0 255
	SetBackgroundColor 150 90 0 210

Show # %D4 $type->leveling->rare->melee1h $tier->l3
	DropLevel >= 15
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords"
	AreaLevel <= 35
	SetFontSize 40
	SetBorderColor 180 180 0 255
	SetBackgroundColor 150 90 0 210

Show # %D4 $type->leveling->rare->melee1h $tier->l4
	DropLevel >= 20
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords"
	AreaLevel <= 45
	SetFontSize 40
	SetBorderColor 180 180 0 255
	SetBackgroundColor 150 90 0 210

Show # %D4 $type->leveling->rare->melee1h $tier->l5
	DropLevel >= 25
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords"
	AreaLevel <= 55
	SetFontSize 40
	SetBorderColor 180 180 0 255
	SetBackgroundColor 150 90 0 210

Show # %D4 $type->leveling->rare->melee1h $tier->l6
	DropLevel >= 30
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords"
	AreaLevel <= 60
	SetFontSize 40
	SetBorderColor 180 180 0 255
	SetBackgroundColor 150 90 0 210

Show # %D4 $type->leveling->rare->melee1h $tier->l7
	DropLevel >= 35
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords"
	AreaLevel <= 65
	SetFontSize 40
	SetBorderColor 180 180 0 255
	SetBackgroundColor 150 90 0 210

Show # %D4 $type->leveling->rare->melee1h $tier->l8
	DropLevel >= 40
	Rarity Rare
	Class == "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords"
	AreaLevel <= 70
	SetFontSize 40
	SetBorderColor 180 180 0 255
	SetBackgroundColor 150 90 0 210

#------------------------------------

# [5308] Rares - Other

#------------------------------------

# !! Waypoint c11.leveling.rares.low : "Leveling - Gear - Low Tier" : "Leveling"

#Show # %D3 $type->leveling->rare->remaining $tier->chromaticrares

# Rarity Rare

# SocketGroup "RGB"

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# SetFontSize 40

# SetBackgroundColor 80 80 80 100

#Show # %D2 $type->leveling->rare->remaining $tier->underlevel68

# ItemLevel <= 68

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# AreaLevel >= 42

# SetFontSize 40

# SetBackgroundColor 80 80 80 100

#Show # %D2 $type->leveling->rare->remaining $tier->underlevel42

# ItemLevel <= 44

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# AreaLevel >= 24

# SetFontSize 40

# SetBackgroundColor 80 80 80 100

#Show # %D2 $type->leveling->rare->remaining $tier->underlevel24

# ItemLevel <= 26

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"

# AreaLevel >= 16

# SetFontSize 40

# SetBackgroundColor 80 80 80 100

Show # %D3 $type->leveling->rare->remaining $tier->underlevel16
	ItemLevel <= 18
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	AreaLevel >= 1
	SetFontSize 40
	SetBackgroundColor 80 80 80 100

#===============================================================================================================

# [[5400]] Leveling - Useful magic and normal items

#===============================================================================================================

# !! Waypoint c11.leveling.linked.all : "Leveling - Linked - 4link" : "Leveling"

#------------------------------------

# [5401] Purpose Picked Items

#------------------------------------

Show # %D4 $type->leveling->normalmagic->4l $tier->general
	LinkedSockets >= 4
	Rarity Normal Magic
	SetFontSize 45
	SetBorderColor 0 140 240 255
	SetBackgroundColor 20 20 0 255
	PlayEffect Grey
	MinimapIcon 2 Grey Diamond

# !! Waypoint c11.leveling.rgb.all : "Leveling - Linked - RGB Recipe" : "Leveling"

#Show # %D5 $type->leveling->normalmagic->rgb $tier->rgbsmall1

# Width 2

# Height 2

# Rarity Normal Magic

# SocketGroup "RGB"

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Hexagon

#Show # %D5 $type->leveling->normalmagic->rgb $tier->rgbsmall2

# Width 1

# Height <= 4

# Rarity Normal Magic

# SocketGroup "RGB"

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Hexagon

#Show # %D4 $type->leveling->normalmagic->rgb $tier->rgblarge

# Width 2

# Height 4

# Rarity Normal Magic

# SocketGroup "RGB"

# SetFontSize 40

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Hexagon

#Show # %D4 $type->leveling->normalmagic->rgb $tier->rgbmedium

# Width 2

# Height 3

# Rarity Normal Magic

# SocketGroup "RGB"

# SetFontSize 40

# SetTextColor 255 255 255 255

# SetBorderColor 255 255 255 255

# SetBackgroundColor 155 138 138 255

# PlayAlertSound 2 300

# PlayEffect Grey

# MinimapIcon 2 Grey Hexagon

# !! Waypoint c11.leveling.3linked.all : "Leveling - Linked - 3links" : "Leveling"

Show # %D3 $type->leveling->normalmagic->3l $tier->earlythreelinks
	LinkedSockets >= 3
	Rarity Normal Magic
	AreaLevel <= 16
	SetFontSize 40
	SetBorderColor 0 120 120 255
	SetBackgroundColor 20 20 0 255
	PlayEffect Grey Temp

#Show # %D2 $type->leveling->normalmagic->3l $tier->general

# LinkedSockets >= 3

# Rarity Normal Magic

# AreaLevel <= 28

# SetFontSize 35

# SetBorderColor 0 120 120 255

# SetBackgroundColor 20 20 0 255

# PlayEffect Grey Temp

# !! Waypoint c11.leveling.act12.all : "Leveling - Normal and Magic - Act1, Act2 special gear" : "Leveling"

Show # %D4 $type->leveling->normalmagic->act1 $tier->casterweapons
	Sockets >= 3
	Rarity Magic
	Class == "Sceptres" "Wands"
	AreaLevel <= 16
	SetFontSize 40
	SetBorderColor 0 120 120 255
	SetBackgroundColor 20 20 0 255
	PlayEffect Grey Temp

Show # %D4 $type->leveling->normalmagic->act1 $tier->castercraftrings
	Rarity Normal Magic
	BaseType == "Iron Ring" "Ruby Ring" "Sapphire Ring" "Topaz Ring" "Two-Stone Ring"
	AreaLevel <= 16
	SetFontSize 40
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->leveling->normalmagic->act1 $tier->general
	Rarity Normal Magic
	BaseType == "Amber Amulet" "Chain Belt" "Coral Ring" "Jade Amulet" "Lapis Amulet" "Leather Belt"
	AreaLevel <= 16
	SetFontSize 40
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->leveling->normalmagic->act1 $tier->boots
	Rarity Magic
	Class == "Boots"
	AreaLevel <= 16
	SetFontSize 40
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->leveling->normalmagic->act1 $tier->quivers
	Rarity Normal Magic
	Class == "Quivers"
	AreaLevel <= 16
	SetFontSize 40
	SetBorderColor 0 150 0 255
	SetBackgroundColor 4 67 4 210

Show # %D4 $type->leveling->normalmagic->act1 $tier->physical
	Rarity Normal Magic
	BaseType == "Iron Ring" "Rustic Sash"
	AreaLevel <= 16
	SetFontSize 40
	SetBorderColor 0 240 190 255
	SetBackgroundColor 20 20 0 255

Show # %D4 $type->leveling->normalmagic->act1 $tier->jewellery
	Rarity Normal Magic
	Class == "Amulets" "Belts" "Rings"
	AreaLevel <= 16
	SetFontSize 40
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 20 0 255

Show # %D3 $type->leveling->normalmagic->act2 $tier->castercraftrings
	Rarity Normal Magic
	BaseType == "Iron Ring" "Ruby Ring" "Sapphire Ring" "Topaz Ring" "Two-Stone Ring"
	AreaLevel >= 16
	AreaLevel <= 24
	SetFontSize 35
	SetBorderColor 100 100 100 150
	SetBackgroundColor 20 20 0 255

Show # %D3 $type->leveling->normalmagic->act2 $tier->physical
	Rarity Normal Magic
	BaseType == "Rustic Sash"
	AreaLevel >= 16
	AreaLevel <= 24
	SetFontSize 35
	SetBorderColor 100 100 100 150
	SetBackgroundColor 20 20 0 255

# !! Waypoint c11.leveling.actlater.all : "Leveling - Normal and Magic - Later Acts" : "Leveling"

#Show # %D2 $type->leveling->normalmagic->otheracts $tier->highphysquivers

# Rarity Normal Magic

# BaseType == "Broadhead Arrow Quiver" "Heavy Arrow Quiver"

# SetFontSize 35

# SetBorderColor 100 100 100 150

# SetBackgroundColor 20 20 0 180

#Show # %D2 $type->leveling->normalmagic->otheracts $tier->fireresistgear

# Rarity Normal Magic

# BaseType == "Ruby Ring"

# AreaLevel >= 24

# AreaLevel <= 51

# SetFontSize 35

# SetBorderColor 100 100 100 150

# SetBackgroundColor 20 20 0 180

#Show # %D2 $type->leveling->normalmagic->otheracts $tier->generalcrafting

# Rarity Normal Magic

# BaseType == "Leather Belt" "Onyx Amulet" "Prismatic Ring" "Two-Stone Ring"

# AreaLevel >= 24

# SetFontSize 35

# SetBorderColor 100 100 100 150

# SetBackgroundColor 20 20 0 180

#Show # %D2 $type->leveling->normalmagic->minion $tier->miniongear

# Rarity Normal Magic

# BaseType == "Bone Ring" "Calling Wand" "Convening Wand" "Convoking Wand"

# SetFontSize 35

# SetBorderColor 100 100 100 150

# SetBackgroundColor 20 20 0 180

#Show # $type->leveling->normalmagic->minion $tier->minionshields

# Rarity Normal Magic

# BaseType == "Bone Spirit Shield" "Fossilised Spirit Shield" "Ivory Spirit Shield"

# SetFontSize 35

# SetBorderColor 100 100 100 150

# SetBackgroundColor 20 20 0 180

#------------------------------------

# [5402] Normals

#------------------------------------

# !! Waypoint c11.leveling.firstlevels.all : "Leveling - Normal and Magic - First Levels" : "Leveling"

Hide # %H2 $type->leveling->firstlevels $tier->earlybodyarmours
	Rarity Normal
	Class == "Body Armours"
	AreaLevel >= 2
	AreaLevel <= 9
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Show # %H3 $type->leveling->firstlevels $tier->threesocketedgear
	Sockets >= 3
	Rarity Normal Magic
	Class == "Boots" "Gloves" "Helmets" "Sceptres" "Shields" "Wands"
	AreaLevel <= 9
	SetFontSize 40
	SetBorderColor 100 100 100 150
	SetBackgroundColor 20 20 0 255

Show # %H3 $type->leveling->firstlevels $tier->firstareas
	Rarity Normal
	AreaLevel <= 4
	SetFontSize 35
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

#------------------------------------

# [5403] Weapon Progression

#------------------------------------

# !! Waypoint c11.leveling.progression.all : "Leveling - Normal and Magic - Item Progression" : "Leveling"

Hide # %H2 $type->leveling->weaponprogression $tier->r01
	Sockets >= 3
	ItemLevel <= 9
	DropLevel >= 5
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r02
	Sockets >= 3
	ItemLevel <= 15
	DropLevel >= 11
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r03
	Sockets >= 3
	ItemLevel <= 18
	DropLevel >= 15
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r04
	Sockets >= 3
	ItemLevel <= 22
	DropLevel >= 18
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r05
	Sockets >= 3
	ItemLevel <= 26
	DropLevel >= 22
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r06
	Sockets >= 3
	ItemLevel <= 30
	DropLevel >= 26
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r07
	Sockets >= 3
	ItemLevel <= 34
	DropLevel >= 30
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r08
	Sockets >= 3
	ItemLevel <= 40
	DropLevel >= 34
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r09
	Sockets >= 3
	ItemLevel <= 44
	DropLevel >= 40
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r10
	Sockets >= 3
	ItemLevel <= 48
	DropLevel >= 44
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r11
	Sockets >= 3
	ItemLevel <= 52
	DropLevel >= 48
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r12
	Sockets >= 3
	ItemLevel <= 56
	DropLevel >= 52
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r13
	Sockets >= 3
	ItemLevel <= 60
	DropLevel >= 56
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r14
	Sockets >= 3
	ItemLevel <= 64
	DropLevel >= 60
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->weaponprogression $tier->r15bas
	Sockets >= 3
	ItemLevel <= 68
	DropLevel >= 64
	Rarity Normal
	Class == "Bows" "Claws" "Daggers" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

#------------------------------------

# [5404] Attack Wand Progression

#------------------------------------

Hide # %H2 $type->leveling->wandprogression $tier->w1
	Rarity Normal
	Class == "Wands"
	BaseType == "Somatic Wand"
	AreaLevel <= 24
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->wandprogression $tier->w2
	Rarity Normal
	Class == "Wands"
	BaseType == "Blasting Wand"
	AreaLevel <= 50
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

Hide # %H2 $type->leveling->wandprogression $tier->w3
	Rarity Normal
	Class == "Wands"
	BaseType == "Kinetic Wand"
	AreaLevel <= 67
	SetTextColor 180 180 180
	SetBorderColor 0 0 0
	SetBackgroundColor 20 20 0 180

#------------------------------------

# [5405] Remaining Magics

#------------------------------------

Show # $type->decorators->leveling->magic $tier->medium1
	Width 1
	Height >= 3
	ItemLevel <= 67
	Rarity Magic
	SetBorderColor 100 100 100 150
	Continue

Show # $type->decorators->leveling->magic $tier->medium2
	Width 2
	Height 2
	ItemLevel <= 67
	Rarity Magic
	SetBorderColor 100 100 100 150
	Continue

Show # $type->decorators->leveling->magic $tier->noticeearly
	ItemLevel <= 67
	Rarity Magic
	AreaLevel <= 9
	SetBorderColor 100 100 100 150
	Continue

Show # $type->decorators->leveling->magic $tier->tiny
	Width <= 2
	Height 1
	ItemLevel <= 67
	Rarity Magic
	SetBorderColor 255 255 255 255
	Continue

# !! Waypoint c11.leveling.magicvendor.all : "Leveling - Normal and Magic - Magic Vendor Items" : "Leveling"

Hide # $type->leveling->magic->remaining $tier->largemagicblocker
	Width >= 2
	Height >= 3
	Rarity Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	AreaLevel >= 16
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # $type->leveling->magic->remaining $tier->mediummagicblocker
	Height > 1
	Rarity Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	AreaLevel >= 24
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # %H1 $type->leveling->magic->remaining $tier->rest
	Rarity Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	AreaLevel >= 34
	AreaLevel <= 67

Hide # %H2 $type->leveling->magic->remaining $tier->act2
	Rarity Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	AreaLevel >= 16
	AreaLevel <= 24
	SetFontSize 35

Show # %H3 $type->leveling->magic->remaining $tier->act1
	Rarity Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	AreaLevel >= 9
	AreaLevel <= 16
	SetFontSize 35

Show # %H3 $type->leveling->magic->remaining $tier->untilmudflats
	Rarity Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	AreaLevel <= 4
	SetFontSize 40

Show # %H3 $type->leveling->magic->remaining $tier->firstlevels
	Rarity Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	AreaLevel >= 1
	AreaLevel <= 9
	SetFontSize 40

# !! Waypoint c12.hide.all : "HIDELAYER - Hide all known untiered items"

#------------------------------------

# [5406] Hide All known Section

#------------------------------------

Hide # $type->hidelayer $tier->final
	Class "Abyss Jewels" "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Heist Brooches" "Heist Cloaks" "Heist Gear" "Heist Tools" "Helmets" "Hybrid Flasks" "Idols" "Jewels" "Life Flasks" "Mana Flasks" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Tinctures" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Utility Flasks" "Wands" "Warstaves"
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

#------------------------------------

# [5407] Show All unknown Section

#------------------------------------

# !! Waypoint c13.show.all : "SAFETYLAYER - Show all unknown items"

# THIS ENTRY IS CAUGHT IN 3 CASES:

# 1) YOUR FILTER IS OUT OF DATE!

# 2) YOU DID SOMETHING SILLY WHEN EDITING THE FILTER

# 3) YOU ENCOUNTERED A PREVIOUSLY UNKNOWN ITEM (VERY UNLIKELY)

Show # $type->anyremaining $tier->restex
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circ


#===============================================================================================================

# NeverSink's Indepth Loot Filter - for Path of Exile 2

#===============================================================================================================

# VERSION:  0.10.4

# TYPE:     5-UBER-STRICT

# STYLE:    DEFAULT

# AUTHOR:   NeverSink

# BUILDNOTES: Filter generated with NeverSink's FilterpolishZ and the domainlanguage Exo.

#------------------------------------

# LINKS TO LATEST VERSION AND FILTER EDITOR

#------------------------------------

# CUSTOMIZE THE POE 2 FILTER ON: 	https://www.FilterBlade.xyz?game=Poe2

# GET THE LATEST VERSION ON: 	    https://www.FilterBlade.xyz or https://github.com/NeverSinkDev/NeverSink-Filter-for-PoE2

#------------------------------------

# INSTALLATION / UPDATE :

#------------------------------------

# 0) It's recommended to check for updates once a month or at least before new leagues, to receive economy finetuning and new features!

# 1) Paste this file into the following folder: %userprofile%/Documents/My Games/Path of Exile 2/

# 2) INGAME: Escape -> Options -> UI -> Scroll down -> Select the filter from the Dropdown box

#------------------------------------

# AUTO-UPDATER SERVICE AND SUPPORT THE DEVELOPMENT

#------------------------------------

# Patreon supporters get access to the FilterBlade Auto-Updater that combines 100% automated updates with custom styles and your customizations!

# It's a great way to support us and get something in return and it helps us on our journey of making our own company and potentially game. Thank you

# Learn more about the ItemFilter-AutoUpdate feature here: https://www.youtube.com/watch?v=i8RJx0s0zsA

# PATREON:               		https://www.patreon.com/Neversink

# OTHER:                        https://www.filterblade.xyz/About

#------------------------------------

# CONTACT - if you want to get notifications about updates or just get in touch:

#------------------------------------

# For feedback, questions and suggestions please join our discord!

# DISCORD: https://discord.gg/zFEx92a

# TWITTER: @NeverSinkDev

# TWITCH:  https://www.twitch.tv/neversink

# BSKY:    @neversink.bsky.social

# FORUM:   https://www.pathofexile.com/forum/view-thread/3693141

#===============================================================================================================

# [WELCOME] TABLE OF CONTENTS + QUICKJUMP TABLE

#===============================================================================================================

# [[0100]] OVERRIDE AREA 1 - Override ALL rules here

# [[0100]] Gold

# [[0200]] Exotic Bases

# [[0300]] Exceptional Items

# [0301] Crafting and Chancing Bases

# [[0400]] IDENTIFIED MODS: RECOMBINATOR MODS

# [[0500]] Rare Item Decorators

# [[0600]] Normal, Magic, Rare Hiding Rules

# [[0700]] Economy Crafting Bases

# [[0800]] High Unidentified Mod Tier

# [[0900]] Endgame Flasks

# [[1000]] Endgame Charms

# [[1100]] Normal and Magic Items: Endgame

# [1101] Normal, Magic Crafting Decorators

# [1102] Additional High Value Rules

# [1103] Normal, Magic Crafting: Level 82+

# [1104] Normal, Magic Crafting: Optional Rules

# [1105] Normal, Magic Crafting: Endgame Progression

# [1106] Normal, Magic Crafting: Rings+Amulets

# [1107] Normal, Magic Crafting: Decorator Removers

# [1108] Salvagables

# [[1200]] Hide Layer 1 - Normal and Magic Endgame Gear

# [[1300]] Endgame - Conditional Hide Layers

# [[1400]] Endgame - Rare - Jewellery

# [[1500]] Endgame - Rare - Gear

# [[1600]] Untiered Rare Catcher

# [[1700]] Hide Layer 2 - Rare Gear

# [[1800]] New League Unknown Items

# [[1900]] Socketables - Runes and Soul Cores

# [[2000]] Jewels

# [[2100]] Relics

# [[2200]] Gems and Uncut Gems

# [[2300]] Waystones

# [[2400]] Normal Waystone Progression

# [2401] Generic Decorators

# [2402] Special Maps

# [2403] Waystone progression

# [[2500]] Currency - Exceptions - Leveling Currencies

# [[2600]] Currency - Regular Currency Tiering

# [[2700]] Currency - SPECIAL

# [2701] Distilled Emotions (Delirium)

# [2702] Catalysts (breach)

# [2703] Essences

# [2704] Omen (ritual)

# [[2800]] Misc Map Like

# [[2900]] Uniques

# [2901] Exceptions #1

# [2902] Tier 1 and 2 uniques

# [2903] Multi-Unique bases.

# [2904] Low tier exceptions

# [2905] Tier 3 uniques

# [2906] Tier 4 uniques

# [[3000]] Splinters, Tablets, Fragments

# [[3100]] Misc Map Items

# [[3200]] Remaining Currency

# [[3300]] Leveling - Salvagable

# [[3400]] Leveling - Hide outdated leveling flasks

# [[3500]] Leveling - Life Mana Flasks

# [3501] Life flasks

# [3502] Mana flasks

# [3503] Charms

# [[3600]] Leveling - Rules

# [3601] Rares - Decorators

# [3602] Rares - Universal

# [3603] Rares - Other

# [[3700]] Leveling - Useful magic and normal items

# [3701] Decorators

# [3702] Purpose Picked Items

# [3703] Conditional Rules

# [3704] Hide All known Section

# [3705] Show All unknown Section

#===============================================================================================================

# [[0100]] Gold

#===============================================================================================================

# !! Waypoint c0.start : "Start - Override ALL rules" : "Gold"

Show # %D7 $type->gold $tier->stack3 !gold_pilehuge
	StackSize >= 5000
	BaseType == "Gold"
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 20 20 0 255
	PlayEffect Orange
	MinimapIcon 1 Yellow Cross

Show # %D6 $type->gold $tier->stack2 !gold_pilelarge
	StackSize >= 2000
	BaseType == "Gold"
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	PlayEffect Orange Temp
	MinimapIcon 1 White Cross

Show # %D5 $type->gold $tier->stack1 !gold_pilemedium
	StackSize >= 650
	BaseType == "Gold"
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	PlayEffect Orange Temp

Show # %D6 $type->gold $tier->stackxl1lvl !gold_pilelarge
	StackSize >= 500
	BaseType == "Gold"
	AreaLevel <= 24
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	PlayEffect Orange Temp
	MinimapIcon 1 White Cross

Show # %D6 $type->gold $tier->stackxl2lvl !gold_pilelarge
	StackSize >= 1000
	BaseType == "Gold"
	AreaLevel <= 64
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	PlayEffect Orange Temp
	MinimapIcon 1 White Cross

Show # %D5 $type->gold $tier->stack1lvl !gold_pilemedium
	StackSize >= 100
	BaseType == "Gold"
	AreaLevel <= 16
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	PlayEffect Orange Temp

Show # %D5 $type->gold $tier->stack2lvl !gold_pilemedium
	StackSize >= 250
	BaseType == "Gold"
	AreaLevel <= 34
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	PlayEffect Orange Temp

Show # %D5 $type->gold $tier->stack3lvl !gold_pilemedium
	StackSize >= 400
	BaseType == "Gold"
	AreaLevel <= 64
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	PlayEffect Orange Temp

Hide # %H3 $type->gold $tier->any !gold_pilesmall
	BaseType == "Gold"
	SetTextColor 180 180 180
	SetBorderColor 0 0 0 255
	SetBackgroundColor 20 20 0 180

#===============================================================================================================

# [[0200]] Exotic Bases

#===============================================================================================================

# !! Waypoint c2.exotic.all : "Exotic Items - Breach Rings, Fishing Rods, Quest Items" : "SpecialCases"

# Currently contains mostly undroppable bases

Show # %D9 $type->exoticbases $tier->superexoticbases !exotics_btier
	Rarity Normal Magic Rare
	BaseType == "Aberrant Sledge" "Abyssal Signet" "Ancient Gauntlets" "Ancient Leggings" "Ancient Mail" "Ancient Visor" "Diamond" "Glacial Fortress" "Heartwood Shortbow" "Ornate Ringmail" "Pearlescent Amulet" "Perching Staff" "Primal Markings" "Reflecting Staff" "Runic Fork" "Sacrificial Regalia" "Tenebrous Crown" "Time-Lost Diamond" "Twisted Wand" "Two-Stone Ring" "Venerable Defender" "Veridical Chain" "Warding Quarterstaff"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->exoticbases $tier->kalandrabases !exotics_btier
	Rarity Normal Magic Rare
	BaseType == "Dusk Amulet" "Dusk Ring" "Gloam Amulet" "Gloam Ring" "Penumbra Amulet" "Penumbra Ring" "Tenebrous Amulet" "Tenebrous Ring"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->exoticbases $tier->pseudocrafts1 !exotics_btier
	Rarity Normal Magic Rare
	BaseType == "Absent Amulet" "Grasping Mail" "Refined Breach Ring"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D8 $type->exoticbases $tier->pseudocrafts2 !exotics_ctier
	Rarity Normal Magic Rare
	BaseType == "Biostatic Ring" "Corona Amulet" "Distorted Amulet" "Forking Belt" "Grasping Ring" "Invoking Belt" "Kinetic Ring" "Lament Amulet" "Mnemonic Ring" "Oneiric Ring" "Portent Amulet" "Sinew Belt" "Stalking Belt" "Twisted Amulet" "Vitalic Ring"
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

# Currently contains breach rings

Show # %D8 $type->exoticbases $tier->commonexoticbaseshigh !gear_jewelmagic
	ItemLevel >= 82
	Rarity Normal Magic
	BaseType == "Breach Ring"
	SetFontSize 42
	SetTextColor 0 70 255 255
	SetBorderColor 0 70 255 255
	SetBackgroundColor 30 0 70 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D4 $type->exoticbases $tier->commonexoticbases !gear_jewelmagiclow

# Rarity Normal Magic

# BaseType == "Breach Ring"

# SetFontSize 38

# SetTextColor 0 70 255 255

# SetBorderColor 0 70 255 255

# PlayEffect Blue Temp

# MinimapIcon 2 Blue Diamond

# Sanctum keys

Show # $type->questlikeexception $tier->questlike !typebased_quest
	BaseType == "Bronze Key" "Gold Key" "Silver Key"
	SetFontSize 42
	SetTextColor 74 230 58 255
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 0 Green Pentagon

Show # $type->questlikeexception $tier->questitems !typebased_quest
	Class == "Instance Local Items" "Quest Items"
	SetFontSize 42
	SetTextColor 74 230 58 255
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 0 Green Pentagon

Show # $type->artifact $tier->fishingrod !exotics_artifact
	Rarity Normal Magic Rare
	Class == "Fishing Rods"
	SetFontSize 40
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 1 Orange Pentagon

#===============================================================================================================

# [[0300]] Exceptional Items

#===============================================================================================================

# !! Waypoint c3.exotic.state.exceptional : "Exotic State - Exceptional Items" : "Exotics"

Show # %D9 $type->exotic->exceptional $tier->overqual1q1 !exotics_artifacthigh
	Corrupted False
	Quality >= 27
	Rarity Normal Magic Rare
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"
	SetFontSize 42
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # %D9 $type->exotic->exceptional $tier->oversockt1s3 !exotics_artifacthigh
	Corrupted False
	Sockets >= 3
	Rarity Normal Magic Rare
	Class == "Body Armours" "Bows" "Crossbows" "Quarterstaves" "Staves" "Talismans" "Two Hand Maces"
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"
	SetFontSize 42
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # %D9 $type->exotic->exceptional $tier->oversockt1s2 !exotics_artifacthigh
	Corrupted False
	Sockets >= 2
	Rarity Normal Magic Rare
	Class == "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "One Hand Maces" "Sceptres" "Shields" "Spears" "Wands"
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"
	SetFontSize 42
	SetTextColor 240 0 0 255
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 3 300
	PlayEffect Orange
	MinimapIcon 0 Orange Pentagon

Show # %D9 $type->exotic->exceptional $tier->chancingoverqual !itemproperty_achancing
	Corrupted False
	Quality >= 24
	Rarity Normal
	BaseType == "Aberrant Sledge" "Abyss Tablet" "Armoured Cap" "Armoured Vest" "Array Buckler" "Ashbark Talisman" "Chain Tiara" "Cinched Boots" "Desolate Crossbow" "Diamond" "Emerald" "Engraved Bracers" "Exquisite Vest" "Felt Cap" "Fine Bracers" "Gargantuan Mana Flask" "Garment" "Glacial Fortress" "Golden Charm" "Grand Manchettes" "Grand Regalia" "Grand Spear" "Heartwood Shortbow" "Incense Relic" "Intricate Crest Shield" "Ironclad Vestments" "Lattice Sandals" "Morning Star" "Ornate Gauntlets" "Perching Staff" "Permafrost Staff" "Primed Quiver" "Pronged Spear" "Reflecting Staff" "Ring" "Ritual Tablet" "Ruby" "Sacred Focus" "Sacrificial Regalia" "Sapphire" "Shrine Sceptre" "Silver Charm" "Siphoning Wand" "Spiral Wraps" "Stocky Mitts" "Stoic Sceptre" "Stone Charm" "Temple Tablet" "Thawing Charm" "Timeless Jewel" "Time-Lost Diamond" "Totemic Greatclub" "Trarthan Cannon" "Twisted Wand" "Two-Stone Ring" "Ultimate Mana Flask" "Unset Ring" "Utility Wraps" "Vase Relic" "Veridical Chain" "Warding Quarterstaff" "Winged Spear"
	SetFontSize 45
	SetTextColor 125 255 89 255
	SetBorderColor 125 255 89 255
	SetBackgroundColor 0 50 0
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

Show # %D9 $type->exotic->exceptional $tier->chancingoversocket3 !itemproperty_achancing
	Corrupted False
	Sockets >= 3
	Rarity Normal
	Class == "Body Armours" "Bows" "Crossbows" "Quarterstaves" "Staves" "Talismans" "Two Hand Maces"
	BaseType == "Aberrant Sledge" "Abyss Tablet" "Armoured Cap" "Armoured Vest" "Array Buckler" "Ashbark Talisman" "Chain Tiara" "Cinched Boots" "Desolate Crossbow" "Diamond" "Emerald" "Engraved Bracers" "Exquisite Vest" "Felt Cap" "Fine Bracers" "Gargantuan Mana Flask" "Garment" "Glacial Fortress" "Golden Charm" "Grand Manchettes" "Grand Regalia" "Grand Spear" "Heartwood Shortbow" "Incense Relic" "Intricate Crest Shield" "Ironclad Vestments" "Lattice Sandals" "Morning Star" "Ornate Gauntlets" "Perching Staff" "Permafrost Staff" "Primed Quiver" "Pronged Spear" "Reflecting Staff" "Ring" "Ritual Tablet" "Ruby" "Sacred Focus" "Sacrificial Regalia" "Sapphire" "Shrine Sceptre" "Silver Charm" "Siphoning Wand" "Spiral Wraps" "Stocky Mitts" "Stoic Sceptre" "Stone Charm" "Temple Tablet" "Thawing Charm" "Timeless Jewel" "Time-Lost Diamond" "Totemic Greatclub" "Trarthan Cannon" "Twisted Wand" "Two-Stone Ring" "Ultimate Mana Flask" "Unset Ring" "Utility Wraps" "Vase Relic" "Veridical Chain" "Warding Quarterstaff" "Winged Spear"
	SetFontSize 45
	SetTextColor 125 255 89 255
	SetBorderColor 125 255 89 255
	SetBackgroundColor 0 50 0
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

Show # %D9 $type->exotic->exceptional $tier->chancingoversocket2 !itemproperty_achancing
	Corrupted False
	Sockets >= 2
	Rarity Normal
	Class == "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "One Hand Maces" "Sceptres" "Shields" "Spears" "Wands"
	BaseType == "Aberrant Sledge" "Abyss Tablet" "Armoured Cap" "Armoured Vest" "Array Buckler" "Ashbark Talisman" "Chain Tiara" "Cinched Boots" "Desolate Crossbow" "Diamond" "Emerald" "Engraved Bracers" "Exquisite Vest" "Felt Cap" "Fine Bracers" "Gargantuan Mana Flask" "Garment" "Glacial Fortress" "Golden Charm" "Grand Manchettes" "Grand Regalia" "Grand Spear" "Heartwood Shortbow" "Incense Relic" "Intricate Crest Shield" "Ironclad Vestments" "Lattice Sandals" "Morning Star" "Ornate Gauntlets" "Perching Staff" "Permafrost Staff" "Primed Quiver" "Pronged Spear" "Reflecting Staff" "Ring" "Ritual Tablet" "Ruby" "Sacred Focus" "Sacrificial Regalia" "Sapphire" "Shrine Sceptre" "Silver Charm" "Siphoning Wand" "Spiral Wraps" "Stocky Mitts" "Stoic Sceptre" "Stone Charm" "Temple Tablet" "Thawing Charm" "Timeless Jewel" "Time-Lost Diamond" "Totemic Greatclub" "Trarthan Cannon" "Twisted Wand" "Two-Stone Ring" "Ultimate Mana Flask" "Unset Ring" "Utility Wraps" "Vase Relic" "Veridical Chain" "Warding Quarterstaff" "Winged Spear"
	SetFontSize 45
	SetTextColor 125 255 89 255
	SetBorderColor 125 255 89 255
	SetBackgroundColor 0 50 0
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

Show # %D7 $type->exotic->exceptional $tier->oversockt2s3 !exotics_btier
	Corrupted False
	Sockets >= 3
	Rarity Normal Magic Rare
	Class == "Body Armours" "Bows" "Crossbows" "Quarterstaves" "Staves" "Talismans" "Two Hand Maces"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D7 $type->exotic->exceptional $tier->oversockt2s2 !exotics_btier
	Corrupted False
	Sockets >= 2
	Rarity Normal Magic Rare
	Class == "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "One Hand Maces" "Sceptres" "Shields" "Spears" "Wands"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D7 $type->exotic->exceptional $tier->overqual1q2 !exotics_ctier
	Corrupted False
	Quality >= 21
	Rarity Normal Magic Rare
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D9 $type->exotic->state $tier->twicecorruptedrare !exotics_btier
	TwiceCorrupted True
	Rarity Rare
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D9 $type->exotic->state $tier->twicecorruptedmagic !exotics_ctier
	TwiceCorrupted True
	Rarity Normal Magic
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#------------------------------------

# [0301] Crafting and Chancing Bases

#------------------------------------

# !! Waypoint c3.gear.chancing : "Chancing bases" : "Exotics"

#Show # %D9 $type->chancing $tier->chances !apex_stier

# Mirrored False

# Corrupted False

# Rarity Normal

# SetFontSize 45

# SetTextColor 255 0 0 255

# SetBorderColor 255 0 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 6 300

# PlayEffect Red

# MinimapIcon 0 Red Star

Show # %D7 $type->chancing $tier->chancea !itemproperty_achancing
	Mirrored False
	Corrupted False
	Rarity Normal
	BaseType == "Heavy Belt" "Utility Belt"
	SetFontSize 45
	SetTextColor 125 255 89 255
	SetBorderColor 125 255 89 255
	SetBackgroundColor 0 50 0
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

#Show # %D2 $type->chancing $tier->chanceany !itemproperty_bchancing

# Mirrored False

# Corrupted False

# Rarity Normal

# BaseType == "Silver Charm"

# SetFontSize 40

# SetBorderColor 0 200 95

# PlayAlertSound 3 300

# PlayEffect Green Temp

# MinimapIcon 1 Green Diamond

#===============================================================================================================

# [[0400]] IDENTIFIED MODS: RECOMBINATOR MODS

#===============================================================================================================

# !! Waypoint c3.exotic.state.idmods : "Exotic State - Identified Mod Filtering" : "Exotics"

Show # %D6 $type->exoticmods $tier->cmboots !exotics_identifiedmod
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Boots"
	HasExplicitMod >=1 "Hellion's"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->exoticmods $tier->cmamulets !exotics_identifiedmod
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Amulets"
	HasExplicitMod >=1 "Countess'" "of the Sharpshooter"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->exoticmods $tier->cmcasterweapons !exotics_identifiedmod
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Staves" "Wands"
	HasExplicitMod >=1 "Runic" "of the Wizard" "of Inferno" "of Frostbite" "of Thunder" "of Armageddon" "of Grief"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->exoticmods $tier->cmsceptres !exotics_identifiedmod
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Sceptres"
	HasExplicitMod >=1 "King's" "of the Slavedriver" "Empowering"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->exoticmods $tier->cmranged !exotics_identifiedmod
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Bows" "Crossbows"
	HasExplicitMod >=1 "of Many" "Merciless" "of the Sniper"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->exoticmods $tier->cmspears !exotics_identifiedmod
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Spears"
	HasExplicitMod >=1 "Merciless" "Flaring" "Amazon's" "of the Sniper"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->exoticmods $tier->cm2handed !exotics_identifiedmod
	Mirrored False
	Corrupted False
	Identified True
	Rarity Normal Magic Rare
	Class == "Quarterstaves" "Talismans" "Two Hand Maces"
	HasExplicitMod >=1 "Merciless" "of War"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 47 0 74 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

#===============================================================================================================

# [[0500]] Rare Item Decorators

#===============================================================================================================

# !! Waypoint c3.rare.decorator.all : "Normal-Rare items - including visual decorators" : "Technical"

Show # $type->decorators->rareeg $tier->basicraredecorator !utility_basicraredecorator
	Rarity Rare
	AreaLevel >= 65
	SetBorderColor 0 0 0 255
	Continue

#Show # $type->decorators->rareeg $tier->largerares !gear_unstyled

# Width >= 2

# Height >= 3

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# Continue

#Show # $type->decorators->rareeg $tier->mediumrares1 !gear_unstyled

# Width 1

# Height >= 3

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# Continue

#Show # $type->decorators->rareeg $tier->mediumrares2 !gear_unstyled

# Width 2

# Height 2

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# Continue

Show # $type->decorators->rareeg $tier->tinyrares !gear_decojewellery
	Width <= 2
	Height 1
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetBorderColor 220 220 0
	Continue

#Show # $type->decorators->rareeg $tier->ilvl80 !gear_unstyled

# ItemLevel >= 80

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# Continue

Show # $type->decorators->rareeg $tier->ilvl82 !itemproperty_level82
	ItemLevel >= 82
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetTextColor 245 175 0
	Continue

# Optional: caster weapons get their most important mods on 81

#Show # %D0 $type->decorators->rareeg $tier->ilvl81caster !itemproperty_level82

# ItemLevel >= 81

# Rarity Rare

# Class == "Sceptres" "Staves" "Wands"

# AreaLevel >= 65

# SetTextColor 245 175 0

# Continue

Show # $type->decorators->rareeg $tier->corruptedrares !exotics_corrupt
	AnyEnchantment False
	Corrupted True
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetBorderColor 120 0 0 240
	Continue

Show # $type->decorators->rareeg $tier->corruptedraresimplicit !exotics_corrupthigh
	AnyEnchantment True
	Corrupted True
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetBorderColor 250 0 0 255
	Continue

#===============================================================================================================

# [[0600]] Normal, Magic, Rare Hiding Rules

#===============================================================================================================

# !! Waypoint c3.gear.any.hiding : "Normal, Magic, Rare Hiding Rules, Except chancing" : "Technical"

#Hide # $type->endgame->conditionalhiders->crafting $tier->hideweaponsbytype !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# Rarity Normal Magic

# Class == "Bows" "Crossbows" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->crafting $tier->arhider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield 0

# BaseEvasion 0

# BaseArmour > 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->crafting $tier->evhider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield 0

# BaseEvasion > 0

# BaseArmour 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->crafting $tier->eshider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield > 0

# BaseEvasion 0

# BaseArmour 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->crafting $tier->arevhider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield 0

# BaseEvasion > 0

# BaseArmour > 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->crafting $tier->areshider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield > 0

# BaseEvasion 0

# BaseArmour > 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->crafting $tier->eveshider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield > 0

# BaseEvasion > 0

# BaseArmour 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

# !! Waypoint c3.gear.rare.hiding : "Rare Hiding Rules" : "Technical"

#Hide # $type->endgame->conditionalhiders->rare $tier->hideweaponsbytype !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# Rarity Rare

# Class == "Bows" "Crossbows" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->rare $tier->arhider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield 0

# BaseEvasion 0

# BaseArmour > 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->rare $tier->evhider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield 0

# BaseEvasion > 0

# BaseArmour 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->rare $tier->eshider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield > 0

# BaseEvasion 0

# BaseArmour 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->rare $tier->arevhider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield 0

# BaseEvasion > 0

# BaseArmour > 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->rare $tier->areshider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield > 0

# BaseEvasion 0

# BaseArmour > 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->endgame->conditionalhiders->rare $tier->eveshider !utility_minimize

# Sockets 0

# Quality 0

# UnidentifiedItemTier <= 3

# BaseEnergyShield > 0

# BaseEvasion > 0

# BaseArmour 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#===============================================================================================================

# [[0700]] Economy Crafting Bases

#===============================================================================================================

# !! Waypoint c3.exotic.state.ecocraft : "High Value Crafting Bases" : "Crafting"

Show # %D9 $type->endgame->normalcraft->economy $tier->group1t1 !itemproperty_aecocraft
	Mirrored False
	Corrupted False
	ItemLevel >= 82
	Rarity Normal
	BaseType == "Ancestral Tiara" "Dousing Charm" "Gold Amulet" "Gold Ring" "Prismatic Ring" "Sekhema Sandals" "Sinister Quarterstaff" "Sirenscale Gloves" "Solar Amulet" "Staunching Charm" "Stone Charm" "Unset Ring" "Vile Robe" "Visceral Quiver"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 127 127 255
	SetBackgroundColor 65 0 0
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

Show # %D7 $type->endgame->normalcraft->economy $tier->group1t2 !itemproperty_becocraft
	Mirrored False
	Corrupted False
	ItemLevel >= 82
	Rarity Normal
	BaseType == "Akoyan Spear" "Antidote Charm" "Daggerfoot Shoes" "Dueling Wand" "Flowing Raiment" "Flying Spear" "Gemini Crossbow" "Golden Charm" "Lapis Amulet" "Obliterator Bow" "Paralysing Staff" "Plate Belt" "Polished Bracers" "Sacred Focus" "Sleek Jacket" "Soaring Spear" "Stellar Amulet" "Thawing Charm" "Topaz Ring" "Warmonger Bow"
	SetFontSize 40
	SetBorderColor 255 127 127
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

#Show # %D9 $type->endgame->normalcraft->economy $tier->group2t1 !itemproperty_aecocraft

# Mirrored False

# Corrupted False

# ItemLevel >= 81

# Rarity Normal

# SetFontSize 45

# SetTextColor 255 255 255 255

# SetBorderColor 255 127 127 255

# SetBackgroundColor 65 0 0

# PlayAlertSound 1 300

# PlayEffect Red

# MinimapIcon 0 Red Diamond

Show # %D6 $type->endgame->normalcraft->economy $tier->group2t2 !itemproperty_becocraft
	Mirrored False
	Corrupted False
	ItemLevel >= 81
	Rarity Normal
	BaseType == "Ancestral Tiara" "Gold Amulet" "Gold Ring" "Golden Charm" "Ruby Charm" "Sacred Focus" "Sinister Quarterstaff" "Solar Amulet" "Stone Charm" "Thawing Charm" "Vile Robe"
	SetFontSize 40
	SetBorderColor 255 127 127
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D6 $type->endgame->normalcraft->economy $tier->group3t2 !itemproperty_becocraft
	Mirrored False
	Corrupted False
	ItemLevel >= 79
	Rarity Normal
	BaseType == "Golden Charm" "Sacred Focus"
	SetFontSize 40
	SetBorderColor 255 127 127
	SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

#===============================================================================================================

# [[0800]] High Unidentified Mod Tier

#===============================================================================================================

# !! Waypoint c3.exotic.state.hightier : "Rare items with Mod Tier" : "ModTierRare"

Show # %D7 $type->ut->rare $tier->gear4a !exotics_btier
	UnidentifiedItemTier >= 4
	Rarity Rare
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->ut->rare $tier->gear3a !exotics_ctier
	UnidentifiedItemTier >= 3
	Rarity Rare
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D4 $type->ut->rare $tier->gear2a !gear_highlightedsize

# UnidentifiedItemTier >= 2

# Rarity Rare

# BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"

# AreaLevel >= 65

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

Show # %D6 $type->ut->rare $tier->gear4b !exotics_ctier
	UnidentifiedItemTier >= 4
	Rarity Rare
	BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->ut->rare $tier->gear3b !gear_highlightedsize
	UnidentifiedItemTier >= 3
	Rarity Rare
	BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"
	AreaLevel >= 65
	SetFontSize 40
	SetBackgroundColor 20 20 0 255

#Show # %D4 $type->ut->rare $tier->gear2b !gear_highlightedsize

# UnidentifiedItemTier >= 2

# Rarity Rare

# BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"

# AreaLevel >= 65

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

Show # %D5 $type->ut->rare $tier->gear4c !exotics_ctier
	UnidentifiedItemTier >= 4
	Rarity Rare
	BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D4 $type->ut->rare $tier->gear3c !gear_highlightedsize

# UnidentifiedItemTier >= 3

# Rarity Rare

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# AreaLevel >= 65

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D3 $type->ut->rare $tier->gear2c !gear_highlightedsize

# UnidentifiedItemTier >= 2

# Rarity Rare

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# AreaLevel >= 65

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

Show # %D8 $type->ut->rare $tier->j4a !exotics_btier
	UnidentifiedItemTier >= 4
	Rarity Rare
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D7 $type->ut->rare $tier->j3a !exotics_btier
	UnidentifiedItemTier >= 3
	Rarity Rare
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->ut->rare $tier->j2a !gear_tieredjewellery
	UnidentifiedItemTier >= 2
	Rarity Rare
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 255 255 0 255
	SetBorderColor 220 220 0
	SetBackgroundColor 75 75 0
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %D6 $type->ut->rare $tier->j4b !exotics_btier
	UnidentifiedItemTier >= 4
	Rarity Rare
	BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->ut->rare $tier->j3b !gear_tieredjewellery
	UnidentifiedItemTier >= 3
	Rarity Rare
	BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 255 255 0 255
	SetBorderColor 220 220 0
	SetBackgroundColor 75 75 0
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

#Show # %D4 $type->ut->rare $tier->j2b !gear_tieredjewellery

# UnidentifiedItemTier >= 2

# Rarity Rare

# BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"

# AreaLevel >= 65

# SetFontSize 42

# SetTextColor 255 255 0 255

# SetBorderColor 220 220 0

# SetBackgroundColor 75 75 0

# PlayAlertSound 2 300

# PlayEffect Yellow

# MinimapIcon 1 Yellow Diamond

Show # %D6 $type->ut->rare $tier->j4c !exotics_btier
	UnidentifiedItemTier >= 4
	Rarity Rare
	BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->ut->rare $tier->j3c !gear_tieredjewellery
	UnidentifiedItemTier >= 3
	Rarity Rare
	BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 255 255 0 255
	SetBorderColor 220 220 0
	SetBackgroundColor 75 75 0
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

#Show # %D4 $type->ut->rare $tier->j2c !gear_highlightedsize

# UnidentifiedItemTier >= 2

# Rarity Rare

# BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"

# AreaLevel >= 65

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

Show # %D5 $type->ut->rare $tier->anyremaining5gear !exotics_btier
	UnidentifiedItemTier >= 5
	Rarity Rare
	Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

#Show # %D4 $type->ut->rare $tier->anyremaining4gear !exotics_ctier

# UnidentifiedItemTier >= 4

# Rarity Rare

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 40

# SetTextColor 0 240 190 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 1 Blue Diamond

Show # %D7 $type->ut->rare $tier->anyremaining5j !exotics_btier
	UnidentifiedItemTier >= 5
	Rarity Rare
	Class == "Amulets" "Belts" "Rings"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->ut->rare $tier->anyremaining4j !gear_tieredjewellery
	UnidentifiedItemTier >= 4
	Rarity Rare
	Class == "Amulets" "Belts" "Rings"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 255 255 0 255
	SetBorderColor 220 220 0
	SetBackgroundColor 75 75 0
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

# !! Waypoint c3.exotic.state.hightierMagic : "Magic items with Mod Tier" : "ModTierMagic"

Show # %D7 $type->ut->magic $tier->gear4a !exotics_ctier
	UnidentifiedItemTier >= 4
	Rarity Magic
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D6 $type->ut->magic $tier->gear3a !exotics_ctier
	UnidentifiedItemTier >= 3
	Rarity Magic
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D4 $type->ut->magic $tier->gear2a !gear_highlightdrop2

# UnidentifiedItemTier >= 2

# Rarity Magic

# BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"

# AreaLevel >= 65

# SetFontSize 42

# SetBackgroundColor 30 0 70 255

Show # %D6 $type->ut->magic $tier->gear4b !exotics_ctier
	UnidentifiedItemTier >= 4
	Rarity Magic
	BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->ut->magic $tier->gear3b !gear_highlightdrop2
	UnidentifiedItemTier >= 3
	Rarity Magic
	BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"
	AreaLevel >= 65
	SetFontSize 42
	SetBackgroundColor 30 0 70 255

#Show # %D4 $type->ut->magic $tier->gear2b !gear_highlightdrop2

# UnidentifiedItemTier >= 2

# Rarity Magic

# BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"

# AreaLevel >= 65

# SetFontSize 42

# SetBackgroundColor 30 0 70 255

Show # %D5 $type->ut->magic $tier->gear4c !exotics_ctier
	UnidentifiedItemTier >= 4
	Rarity Magic
	BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D3 $type->ut->magic $tier->gear3c !gear_highlightdrop2

# UnidentifiedItemTier >= 3

# Rarity Magic

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# AreaLevel >= 65

# SetFontSize 42

# SetBackgroundColor 30 0 70 255

#Show # %D3 $type->ut->magic $tier->gear2c !gear_highlightdrop2

# UnidentifiedItemTier >= 2

# Rarity Magic

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# AreaLevel >= 65

# SetFontSize 42

# SetBackgroundColor 30 0 70 255

Show # %D8 $type->ut->magic $tier->j4a !exotics_btier
	UnidentifiedItemTier >= 4
	Rarity Magic
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D7 $type->ut->magic $tier->j3a !exotics_ctier
	UnidentifiedItemTier >= 3
	Rarity Magic
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D6 $type->ut->magic $tier->j2a !gear_highlightdrop2
	UnidentifiedItemTier >= 2
	Rarity Magic
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	AreaLevel >= 65
	SetFontSize 42
	SetBackgroundColor 30 0 70 255

Show # %D7 $type->ut->magic $tier->j4b !exotics_ctier
	UnidentifiedItemTier >= 4
	Rarity Magic
	BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D6 $type->ut->magic $tier->j3b !exotics_ctier
	UnidentifiedItemTier >= 3
	Rarity Magic
	BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->ut->magic $tier->j2b !gear_highlightdrop2
	UnidentifiedItemTier >= 2
	Rarity Magic
	BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"
	AreaLevel >= 65
	SetFontSize 42
	SetBackgroundColor 30 0 70 255

Show # %D6 $type->ut->magic $tier->j4c !exotics_ctier
	UnidentifiedItemTier >= 4
	Rarity Magic
	BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->ut->magic $tier->j3c !gear_highlightdrop2
	UnidentifiedItemTier >= 3
	Rarity Magic
	BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"
	AreaLevel >= 65
	SetFontSize 42
	SetBackgroundColor 30 0 70 255

#Show # %D4 $type->ut->magic $tier->j2c !gear_highlightdrop2

# UnidentifiedItemTier >= 2

# Rarity Magic

# BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"

# AreaLevel >= 65

# SetFontSize 42

# SetBackgroundColor 30 0 70 255

Show # %D5 $type->ut->magic $tier->anyremaining5gear !exotics_ctier
	UnidentifiedItemTier >= 5
	Rarity Magic
	Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#Show # %D4 $type->ut->magic $tier->anyremaining4gear !gear_highlightdrop2

# UnidentifiedItemTier >= 4

# Rarity Magic

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 42

# SetBackgroundColor 30 0 70 255

Show # %D6 $type->ut->magic $tier->anyremaining5j !exotics_ctier
	UnidentifiedItemTier >= 5
	Rarity Magic
	Class == "Amulets" "Belts" "Rings"
	AreaLevel >= 65
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D5 $type->ut->magic $tier->anyremaining4j !gear_highlightdrop2
	UnidentifiedItemTier >= 4
	Rarity Magic
	Class == "Amulets" "Belts" "Rings"
	AreaLevel >= 65
	SetFontSize 42
	SetBackgroundColor 30 0 70 255

#===============================================================================================================

# [[0900]] Endgame Flasks

#===============================================================================================================

# !! Waypoint c3.flasks.endgame : "Flasks (Endgame)" : "SalvageMisc"

Show # %D5 $type->endgame->flasks $tier->toplevelqualityflasks
	Mirrored False
	Corrupted False
	Quality > 10
	ItemLevel >= 83
	Rarity Normal Magic
	BaseType == "Ultimate Life Flask" "Ultimate Mana Flask"
	AreaLevel >= 65
	SetFontSize 40
	SetBorderColor 245 175 0
	SetBackgroundColor 10 60 40

Show # %D5 $type->endgame->flasks $tier->toplevelflasks
	Mirrored False
	Corrupted False
	ItemLevel >= 83
	Rarity Normal Magic
	BaseType == "Ultimate Life Flask" "Ultimate Mana Flask"
	AreaLevel >= 65
	SetFontSize 40
	SetBorderColor 245 175 0
	SetBackgroundColor 10 60 40

#Show # %D1 $type->endgame->flasks $tier->earlymappinglifemana !typebased_flaskcharms

# Mirrored False

# Corrupted False

# Quality 0

# ItemLevel >= 65

# Rarity Normal Magic

# BaseType == "Ultimate Life Flask" "Ultimate Mana Flask"

# AreaLevel >= 65

# AreaLevel <= 67

# SetFontSize 40

# SetBorderColor 100 100 100

# SetBackgroundColor 10 60 40

#===============================================================================================================

# [[1000]] Endgame Charms

#===============================================================================================================

# !! Waypoint c3.charms.endgame : "Charms (Endgame)" : "SalvageMisc"

Show # %D9 $type->endgame->charms $tier->topqualitycharms !exotics_btier
	Mirrored False
	Corrupted False
	Quality >= 18
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Charms"
	AreaLevel >= 65
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->endgame->charms $tier->hight1charms !typebased_flaskcharms1high
	Mirrored False
	Corrupted False
	ItemLevel >= 83
	Rarity Normal Magic
	Class == "Charms"
	BaseType == "Amethyst Charm" "Antidote Charm" "Dousing Charm" "Golden Charm" "Grounding Charm" "Stone Charm" "Thawing Charm"
	AreaLevel >= 65
	SetFontSize 40
	SetBorderColor 245 175 0
	SetBackgroundColor 10 60 40

#Show # %D4 $type->endgame->charms $tier->highothercharms !typebased_flaskcharms1high

# Mirrored False

# Corrupted False

# ItemLevel >= 83

# Rarity Normal Magic

# Class == "Charms"

# BaseType == "Amethyst Charm" "Antidote Charm" "Dousing Charm" "Golden Charm" "Grounding Charm" "Ruby Charm" "Sapphire Charm" "Silver Charm" "Staunching Charm" "Stone Charm" "Thawing Charm" "Topaz Charm"

# AreaLevel >= 65

# SetFontSize 40

# SetBorderColor 245 175 0

# SetBackgroundColor 10 60 40

#Show # %D3 $type->endgame->charms $tier->qualitycharms !typebased_flaskcharms

# Mirrored False

# Corrupted False

# Quality > 0

# Rarity Normal Magic

# Class == "Charms"

# AreaLevel >= 65

# SetFontSize 40

# SetBorderColor 100 100 100

# SetBackgroundColor 10 60 40

#Show # %D4 $type->endgame->charms $tier->earlymappingcharms !typebased_flaskcharms

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# Class == "Charms"

# BaseType == "Amethyst Charm" "Antidote Charm" "Dousing Charm" "Golden Charm" "Grounding Charm" "Stone Charm" "Thawing Charm"

# AreaLevel >= 65

# AreaLevel <= 70

# SetFontSize 40

# SetBorderColor 100 100 100

# SetBackgroundColor 10 60 40

#Show # %D2 $type->endgame->charms $tier->anycharm !typebased_flaskcharms

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# Class == "Charms"

# AreaLevel >= 65

# SetFontSize 40

# SetBorderColor 100 100 100

# SetBackgroundColor 10 60 40

#===============================================================================================================

# [[1100]] Normal and Magic Items: Endgame

#===============================================================================================================

#------------------------------------

# [1101] Normal, Magic Crafting Decorators

#------------------------------------

# !! Waypoint c4.gear.crafting.decorators : "Crafting Decorators - Visual override for crafting items" : "Technical"

Show # $type->endgame->normalcraft->decorator $tier->regulargeardecorator !gear_unstyled
	Mirrored False
	Corrupted False
	Rarity Normal Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	Continue

#Show # $type->endgame->normalcraft->decorator $tier->normal80 !gear_unstyled

# Mirrored False

# Corrupted False

# ItemLevel >= 80

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# Continue

Show # $type->endgame->normalcraft->decorator $tier->normal82 !itemproperty_toplevelbased1
	Mirrored False
	Corrupted False
	ItemLevel >= 82
	Rarity Normal Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetBorderColor 122 87 0
	Continue

Show # $type->endgame->normalcraft->decorator $tier->qualitydecorator1 !itemproperty_salvage1
	Mirrored False
	Corrupted False
	Quality >= 10
	Rarity Normal Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetFontSize 38
	SetBorderColor 180 180 180
	Continue

Show # $type->endgame->normalcraft->decorator $tier->qualitydecorator2 !itemproperty_salvage2
	Mirrored False
	Corrupted False
	Quality >= 1
	Rarity Normal Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetFontSize 35
	SetBorderColor 127 127 127
	Continue

Show # $type->endgame->normalcraft->decorator $tier->normaldecoratorjwlry !gear_unstyled
	Mirrored False
	Corrupted False
	Rarity Normal Magic
	Class == "Amulets" "Rings"
	AreaLevel >= 65
	Continue

#------------------------------------

# [1102] Additional High Value Rules

#------------------------------------

# !! Waypoint c4.gear.crafting.all : "Crafting Bases - Handpicked Magic and Normal Bases" : "Crafting"

#Show # %D3 $type->endgame->normalcraft->extra $tier->wands !itemproperty_toplevelbased1

# Mirrored False

# Corrupted False

# ItemLevel >= 81

# Rarity Normal Magic

# Class == "Sceptres" "Staves" "Wands"

# BaseType == "Dueling Wand" "Galvanic Wand" "Withered Wand"

# SetBorderColor 122 87 0

#------------------------------------

# [1103] Normal, Magic Crafting: Level 82+

#------------------------------------

# Best itemlevel bases (82)

Show # %D5 $type->endgame->normalcraft->any $tier->t1ideallevel !gear_unstyled
	Mirrored False
	Corrupted False
	ItemLevel >= 82
	Rarity Normal Magic
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"

#Show # %D2 $type->endgame->normalcraft->any $tier->t2ideallevel !gear_unstyled

# Mirrored False

# Corrupted False

# ItemLevel >= 82

# Rarity Normal Magic

# BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"

#Show # $type->endgame->normalcraft->any $tier->t3ideallevel !gear_unstyled

# Mirrored False

# Corrupted False

# ItemLevel >= 82

# Rarity Normal Magic

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

#------------------------------------

# [1104] Normal, Magic Crafting: Optional Rules

#------------------------------------

# Matrix pauses: Optional: highlight +5minion bases for sumonners (81)

#Show # $type->endgame->normalcraft->any $tier->minionsceptresoptional !itemproperty_toplevelbased1

# Mirrored False

# Corrupted False

# ItemLevel >= 81

# Rarity Normal Magic

# Class == "Sceptres"

# SetBorderColor 122 87 0

#------------------------------------

# [1105] Normal, Magic Crafting: Endgame Progression

#------------------------------------

# Matrix proceeds here. Best available bases

#Show # %D4 $type->endgame->normalcraft->any $tier->t1 !gear_unstyled

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"

# AreaLevel >= 65

#Show # %D3 $type->endgame->normalcraft->any $tier->t2onlevel !gear_unstyled

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"

# AreaLevel >= 65

# AreaLevel <= 75

#Show # %D2 $type->endgame->normalcraft->any $tier->t3onlevel !gear_unstyled

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# AreaLevel >= 65

# AreaLevel <= 70

#------------------------------------

# [1106] Normal, Magic Crafting: Rings+Amulets

#------------------------------------

# !! Waypoint c4.gear.jewellery : "Jewellery - Endgame Magic&Normal" : "Crafting"

Show # %D7 $type->endgame->jewellery $tier->jt1ideallevel !gear_highlightdrop2
	Mirrored False
	Corrupted False
	ItemLevel >= 82
	Rarity Normal Magic
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	AreaLevel >= 65
	SetFontSize 42
	SetBackgroundColor 30 0 70 255

Show # %D5 $type->endgame->jewellery $tier->jt2ideallevel !gear_highlightdrop2
	Mirrored False
	Corrupted False
	ItemLevel >= 82
	Rarity Normal Magic
	BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"
	AreaLevel >= 65
	SetFontSize 42
	SetBackgroundColor 30 0 70 255

#Show # %D3 $type->endgame->jewellery $tier->jt3ideallevel !utility_highlight3

# Mirrored False

# Corrupted False

# ItemLevel >= 82

# Rarity Normal Magic

# BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"

# AreaLevel >= 65

# SetFontSize 40

#Show # %D2 $type->endgame->jewellery $tier->jt4ideallevel !utility_highlight3

# Mirrored False

# Corrupted False

# ItemLevel >= 82

# Rarity Normal Magic

# BaseType == "Linen Belt" "Mail Belt" "Ornate Belt" "Wide Belt"

# AreaLevel >= 65

# SetFontSize 40

Show # %D5 $type->endgame->jewellery $tier->jt1 !gear_highlightdrop3
	Mirrored False
	Corrupted False
	Rarity Normal Magic
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	AreaLevel >= 65
	SetFontSize 40
	SetBackgroundColor 30 0 70 255

#Show # %D4 $type->endgame->jewellery $tier->jt2 !gear_highlightdrop3

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"

# AreaLevel >= 65

# SetFontSize 40

# SetBackgroundColor 30 0 70 255

#Show # %D3 $type->endgame->jewellery $tier->jt3 !utility_highlight4

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"

# AreaLevel >= 65

# SetFontSize 38

#Show # %D2 $type->endgame->jewellery $tier->jt4 !utility_highlight4

# Mirrored False

# Corrupted False

# Rarity Normal Magic

# BaseType == "Linen Belt" "Mail Belt" "Ornate Belt" "Wide Belt"

# AreaLevel >= 65

# SetFontSize 38

#------------------------------------

# [1107] Normal, Magic Crafting: Decorator Removers

#------------------------------------

Show # $type->endgame->normalcraft->decorator $tier->magicdecoratorremover !utility_decoremovermagic
	Mirrored False
	Corrupted False
	Rarity Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetFontSize 32
	SetTextColor 136 136 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 20 20 0 240
	Continue

Show # $type->endgame->normalcraft->decorator $tier->normaldecoratorremover !utility_decoremovernormal
	Mirrored False
	Corrupted False
	Rarity Normal
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetFontSize 32
	SetTextColor 200 200 200
	SetBorderColor 0 0 0 255
	SetBackgroundColor 20 20 0 240
	Continue

#------------------------------------

# [1108] Salvagables

#------------------------------------

# !! Waypoint c4.gear.salvagable : "Normal-Rare items, excluding High Tier & Chancing" : "SalvageMisc"

# Double Quality Currencies

#Show # %D3 $type->endgame->salvagable $tier->quality2martialany !itemproperty_salvage2

# Quality >= 10

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Bows" "Crossbows" "One Hand Maces" "Quarterstaves" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 65

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D3 $type->endgame->salvagable $tier->quality2casterany !itemproperty_salvage1

# Quality >= 10

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Sceptres" "Staves" "Wands"

# AreaLevel >= 65

# SetFontSize 38

# SetBorderColor 180 180 180

#Show # %D4 $type->endgame->salvagable $tier->quality2armorany !itemproperty_salvage1

# Quality >= 10

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 38

# SetBorderColor 180 180 180

#Show # %D4 $type->endgame->salvagable $tier->quality2flask !itemproperty_salvage1

# Quality >= 10

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Charms" "Life Flasks" "Mana Flasks"

# AreaLevel >= 65

# SetFontSize 38

# SetBorderColor 180 180 180

# Single Quality Currencies

#Show # %D2 $type->endgame->salvagable $tier->qualitymartialany !itemproperty_salvage2

# Quality >= 1

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Bows" "Crossbows" "One Hand Maces" "Quarterstaves" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 65

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D2 $type->endgame->salvagable $tier->qualitycasterany !itemproperty_salvage2

# Quality >= 1

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Sceptres" "Staves" "Wands"

# AreaLevel >= 65

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D4 $type->endgame->salvagable $tier->qualityarmorany !itemproperty_salvage2

# Quality >= 1

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel >= 65

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D4 $type->endgame->salvagable $tier->qualityflask !itemproperty_salvage2

# Quality >= 1

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Charms" "Life Flasks" "Mana Flasks"

# AreaLevel >= 65

# SetFontSize 35

# SetBorderColor 127 127 127

# Artificer Scraps

#Show # %D2 $type->endgame->salvagable $tier->socketssmall1 !itemproperty_salvage2

# Sockets > 0

# UnidentifiedItemTier <= 2

# Width <= 2

# Height <= 2

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D2 $type->endgame->salvagable $tier->socketssmall2 !itemproperty_salvage2

# Sockets > 0

# UnidentifiedItemTier <= 2

# Width <= 1

# Height <= 4

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D1 $type->endgame->salvagable $tier->socketsothers !itemproperty_salvage2

# Sockets > 0

# UnidentifiedItemTier <= 2

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 35

# SetBorderColor 127 127 127

Show # $type->special->alwaysshow $tier->any !exotics_dtier
	AlwaysShow True
	Rarity Normal Magic Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue Temp

#===============================================================================================================

# [[1200]] Hide Layer 1 - Normal and Magic Endgame Gear

#===============================================================================================================

# !! Waypoint c5.hidelayer.normalmagic : "HIDELAYER - All other endgame equipment normal&magic items" : "Technical"

#Show # %D0 $type->lowstrictnessshowlayer $tier->normalmagicendgameany !utility_unremarkabledrop

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Charms" "Crossbows" "Foci" "Gloves" "Helmets" "Life Flasks" "Mana Flasks" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 26

# SetBorderColor 0 0 0 0

# SetBackgroundColor 20 20 0 140

# DisableDropSound True

Hide # $type->hidelayer $tier->normalmagicendgame
	Rarity Normal Magic
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Charms" "Crossbows" "Foci" "Gloves" "Helmets" "Life Flasks" "Mana Flasks" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

#===============================================================================================================

# [[1300]] Endgame - Conditional Hide Layers

#===============================================================================================================

# !! Waypoint c6.rare.optionalhide : "Rare Endgame Items - (Optional) Hiding Corrupted and Mirrored Items" : "Technical"

#Hide # $type->conditionalhide $tier->idhider !utility_minimize

# Identified True

# ItemLevel >= 65

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->conditionalhide $tier->corruptedrares !utility_minimize

# AnyEnchantment False

# Corrupted True

# Identified False

# ItemLevel >= 65

# Rarity Rare

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#===============================================================================================================

# [[1400]] Endgame - Rare - Jewellery

#===============================================================================================================

# !! Waypoint c6.rare.jewellery.all : "Rare Endgame Items - Amulets, Rings" : "Rares"

Show # %D7 $type->rr->jewelleryeg $tier->t1 !gear_jewellery1
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	SetFontSize 42
	SetBackgroundColor 75 75 0
	PlayEffect Yellow
	MinimapIcon 1 White Diamond

Show # %D6 $type->rr->jewelleryeg $tier->t2 !gear_jewellery1
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"
	SetFontSize 42
	SetBackgroundColor 75 75 0
	PlayEffect Yellow
	MinimapIcon 1 White Diamond

Show # %D5 $type->rr->jewelleryeg $tier->t3 !gear_jewellery2
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"
	SetFontSize 40
	SetBackgroundColor 20 20 0 255
	PlayEffect Yellow
	MinimapIcon 1 White Diamond

#Show # %D4 $type->rr->jewelleryeg $tier->t4 !gear_jewellery2

# ItemLevel >= 82

# Rarity Rare

# BaseType == "Linen Belt" "Mail Belt" "Ornate Belt" "Wide Belt"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

# PlayEffect Yellow

# MinimapIcon 1 White Diamond

Show # %D6 $type->rr->jewellery $tier->t1 !gear_jewellery1
	ItemLevel >= 65
	Rarity Rare
	BaseType == "Amethyst Ring" "Breach Ring" "Prismatic Ring" "Solar Amulet"
	SetFontSize 42
	SetBackgroundColor 75 75 0
	PlayEffect Yellow
	MinimapIcon 1 White Diamond

Show # %D5 $type->rr->jewellery $tier->t2 !gear_jewellery1
	ItemLevel >= 65
	Rarity Rare
	BaseType == "Amber Amulet" "Azure Amulet" "Bloodstone Amulet" "Gold Amulet" "Gold Ring" "Jade Amulet" "Lapis Amulet" "Lunar Amulet" "Pearl Ring" "Plate Belt" "Ruby Ring" "Sapphire Ring" "Stellar Amulet" "Topaz Ring" "Unset Ring" "Utility Belt"
	SetFontSize 42
	SetBackgroundColor 75 75 0
	PlayEffect Yellow
	MinimapIcon 1 White Diamond

#Show # %D4 $type->rr->jewellery $tier->t3 !gear_jewellery2

# ItemLevel >= 65

# Rarity Rare

# BaseType == "Crimson Amulet" "Double Belt" "Emerald Ring" "Fine Belt" "Heavy Belt" "Iron Ring" "Lazuli Ring" "Long Belt" "Rawhide Belt"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

# PlayEffect Yellow

# MinimapIcon 1 White Diamond

#Show # %D3 $type->rr->jewellery $tier->t4 !gear_jewellery2

# ItemLevel >= 65

# Rarity Rare

# BaseType == "Linen Belt" "Mail Belt" "Ornate Belt" "Wide Belt"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

# PlayEffect Yellow

# MinimapIcon 1 White Diamond

#===============================================================================================================

# [[1500]] Endgame - Rare - Gear

#===============================================================================================================

# !! Waypoint c6.rare.t1.all : "Rare Endgame Items - T1 (75ish+ gear), no tier" : "Rares"

# T1 rares

Show # %D5 $type->rr $tier->t1_top !gear_highlightedsize
	ItemLevel >= 82
	Rarity Rare
	BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"
	SetFontSize 40
	SetBackgroundColor 20 20 0 255

#Show # %D4 $type->rr $tier->t1_other !gear_highlightedsize

# ItemLevel >= 65

# ItemLevel <= 81

# Rarity Rare

# BaseType == "Adherent Cuffs" "Akoyan Spear" "Alpha Talisman" "Ancestral Tiara" "Blacksteel Crest Shield" "Blacksteel Gauntlets" "Blacksteel Sabatons" "Bolting Quarterstaff" "Chiming Staff" "Conjurer Mantle" "Corsair Coat" "Cryptic Crown" "Cryptic Leggings" "Daggerfoot Shoes" "Dastard Armour" "Death Mail" "Desert Buckler" "Desolate Crossbow" "Drakeskin Boots" "Dueling Wand" "Falconer's Jacket" "Fanatic Greathammer" "Flying Spear" "Freebooter Cap" "Galvanic Wand" "Gemini Bow" "Gladiatorial Helm" "Golden Targe" "Grinning Mask" "Imperial Greathelm" "Jade Talisman" "Maji Talisman" "Marauding Mace" "Massive Greathammer" "Massive Mitts" "Obliterator Bow" "Omen Sceptre" "Paralysing Staff" "Polished Bracers" "Primed Quiver" "Rattling Sceptre" "Razor Quarterstaff" "Secured Wraps" "Sekhema Sandals" "Siege Crossbow" "Sinister Quarterstaff" "Sirenscale Gloves" "Skullcrusher Quarterstaff" "Sleek Jacket" "Slipstrike Vest" "Soldier Cuirass" "Tasalian Focus" "Tasalian Greaves" "Tawhoan Tower Shield" "Trarthan Cannon" "Vile Robe" "Warlord Cuirass" "Warmonger Bow" "Withered Wand" "Wolfskin Mantle"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

# !! Waypoint c6.rare.t2.all : "Rare Endgame Items - T2 (70ish+ gear), no tier" : "Rares"

#Show # %D4 $type->rr $tier->t2_top !gear_highlightedsize

# ItemLevel >= 82

# Rarity Rare

# BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D3 $type->rr $tier->t2_a1 !gear_weakrare1

# ItemLevel >= 75

# ItemLevel <= 81

# Rarity Rare

# BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"

# SetFontSize 35

# SetBackgroundColor 35 35 35 240

#Show # %D4 $type->rr $tier->t2_other !gear_highlightedsize

# ItemLevel >= 65

# ItemLevel <= 74

# Rarity Rare

# BaseType == "Acrid Wand" "Aegis Quarterstaff" "Akoyan Club" "Ancient Buckler" "Ancient Cuffs" "Apostle Leggings" "Ashbark Talisman" "Attuned Wand" "Austere Garb" "Barbed Bracers" "Baroque Targe" "Cavalry Boots" "Champion Helm" "Charmed Shoes" "Cinched Boots" "Commander Gauntlets" "Cryptic Helm" "Cultist Gauntlets" "Death Mantle" "Desert Cap" "Divine Crown" "Dragonscale Boots" "Dreaming Quarterstaff" "Elegant Crossbow" "Elegant Wraps" "Fanatic Bow" "Fang Talisman" "Faridun Mask" "Feathered Raiment" "Flexed Crossbow" "Flowing Raiment" "Fortified Hammer" "Fortress Sabatons" "Fortress Tower Shield" "Fungal Talisman" "Gemini Crossbow" "Gleaming Cuffs" "Grand Bracers" "Grand Spear" "Guardian Bow" "Guardian Spear" "Kamasan Tiara" "Leyline Focus" "Luxurious Slippers" "Masked Greathelm" "Noble Sabatons" "Opulent Gloves" "Ornate Greaves" "Ornate Mitts" "Ornate Plate" "Paragon Greathelm" "Penetrating Quiver" "Quickslip Shoes" "Rambler Jacket" "Reaping Staff" "Roaring Staff" "Ruination Maul" "Sacramental Robe" "Sacred Focus" "Saintly Crown" "Sanctified Staff" "Sandsworn Sandals" "Seastorm Mantle" "Shrouded Mail" "Siphoning Wand" "Soaring Mask" "Soaring Spear" "Soaring Targe" "Sorcerous Tiara" "Spiked Spear" "Stalking Bracers" "Stalking Spear" "Stoic Sceptre" "Strife Pick" "Striking Quarterstaff" "Swiftstalker Coat" "Tawhoan Greatclub" "Thane Mail" "Thunder Talisman" "Trapper Hood" "Utzaal Cuirass" "Vaal Crest Shield" "Vaal Gloves" "Vaal Greaves" "Vaal Mitts" "Vaal Tower Shield" "Vaal Wraps" "Visceral Quiver" "Volant Quiver" "Voltaic Staff" "Warlock Leggings" "Woven Cap" "Wrath Sceptre" "Wyrmscale Coat"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

# !! Waypoint c6.rare.t3.all : "Rare Endgame Items - T3 (65ish+ gear), no tier" : "Rares"

#Show # %D3 $type->rr $tier->t3_top !gear_weakrare1

# ItemLevel >= 82

# Rarity Rare

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# SetFontSize 35

# SetBackgroundColor 35 35 35 240

#Show # %D2 $type->rr $tier->t3_a1 !gear_weakrare2

# ItemLevel >= 75

# ItemLevel <= 81

# Rarity Rare

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# SetFontSize 32

# SetBackgroundColor 80 80 80 190

#Show # %D3 $type->rr $tier->t3_a2 !gear_weakrare1

# ItemLevel >= 70

# ItemLevel <= 74

# Rarity Rare

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# SetFontSize 35

# SetBackgroundColor 35 35 35 240

#Show # %D4 $type->rr $tier->t3_other !gear_highlightedsize

# ItemLevel >= 65

# ItemLevel <= 69

# Rarity Rare

# BaseType == "Adorned Wraps" "Anvil Maul" "Ashen Staff" "Avian Mask" "Bastion Sabatons" "Bladed Quarterstaff" "Bone Wand" "Bound Cuffs" "Bound Sandals" "Brigand Mask" "Bulwark Greaves" "Cannonade Crossbow" "Carved Greaves" "Cassis Helm" "Cavalry Bow" "Ceremonial Robe" "Condemned Talisman" "Crown Mace" "Deerstalker Hood" "Druidic Crown" "Druidic Focus" "Dunerunner Sandals" "Engraved Crossbow" "Faithful Leggings" "Feathered Mitts" "Flanged Mace" "Gelid Staff" "Gold Gloves" "Golden Mail" "Goldworked Tower Shield" "Grim Gloves" "Guardian Quarterstaff" "Gutspike Buckler" "Hallowed Focus" "Hawker's Jacket" "Heartcarver Mantle" "Inquisitor Crown" "Intricate Crest Shield" "Ironwood Greathammer" "Ironwood Shortbow" "Jungle Tiara" "Knightly Mitts" "Lizardscale Coat" "Lunar Quarterstaff" "Mammoth Targe" "Massive Spear" "Molten Hammer" "Noble Greathelm" "Orichalcum Spear" "Ornate Buckler" "Ornate Cuffs" "Pronged Spear" "Pyrophyte Staff" "Royal Tower Shield" "Sacred Maul" "Seaglass Spear" "Sekheman Crest Shield" "Serpentscale Boots" "Shamanistic Leggings" "Shrine Sceptre" "Skycrown Tiara" "Spiked Bracers" "Spiny Talisman" "Steelmail Gauntlets" "Stone Cuirass" "Stout Crossbow" "Toxic Quiver" "Trailblazer Armour" "Treerunner Shoes" "Twin Bow" "Two-Point Quiver" "Veteran Sabatons" "Volatile Wand" "Wanderer Shoes" "War Wraps" "Warded Helm" "Warmonger Greathelm" "Wildwood Talisman" "Wingbeat Talisman" "Zealot Gauntlets"

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

# !! Waypoint c6.rare.t4.all : "Rare Endgame Items - T4 (55ish+ gear), no tier" : "Rares"

#Show # %D1 $type->rr $tier->t4_a1 !gear_weakrare2

# ItemLevel >= 75

# Rarity Rare

# BaseType == "Adherent Bow" "Adherent's Raiment" "Ancient Mitts" "Arrayed Focus" "Avian Targe" "Bandit Mace" "Baroque Gloves" "Bladeguard Buckler" "Bleak Crossbow" "Blunt Quiver" "Branched Spear" "Buckled Wraps" "Bulwark Tower Shield" "Cabalist Helm" "Corsair Cap" "Covered Sabatons" "Cruel Talisman" "Cultist Focus" "Detailed Mitts" "Disintegrating Maul" "Elegant Greathelm" "Elegant Greaves" "Elegant Plate" "Elegant Slippers" "Embroidered Gloves" "Fierce Greathelm" "Fine Bracers" "Flared Boots" "Flax Sandals" "Fury Talisman" "Glowering Crest Shield" "Goldcast Cuffs" "Hallowed Crown" "Hatungo Garb" "Heavy Greathammer" "Heavy Plate" "Helix Spear" "Howling Talisman" "Hunting Shoes" "Itinerant Jacket" "Jade Tiara" "Jagged Spear" "Jingling Buckler" "Layered Vest" "Leatherbound Hood" "Lizardscale Boots" "Mantled Mail" "Marching Mace" "Militant Bow" "Noble Tower Shield" "Occultist Mantle" "Pariah Mask" "Plate Gauntlets" "Plated Vestments" "Quartered Crest Shield" "Reefsteel Greaves" "Refined Bracers" "River Raiment" "Roaring Talisman" "Runner Vest" "Sandsworn Tiara" "Serrated Quiver" "Smooth Quarterstaff" "Solid Mask" "Spined Bracers" "Spiral Wraps" "Steelpoint Shoes" "Stone Targe" "Structured Hammer" "Studded Boots" "Twin Crossbow" "Waxing Quarterstaff" "Weaver Leggings" "Wrapped Cap"

# SetFontSize 32

# SetBackgroundColor 80 80 80 190

#Show # %D2 $type->rr $tier->t4_a2 !gear_weakrare1

# ItemLevel >= 70

# ItemLevel <= 74

# Rarity Rare

# BaseType == "Adherent Bow" "Adherent's Raiment" "Ancient Mitts" "Arrayed Focus" "Avian Targe" "Bandit Mace" "Baroque Gloves" "Bladeguard Buckler" "Bleak Crossbow" "Blunt Quiver" "Branched Spear" "Buckled Wraps" "Bulwark Tower Shield" "Cabalist Helm" "Corsair Cap" "Covered Sabatons" "Cruel Talisman" "Cultist Focus" "Detailed Mitts" "Disintegrating Maul" "Elegant Greathelm" "Elegant Greaves" "Elegant Plate" "Elegant Slippers" "Embroidered Gloves" "Fierce Greathelm" "Fine Bracers" "Flared Boots" "Flax Sandals" "Fury Talisman" "Glowering Crest Shield" "Goldcast Cuffs" "Hallowed Crown" "Hatungo Garb" "Heavy Greathammer" "Heavy Plate" "Helix Spear" "Howling Talisman" "Hunting Shoes" "Itinerant Jacket" "Jade Tiara" "Jagged Spear" "Jingling Buckler" "Layered Vest" "Leatherbound Hood" "Lizardscale Boots" "Mantled Mail" "Marching Mace" "Militant Bow" "Noble Tower Shield" "Occultist Mantle" "Pariah Mask" "Plate Gauntlets" "Plated Vestments" "Quartered Crest Shield" "Reefsteel Greaves" "Refined Bracers" "River Raiment" "Roaring Talisman" "Runner Vest" "Sandsworn Tiara" "Serrated Quiver" "Smooth Quarterstaff" "Solid Mask" "Spined Bracers" "Spiral Wraps" "Steelpoint Shoes" "Stone Targe" "Structured Hammer" "Studded Boots" "Twin Crossbow" "Waxing Quarterstaff" "Weaver Leggings" "Wrapped Cap"

# SetFontSize 35

# SetBackgroundColor 35 35 35 240

#Show # %D3 $type->rr $tier->t4_other !gear_weakrare1

# ItemLevel >= 65

# ItemLevel <= 69

# Rarity Rare

# BaseType == "Adherent Bow" "Adherent's Raiment" "Ancient Mitts" "Arrayed Focus" "Avian Targe" "Bandit Mace" "Baroque Gloves" "Bladeguard Buckler" "Bleak Crossbow" "Blunt Quiver" "Branched Spear" "Buckled Wraps" "Bulwark Tower Shield" "Cabalist Helm" "Corsair Cap" "Covered Sabatons" "Cruel Talisman" "Cultist Focus" "Detailed Mitts" "Disintegrating Maul" "Elegant Greathelm" "Elegant Greaves" "Elegant Plate" "Elegant Slippers" "Embroidered Gloves" "Fierce Greathelm" "Fine Bracers" "Flared Boots" "Flax Sandals" "Fury Talisman" "Glowering Crest Shield" "Goldcast Cuffs" "Hallowed Crown" "Hatungo Garb" "Heavy Greathammer" "Heavy Plate" "Helix Spear" "Howling Talisman" "Hunting Shoes" "Itinerant Jacket" "Jade Tiara" "Jagged Spear" "Jingling Buckler" "Layered Vest" "Leatherbound Hood" "Lizardscale Boots" "Mantled Mail" "Marching Mace" "Militant Bow" "Noble Tower Shield" "Occultist Mantle" "Pariah Mask" "Plate Gauntlets" "Plated Vestments" "Quartered Crest Shield" "Reefsteel Greaves" "Refined Bracers" "River Raiment" "Roaring Talisman" "Runner Vest" "Sandsworn Tiara" "Serrated Quiver" "Smooth Quarterstaff" "Solid Mask" "Spined Bracers" "Spiral Wraps" "Steelpoint Shoes" "Stone Targe" "Structured Hammer" "Studded Boots" "Twin Crossbow" "Waxing Quarterstaff" "Weaver Leggings" "Wrapped Cap"

# SetFontSize 35

# SetBackgroundColor 35 35 35 240

# !! Waypoint c6.rare.t5.all : "Rare Endgame Items - T5 (lower), no tier" : "Rares"

#Show # %D1 $type->rr $tier->t5_a1 !gear_weakrare2

# ItemLevel >= 75

# Rarity Rare

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 32

# SetBackgroundColor 80 80 80 190

#Show # %D2 $type->rr $tier->t5_a2 !gear_weakrare2

# ItemLevel >= 70

# ItemLevel <= 74

# Rarity Rare

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 32

# SetBackgroundColor 80 80 80 190

#Show # %D3 $type->rr $tier->t5_other !gear_weakrare1

# ItemLevel >= 65

# ItemLevel <= 69

# Rarity Rare

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 35

# SetBackgroundColor 35 35 35 240

#===============================================================================================================

# [[1600]] Untiered Rare Catcher

#===============================================================================================================

# !! Waypoint c6.rare.rest : "Rare Endgame Items - Others, Salvagable bases" : "SalvageMisc"

# Double Quality Currencies

#Show # %D3 $type->rare->salvagable $tier->quality2martialany !itemproperty_salvage2

# Quality >= 10

# ItemLevel >= 65

# Rarity Rare

# Class == "Bows" "Crossbows" "One Hand Maces" "Quarterstaves" "Spears" "Talismans" "Two Hand Maces"

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D3 $type->rare->salvagable $tier->quality2casterany !itemproperty_salvage1

# Quality >= 10

# ItemLevel >= 65

# Rarity Rare

# Class == "Sceptres" "Staves" "Wands"

# SetFontSize 38

# SetBorderColor 180 180 180

#Show # %D4 $type->rare->salvagable $tier->quality2armorany !itemproperty_salvage1

# Quality >= 10

# ItemLevel >= 65

# Rarity Rare

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# SetFontSize 38

# SetBorderColor 180 180 180

# Single Quality Currencies

#Show # %D2 $type->rare->salvagable $tier->qualitymartialany !itemproperty_salvage2

# Quality >= 1

# ItemLevel >= 65

# Rarity Rare

# Class == "Bows" "Crossbows" "One Hand Maces" "Quarterstaves" "Spears" "Talismans" "Two Hand Maces"

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D2 $type->rare->salvagable $tier->qualitycasterany !itemproperty_salvage2

# Quality >= 1

# ItemLevel >= 65

# Rarity Rare

# Class == "Sceptres" "Staves" "Wands"

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D4 $type->rare->salvagable $tier->qualityarmorany !itemproperty_salvage2

# Quality >= 1

# ItemLevel >= 65

# Rarity Rare

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# SetFontSize 35

# SetBorderColor 127 127 127

# Artificer Scraps

#Show # %D2 $type->rare->salvagable $tier->socketssmall1 !itemproperty_salvage2

# Sockets > 0

# Width <= 2

# Height <= 2

# ItemLevel >= 65

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D2 $type->rare->salvagable $tier->socketssmall2 !itemproperty_salvage2

# Sockets > 0

# Width <= 1

# Height <= 4

# ItemLevel >= 65

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 35

# SetBorderColor 127 127 127

#Show # %D1 $type->rare->salvagable $tier->socketsothers !itemproperty_salvage2

# Sockets > 0

# ItemLevel >= 65

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 35

# SetBorderColor 127 127 127

#===============================================================================================================

# [[1700]] Hide Layer 2 - Rare Gear

#===============================================================================================================

#Show # %D0 $type->lowstrictnessshowlayer $tier->raresendgameany !utility_unremarkabledrop

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 65

# SetFontSize 26

# SetBorderColor 0 0 0 0

# SetBackgroundColor 20 20 0 140

# DisableDropSound True

Hide # $type->hidelayer $tier->raresendgame
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel >= 65
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

#===============================================================================================================

# [[1800]] New League Unknown Items

#===============================================================================================================

Show # $type->xenotiering $tier->s !apex_stier
	BaseType == "Aldur's Saga" "Carved Cunning" "Carved Majesty" "Celestial Alloy" "Emergent Possibility" "Olroth's Crest of the Sun" "Olroth's Saga" "Perfect Flux" "Thaumaturgic Flux (Level 20)" "The Runebinder's Alloy" "The Runefather's Alloy" "Transcendent Alloy" "Uhtred's Saga"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->xenotiering $tier->a !xeno_a
	BaseType == "Carved Mischief" "Carved Tenacity" "Cryptic Key" "Emergent Instinct" "Emergent Protection" "Emergent Vigour" "Liquid Verisium" "Masterwork Rune" "Perfect Adept Rune" "Perfect Body Rune" "Perfect Charging Rune" "Perfect Desert Rune" "Perfect Glacial Rune" "Perfect Inspiration Rune" "Perfect Iron Rune" "Perfect Mind Rune" "Perfect Rebirth Rune" "Perfect Resolve Rune" "Perfect Robust Rune" "Perfect Stone Rune" "Perfect Storm Rune" "Perfect Vision Rune" "Perfect Ward Rune" "Revelatory Wombgift" "Shattered Triskelion" "Sovereign Alloy" "Veridical Starlit Ore" "Void Flux" "Vorana's Saga" "Warding Starlit Ore"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 28 55 135 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red UpsideDownHouse

Show # %H7 $type->xenotiering $tier->b !xeno_b
	BaseType == "Blazing Flux" "Chilling Flux" "Crackling Flux" "Medved's Saga" "Prismatic Alloy" "Protective Alloy" "Starlit Ore" "Thaumaturgic Flux (Level 10)" "Thaumaturgic Flux (Level 11)" "Thaumaturgic Flux (Level 14)" "Thaumaturgic Flux (Level 8)" "Thaumaturgic Flux (Level 9)"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 70 130 225 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow UpsideDownHouse

Show # %H6 $type->xenotiering $tier->c !xeno_c
	BaseType == "Adaptive Alloy" "Banded Wombgift" "Cyclonic Alloy" "Exceptional Verisium" "Lavish Wombgift" "Mystic Alloy" "Ornate Wombgift" "Revered Starlit Ore" "Signet Wombgift" "Swift Alloy" "Thaumaturgic Flux (Level 1)" "Thaumaturgic Flux (Level 13)" "Thaumaturgic Flux (Level 17)" "Thaumaturgic Flux (Level 19)" "Thaumaturgic Flux (Level 2)" "Thaumaturgic Flux (Level 3)" "Thaumaturgic Flux (Level 4)" "Thaumaturgic Flux (Level 5)" "Thaumaturgic Flux (Level 6)" "Thaumaturgic Flux (Level 7)" "Uhtred's Crest of the Chalice" "Venerable Starlit Ore"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 125 180 240 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 White UpsideDownHouse

Show # %H5 $type->xenotiering $tier->d !xeno_d
	BaseType == "Animus Exchange" "Animus Splinters" "Bitter Dead" "Concussive Runes" "Conductive Runes" "Detonate Living" "Eternal March" "Expansive Alloy" "Explosive Transmutation" "Fist of Kalguur" "Fragments of the Past" "Frostflame Nova" "Grim Pillars" "Healing Runes" "Hollow Shell" "Leylines" "Medved's Crest of the Circle" "Powered by Verisium" "Rain of Blades" "Refutation" "Remnants of Kalguur" "Repulsion" "Runeforged Blades" "Runic Alloy" "Runic Extraction" "Runic Infusion" "Runic Reprieve" "Scouring Flame" "Skyfall" "Thaumaturgic Flux (Level 12)" "Thaumaturgic Flux (Level 15)" "Thaumaturgic Flux (Level 16)" "Thaumaturgic Flux (Level 18)" "Triskelion Cascade" "Verisium Manifestations" "Voltaic Barrier" "Vorana's Crest of the Scythe" "Wardbound Minions"
	SetFontSize 40
	SetTextColor 180 215 248 255
	SetBorderColor 180 215 248 255
	PlayAlertSound 2 300
	PlayEffect Yellow Temp
	MinimapIcon 2 White UpsideDownHouse

#Show # %H5 $type->xenotiering $tier->e !xeno_e

# SetFontSize 38

# SetTextColor 180 215 248 255

# PlayEffect Purple Temp

# MinimapIcon 2 Grey UpsideDownHouse

Hide # $type->xenotiering $tier->exhide !utility_minimize
	BaseType == "Adaptive Alloy" "Aldur's Saga" "Animus Exchange" "Animus Splinters" "Banded Wombgift" "Bitter Dead" "Blazing Flux" "Carved Cunning" "Carved Majesty" "Carved Mischief" "Carved Tenacity" "Celestial Alloy" "Chilling Flux" "Concussive Runes" "Conductive Runes" "Crackling Flux" "Cryptic Key" "Cyclonic Alloy" "Detonate Living" "Emergent Instinct" "Emergent Possibility" "Emergent Protection" "Emergent Vigour" "Eternal March" "Exceptional Verisium" "Expansive Alloy" "Explosive Transmutation" "Fist of Kalguur" "Fragments of the Past" "Frostflame Nova" "Grim Pillars" "Healing Runes" "Hollow Shell" "Lavish Wombgift" "Leylines" "Liquid Verisium" "Masterwork Rune" "Medved's Crest of the Circle" "Medved's Saga" "Mystic Alloy" "Olroth's Crest of the Sun" "Olroth's Saga" "Ornate Wombgift" "Perfect Adept Rune" "Perfect Body Rune" "Perfect Charging Rune" "Perfect Desert Rune" "Perfect Flux" "Perfect Glacial Rune" "Perfect Inspiration Rune" "Perfect Iron Rune" "Perfect Mind Rune" "Perfect Rebirth Rune" "Perfect Resolve Rune" "Perfect Robust Rune" "Perfect Stone Rune" "Perfect Storm Rune" "Perfect Vision Rune" "Perfect Ward Rune" "Powered by Verisium" "Prismatic Alloy" "Protective Alloy" "Rain of Blades" "Refutation" "Remnants of Kalguur" "Repulsion" "Revelatory Wombgift" "Revered Starlit Ore" "Runeforged Blades" "Runic Alloy" "Runic Extraction" "Runic Infusion" "Runic Reprieve" "Scouring Flame" "Shattered Triskelion" "Signet Wombgift" "Skyfall" "Sovereign Alloy" "Starlit Ore" "Swift Alloy" "Thaumaturgic Flux (Level 1)" "Thaumaturgic Flux (Level 10)" "Thaumaturgic Flux (Level 11)" "Thaumaturgic Flux (Level 12)" "Thaumaturgic Flux (Level 13)" "Thaumaturgic Flux (Level 14)" "Thaumaturgic Flux (Level 15)" "Thaumaturgic Flux (Level 16)" "Thaumaturgic Flux (Level 17)" "Thaumaturgic Flux (Level 18)" "Thaumaturgic Flux (Level 19)" "Thaumaturgic Flux (Level 2)" "Thaumaturgic Flux (Level 20)" "Thaumaturgic Flux (Level 3)" "Thaumaturgic Flux (Level 4)" "Thaumaturgic Flux (Level 5)" "Thaumaturgic Flux (Level 6)" "Thaumaturgic Flux (Level 7)" "Thaumaturgic Flux (Level 8)" "Thaumaturgic Flux (Level 9)" "The Runebinder's Alloy" "The Runefather's Alloy" "Transcendent Alloy" "Triskelion Cascade" "Uhtred's Crest of the Chalice" "Uhtred's Saga" "Venerable Starlit Ore" "Veridical Starlit Ore" "Verisium Manifestations" "Void Flux" "Voltaic Barrier" "Vorana's Crest of the Scythe" "Vorana's Saga" "Wardbound Minions" "Warding Starlit Ore"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

Show # $type->legacytemp $tier->any !xeno_a
	Class == "Augment"
	BaseType "Legacy of"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 28 55 135 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red UpsideDownHouse

Show # %H8 $type->verisium $tier->massive !xeno_b
	StackSize >= 1000
	BaseType == "Verisium"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 70 130 225 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow UpsideDownHouse

Show # %H7 $type->verisium $tier->huge !xeno_c
	StackSize >= 150
	BaseType == "Verisium"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 125 180 240 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 White UpsideDownHouse

Show # %H6 $type->verisium $tier->large !xeno_d
	StackSize >= 30
	BaseType == "Verisium"
	SetFontSize 40
	SetTextColor 180 215 248 255
	SetBorderColor 180 215 248 255
	PlayAlertSound 2 300
	PlayEffect Yellow Temp
	MinimapIcon 2 White UpsideDownHouse

Show # %H5 $type->verisium $tier->any !xeno_d
	BaseType == "Verisium"
	SetFontSize 40
	SetTextColor 180 215 248 255
	SetBorderColor 180 215 248 255
	PlayAlertSound 2 300
	PlayEffect Yellow Temp
	MinimapIcon 2 White UpsideDownHouse

#===============================================================================================================

# [[1900]] Socketables - Runes and Soul Cores

#===============================================================================================================

# !! Waypoint c7.miscgear.socketables : "Socketables - Runes and Soul Cores" : "Socketables"

#Show # %D4 $type->sockets->general $tier->socketleveling1 !currency_d

# Class == "Augment"

# BaseType == "Adept Rune" "Charging Rune" "Desert Rune" "Glacial Rune" "Greater Adept Rune" "Greater Charging Rune" "Greater Desert Rune" "Greater Glacial Rune" "Greater Iron Rune" "Greater Resolve Rune" "Greater Robust Rune" "Greater Storm Rune" "Iron Rune" "Lesser Adept Rune" "Lesser Charging Rune" "Lesser Desert Rune" "Lesser Glacial Rune" "Lesser Iron Rune" "Lesser Resolve Rune" "Lesser Robust Rune" "Lesser Storm Rune" "Lesser Ward Rune" "Resolve Rune" "Robust Rune" "Storm Rune" "Ward Rune"

# AreaLevel <= 64

# SetFontSize 40

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 240 180 100 255

# PlayAlertSound 2 300

# PlayEffect White

# MinimapIcon 2 White Circle

#Show # %D4 $type->sockets->general $tier->socketleveling2 !currency_supply2

# Class == "Augment"

# BaseType == "Body Rune" "Greater Body Rune" "Greater Inspiration Rune" "Greater Mind Rune" "Greater Rebirth Rune" "Greater Stone Rune" "Greater Vision Rune" "Inspiration Rune" "Lesser Body Rune" "Lesser Inspiration Rune" "Lesser Mind Rune" "Lesser Rebirth Rune" "Lesser Stone Rune" "Lesser Vision Rune" "Mind Rune" "Rebirth Rune" "Stone Rune" "Vision Rune"

# AreaLevel <= 64

# SetFontSize 38

# SetTextColor 220 175 132

# SetBorderColor 220 175 132

Show # $type->sockets->general $tier->s !apex_stier
	Class == "Augment"
	BaseType == "Aldur's Legacy" "Amanamu's Gaze" "Astrid's Creativity" "Breath of Aldur" "Cadigan's Epiphany" "Citaqualotl's Thesis" "Fox Idol" "Greater Rune of Alacrity" "Greater Rune of Leadership" "Guatelitzi's Thesis" "Idol of Ralakesh" "Idol of Sirrius" "Jiquani's Thesis" "Kurgal's Gaze" "Quipolatl's Thesis" "Raven-Touched Shard" "Serle's Triumph" "Soul Core of Azcapa" "Soul Core of Quipolatl" "Tecrod's Gaze" "Tzamoto's Soul Core of Ferocity" "Ulaman's Gaze" "Xopec's Soul Core of Power"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->sockets->general $tier->a !currency_a
	Class == "Augment"
	BaseType == "Atziri's Soul Core of Alacrity" "Atziri's Soul Core of Devotion" "Atziri's Soul Core of Inoculation" "Atziri's Soul Core of Vitality" "Betrayal of Aldur" "Countess Seske's Rune of Archery" "Estazunti's Soul Core of Convalescence" "Farrul's Rune of the Chase" "Greater Rune of Tithing" "Guatelitzi's Soul Core of Endurance" "Hedgewitch Assandra's Rune of Wisdom" "Idol of Alira" "Idol of Eeshta" "Idol of Egrin" "Idol of Eramir" "Jiquani's Soul Core of Abundance" "Jiquani's Soul Core of Automation" "Jiquani's Soul Core of Malediction" "Jiquani's Soul Core of Munitions" "Jiquani's Soul Core of Quaking" "Jiquani's Soul Core of Radiance" "Jiquani's Soul Core of Rallying" "Jiquani's Soul Core of Rippling" "Jiquani's Soul Core of Severing" "Jiquani's Soul Core of Snares" "Jiquani's Soul Core of Squalls" "Jiquani's Soul Core of Targeting" "Jiquani's Soul Core of Thundering" "Katla's Gloom" "Kolr's Hunt" "Masterwork Rune" "Medved's Tending" "Opiloti's Soul Core of Assault" "Quipolatl's Soul Core of Flow" "Rabbit Idol" "Saqawal's Rune of the Sky" "Soul Core of Citaqualotl" "Soul Core of Jiquani" "Soul Core of Tacati" "Soul Core of Zantipi" "The Greatwolf's Rune of Claws" "The Greatwolf's Rune of Willpower" "Uhtred's Sidereus" "Vorana's Carnage"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->sockets->general $tier->b !currency_b
	Class == "Augment"
	BaseType == "Ancient Rune of Detonation" "Craiceann's Rune of Warding" "Greater Ward Rune" "Hawk Idol" "Idol of Greust" "Idol of Grold" "Idol of Oak" "Idol of the Pharisee" "Idol of Thruldana" "Idol of Yeena" "Ire of Aldur" "Panther Idol" "Passion of Aldur" "Primate Idol" "Rune of Consistency" "Rune of Vitality" "Saqawal's Rune of Memory" "Soul Core of Atmohua" "Soul Core of Cholotl" "Soul Core of Opiloti" "Soul Core of Puhuarte" "Soul Core of Ticaba" "Soul Core of Topotante" "Soul Core of Tzamoto" "Soul Core of Xopec" "Soul Core of Zalatl" "Stoat Idol" "Thane Grannell's Rune of Mastery" "Thane Leld's Rune of Spring" "Thrud's Might" "Warding Rune of Armature" "Warding Rune of Nourishment" "Warding Rune of Stability" "Xipocado's Soul Core of Dominion"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->sockets->general $tier->c !currency_c
	Class == "Augment"
	BaseType == "Ancient Rune of Animosity" "Ancient Rune of Control" "Ancient Rune of Decay" "Ancient Rune of Discovery" "Ancient Rune of Dueling" "Ancient Rune of Prowess" "Ancient Rune of Shattering" "Ancient Rune of the Horde" "Ancient Rune of the Titan" "Atmohua's Soul Core of Retreat" "Bear Idol" "Boar Idol" "Cat Idol" "Cholotl's Soul Core of War" "Citaqualotl's Soul Core of Foulness" "Courtesan Mannan's Rune of Cruelty" "Craiceann's Rune of Recovery" "Farrul's Rune of Grace" "Farrul's Rune of the Hunt" "Fenumus' Rune of Agony" "Fenumus' Rune of Draining" "Fenumus' Rune of Spinning" "Greater Rune of Nobility" "Hayoxi's Soul Core of Heatproofing" "Idol of Kraityn" "Idol of Maxarius" "Idol of Silk" "Idol of the Martyr" "Idol of the Sycophant" "Lady Hestra's Rune of Winter" "Ox Idol" "Rune of Accumulation" "Rune of Acrobatics" "Rune of Culmination" "Rune of Foundations" "Rune of Reach" "Rune of Renown" "Rune of the Blossom" "Rune of the Hunt" "Rune of the Prism" "Saqawal's Rune of Erosion" "Snake Idol" "Tacati's Soul Core of Affliction" "Thane Girt's Rune of Wildness" "Thane Myrk's Rune of Summer" "Topotante's Soul Core of Dampening" "Uromoti's Soul Core of Attenuation" "Warding Rune of Annihilation" "Warding Rune of Bodyguards" "Warding Rune of Disintegration" "Warding Rune of Equinox" "Warding Rune of Glancing" "Warding Rune of Heart" "Warding Rune of Hollowing" "Warding Rune of Reinforcement" "Warding Rune of Salvaging" "Wolf Idol" "Zalatl's Soul Core of Insulation"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 139 87 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Circle

Show # %H5 $type->sockets->general $tier->d !currency_d
	Class == "Augment"
	BaseType == "Ancient Rune of Retaliation" "Ancient Rune of Splinters" "Ancient Rune of Witchcraft" "Greater Adept Rune" "Greater Charging Rune" "Greater Desert Rune" "Greater Glacial Rune" "Greater Iron Rune" "Greater Resolve Rune" "Greater Robust Rune" "Greater Storm Rune" "Owl Idol" "Rune of Confrontation" "Rune of Vital Flame" "Stag Idol" "Warding Rune of Courage" "Warding Rune of Desperation" "Warding Rune of Obsession" "Warding Rune of Protection" "Warding Rune of Symbiosis"
	SetFontSize 40
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 180 100 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Hide # %H4 $type->sockets->general $tier->e !currency_e
	Class == "Augment"
	BaseType == "Greater Body Rune" "Greater Inspiration Rune" "Greater Mind Rune" "Greater Rebirth Rune" "Greater Stone Rune" "Greater Vision Rune"
	SetFontSize 40
	SetTextColor 240 207 132
	SetBorderColor 240 207 132

Hide # %H3 $type->sockets->general $tier->supplylow !currency_supply2
	Class == "Augment"
	BaseType == "Adept Rune" "Body Rune" "Charging Rune" "Desert Rune" "Glacial Rune" "Inspiration Rune" "Iron Rune" "Lesser Adept Rune" "Lesser Body Rune" "Lesser Charging Rune" "Lesser Desert Rune" "Lesser Glacial Rune" "Lesser Inspiration Rune" "Lesser Iron Rune" "Lesser Mind Rune" "Lesser Rebirth Rune" "Lesser Resolve Rune" "Lesser Robust Rune" "Lesser Stone Rune" "Lesser Storm Rune" "Lesser Vision Rune" "Lesser Ward Rune" "Mind Rune" "Rebirth Rune" "Resolve Rune" "Robust Rune" "Stone Rune" "Storm Rune" "Vision Rune" "Ward Rune"
	SetFontSize 38
	SetTextColor 220 175 132
	SetBorderColor 220 175 132

Hide # $type->sockets->general $tier->exhide !utility_minimize
	Class == "Augment"
	BaseType == "Ancient Rune of Animosity" "Ancient Rune of Control" "Ancient Rune of Decay" "Ancient Rune of Detonation" "Ancient Rune of Discovery" "Ancient Rune of Dueling" "Ancient Rune of Prowess" "Ancient Rune of Retaliation" "Ancient Rune of Shattering" "Ancient Rune of Splinters" "Ancient Rune of the Horde" "Ancient Rune of the Titan" "Ancient Rune of Witchcraft" "Atmohua's Soul Core of Retreat" "Bear Idol" "Boar Idol" "Body Rune" "Cat Idol" "Cholotl's Soul Core of War" "Citaqualotl's Soul Core of Foulness" "Courtesan Mannan's Rune of Cruelty" "Craiceann's Rune of Recovery" "Craiceann's Rune of Warding" "Farrul's Rune of Grace" "Farrul's Rune of the Hunt" "Fenumus' Rune of Agony" "Fenumus' Rune of Draining" "Fenumus' Rune of Spinning" "Greater Body Rune" "Greater Inspiration Rune" "Greater Mind Rune" "Greater Rebirth Rune" "Greater Rune of Nobility" "Greater Stone Rune" "Greater Vision Rune" "Greater Ward Rune" "Hawk Idol" "Hayoxi's Soul Core of Heatproofing" "Idol of Greust" "Idol of Grold" "Idol of Kraityn" "Idol of Maxarius" "Idol of Oak" "Idol of Silk" "Idol of the Martyr" "Idol of the Pharisee" "Idol of the Sycophant" "Idol of Thruldana" "Idol of Yeena" "Inspiration Rune" "Ire of Aldur" "Lady Hestra's Rune of Winter" "Lesser Body Rune" "Lesser Inspiration Rune" "Lesser Mind Rune" "Lesser Rebirth Rune" "Lesser Stone Rune" "Lesser Vision Rune" "Mind Rune" "Owl Idol" "Ox Idol" "Panther Idol" "Passion of Aldur" "Primate Idol" "Rebirth Rune" "Rune of Accumulation" "Rune of Acrobatics" "Rune of Confrontation" "Rune of Consistency" "Rune of Culmination" "Rune of Foundations" "Rune of Reach" "Rune of Renown" "Rune of the Blossom" "Rune of the Hunt" "Rune of the Prism" "Rune of Vital Flame" "Rune of Vitality" "Saqawal's Rune of Erosion" "Saqawal's Rune of Memory" "Snake Idol" "Soul Core of Atmohua" "Soul Core of Cholotl" "Soul Core of Opiloti" "Soul Core of Puhuarte" "Soul Core of Ticaba" "Soul Core of Topotante" "Soul Core of Tzamoto" "Soul Core of Xopec" "Soul Core of Zalatl" "Stag Idol" "Stoat Idol" "Stone Rune" "Tacati's Soul Core of Affliction" "Thane Girt's Rune of Wildness" "Thane Grannell's Rune of Mastery" "Thane Leld's Rune of Spring" "Thane Myrk's Rune of Summer" "Thrud's Might" "Topotante's Soul Core of Dampening" "Uromoti's Soul Core of Attenuation" "Vision Rune" "Warding Rune of Annihilation" "Warding Rune of Armature" "Warding Rune of Bodyguards" "Warding Rune of Courage" "Warding Rune of Desperation" "Warding Rune of Disintegration" "Warding Rune of Equinox" "Warding Rune of Glancing" "Warding Rune of Heart" "Warding Rune of Hollowing" "Warding Rune of Nourishment" "Warding Rune of Obsession" "Warding Rune of Protection" "Warding Rune of Reinforcement" "Warding Rune of Salvaging" "Warding Rune of Stability" "Warding Rune of Symbiosis" "Wolf Idol" "Xipocado's Soul Core of Dominion" "Zalatl's Soul Core of Insulation"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

Show # $type->sockets->general $tier->restex !utility_unknownitem
	Class == "Augment"
	BaseType "Idol" "Rune" "Soul Core"
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#===============================================================================================================

# [[2000]] Jewels

#===============================================================================================================

# !! Waypoint c7.jewels.generic.all : "Jewels" : "Exotics"

Show # $type->jewels->generic $tier->anytimelost !exotics_btier
	Rarity Normal Magic Rare
	Class == "Jewels"
	BaseType == "Time-Lost Emerald" "Time-Lost Ruby" "Time-Lost Sapphire"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->jewels->generic $tier->anycorruptedmod !exotics_btier
	AnyEnchantment True
	Corrupted True
	Rarity Normal Magic Rare
	Class == "Jewels"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->jewels->generic $tier->any5modded !exotics_btier
	Corrupted True
	Rarity Normal Magic Rare
	Class == "Jewels"
	HasExplicitMod >=5 "a" "o" "e" "u" "i" "y"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->jewels->generic $tier->anyrare !gear_jewelrare
	Rarity Rare
	Class == "Jewels"
	BaseType == "Emerald" "Ruby" "Sapphire"
	SetFontSize 42
	SetTextColor 220 220 0
	SetBorderColor 220 220 0
	SetBackgroundColor 75 75 0
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Diamond

Show # %H5 $type->jewels->generic $tier->anymagic !gear_jewelmagic
	Rarity Normal Magic
	Class == "Jewels"
	BaseType == "Emerald" "Ruby" "Sapphire"
	SetFontSize 42
	SetTextColor 0 70 255 255
	SetBorderColor 0 70 255 255
	SetBackgroundColor 30 0 70 255
	PlayAlertSound 2 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

#===============================================================================================================

# [[2100]] Relics

#===============================================================================================================

# !! Waypoint c7.relics.generic.all : "Relics (Trial of the Sekhema)" : "Fragments"

Show # $type->relics->generic $tier->any !exotics_dtier
	Rarity Normal Magic
	BaseType == "Amphora Relic" "Coffer Relic" "Incense Relic" "Seal Relic" "Tapestry Relic" "Urn Relic" "Vase Relic"
	SetFontSize 40
	SetTextColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue Temp

#===============================================================================================================

# [[2200]] Gems and Uncut Gems

#===============================================================================================================

# !! Waypoint c8.gems.uncut : "Gems - Uncut" : "Gems"

Show # $type->gems->lineage $tier->s !apex_stier
	Class == "Skill Gems" "Support Gems"
	BaseType == "Ailith's Chimes" "Arbiter's Ignition" "Atalui's Bloodletting" "Atziri's Impatience" "Breachlord's Amalgam" "Breachlord's Rift" "Brutus' Brain" "Catha's Brilliance" "Dialla's Desire" "Esh's Prowess" "Esh's Radiance" "Garukhan's Resolve" "Her Declaration" "Ixchel's Torment" "Khatal's Rejuvenation" "Mórrigan's Insight" "Olroth's Conviction" "Olroth's Hubris" "Rakiata's Flow" "Rigwald's Ferocity" "Seraph's Heart" "Sione's Temper" "Styrn's Ferocity" "Tangmazu's Thurible" "Tecrod's Revenge" "Trickster's Shard" "Tul's Stillness" "Uhtred's Augury" "Uhtred's Constellation" "Uhtred's Exodus" "Uhtred's Omen" "Uul-Netol's Embrace" "Vorana's Siege" "Xoph's Pyre" "Zarokh's Revolt" "Zerphi's Infamy"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->gems->lineage $tier->a !uniques_a
	Class == "Skill Gems" "Support Gems"
	BaseType == "Ahn's Citadel" "Amanamu's Tithe" "Atziri's Call" "Atziri's Communion" "Doedre's Undoing" "Dreamer's Knell" "Eonyr's Thunder" "Hayoxi's Fulmination" "Oisín's Oath" "Styrn's Mountain" "Uhtred's Rite" "Zarokh's Refrain"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

Show # %H7 $type->gems->lineage $tier->b !uniques_x
	Class == "Skill Gems" "Support Gems"
	BaseType == "Arbiter's Reach" "Atziri's Allure" "Einhar's Beastrite" "Guatelitzi's Ablation" "Kaom's Madness" "Kulemak's Dominion" "Medved's Felling" "Prototype Seventeen" "Ratha's Assault" "Romira's Requital" "Tul's Avalanche" "Uruk's Smelting"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # %H6 $type->gems->lineage $tier->c !uniques_b
	Class == "Skill Gems" "Support Gems"
	BaseType == "Arakaali's Lust" "Arjun's Medal" "Bhatair's Vengeance" "Cirel's Cultivation" "Daresso's Passion" "Dominus' Grasp" "Helbrym's Hide" "Kalisa's Crescendo" "Kurgal's Leash" "Morgana's Tempest" "Paquate's Pact" "Tacati's Ire" "Tasalio's Rhythm" "Tawhoa's Tending" "Varashta's Blessing" "Vilenta's Propulsion" "Vruun's Aftermath" "Vruun's Inevitability" "Xibaqua's Rending"
	SetFontSize 42
	SetTextColor 188 96 37 255
	SetBorderColor 188 96 37 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 1 Brown Star

# Level20

Show # $type->gems->uncut $tier->spirit20 !apex_stier
	GemLevel >= 20
	BaseType "Uncut Spirit Gem"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->gems->uncut $tier->skill20 !apex_stier
	GemLevel >= 20
	BaseType "Uncut Skill Gem"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

# Level19

Show # %H6 $type->gems->uncut $tier->spirit19 !typebased_gems1
	GemLevel 19
	BaseType "Uncut Spirit Gem"
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240
	SetBackgroundColor 6 0 60
	PlayAlertSound 2 300
	PlayEffect Cyan
	MinimapIcon 1 Cyan Triangle

Show # %H6 $type->gems->uncut $tier->skill19 !typebased_gems1
	GemLevel 19
	BaseType "Uncut Skill Gem"
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240
	SetBackgroundColor 6 0 60
	PlayAlertSound 2 300
	PlayEffect Cyan
	MinimapIcon 1 Cyan Triangle

# Spirit Gem Progression

Hide # %H4 $type->gems->uncut $tier->spiritgemprogression18 !typebased_gems2
	GemLevel 18
	BaseType "Uncut Spirit Gem"
	AreaLevel <= 79
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H4 $type->gems->uncut $tier->spiritgemprogression17 !typebased_gems2
	GemLevel 17
	BaseType "Uncut Spirit Gem"
	AreaLevel <= 77
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H4 $type->gems->uncut $tier->spiritgemprogression16 !typebased_gems2
	GemLevel 16
	BaseType "Uncut Spirit Gem"
	AreaLevel <= 73
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H4 $type->gems->uncut $tier->spiritgemprogression15 !typebased_gems2
	GemLevel 15
	BaseType "Uncut Spirit Gem"
	AreaLevel <= 69
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H4 $type->gems->uncut $tier->spiritgemprogression14 !typebased_gems2
	GemLevel 14
	BaseType "Uncut Spirit Gem"
	AreaLevel <= 65
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

# Skill Gem Progression

Hide # %H3 $type->gems->uncut $tier->skillgemprogression18 !typebased_gems2
	GemLevel 18
	BaseType "Uncut Skill Gem"
	AreaLevel <= 79
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H3 $type->gems->uncut $tier->skillgemprogression17 !typebased_gems2
	GemLevel 17
	BaseType "Uncut Skill Gem"
	AreaLevel <= 77
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H3 $type->gems->uncut $tier->skillgemprogression16 !typebased_gems2
	GemLevel 16
	BaseType "Uncut Skill Gem"
	AreaLevel <= 73
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H3 $type->gems->uncut $tier->skillgemprogression15 !typebased_gems2
	GemLevel 15
	BaseType "Uncut Skill Gem"
	AreaLevel <= 69
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H3 $type->gems->uncut $tier->skillgemprogression14 !typebased_gems2
	GemLevel 14
	BaseType "Uncut Skill Gem"
	AreaLevel <= 65
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

# All gems during campaign with sounds

Show # %H5 $type->gems->uncut $tier->spiritcampaign !typebased_gems2
	BaseType "Uncut Spirit Gem"
	AreaLevel <= 64
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240
	PlayAlertSound 2 300
	PlayEffect Cyan
	MinimapIcon 1 Cyan Triangle

Show # %H5 $type->gems->uncut $tier->skillcampaign !typebased_gems2
	BaseType "Uncut Skill Gem"
	AreaLevel <= 64
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240
	PlayAlertSound 2 300
	PlayEffect Cyan
	MinimapIcon 1 Cyan Triangle

Show # %H5 $type->gems->uncut $tier->supportcampaign !typebased_gems2
	BaseType "Uncut Support Gem"
	AreaLevel <= 64
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240
	PlayAlertSound 2 300
	PlayEffect Cyan
	MinimapIcon 1 Cyan Triangle

Show # %H5 $type->gems->uncut $tier->supportearlymaps !typebased_gems2
	BaseType "Uncut Support Gem"
	AreaLevel <= 78
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240
	PlayAlertSound 2 300
	PlayEffect Cyan
	MinimapIcon 1 Cyan Triangle

# Lower highlight for lower level gems in maps

Hide # %H4 $type->gems->uncut $tier->otherspiriteg !typebased_gems3
	BaseType "Uncut Spirit Gem"
	AreaLevel >= 65
	SetFontSize 35
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Hide # %H3 $type->gems->uncut $tier->otherskilleg !typebased_gems3
	BaseType "Uncut Skill Gem"
	AreaLevel >= 65
	SetFontSize 35
	SetTextColor 20 240 240
	SetBorderColor 20 240 240

Show # %H6 $type->gems->uncut $tier->othersupporteg !typebased_gems3
	BaseType "Uncut Support Gem"
	AreaLevel >= 65
	SetFontSize 35
	SetTextColor 20 240 240
	SetBorderColor 20 240 240
	PlayEffect Cyan Temp

# Hider for filterblade

Hide # $type->gems->uncut $tier->exhide !utility_minimize
	BaseType "Uncut Skill Gem" "Uncut Spirit Gem" "Uncut Support Gem"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

# !! Waypoint c8.gems.others : "Gems - Specific" : "Gems"

Show # $type->gems $tier->upgradedgemstwice !apex_stier
	TwiceCorrupted True
	Quality > 20
	GemLevel > 20
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->gems $tier->upgradedgemslevel !exotics_btier
	TwiceCorrupted True
	Class == "Skill Gems" "Support Gems"
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->gems $tier->any !typebased_gems2
	Class == "Skill Gems" "Support Gems"
	SetFontSize 42
	SetTextColor 20 240 240
	SetBorderColor 20 240 240
	PlayAlertSound 2 300
	PlayEffect Cyan
	MinimapIcon 1 Cyan Triangle

#===============================================================================================================

# [[2300]] Waystones

#===============================================================================================================

# !! Waypoint c9.waystones.all : "Waystones - Override All" : "Maps"

#===============================================================================================================

# [[2400]] Normal Waystone Progression

#===============================================================================================================

# !! Waypoint c9.waystone.special : "Waystones - Override Hider Rules" : "Maps"

#Hide # $type->waystone->hiders $tier->corruptedmaphider !utility_minimize

# Corrupted True

# Rarity Normal Magic

# Class == "Waystones"

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # $type->waystone->hiders $tier->mirroredmaphider !utility_minimize

# Mirrored True

# Rarity Normal Magic

# Class == "Waystones"

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#------------------------------------

# [2401] Generic Decorators

#------------------------------------

# !! Waypoint c9.waystone.decorators.all : "Waystones - Decorators" : "Maps"

Show # $type->waystones $tier->decomap1 !maps_deco1
	WaystoneTier >= 15
	Class == "Waystones"
	SetFontSize 42
	SetBorderColor 0 0 0 255
	Continue

Show # $type->waystones $tier->decomap2 !maps_deco2
	WaystoneTier >= 12
	WaystoneTier <= 14
	Class == "Waystones"
	SetFontSize 40
	SetBorderColor 0 0 0 255
	Continue

Show # $type->waystones $tier->decomap3 !maps_deco3
	WaystoneTier >= 6
	WaystoneTier <= 11
	Class == "Waystones"
	SetFontSize 40
	SetBorderColor 200 200 200 255
	Continue

Show # $type->waystones $tier->decomap4 !maps_deco4
	WaystoneTier >= 1
	WaystoneTier <= 5
	Class == "Waystones"
	SetFontSize 40
	SetBorderColor 200 200 200 255
	Continue

Show # $type->waystones $tier->deco_wsup_t16 !maps_decotierupgrade
	WaystoneTier >= 16
	Class == "Waystones"
	AreaLevel < 80
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t15 !maps_decotierupgrade
	WaystoneTier >= 15
	Class == "Waystones"
	AreaLevel < 79
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t14 !maps_decotierupgrade
	WaystoneTier >= 14
	Class == "Waystones"
	AreaLevel < 78
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t13 !maps_decotierupgrade
	WaystoneTier >= 13
	Class == "Waystones"
	AreaLevel < 76
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t12 !maps_decotierupgrade
	WaystoneTier >= 12
	Class == "Waystones"
	AreaLevel < 75
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t11 !maps_decotierupgrade
	WaystoneTier >= 11
	Class == "Waystones"
	AreaLevel < 74
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t10 !maps_decotierupgrade
	WaystoneTier >= 10
	Class == "Waystones"
	AreaLevel < 73
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t9 !maps_decotierupgrade
	WaystoneTier >= 9
	Class == "Waystones"
	AreaLevel < 72
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t8 !maps_decotierupgrade
	WaystoneTier >= 8
	Class == "Waystones"
	AreaLevel < 72
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t7 !maps_decotierupgrade
	WaystoneTier >= 7
	Class == "Waystones"
	AreaLevel < 71
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t6 !maps_decotierupgrade
	WaystoneTier >= 6
	Class == "Waystones"
	AreaLevel < 70
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t5 !maps_decotierupgrade
	WaystoneTier >= 5
	Class == "Waystones"
	AreaLevel < 69
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t4 !maps_decotierupgrade
	WaystoneTier >= 4
	Class == "Waystones"
	AreaLevel < 68
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t3 !maps_decotierupgrade
	WaystoneTier >= 3
	Class == "Waystones"
	AreaLevel < 67
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t2 !maps_decotierupgrade
	WaystoneTier >= 2
	Class == "Waystones"
	AreaLevel < 66
	SetBorderColor 220 50 0 255
	Continue

Show # $type->waystones $tier->deco_wsup_t1 !maps_decotierupgrade
	WaystoneTier >= 1
	Class == "Waystones"
	AreaLevel < 65
	SetBorderColor 220 50 0 255
	Continue

#Show # $type->waystones $tier->decomap1overleveled !maps_decooverlevel

# WaystoneTier >= 1

# WaystoneTier <= 11

# Class == "Waystones"

# AreaLevel >= 78

# SetFontSize 38

# SetBorderColor 200 200 200 255

# Continue

#Show # $type->waystones $tier->decomap2overleveled !maps_decooverlevel

# WaystoneTier >= 1

# WaystoneTier <= 8

# Class == "Waystones"

# AreaLevel >= 76

# SetFontSize 38

# SetBorderColor 200 200 200 255

# Continue

#Show # $type->waystones $tier->decomap3overleveled !maps_decooverlevel

# WaystoneTier >= 1

# WaystoneTier <= 6

# Class == "Waystones"

# AreaLevel >= 74

# SetFontSize 38

# SetBorderColor 200 200 200 255

# Continue

#Show # $type->waystones $tier->decomap4overleveled !maps_decooverlevel

# WaystoneTier >= 1

# WaystoneTier <= 3

# Class == "Waystones"

# AreaLevel >= 72

# SetFontSize 38

# SetBorderColor 200 200 200 255

# Continue

# semi-strict, currently: t14 map, find: t1 map, shown based on t1

Show # $type->waystones $tier->deco_corruptedmod !exotics_corrupthigh
	AnyEnchantment True
	Class == "Waystones"
	SetBorderColor 250 0 0 255
	Continue

#------------------------------------

# [2402] Special Maps

#------------------------------------

# !! Waypoint c9.waystone.decorators.special : "Waystones - Special Cases" : "Maps"

Show # $type->waystones $tier->corrupted8high !maps_specialb
	Corrupted True
	WaystoneTier >= 14
	Class == "Waystones"
	HasExplicitMod >=7 "a" "o" "e" "u" "i" "y"
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Red
	MinimapIcon 0 Purple Square

Show # $type->waystones $tier->enchanted1 !maps_specialb
	AnyEnchantment True
	WaystoneTier >= 14
	Class == "Waystones"
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Red
	MinimapIcon 0 Purple Square

Show # %D5 $type->waystones $tier->enchanted2 !maps_specialc
	AnyEnchantment True
	WaystoneTier >= 11
	WaystoneTier <= 13
	Class == "Waystones"
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 200 200 200 255
	PlayAlertSound 4 300
	PlayEffect Yellow
	MinimapIcon 2 Purple Square

#Show # %D4 $type->waystones $tier->enchanted34 !maps_specialc

# AnyEnchantment True

# WaystoneTier >= 1

# WaystoneTier <= 10

# Class == "Waystones"

# SetTextColor 145 30 220 255

# SetBorderColor 145 30 220 255

# SetBackgroundColor 200 200 200 255

# PlayAlertSound 4 300

# PlayEffect Yellow

# MinimapIcon 2 Purple Square

Hide # %H4 $type->waystones $tier->corrupted8 !maps_specialc
	Corrupted True
	Class == "Waystones"
	HasExplicitMod >=7 "a" "o" "e" "u" "i" "y"
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 200 200 200 255

#------------------------------------

# [2403] Waystone progression

#------------------------------------

# !! Waypoint c9.waystone.generic.t16 : "Waystones - t15-t16" : "Maps"

Show # $type->waystones $tier->waystone_t16 !maps_specialb
	WaystoneTier >= 16
	Class == "Waystones"
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Red
	MinimapIcon 0 Purple Square

Show # $type->waystones $tier->waystone_t15 !maps_regularhighest
	WaystoneTier 15
	Class == "Waystones"
	SetTextColor 0 0 0 255
	SetBackgroundColor 235 235 235 255
	PlayAlertSound 5 300
	PlayEffect Yellow
	MinimapIcon 1 Red Square

# !! Waypoint c9.waystone.generic.t14 : "Waystones - t12-t14" : "Maps"

Show # %D5 $type->waystones $tier->waystone_t14 !maps_regularhigh
	WaystoneTier 14
	Class == "Waystones"
	SetTextColor 0 0 0 255
	SetBackgroundColor 200 200 200 255
	PlayAlertSound 4 300
	PlayEffect Yellow Temp
	MinimapIcon 1 Yellow Square

#Show # %DS3 $type->waystones $tier->waystone_t13 !maps_regularhigh

# WaystoneTier 13

# Class == "Waystones"

# SetTextColor 0 0 0 255

# SetBackgroundColor 200 200 200 255

#Show # %DS3 $type->waystones $tier->waystone_t12 !maps_regularhigh

# WaystoneTier 12

# Class == "Waystones"

# SetTextColor 0 0 0 255

# SetBackgroundColor 200 200 200 255

# !! Waypoint c9.waystone.generic.t11 : "Waystones - t7-t11" : "Maps"

#Show # %DS3 $type->waystones $tier->waystone_t11 !maps_regularmid

# WaystoneTier 11

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t10 !maps_regularmid

# WaystoneTier 10

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t9 !maps_regularmid

# WaystoneTier 9

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t8 !maps_regularmid

# WaystoneTier 8

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t7 !maps_regularmid

# WaystoneTier 7

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

# !! Waypoint c9.waystone.generic.t6 : "Waystones - T1-T6" : "Maps"

#Show # %DS3 $type->waystones $tier->waystone_t6 !maps_regularlow

# WaystoneTier 6

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t5 !maps_regularlow

# WaystoneTier 5

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t4 !maps_regularlow

# WaystoneTier 4

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t3 !maps_regularlow

# WaystoneTier 3

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t2 !maps_regularlow

# WaystoneTier 2

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %DS3 $type->waystones $tier->waystone_t1 !maps_regularlow

# WaystoneTier 1

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->waystones $tier->waystone_rares_other !maps_regularlow

# Rarity Rare

# Class == "Waystones"

# SetTextColor 255 255 255 255

# SetBackgroundColor 20 20 0 255

# PlayAlertSound 4 300

# PlayEffect White Temp

# MinimapIcon 2 White Square

Hide # $type->waystones $tier->exhide !utility_minimize
	WaystoneTier <= 15
	Rarity Normal Magic Rare
	Class == "Waystones"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

Show # $type->waystones $tier->restex !utility_unknownitem
	Class == "Waystones"
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#===============================================================================================================

# [[2500]] Currency - Exceptions - Leveling Currencies

#===============================================================================================================

# !! Waypoint c9.currency.leveling.nonstacked : "Tierlist - Currency - Leveling Currency" : "Leveling"

#Show # %D4 $type->currency->leveling $tier->jewellers !currency_c

# Class == "Stackable Currency"

# BaseType == "Lesser Jeweller's Orb"

# AreaLevel <= 64

# SetFontSize 42

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 245 139 87 255

# PlayAlertSound 2 300

# PlayEffect White

# MinimapIcon 1 Yellow Circle

Show # %D5 $type->currency->leveling $tier->rare
	Class == "Stackable Currency"
	BaseType == "Artificer's Orb" "Gnawed Collarbone" "Gnawed Jawbone" "Gnawed Rib" "Greater Orb of Augmentation" "Greater Orb of Transmutation" "Lesser Essence of Abrasion" "Lesser Essence of Alacrity" "Lesser Essence of Battle" "Lesser Essence of Command" "Lesser Essence of Electricity" "Lesser Essence of Enhancement" "Lesser Essence of Flames" "Lesser Essence of Grounding" "Lesser Essence of Haste" "Lesser Essence of Ice" "Lesser Essence of Insulation" "Lesser Essence of Opulence" "Lesser Essence of Ruin" "Lesser Essence of Seeking" "Lesser Essence of Sorcery" "Lesser Essence of Thawing" "Lesser Essence of the Body" "Lesser Essence of the Infinite" "Lesser Essence of the Mind" "Regal Orb"
	AreaLevel <= 64
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 180 100 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

#Show # %D4 $type->currency->leveling $tier->magic

# Class == "Stackable Currency"

# BaseType == "Orb of Augmentation" "Orb of Transmutation"

# AreaLevel <= 64

# SetFontSize 42

# SetTextColor 220 175 132

# SetBorderColor 220 175 132

#Show # %D3 $type->currency->leveling $tier->wisdomstart

# Class == "Stackable Currency"

# BaseType == "Scroll of Wisdom"

# AreaLevel <= 17

# SetFontSize 40

# SetTextColor 170 158 130

# SetBorderColor 170 158 130

#Show # %D3 $type->currency->leveling $tier->wisdom !currency_supply4

# Class == "Stackable Currency"

# BaseType == "Scroll of Wisdom"

# AreaLevel <= 64

# SetFontSize 35

# SetTextColor 170 158 130

#===============================================================================================================

# [[2600]] Currency - Regular Currency Tiering

#===============================================================================================================

# !! Waypoint c9.currency.single : "Tierlist - Currency - General" : "Currency"

Show # $type->currency $tier->s !apex_stier
	Class == "Incubators" "Stackable Currency"
	BaseType == "Albino Rhoa Feather" "Altered Collarbone" "Ancient Collarbone" "Ancient Jawbone" "Ancient Rib" "Divine Orb" "Fracturing Orb" "Hinekora's Lock" "Mirror of Kalandra" "Orb of Extraction" "Perfect Chaos Orb" "Perfect Exalted Orb" "Perfect Jeweller's Orb" "Vaal Cultivation Orb"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency $tier->a !currency_a
	Class == "Incubators" "Stackable Currency"
	BaseType == "Architect's Orb" "Core Destabiliser" "Crystallised Corruption" "Greater Chaos Orb" "Kamasa's Orb of Sacrifice" "Kopec's Orb of Sacrifice" "Orb of Annulment" "Orb of Chance" "Perfect Regal Orb" "Preserved Collarbone" "Preserved Cranium" "Vaal Armourer's Infuser" "Vaal Blacksmith's Infuser" "Vaal Catalysing Infuser" "Yaomac's Orb of Sacrifice" "Yugul's Orb of Sacrifice"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency $tier->b !currency_b
	Class == "Incubators" "Stackable Currency"
	BaseType == "Ancient Infuser" "Chaos Orb" "Greater Exalted Orb" "Perfect Orb of Augmentation" "Perfect Orb of Transmutation" "Preserved Rib"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->currency $tier->c !currency_c
	Class == "Incubators" "Stackable Currency"
	BaseType == "Chance Shard" "Exalted Orb" "Gemcutter's Prism" "Glassblower's Bauble" "Gnawed Collarbone" "Greater Jeweller's Orb" "Greater Orb of Transmutation" "Greater Regal Orb" "Orb of Alchemy" "Vaal Arcanist's Infuser" "Vaal Orb"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 139 87 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Circle

Show # %H5 $type->currency $tier->d !currency_d
	Class == "Incubators" "Stackable Currency"
	BaseType == "Armourer's Scrap" "Artificer's Orb" "Blacksmith's Whetstone" "Gnawed Jawbone" "Gnawed Rib" "Greater Orb of Augmentation" "Preserved Jawbone" "Regal Orb" "Vaal Siphoner"
	SetFontSize 40
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 180 100 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Hide # %H3 $type->currency $tier->e !currency_e
	Class == "Incubators" "Stackable Currency"
	BaseType == "Arcanist's Etcher" "Lesser Jeweller's Orb"
	SetFontSize 40
	SetTextColor 240 207 132
	SetBorderColor 240 207 132

Hide # %H2 $type->currency $tier->supplymagic !currency_supply2
	Class == "Incubators" "Stackable Currency"
	BaseType == "Alchemy Shard" "Artificer's Shard" "Orb of Augmentation" "Orb of Transmutation" "Regal Shard"
	SetFontSize 38
	SetTextColor 220 175 132
	SetBorderColor 220 175 132

Hide # %H1 $type->currency $tier->supplieslow !currency_supply4
	Class == "Incubators" "Stackable Currency"
	BaseType == "Scroll of Wisdom" "Transmutation Shard"
	SetFontSize 35
	SetTextColor 170 158 130

Hide # $type->currency $tier->exhide !utility_minimize
	Class == "Incubators" "Stackable Currency"
	BaseType == "Alchemy Shard" "Ancient Infuser" "Arcanist's Etcher" "Armourer's Scrap" "Artificer's Orb" "Artificer's Shard" "Blacksmith's Whetstone" "Chance Shard" "Chaos Orb" "Exalted Orb" "Gemcutter's Prism" "Glassblower's Bauble" "Gnawed Collarbone" "Gnawed Jawbone" "Gnawed Rib" "Greater Exalted Orb" "Greater Jeweller's Orb" "Greater Orb of Augmentation" "Greater Orb of Transmutation" "Greater Regal Orb" "Lesser Jeweller's Orb" "Orb of Alchemy" "Orb of Augmentation" "Orb of Transmutation" "Perfect Orb of Augmentation" "Perfect Orb of Transmutation" "Preserved Jawbone" "Preserved Rib" "Regal Orb" "Regal Shard" "Scroll of Wisdom" "Transmutation Shard" "Vaal Arcanist's Infuser" "Vaal Orb" "Vaal Siphoner"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

#===============================================================================================================

# [[2700]] Currency - SPECIAL

#===============================================================================================================
#------------------------------------

# [2701] Distilled Emotions (Delirium)

#------------------------------------

# !! Waypoint c9.currency.emotions.all : "Tierlist - Distilled Emotions (Delirium)" : "Currency"

Show # $type->currency->emotions $tier->s !apex_stier
	Class == "Stackable Currency"
	BaseType == "Ancient Concentrated Liquid Fear" "Ancient Potent Liquid Melancholy" "Concentrated Liquid Fear" "Concentrated Liquid Isolation" "Concentrated Liquid Suffering" "Potent Liquid Contempt"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency->emotions $tier->a !currency_a
	Class == "Stackable Currency"
	BaseType == "Ancient Concentrated Liquid Isolation" "Ancient Concentrated Liquid Suffering" "Ancient Liquid Despair" "Ancient Potent Liquid Contempt" "Ancient Potent Liquid Ferocity" "Liquid Despair" "Liquid Disgust" "Potent Liquid Ferocity"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency->emotions $tier->b !currency_b
	Class == "Stackable Currency"
	BaseType == "Liquid Envy" "Liquid Paranoia"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->currency->emotions $tier->c !currency_c
	Class == "Stackable Currency"
	BaseType == "Ancient Diluted Liquid Greed" "Ancient Liquid Disgust" "Ancient Liquid Paranoia" "Diluted Liquid Greed" "Potent Liquid Melancholy"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 139 87 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Circle

Show # %H5 $type->currency->emotions $tier->d !currency_d
	Class == "Stackable Currency"
	BaseType == "Ancient Diluted Liquid Guilt" "Ancient Diluted Liquid Ire" "Ancient Liquid Envy" "Diluted Liquid Guilt" "Diluted Liquid Ire"
	SetFontSize 40
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 180 100 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

#Show # %H4 $type->currency->emotions $tier->e !currency_e

# Class == "Stackable Currency"

# SetFontSize 40

# SetTextColor 240 207 132

# SetBorderColor 240 207 132

# PlayEffect White Temp

# MinimapIcon 2 Grey Circle

Hide # $type->currency->emotions $tier->exhide !utility_minimize
	Class == "Stackable Currency"
	BaseType == "Ancient Diluted Liquid Greed" "Ancient Diluted Liquid Guilt" "Ancient Diluted Liquid Ire" "Ancient Liquid Disgust" "Ancient Liquid Envy" "Ancient Liquid Paranoia" "Diluted Liquid Greed" "Diluted Liquid Guilt" "Diluted Liquid Ire" "Liquid Envy" "Liquid Paranoia" "Potent Liquid Melancholy"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

Show # $type->currency->emotions $tier->restex !utility_unknownitem
	Class == "Stackable Currency"
	BaseType "Liquid "
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#------------------------------------

# [2702] Catalysts (breach)

#------------------------------------

# !! Waypoint c9.currency.catalysts.all : "Tierlist - Catalysts (Breach)" : "Currency"

#Show # $type->currency->catalysts $tier->s !apex_stier

# Class == "Stackable Currency"

# SetFontSize 45

# SetTextColor 255 0 0 255

# SetBorderColor 255 0 0 255

# SetBackgroundColor 255 255 255 255

# PlayAlertSound 6 300

# PlayEffect Red

# MinimapIcon 0 Red Star

Show # %H8 $type->currency->catalysts $tier->a !currency_a
	Class == "Stackable Currency"
	BaseType == "Reaver Catalyst" "Refined Necrotic Catalyst" "Refined Reaver Catalyst" "Refined Sibilant Catalyst"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency->catalysts $tier->b !currency_b
	Class == "Stackable Currency"
	BaseType == "Chayula's Catalyst" "Esh's Catalyst" "Necrotic Catalyst" "Refined Carapace Catalyst" "Refined Esh's Catalyst" "Refined Skittering Catalyst" "Refined Tul's Catalyst" "Refined Xoph's Catalyst" "Sibilant Catalyst" "Tul's Catalyst" "Uul-Netol's Catalyst" "Xoph's Catalyst"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->currency->catalysts $tier->c !currency_c
	Class == "Stackable Currency"
	BaseType == "Adaptive Catalyst" "Carapace Catalyst" "Flesh Catalyst" "Neural Catalyst" "Refined Adaptive Catalyst" "Refined Chayula's Catalyst" "Refined Flesh Catalyst" "Refined Neural Catalyst" "Refined Uul-Netol's Catalyst" "Skittering Catalyst"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 139 87 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Circle

#Show # %HS4 $type->currency->catalysts $tier->d !currency_d

# Class == "Stackable Currency"

# SetFontSize 40

# SetTextColor 0 0 0 255

# SetBorderColor 0 0 0 255

# SetBackgroundColor 240 180 100 255

# PlayAlertSound 2 300

# PlayEffect White

# MinimapIcon 2 White Circle

#Show # %HS2 $type->currency->catalysts $tier->e !currency_e

# Class == "Stackable Currency"

# SetFontSize 40

# SetTextColor 240 207 132

# SetBorderColor 240 207 132

# PlayEffect White Temp

# MinimapIcon 2 Grey Circle

Hide # $type->currency->catalysts $tier->exhide !utility_minimize
	Class == "Stackable Currency"
	BaseType == "Adaptive Catalyst" "Carapace Catalyst" "Chayula's Catalyst" "Esh's Catalyst" "Flesh Catalyst" "Necrotic Catalyst" "Neural Catalyst" "Refined Adaptive Catalyst" "Refined Carapace Catalyst" "Refined Chayula's Catalyst" "Refined Esh's Catalyst" "Refined Flesh Catalyst" "Refined Neural Catalyst" "Refined Skittering Catalyst" "Refined Tul's Catalyst" "Refined Uul-Netol's Catalyst" "Refined Xoph's Catalyst" "Sibilant Catalyst" "Skittering Catalyst" "Tul's Catalyst" "Uul-Netol's Catalyst" "Xoph's Catalyst"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

Show # $type->currency->catalysts $tier->restex !utility_unknownitem
	Class == "Stackable Currency"
	BaseType "Catalyst"
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#------------------------------------

# [2703] Essences

#------------------------------------

# !! Waypoint c9.currency.essences.all : "Tierlist - Essences" : "Currency"

Show # $type->currency->essence $tier->s !apex_stier
	Class == "Stackable Currency"
	BaseType == "Essence of Hysteria"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency->essence $tier->a !currency_a
	Class == "Stackable Currency"
	BaseType == "Essence of Delirium" "Essence of Horror"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency->essence $tier->b !currency_b
	Class == "Stackable Currency"
	BaseType == "Essence of Insanity" "Essence of the Breach" "Greater Essence of Opulence" "Greater Essence of Ruin" "Greater Essence of Seeking" "Perfect Essence of Battle"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->currency->essence $tier->c !currency_c
	Class == "Stackable Currency"
	BaseType == "Essence of the Abyss" "Greater Essence of Abrasion" "Greater Essence of Command" "Greater Essence of Enhancement" "Greater Essence of Grounding" "Greater Essence of Haste" "Greater Essence of Insulation" "Greater Essence of Thawing" "Greater Essence of the Infinite" "Perfect Essence of Abrasion" "Perfect Essence of Alacrity" "Perfect Essence of Command" "Perfect Essence of Electricity" "Perfect Essence of Enhancement" "Perfect Essence of Haste" "Perfect Essence of Ice" "Perfect Essence of Insulation" "Perfect Essence of Ruin" "Perfect Essence of Seeking" "Perfect Essence of Sorcery" "Perfect Essence of the Mind"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 139 87 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Circle

Show # %H5 $type->currency->essence $tier->d !currency_d
	Class == "Stackable Currency"
	BaseType == "Essence of Abrasion" "Essence of Alacrity" "Essence of Battle" "Essence of Command" "Essence of Electricity" "Essence of Enhancement" "Essence of Flames" "Essence of Grounding" "Essence of Haste" "Essence of Ice" "Essence of Insulation" "Essence of Opulence" "Essence of Ruin" "Essence of Seeking" "Essence of Sorcery" "Essence of Thawing" "Essence of the Body" "Essence of the Infinite" "Essence of the Mind" "Greater Essence of Alacrity" "Greater Essence of Electricity" "Greater Essence of Flames" "Greater Essence of Ice" "Greater Essence of Sorcery" "Greater Essence of the Body" "Lesser Essence of Abrasion" "Lesser Essence of Alacrity" "Lesser Essence of Battle" "Lesser Essence of Command" "Lesser Essence of Electricity" "Lesser Essence of Enhancement" "Lesser Essence of Flames" "Lesser Essence of Grounding" "Lesser Essence of Haste" "Lesser Essence of Ice" "Lesser Essence of Insulation" "Lesser Essence of Opulence" "Lesser Essence of Ruin" "Lesser Essence of Seeking" "Lesser Essence of Sorcery" "Lesser Essence of Thawing" "Lesser Essence of the Body" "Lesser Essence of the Infinite" "Lesser Essence of the Mind" "Perfect Essence of Flames" "Perfect Essence of Grounding" "Perfect Essence of Opulence" "Perfect Essence of Thawing" "Perfect Essence of the Body" "Perfect Essence of the Infinite"
	SetFontSize 40
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 180 100 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

Hide # %H4 $type->currency->essence $tier->e !currency_e
	Class == "Stackable Currency"
	BaseType == "Greater Essence of Battle" "Greater Essence of the Mind"
	SetFontSize 40
	SetTextColor 240 207 132
	SetBorderColor 240 207 132

Hide # $type->currency->essence $tier->exhide !utility_minimize
	Class == "Stackable Currency"
	BaseType == "Essence of Abrasion" "Essence of Alacrity" "Essence of Battle" "Essence of Command" "Essence of Electricity" "Essence of Enhancement" "Essence of Flames" "Essence of Grounding" "Essence of Haste" "Essence of Ice" "Essence of Insanity" "Essence of Insulation" "Essence of Opulence" "Essence of Ruin" "Essence of Seeking" "Essence of Sorcery" "Essence of Thawing" "Essence of the Abyss" "Essence of the Body" "Essence of the Breach" "Essence of the Infinite" "Essence of the Mind" "Greater Essence of Abrasion" "Greater Essence of Alacrity" "Greater Essence of Battle" "Greater Essence of Command" "Greater Essence of Electricity" "Greater Essence of Enhancement" "Greater Essence of Flames" "Greater Essence of Grounding" "Greater Essence of Haste" "Greater Essence of Ice" "Greater Essence of Insulation" "Greater Essence of Opulence" "Greater Essence of Ruin" "Greater Essence of Seeking" "Greater Essence of Sorcery" "Greater Essence of Thawing" "Greater Essence of the Body" "Greater Essence of the Infinite" "Greater Essence of the Mind" "Lesser Essence of Abrasion" "Lesser Essence of Alacrity" "Lesser Essence of Battle" "Lesser Essence of Command" "Lesser Essence of Electricity" "Lesser Essence of Enhancement" "Lesser Essence of Flames" "Lesser Essence of Grounding" "Lesser Essence of Haste" "Lesser Essence of Ice" "Lesser Essence of Insulation" "Lesser Essence of Opulence" "Lesser Essence of Ruin" "Lesser Essence of Seeking" "Lesser Essence of Sorcery" "Lesser Essence of Thawing" "Lesser Essence of the Body" "Lesser Essence of the Infinite" "Lesser Essence of the Mind" "Perfect Essence of Abrasion" "Perfect Essence of Alacrity" "Perfect Essence of Battle" "Perfect Essence of Command" "Perfect Essence of Electricity" "Perfect Essence of Enhancement" "Perfect Essence of Flames" "Perfect Essence of Grounding" "Perfect Essence of Haste" "Perfect Essence of Ice" "Perfect Essence of Insulation" "Perfect Essence of Opulence" "Perfect Essence of Ruin" "Perfect Essence of Seeking" "Perfect Essence of Sorcery" "Perfect Essence of Thawing" "Perfect Essence of the Body" "Perfect Essence of the Infinite" "Perfect Essence of the Mind"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

Show # $type->currency->essence $tier->restex !utility_unknownitem
	Class == "Stackable Currency"
	BaseType "Essence"
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#------------------------------------

# [2704] Omen (ritual)

#------------------------------------

# !! Waypoint c9.currency.omen.all : "Tierlist - Omen (Ritual)" : "Currency"

Show # $type->currency->omen $tier->s !apex_stier
	Class == "Omen"
	BaseType == "Head of the King" "Omen of Abyssal Echoes" "Omen of Chance" "Omen of Dextral Annulment" "Omen of Dextral Erasure" "Omen of Light" "Omen of Sinistral Annulment" "Omen of Sinistral Erasure" "Omen of Whittling"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->currency->omen $tier->a !currency_a
	Class == "Omen"
	BaseType == "Aldur's Saga" "Medved's Saga" "Olroth's Saga" "Omen of Corruption" "Omen of Dextral Crystallisation" "Omen of Putrefaction" "Omen of Reinforcements" "Omen of Sanctification" "Omen of Sinistral Crystallisation" "Omen of the Hunt" "Uhtred's Saga" "Vorana's Saga"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Circle

Show # %H7 $type->currency->omen $tier->b !currency_b
	Class == "Omen"
	BaseType == "Omen of Amelioration" "Omen of Catalysing Exaltation" "Omen of Chaotic Quantity" "Omen of Greater Exaltation" "Omen of Secret Compartments" "Omen of Sinistral Necromancy" "Omen of the Blessed"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 105 90 255
	PlayAlertSound 2 300
	PlayEffect Yellow
	MinimapIcon 1 Yellow Circle

Show # %H6 $type->currency->omen $tier->c !currency_c
	Class == "Omen"
	BaseType == "Omen of Answered Prayers" "Omen of Bartering" "Omen of Chaotic Effectiveness" "Omen of Chaotic Monsters" "Omen of Chaotic Rarity" "Omen of Dextral Exaltation" "Omen of Dextral Necromancy" "Omen of Resurgence" "Omen of Sinistral Exaltation" "Omen of the Ancients" "Omen of the Blackblooded" "Omen of the Sovereign"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 245 139 87 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 1 Yellow Circle

Show # %H5 $type->currency->omen $tier->d !currency_d
	Class == "Omen"
	BaseType == "Omen of Gambling" "Omen of Refreshment" "Omen of the Liege"
	SetFontSize 40
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 240 180 100 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle

#Show # %H4 $type->currency->omen $tier->e !currency_e

# Class == "Omen"

# SetFontSize 40

# SetTextColor 240 207 132

# SetBorderColor 240 207 132

# PlayEffect White Temp

# MinimapIcon 2 Grey Circle

Hide # $type->currency->omen $tier->exhide !utility_minimize
	Class == "Omen"
	BaseType == "Omen of Amelioration" "Omen of Answered Prayers" "Omen of Bartering" "Omen of Catalysing Exaltation" "Omen of Chaotic Effectiveness" "Omen of Chaotic Monsters" "Omen of Chaotic Quantity" "Omen of Chaotic Rarity" "Omen of Dextral Exaltation" "Omen of Dextral Necromancy" "Omen of Gambling" "Omen of Greater Exaltation" "Omen of Refreshment" "Omen of Resurgence" "Omen of Secret Compartments" "Omen of Sinistral Exaltation" "Omen of Sinistral Necromancy" "Omen of the Ancients" "Omen of the Blackblooded" "Omen of the Blessed" "Omen of the Liege" "Omen of the Sovereign"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

Show # $type->currency->omen $tier->restex !utility_unknownitem
	Class == "Omen"
	BaseType "Omen "
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#===============================================================================================================

# [[2800]] Misc Map Like

#===============================================================================================================

# !! Waypoint c10.fragments.special : "Special Keys - Pinnacle, Logbook, Calamity, RelicKeys" : "Fragments"

Show # $type->maplike->special $tier->vaultkeysrare !fragments_a
	BaseType == "Olroth's Reliquary Key" "Ritualistic Reliquary Key" "Tangmazu's Reliquary Key" "The Arbiter's Reliquary Key" "The Trialmaster's Reliquary Key" "Xesht's Reliquary Key" "Zarokh's Reliquary Key"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 220 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

Show # $type->maplike->special $tier->vaultkeys !fragments_b
	BaseType == "Twilight Reliquary Key"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 220 0 255 255
	PlayAlertSound 2 300
	PlayEffect Purple
	MinimapIcon 1 Yellow Hexagon

Show # $type->maplike->special $tier->superkeys !fragments_a
	Class == "Pinnacle Keys"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 220 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

Show # $type->maplike->special $tier->logbookshigh !apex_stier
	Class == "Expedition Logbook"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

#===============================================================================================================

# [[2900]] Uniques

#===============================================================================================================

# !! Waypoint c11.uniques.all : "Tierlist - Uniques - All" : "Uniques"

#------------------------------------

# [2901] Exceptions #1

#------------------------------------

Show # $type->uniques $tier->sekhemaring !uniques_a
	Sockets > 0
	Rarity Unique
	BaseType == "Ring"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

#------------------------------------

# [2902] Tier 1 and 2 uniques

#------------------------------------

# !! Waypoint c11.uniques.t1 : "Tierlist - Uniques - T1, T2" : "Uniques"

Show # $type->uniques $tier->t1 !apex_stier
	Rarity Unique
	BaseType == "Aberrant Sledge" "Abyss Tablet" "Armoured Cap" "Armoured Vest" "Ashbark Talisman" "Chain Tiara" "Emerald" "Engraved Bracers" "Exquisite Vest" "Fine Bracers" "Gargantuan Mana Flask" "Glacial Fortress" "Golden Charm" "Grand Manchettes" "Grand Spear" "Heartwood Shortbow" "Incense Relic" "Ornate Gauntlets" "Perching Staff" "Primed Quiver" "Pronged Spear" "Ring" "Ruby" "Sapphire" "Silver Charm" "Stoic Sceptre" "Time-Lost Diamond" "Trarthan Cannon" "Twisted Wand" "Two-Stone Ring" "Ultimate Mana Flask" "Unset Ring" "Vase Relic" "Veridical Chain" "Warding Quarterstaff"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # %H8 $type->uniques $tier->t2 !uniques_a
	Rarity Unique
	BaseType == "Array Buckler" "Cinched Boots" "Desolate Crossbow" "Diamond" "Felt Cap" "Garment" "Grand Regalia" "Intricate Crest Shield" "Ironclad Vestments" "Lattice Sandals" "Morning Star" "Permafrost Staff" "Reflecting Staff" "Ritual Tablet" "Sacred Focus" "Sacrificial Regalia" "Shrine Sceptre" "Siphoning Wand" "Spiral Wraps" "Stocky Mitts" "Stone Charm" "Temple Tablet" "Thawing Charm" "Timeless Jewel" "Totemic Greatclub" "Utility Wraps" "Winged Spear"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Yellow Star

#------------------------------------

# [2903] Multi-Unique bases.

#------------------------------------

Show # $type->uniques $tier->twicecorrupteduniques !uniques_exceptional
	TwiceCorrupted True
	Rarity Unique
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 0 Purple Star

Show # $type->uniques $tier->vaalmodunique !uniques_exceptional
	HasVaalUniqueMod True
	Rarity Unique
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 0 Purple Star

Show # $type->uniques $tier->multispecialhigh !uniques_x
	Rarity Unique
	BaseType == "Heavy Belt" "Irradiated Tablet" "Tribal Mask" "Utility Belt"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

Show # %D5 $type->uniques $tier->overqualityuniques !uniques_exceptional
	Quality >= 21
	Rarity Unique
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 0 Purple Star

Show # %D5 $type->uniques $tier->oversocketuniques1 !uniques_exceptional
	Sockets >= 3
	Rarity Unique
	Class == "Body Armours" "Bows" "Crossbows" "Quarterstaves" "Staves" "Talismans" "Two Hand Maces"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 0 Purple Star

Show # %D5 $type->uniques $tier->oversocketuniques2 !uniques_exceptional
	Sockets >= 2
	Rarity Unique
	Class == "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "One Hand Maces" "Sceptres" "Shields" "Spears" "Wands"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 3 300
	PlayEffect Purple
	MinimapIcon 0 Purple Star

Show # $type->uniques $tier->multispecial !uniques_x
	Rarity Unique
	BaseType == "Bloodstone Amulet" "Fine Belt" "Gold Amulet" "Jade Amulet" "Lazuli Ring" "Overseer Tablet" "Stellar Amulet"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 188 96 37 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Star

#------------------------------------

# [2904] Low tier exceptions

#------------------------------------

# !! Waypoint c11.uniques.low : "Tierlist - Uniques - Low Tier Uniques" : "Uniques"

#Show # %H6 $type->uniques $tier->earlyleague !uniques_b

# Rarity Unique

# SetFontSize 42

# SetTextColor 188 96 37 255

# SetBorderColor 188 96 37 255

# SetBackgroundColor 53 13 13 255

# PlayAlertSound 3 300

# PlayEffect Brown

# MinimapIcon 1 Brown Star

Show # %D5 $type->uniques $tier->loreweaverecipe !uniques_b
	Rarity Unique
	Class == "Rings"
	SetFontSize 42
	SetTextColor 188 96 37 255
	SetBorderColor 188 96 37 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 1 Brown Star

Show # $type->uniques $tier->corrupteduniques !uniques_b
	AnyEnchantment True
	Corrupted True
	Rarity Unique
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	SetFontSize 42
	SetTextColor 188 96 37 255
	SetBorderColor 188 96 37 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 1 Brown Star

#------------------------------------

# [2905] Tier 3 uniques

#------------------------------------

Show # %D5 $type->uniques $tier->vaaltypeuniques !uniques_b
	IsVaalUnique True
	Rarity Unique
	SetFontSize 42
	SetTextColor 188 96 37 255
	SetBorderColor 188 96 37 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 1 Brown Star

Show # %H5 $type->uniques $tier->t3boss !uniques_xbossdrop
	Rarity Unique
	BaseType == "Abyssal Signet" "Closed Helm" "Crucible Tower Shield" "Grand Cuisses" "Grand Visage" "Lapis Amulet" "Moulded Mitts" "Omen Crest Shield" "Penetrating Quiver" "Primal Markings" "Ravenous Staff" "Revered Vestments" "Silk Robe" "Spiritbone Crown" "Ultimate Life Flask" "Venerable Defender" "Visceral Quiver" "Wide Belt" "Wyrm Quarterstaff"
	SetFontSize 42
	SetTextColor 188 96 37 255
	SetBorderColor 188 96 37 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 2 Blue Star

Show # %H5 $type->uniques $tier->t3 !uniques_b
	Rarity Unique
	BaseType == "Altar Robe" "Amethyst Charm" "Amphora Relic" "Ancestral Mail" "Anchorite Garb" "Ancient Leggings" "Antidote Charm" "Antler Focus" "Azure Amulet" "Blacksteel Tower Shield" "Bolstered Mitts" "Breach Tablet" "Broadhead Quiver" "Burnished Gauntlets" "Champion Cuirass" "Coffer Relic" "Conqueror Plate" "Corsair Cap" "Corvus Mantle" "Crimson Amulet" "Crude Bow" "Decorated Helm" "Delirium Tablet" "Double Belt" "Dousing Charm" "Embroidered Gloves" "Enlightened Robe" "Face Mask" "Fanatic Bow" "Forked Spear" "Furtive Wraps" "Gargantuan Life Flask" "Giant Maul" "Gilded Vestments" "Gold Circlet" "Gold Ring" "Grounding Charm" "Heavy Bow" "Heavy Crown" "Helix Spear" "Heraldric Tower Shield" "Heroic Armour" "Iron Greaves" "Jewelled Gloves" "Linen Belt" "Long Belt" "Lunar Amulet" "Magus Tiara" "Mail Belt" "Marching Mace" "Martyr Crown" "Ornate Belt" "Pauascale Gloves" "Pelage Targe" "Plate Belt" "Plated Mace" "Plated Vestments" "Prismatic Ring" "Riveted Mitts" "Rope Cuffs" "Ruby Charm" "Sacral Quiver" "Sacrificial Mantle" "Sapphire Charm" "Sapphire Ring" "Seal Relic" "Secured Leggings" "Shaman Mantle" "Smuggler Coat" "Solar Amulet" "Solid Mask" "Spiked Club" "Spined Bracers" "Spired Greathelm" "Staunching Charm" "Stone Greaves" "Stone Tower Shield" "Tapestry Relic" "Tenebrous Crown" "Topaz Charm" "Torment Club" "Torn Gloves" "Transcendent Mana Flask" "Trimmed Greaves" "Vaal Cuirass" "Velvet Cap" "Viper Cap" "Voodoo Focus" "Wrapped Greathelm"
	SetFontSize 42
	SetTextColor 188 96 37 255
	SetBorderColor 188 96 37 255
	SetBackgroundColor 53 13 13 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 1 Brown Star

#------------------------------------

# [2906] Tier 4 uniques

#------------------------------------

Hide # %H4 $type->uniques $tier->hideable !uniques_c
	Rarity Unique
	BaseType == "Acrid Wand" "Aged Cuffs" "Amber Amulet" "Amethyst Ring" "Ancient Mail" "Ancient Visor" "Artillery Bow" "Ashen Staff" "Assassin Garb" "Attuned Wand" "Barbed Spear" "Barricade Tower Shield" "Beaded Circlet" "Blazon Crest Shield" "Blunt Quiver" "Bone Raiment" "Bone Wand" "Braced Sabatons" "Braced Tower Shield" "Brimmed Helm" "Bronze Greaves" "Chain Mail" "Changeling Talisman" "Chiming Staff" "Cleric Vestments" "Cloaked Mail" "Composite Bow" "Covered Sabatons" "Covert Hood" "Cowled Helm" "Crescent Quarterstaff" "Crescent Targe" "Crumbling Maul" "Crystal Focus" "Cultist Crown" "Cultist Greathammer" "Death Mask" "Doubled Gauntlets" "Dualstring Bow" "Dyad Crossbow" "Effigial Tower Shield" "Elementalist Robe" "Elite Greathelm" "Emblem Crest Shield" "Embossed Boots" "Emerald Ring" "Engraved Focus" "Execratus Hammer" "Explorer Armour" "Familial Talisman" "Feathered Robe" "Feathered Sandals" "Feathered Tiara" "Felled Greatclub" "Fierce Greathelm" "Fire Quiver" "Firm Bracers" "Flanged Mace" "Forge Maul" "Full Plate" "Fur Plate" "Gauze Wraps" "Gelid Staff" "Goldcast Cuffs" "Gothic Quarterstaff" "Guarded Helm" "Hardwood Spear" "Hardwood Targe" "Havoc Raiment" "Hermit Garb" "Hewn Mask" "Hexer's Robe" "Hooded Mask" "Horned Crown" "Hunter Hood" "Hunting Shoes" "Hunting Spear" "Intricate Gloves" "Iron Buckler" "Iron Crown" "Iron Cuirass" "Iron Ring" "Ironhead Spear" "Jade Tiara" "Jingling Crest Shield" "Kalguuran Cuffs" "Kalguuran Forgehammer" "Keth Raiment" "Knight Armour" "Lace Hood" "Laced Boots" "Lamellar Mail" "Layered Gauntlets" "Leaden Greathammer" "Leather Buckler" "Leather Vest" "Leatherbound Hood" "Linen Wraps" "Lizardscale Boots" "Long Quarterstaff" "Lumbering Talisman" "Mail Sabatons" "Mail Vestments" "Makeshift Crossbow" "Marabout Garb" "Maraketh Cuirass" "Nettle Talisman" "Oak Greathammer" "Omen Sceptre" "Ornate Buckler" "Painted Tower Shield" "Pathfinder Coat" "Pearl Ring" "Pilgrim Vestments" "Plate Gauntlets" "Plated Buckler" "Plated Raiment" "Pointed Maul" "Pyrophyte Staff" "Quilted Vest" "Raider Plate" "Rampart Tower Shield" "Rattling Sceptre" "Rawhide Belt" "Recurve Bow" "Rhoahide Coat" "Ridged Buckler" "Ringmail Gauntlets" "Rogue Armour" "Rough Greaves" "Ruby Ring" "Rusted Cuirass" "Rusted Greathelm" "Scale Mail" "Scalper's Jacket" "Scout's Vest" "Sectioned Bracers" "Serpentscale Coat" "Shabby Hood" "Shielded Helm" "Shortbow" "Shrouded Vest" "Sigil Crest Shield" "Silk Slippers" "Slim Mace" "Smithing Hammer" "Soldier Greathelm" "Sombre Gloves" "Spiked Buckler" "Splintered Tower Shield" "Stacked Sabatons" "Steel Plate" "Steelpoint Quarterstaff" "Steeltoe Boots" "Stitched Gloves" "Straw Sandals" "Strider Vest" "Studded Greatclub" "Studded Vest" "Suede Bracers" "Tattered Robe" "Tempered Mitts" "Temple Maul" "Tense Crossbow" "Threaded Shoes" "Tideseer Mantle" "Titan Mitts" "Tonal Focus" "Topaz Ring" "Toxic Quiver" "Twig Circlet" "Twig Focus" "Vaal Tower Shield" "Vagabond Armour" "Veiled Mask" "Velour Shoes" "Vermeil Circlet" "Vicious Talisman" "Visored Helm" "Volatile Wand" "Voltaic Staff" "Votive Raiment" "War Spear" "Warden Bow" "Warpick" "Warrior Greathelm" "Waxed Jacket" "Wayfarer Jacket" "Wicker Tiara" "Withered Wand" "Wooden Buckler" "Wooden Club" "Woven Focus" "Wrapped Quarterstaff" "Wrapped Sandals" "Zealot Bow"
	SetFontSize 40
	SetTextColor 188 96 37 255

Show # $type->uniques $tier->restex !utility_unknownitem
	Rarity Unique
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#===============================================================================================================

# [[3000]] Splinters, Tablets, Fragments

#===============================================================================================================

# !! Waypoint c10.fragments.most : "Fragments and Splinters" : "Fragments"

Show # %H6 $type->currency->splinter $tier->t1 !fragments_splinter1
	StackSize >= 20
	Class == "Stackable Currency"
	BaseType == "Breach Splinter" "Petition Splinter" "Runic Splinter" "Simulacrum Splinter"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 220 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Kite

Show # %H6 $type->currency->splinter $tier->t2 !fragments_splinter2
	StackSize >= 8
	Class == "Stackable Currency"
	BaseType == "Breach Splinter" "Petition Splinter" "Runic Splinter" "Simulacrum Splinter"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 220 0 255 255
	PlayAlertSound 2 300
	PlayEffect Purple
	MinimapIcon 0 Red Kite

Show # %H6 $type->currency->splinter $tier->t3 !fragments_splinter3
	StackSize >= 4
	Class == "Stackable Currency"
	BaseType == "Breach Splinter" "Petition Splinter" "Runic Splinter" "Simulacrum Splinter"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 75 225 255
	PlayAlertSound 2 300
	PlayEffect Purple
	MinimapIcon 1 Orange Kite

Show # %H6 $type->currency->splinter $tier->t4 !fragments_splinter4
	StackSize >= 2
	Class == "Stackable Currency"
	BaseType == "Breach Splinter" "Petition Splinter" "Runic Splinter" "Simulacrum Splinter"
	SetFontSize 40
	SetTextColor 200 75 200 255
	SetBorderColor 200 75 200 255
	SetBackgroundColor 50 0 75
	PlayAlertSound 2 100
	PlayEffect Purple Temp
	MinimapIcon 1 Yellow Kite

Show # %H6 $type->currency->splinter $tier->t5 !fragments_splinter5
	Class == "Stackable Currency"
	BaseType == "Breach Splinter" "Petition Splinter" "Runic Splinter" "Simulacrum Splinter"
	SetFontSize 38
	SetTextColor 200 75 200 255
	SetBorderColor 200 75 200 255
	PlayAlertSound 2 100
	PlayEffect Purple Temp
	MinimapIcon 1 White Kite

Show # $type->fragments->generic $tier->s !apex_stier
	BaseType == "Breachlord Sac" "Origin Spark" "Simulacrum"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show # $type->fragments->generic $tier->a !fragments_a
	BaseType == "An Audience with the King" "Breachstone" "Call of the Shadows" "Cowardly Fate" "Deadly Fate" "Head of the King" "Idol of Estazunti" "Kulemak's Invitation" "Raven's Reflection" "Sacred Bloom" "The Triskelion Reforged" "Victorious Fate"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 220 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

Show # $type->fragments->generic $tier->b !fragments_b
	BaseType == "Expedition Tablet" "Ritual Tablet"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 220 0 255 255
	PlayAlertSound 2 300
	PlayEffect Purple
	MinimapIcon 1 Yellow Hexagon

Show # $type->fragments->generic $tier->c !fragments_c
	BaseType == "Abyss Tablet" "Breach Tablet" "Delirium Tablet" "Irradiated Tablet" "Overseer Tablet" "Temple Tablet"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 75 225 255
	PlayAlertSound 2 300
	PlayEffect Purple Temp
	MinimapIcon 1 White Hexagon

#Show # $type->fragments->generic $tier->d !fragments_d

# SetFontSize 40

# SetTextColor 200 75 200 255

# SetBorderColor 200 75 200 255

# SetBackgroundColor 50 0 75

# PlayAlertSound 2 300

# PlayEffect Purple Temp

# MinimapIcon 2 White Hexagon

#Show # $type->fragments->generic $tier->e !fragments_e

# SetFontSize 38

# SetTextColor 180 75 225 255

# PlayEffect Purple Temp

# MinimapIcon 2 Grey Hexagon

Hide # $type->fragments->generic $tier->exhide !utility_minimize
	BaseType == "Abyss Tablet" "Breach Tablet" "Delirium Tablet" "Expedition Tablet" "Irradiated Tablet" "Overseer Tablet" "Ritual Tablet" "Temple Tablet"
	SetFontSize 18
	SetBackgroundColor 20 20 0 0

Show # $type->fragments->generic $tier->restex !utility_unknownitem
	Class "Map Fragments" "Tablet"
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#===============================================================================================================

# [[3100]] Misc Map Items

#===============================================================================================================

# !! Waypoint c10.ascendancy.all : "Trial Keys" : "Fragments"

Show # $type->miscmapitemsextra $tier->trialkeyultimatumreward !fragments_a
	Rarity Magic Rare Unique
	BaseType == "Inscribed Ultimatum"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 220 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

Show # %HS4 $type->miscmapitemsextra $tier->trialkeysanctumtop !fragments_c
	ItemLevel >= 80
	BaseType == "Djinn Barya"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 75 225 255

Hide # %H4 $type->miscmapitemsextra $tier->trialkeysanctum3 !fragments_c
	ItemLevel >= 60
	ItemLevel <= 79
	BaseType == "Djinn Barya"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 75 225 255

Hide # %HS3 $type->miscmapitemsextra $tier->trialkeysanctum2 !fragments_fragdmuted
	ItemLevel >= 45
	ItemLevel <= 59
	BaseType == "Djinn Barya"
	SetFontSize 40
	SetTextColor 200 75 200 255
	SetBorderColor 200 75 200 255
	SetBackgroundColor 50 0 75

Hide # %H2 $type->miscmapitemsextra $tier->trialkeysanctum1 !fragments_fragdmuted
	ItemLevel <= 44
	BaseType == "Djinn Barya"
	SetFontSize 40
	SetTextColor 200 75 200 255
	SetBorderColor 200 75 200 255
	SetBackgroundColor 50 0 75

Show # %HS5 $type->miscmapitemsextra $tier->trialspecial !fragments_c
	BaseType == "Test of Cunning Barya" "Test of Strength Barya" "Test of Time Barya" "Test of Will Barya"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 75 225 255
	PlayAlertSound 2 300
	PlayEffect Purple Temp
	MinimapIcon 1 White Hexagon

Show # %HS4 $type->miscmapitemsextra $tier->trialkeyultimatumtop !fragments_c
	ItemLevel >= 80
	BaseType == "Inscribed Ultimatum"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 75 225 255

Hide # %H4 $type->miscmapitemsextra $tier->trialkeyultimatumhigh !fragments_c
	ItemLevel >= 75
	ItemLevel <= 79
	BaseType == "Inscribed Ultimatum"
	SetFontSize 42
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 180 75 225 255

Hide # %HS2 $type->miscmapitemsextra $tier->trialkeyultimatumlow !fragments_fragdmuted
	ItemLevel <= 74
	BaseType == "Inscribed Ultimatum"
	SetFontSize 40
	SetTextColor 200 75 200 255
	SetBorderColor 200 75 200 255
	SetBackgroundColor 50 0 75

Show # $type->miscmapitemsextra $tier->relickeyssafe !apex_stier
	Class == "Vault Keys"
	SetFontSize 45
	SetTextColor 255 0 0 255
	SetBorderColor 255 0 0 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

#===============================================================================================================

# [[3200]] Remaining Currency

#===============================================================================================================

Show # $type->currency $tier->restex !utility_unknownitem
	Class == "Incubators" "Stackable Currency"
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon

#===============================================================================================================

# [[3300]] Leveling - Salvagable

#===============================================================================================================

# !! Waypoint c20.leveling.salvagable.all: "Leveling - Salvagable bases" : "Leveling"

# Double Quality Currencies

#Show # %D4 $type->leveling->salvagable $tier->quality2martialany !itemproperty_salvagelvl1

# Quality >= 10

# Rarity Normal Magic

# Class == "Bows" "Crossbows" "One Hand Maces" "Quarterstaves" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

#Show # %D4 $type->leveling->salvagable $tier->quality2casterany !itemproperty_salvagelvl1

# Quality >= 10

# Rarity Normal Magic

# Class == "Sceptres" "Staves" "Wands"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

#Show # %D4 $type->leveling->salvagable $tier->quality2armorany !itemproperty_salvagelvl1

# Quality >= 10

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

Show # %D5 $type->leveling->salvagable $tier->quality2flask !itemproperty_salvagelvl1
	Quality >= 10
	Rarity Normal Magic
	Class == "Charms" "Life Flasks" "Mana Flasks"
	AreaLevel <= 64
	SetFontSize 40
	SetBorderColor 180 180 180

# Single Quality Currencies

#Show # %D4 $type->leveling->salvagable $tier->qualitymartialany !itemproperty_salvagelvl1

# Quality >= 1

# Rarity Normal Magic

# Class == "Bows" "Crossbows" "One Hand Maces" "Quarterstaves" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

#Show # %D4 $type->leveling->salvagable $tier->qualitycasterany !itemproperty_salvagelvl1

# Quality >= 1

# Rarity Normal Magic

# Class == "Sceptres" "Staves" "Wands"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

#Show # %D4 $type->leveling->salvagable $tier->qualityarmorany !itemproperty_salvagelvl1

# Quality >= 1

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Bucklers" "Foci" "Gloves" "Helmets" "Shields"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

#Show # %D4 $type->leveling->salvagable $tier->qualityflask !itemproperty_salvagelvl1

# Quality >= 1

# Rarity Normal Magic

# Class == "Charms" "Life Flasks" "Mana Flasks"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

# Artificer Scraps

#Show # %D3 $type->leveling->salvagable $tier->socketssmall1 !itemproperty_salvagelvl1

# Sockets > 0

# Width <= 2

# Height <= 2

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

#Show # %D3 $type->leveling->salvagable $tier->socketssmall2 !itemproperty_salvagelvl1

# Sockets > 0

# Width <= 1

# Height <= 4

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 180 180 180

#Show # %D3 $type->leveling->salvagable $tier->socketsothers !itemproperty_salvage2

# Sockets > 0

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel <= 64

# SetFontSize 35

# SetBorderColor 127 127 127

#===============================================================================================================

# [[3400]] Leveling - Hide outdated leveling flasks

#===============================================================================================================

# !! Waypoint c20.leveling.flasks.hidelayer : "Leveling - All flask rules" : "Leveling"

Hide # %H0 $type->hidelayer $tier->outdatedlevelflaska
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Lesser" "Medium"
	AreaLevel >= 15
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # %H0 $type->hidelayer $tier->outdatedlevelflaskb
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Grand" "Greater"
	AreaLevel >= 30
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # %H0 $type->hidelayer $tier->outdatedlevelflaskc
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Colossal" "Giant"
	AreaLevel >= 42
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # %H0 $type->hidelayer $tier->outdatedlevelflaskd
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Gargantuan"
	AreaLevel >= 52
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

Hide # %H0 $type->hidelayer $tier->outdatedlevelflaske
	Quality 0
	Class == "Life Flasks" "Mana Flasks"
	BaseType "Transcendent"
	AreaLevel >= 62
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

#===============================================================================================================

# [[3500]] Leveling - Life Mana Flasks

#===============================================================================================================
#------------------------------------

# [3501] Life flasks

#------------------------------------

# !! Waypoint c20.leveling.flasks.progression : "Leveling - Flask Progression" : "Leveling"

Show # $type->leveling->flasks->life $tier->t1
	Class == "Life Flasks"
	BaseType "Medium"
	AreaLevel <= 9
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->life $tier->t2
	Class == "Life Flasks"
	BaseType "Greater"
	AreaLevel <= 15
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->life $tier->t3
	Class == "Life Flasks"
	BaseType "Grand"
	AreaLevel <= 22
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->life $tier->t4
	Class == "Life Flasks"
	BaseType "Giant"
	AreaLevel <= 29
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->life $tier->t5
	Class == "Life Flasks"
	BaseType "Colossal"
	AreaLevel <= 39
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->life $tier->t6
	Class == "Life Flasks"
	BaseType "Gargantuan"
	AreaLevel <= 49
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->life $tier->t7
	Class == "Life Flasks"
	BaseType "Transcendent"
	AreaLevel <= 59
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->life $tier->t8
	Class == "Life Flasks"
	BaseType "Ultimate"
	AreaLevel <= 65
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

#------------------------------------

# [3502] Mana flasks

#------------------------------------

Show # $type->leveling->flasks->mana $tier->t1
	Class == "Mana Flasks"
	BaseType "Medium"
	AreaLevel <= 9
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->mana $tier->t2
	Class == "Mana Flasks"
	BaseType "Greater"
	AreaLevel <= 15
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->mana $tier->t3
	Class == "Mana Flasks"
	BaseType "Grand"
	AreaLevel <= 22
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->mana $tier->t4
	Class == "Mana Flasks"
	BaseType "Giant"
	AreaLevel <= 29
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->mana $tier->t5
	Class == "Mana Flasks"
	BaseType "Colossal"
	AreaLevel <= 39
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->mana $tier->t6
	Class == "Mana Flasks"
	BaseType "Gargantuan"
	AreaLevel <= 49
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->mana $tier->t7
	Class == "Mana Flasks"
	BaseType "Transcendent"
	AreaLevel <= 59
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

Show # $type->leveling->flasks->mana $tier->t8
	Class == "Mana Flasks"
	BaseType "Ultimate"
	AreaLevel <= 65
	SetFontSize 40
	SetBorderColor 100 100 100
	SetBackgroundColor 10 60 40

#------------------------------------

# [3503] Charms

#------------------------------------

# !! Waypoint c21.leveling.gear.all : "Leveling - Gear - All" : "Leveling"

#Show # %D4 $type->leveling->charms $tier->selected !typebased_flaskcharms

# Rarity Normal Magic

# BaseType == "Amethyst Charm" "Antidote Charm" "Dousing Charm" "Golden Charm" "Grounding Charm" "Stone Charm" "Thawing Charm"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 100 100 100

# SetBackgroundColor 10 60 40

#Show # %D2 $type->leveling->charms $tier->any !typebased_flaskcharms

# Rarity Normal Magic

# Class == "Charms"

# AreaLevel <= 64

# SetFontSize 40

# SetBorderColor 100 100 100

# SetBackgroundColor 10 60 40

#===============================================================================================================

# [[3600]] Leveling - Rules

#===============================================================================================================
#------------------------------------

# [3601] Rares - Decorators

#------------------------------------

# !! Waypoint c21.leveling.decorators.all : "Leveling - Rares - Decorators" : "Leveling"

#Show # $type->leveling->decorators->rare $tier->largerares !gear_unstyled

# Width >= 2

# Height >= 3

# Rarity Rare

# AreaLevel <= 64

# Continue

#Show # $type->leveling->decorators->rare $tier->mediumrares1 !gear_unstyled

# Width 1

# Height >= 3

# Rarity Rare

# AreaLevel <= 64

# Continue

#Show # $type->leveling->decorators->rare $tier->mediumrares2 !gear_unstyled

# Width 2

# Height 2

# Rarity Rare

# AreaLevel <= 64

# Continue

Show # $type->leveling->decorators->rare $tier->tinyrares !gear_decojewellery
	Width <= 2
	Height 1
	Rarity Rare
	AreaLevel <= 64
	SetBorderColor 220 220 0
	Continue

#------------------------------------

# [3602] Rares - Universal

#------------------------------------

# !! Waypoint c21.leveling.rares.jewellery : "Leveling - Rares - Belts, Rings, Amulets" : "Leveling"

Show # %D6 $type->leveling->rare->universal $tier->jewellery !gear_jewellery1
	Rarity Rare
	Class == "Amulets" "Belts" "Rings"
	AreaLevel <= 64
	SetFontSize 42
	SetBackgroundColor 75 75 0
	PlayEffect Yellow
	MinimapIcon 1 White Diamond

Show # %D6 $type->leveling->rare->universal $tier->highertier4 !exotics_btier
	UnidentifiedItemTier >= 4
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	AreaLevel <= 64
	SetFontSize 42
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

#Show # %D4 $type->leveling->rare->universal $tier->highertier3 !exotics_ctier

# UnidentifiedItemTier >= 3

# Rarity Rare

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel <= 64

# SetFontSize 40

# SetTextColor 0 240 190 255

# PlayAlertSound 3 300

# PlayEffect Blue

# MinimapIcon 1 Blue Diamond

# !! Waypoint c21.leveling.rares.armors : "Leveling - Rares - Armour Pieces" : "Leveling"

#Show # %D4 $type->leveling->rare->armours $tier->ar !gear_highlightedsize

# BaseEnergyShield 0

# BaseEvasion 0

# BaseArmour > 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->armours $tier->ev !gear_highlightedsize

# BaseEnergyShield 0

# BaseEvasion > 0

# BaseArmour 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->armours $tier->es !gear_highlightedsize

# BaseEnergyShield > 0

# BaseEvasion 0

# BaseArmour 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->armours $tier->arev !gear_highlightedsize

# BaseEnergyShield 0

# BaseEvasion > 0

# BaseArmour > 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->armours $tier->ares !gear_highlightedsize

# BaseEnergyShield > 0

# BaseEvasion 0

# BaseArmour > 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->armours $tier->eves !gear_highlightedsize

# BaseEnergyShield > 0

# BaseEvasion > 0

# BaseArmour 0

# Rarity Rare

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->wands !gear_highlightedsize

# Rarity Rare

# Class == "Wands"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->foci !gear_highlightedsize

# Rarity Rare

# Class == "Foci"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->shieldsar !gear_highlightedsize

# Rarity Rare

# Class == "Shields"

# BaseType "Tower Shield"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->shieldsarev !gear_highlightedsize

# Rarity Rare

# Class == "Shields"

# BaseType "Targe"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->shieldsares !gear_highlightedsize

# Rarity Rare

# Class == "Shields"

# BaseType "Crest Shield"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->sceptres !gear_highlightedsize

# Rarity Rare

# Class == "Sceptres"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->staves !gear_highlightedsize

# Rarity Rare

# Class == "Staves"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->bows !gear_highlightedsize

# Rarity Rare

# Class == "Bows"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->quivers !gear_highlightedsize

# Rarity Rare

# Class == "Quivers"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->crossbows !gear_highlightedsize

# Rarity Rare

# Class == "Crossbows"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->spears !gear_highlightedsize

# Rarity Rare

# Class == "Spears"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->bucklers !gear_highlightedsize

# Rarity Rare

# Class == "Bucklers"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->onehandmaces !gear_highlightedsize

# Rarity Rare

# Class == "One Hand Maces"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->twohandmaces !gear_highlightedsize

# Rarity Rare

# Class == "Two Hand Maces"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->talismans !gear_highlightedsize

# Rarity Rare

# Class == "Talismans"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#Show # %D4 $type->leveling->rare->weapons $tier->quarterstaves !gear_highlightedsize

# Rarity Rare

# Class == "Quarterstaves"

# AreaLevel <= 64

# SetFontSize 40

# SetBackgroundColor 20 20 0 255

#------------------------------------

# [3603] Rares - Other

#------------------------------------

# !! Waypoint c21.leveling.rares.low : "Leveling - Gear - Low Tier" : "Leveling"

Show # %H5 $type->leveling->rare->remaining $tier->anythingact1 class == "body armours" "gloves" "boots" "helmets" "shields" "foci" "bucklers" "staves" "sceptres" "wands" "one hand maces" "spears" "quarterstaves" "two hand maces" "bows" "crossbows" "talismans" "quivers" "amulets" "belts" "rings" !gear_weakrareleveling1
	Rarity Rare
	AreaLevel <= 16
	SetFontSize 38
	SetBackgroundColor 35 35 35 240

Hide # %H4 $type->leveling->rare->remaining $tier->anythingact2 class == "body armours" "gloves" "boots" "helmets" "shields" "foci" "bucklers" "staves" "sceptres" "wands" "one hand maces" "spears" "quarterstaves" "two hand maces" "bows" "crossbows" "talismans" "quivers" "amulets" "belts" "rings" !gear_weakrareleveling1
	Rarity Rare
	AreaLevel <= 24
	SetFontSize 38
	SetBackgroundColor 35 35 35 240

Hide # %H3 $type->leveling->rare->remaining $tier->any class == "body armours" "gloves" "boots" "helmets" "shields" "foci" "bucklers" "staves" "sceptres" "wands" "one hand maces" "spears" "quarterstaves" "two hand maces" "bows" "crossbows" "talismans" "quivers" "amulets" "belts" "rings" !gear_weakrare1
	Rarity Rare
	AreaLevel <= 64
	SetFontSize 35
	SetBackgroundColor 35 35 35 240

#===============================================================================================================

# [[3700]] Leveling - Useful magic and normal items

#===============================================================================================================
#------------------------------------

# [3701] Decorators

#------------------------------------

# !! Waypoint c21.leveling.magicvendor.all : "Leveling - Normal and Magic - Magic Vendor Items" : "Leveling"

Show # $type->decorators->leveling->magic $tier->largemagic !utility_highlight4
	Width >= 2
	Height >= 3
	Rarity Magic
	AreaLevel <= 64
	SetFontSize 38
	Continue

Show # $type->decorators->leveling->magic $tier->medium1 !utility_highlight4
	Width 1
	Height >= 3
	Rarity Magic
	AreaLevel <= 64
	SetFontSize 38
	Continue

Show # $type->decorators->leveling->magic $tier->medium2 !utility_highlight4
	Width 2
	Height 2
	Rarity Magic
	AreaLevel <= 64
	SetFontSize 38
	Continue

Show # $type->decorators->leveling->magic $tier->noticeearly !utility_highlight3
	Rarity Magic
	AreaLevel <= 9
	SetFontSize 40
	Continue

Show # $type->decorators->leveling->magic $tier->tiny !utility_highlight3
	Width <= 2
	Height 1
	Rarity Magic
	AreaLevel <= 64
	SetFontSize 40
	Continue

#------------------------------------

# [3702] Purpose Picked Items

#------------------------------------

# !! Waypoint c21.leveling.normalmagic : "Leveling - Remarkable Normal and Magic Gear" : "Leveling"

#Show # %D4 $type->leveling->normalmagicremarkable $tier->jewellery !gear_highlightdrop2

# Rarity Normal Magic

# Class == "Amulets" "Belts" "Rings"

# SetFontSize 42

# SetBackgroundColor 30 0 70 255

Show # %D5 $type->leveling->normalmagicremarkable $tier->earlyboots !gear_highlightdrop2
	Rarity Magic
	Class == "Boots"
	AreaLevel <= 32
	SetFontSize 42
	SetBackgroundColor 30 0 70 255

#------------------------------------

# [3703] Conditional Rules

#------------------------------------

# !! Waypoint c21.leveling.firstlevels.all : "Leveling - Normal and Magic - First Levels" : "Leveling"

Show # %D5 $type->leveling->firstlevelsmagic $tier->any !utility_highlight4
	Rarity Magic
	AreaLevel <= 3
	SetFontSize 38

#Hide # %RH1 $type->leveling->progressivehide $tier->normal1 !utility_minimize

# DropLevel < 8

# Rarity Normal

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 22

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH1 $type->leveling->progressivehide $tier->normal2 !utility_minimize

# DropLevel < 16

# Rarity Normal

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 30

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH1 $type->leveling->progressivehide $tier->normal3 !utility_minimize

# DropLevel < 24

# Rarity Normal

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 40

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH1 $type->leveling->progressivehide $tier->normal4 !utility_minimize

# DropLevel < 32

# Rarity Normal

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 48

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH1 $type->leveling->progressivehide $tier->normal5 !utility_minimize

# DropLevel < 40

# Rarity Normal

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 56

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH1 $type->leveling->progressivehide $tier->normal6 !utility_minimize

# DropLevel < 44

# Rarity Normal

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 60

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH2 $type->leveling->progressivehide $tier->magic1 !utility_minimize

# DropLevel < 8

# Rarity Magic

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 22

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH2 $type->leveling->progressivehide $tier->magic2 !utility_minimize

# DropLevel < 16

# Rarity Magic

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 30

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH2 $type->leveling->progressivehide $tier->magic3 !utility_minimize

# DropLevel < 24

# Rarity Magic

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 40

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH2 $type->leveling->progressivehide $tier->magic4 !utility_minimize

# DropLevel < 32

# Rarity Magic

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 48

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH2 $type->leveling->progressivehide $tier->magic5 !utility_minimize

# DropLevel < 40

# Rarity Magic

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 56

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Hide # %RH2 $type->leveling->progressivehide $tier->magic6 !utility_minimize

# DropLevel < 44

# Rarity Magic

# Class == "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Shields" "Spears" "Talismans" "Two Hand Maces"

# AreaLevel >= 60

# SetFontSize 18

# SetBackgroundColor 20 20 0 0

#Show # %D3 $type->leveling->normalmagic->armours $tier->ar !gear_unstyled

# BaseEnergyShield 0

# BaseEvasion 0

# BaseArmour > 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

#Show # %D3 $type->leveling->normalmagic->armours $tier->ev !gear_unstyled

# BaseEnergyShield 0

# BaseEvasion > 0

# BaseArmour 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

#Show # %D3 $type->leveling->normalmagic->armours $tier->es !gear_unstyled

# BaseEnergyShield > 0

# BaseEvasion 0

# BaseArmour 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

#Show # %D3 $type->leveling->normalmagic->armours $tier->arev !gear_unstyled

# BaseEnergyShield 0

# BaseEvasion > 0

# BaseArmour > 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

#Show # %D3 $type->leveling->normalmagic->armours $tier->ares !gear_unstyled

# BaseEnergyShield > 0

# BaseEvasion 0

# BaseArmour > 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

#Show # %D3 $type->leveling->normalmagic->armours $tier->eves !gear_unstyled

# BaseEnergyShield > 0

# BaseEvasion > 0

# BaseArmour 0

# Rarity Normal Magic

# Class == "Body Armours" "Boots" "Gloves" "Helmets"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->wands !gear_unstyled

# Rarity Normal Magic

# Class == "Wands"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->foci !gear_unstyled

# Rarity Normal Magic

# Class == "Foci"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->shieldsar !gear_unstyled

# Rarity Normal Magic

# Class == "Shields"

# BaseType "Tower Shield"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->shieldsarev !gear_unstyled

# Rarity Normal Magic

# Class == "Shields"

# BaseType "Targe"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->shieldsares !gear_unstyled

# Rarity Normal Magic

# Class == "Shields"

# BaseType "Crest Shield"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->sceptres !gear_unstyled

# Rarity Normal Magic

# Class == "Sceptres"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->staves !gear_unstyled

# Rarity Normal Magic

# Class == "Staves"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->bows !gear_unstyled

# Rarity Normal Magic

# Class == "Bows"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->quivers !gear_unstyled

# Rarity Normal Magic

# Class == "Quivers"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->crossbows !gear_unstyled

# Rarity Normal Magic

# Class == "Crossbows"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->spears !gear_unstyled

# Rarity Normal Magic

# Class == "Spears"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->bucklers !gear_unstyled

# Rarity Normal Magic

# Class == "Bucklers"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->onehandmaces !gear_unstyled

# Rarity Normal Magic

# Class == "One Hand Maces"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->twohandmaces !gear_unstyled

# Rarity Normal Magic

# Class == "Two Hand Maces"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->talismans !gear_unstyled

# Rarity Normal Magic

# Class == "Talismans"

#Show # %D3 $type->leveling->normalmagic->weapons $tier->quarterstaves !gear_unstyled

# Rarity Normal Magic

# Class == "Quarterstaves"

#Show # %D2 $type->leveling->magic->remaining $tier->rest !gear_vendor

# Rarity Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 24

# AreaLevel <= 64

# SetFontSize 30

# SetBorderColor 0 0 0 0

# SetBackgroundColor 20 20 0 180

#Show # %D4 $type->leveling->magic->remaining $tier->act2 !gear_vendor

# Rarity Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 16

# AreaLevel <= 24

# SetFontSize 30

# SetBorderColor 0 0 0 0

# SetBackgroundColor 20 20 0 180

#Show # %D4 $type->leveling->magic->remaining $tier->act1 !gear_vendor

# Rarity Magic

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Crossbows" "Foci" "Gloves" "Helmets" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# AreaLevel >= 3

# AreaLevel <= 16

# SetFontSize 30

# SetBorderColor 0 0 0 0

# SetBackgroundColor 20 20 0 180

Show # %D5 $type->leveling->firstlevelsnormal $tier->any !gear_unstyled
	Rarity Normal
	AreaLevel <= 3

# !! Waypoint c22.hide.all : "HIDELAYER - Hide all known untiered items" : "Technical"

#------------------------------------

# [3704] Hide All known Section

#------------------------------------

#Show # %D0 $type->lowstrictnessshowlayer $tier->anyfinal

# Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Charms" "Crossbows" "Foci" "Gloves" "Helmets" "Jewels" "Life Flasks" "Mana Flasks" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"

# SetFontSize 32

# SetBorderColor 0 0 0 0

# SetBackgroundColor 20 20 0 180

# DisableDropSound True

Hide # $type->hidelayer $tier->final
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Bucklers" "Charms" "Crossbows" "Foci" "Gloves" "Helmets" "Jewels" "Life Flasks" "Mana Flasks" "One Hand Maces" "Quarterstaves" "Quivers" "Rings" "Sceptres" "Shields" "Spears" "Staves" "Talismans" "Two Hand Maces" "Wands"
	SetFontSize 18
	SetBorderColor 0 0 0 0
	SetBackgroundColor 20 20 0 0
	DisableDropSound True

#------------------------------------

# [3705] Show All unknown Section

#------------------------------------

# !! Waypoint c22.show.all : "SAFETYLAYER - Show all unknown items" : "Technical"

# THIS ENTRY IS CAUGHT IN 3 CASES:

# 1) YOUR FILTER IS OUT OF DATE!

# 2) YOU DID SOMETHING SILLY WHEN EDITING THE FILTER

# 3) YOU ENCOUNTERED A PREVIOUSLY UNKNOWN ITEM (VERY UNLIKELY)

Show # $type->anyremaining $tier->restex !utility_unknownitem
	SetFontSize 45
	SetTextColor 0 255 255 255
	SetBorderColor 0 255 255 255
	SetBackgroundColor 255 0 255 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Pentagon
