"""
A Keymaster's Keep implementation of Bloons TD 6, created by Archer (ArcherestArcher).
Depending on YAML Options, the following objective types can be included:

- Completing specific difficulties on specific maps
- Beating specific tiers of specific boss bloons on specific maps
- Beating specific tiers of specific elite boss bloons on specific maps
"""

from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class BloonsTD6ArchipelagoOptions:
    bloons_td_6_include_beginner_maps: BloonsTD6IncludeBeginnerMaps
    bloons_td_6_include_intermediate_maps: BloonsTD6IncludeIntermediateMaps
    bloons_td_6_include_advanced_maps: BloonsTD6IncludeAdvancedMaps
    bloons_td_6_include_expert_maps: BloonsTD6IncludeExpertMaps
    bloons_td_6_include_easy_modes: BloonsTD6IncludeEasyModes
    bloons_td_6_easy_modes_selection: BloonsTD6EasyModesSelection
    bloons_td_6_include_medium_modes: BloonsTD6IncludeMediumModes
    bloons_td_6_medium_modes_selection: BloonsTD6MediumModesSelection
    bloons_td_6_include_hard_modes: BloonsTD6IncludeHardModes
    bloons_td_6_hard_modes_selection: BloonsTD6HardModesSelection
    bloons_td_6_include_boss_bloon_challenges: BloonsTD6IncludeBossBloonChallenges

class BloonsTD6Game(Game):
    """
    Bloons TD 6 is the 6th major installment of the Bloons TD series; a tower defense series where you place monkeys to pop bloons.
    """
    
    name = "Bloons TD 6"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.XONE,
    ]

    is_adult_only_or_unrated = False

    options_cls = BloonsTD6ArchipelagoOptions
    
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Cannot use Heroes",
                data={
                },
            ),
            GameObjectiveTemplate(
                label="Cannot use Tier 5 Upgrades",
                data={
                },
            ),
            GameObjectiveTemplate(
                label="Disable all Monkey Knowledge",
                data={
                },
            ),
        ]
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = list()
        
        if self.include_beginner_maps:
            if self.include_easy_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete BEGINNERMAP on EASYMODE",
                        data={
                            "BEGINNERMAP": (self.beginner_maps, 1),
                            "EASYMODE": (self.included_easy_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    ),
                )
            if self.include_medium_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete BEGINNERMAP on MEDIUMMODE",
                        data={
                            "BEGINNERMAP": (self.beginner_maps, 1),
                            "MEDIUMMODE": (self.included_medium_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    ),
                )
            if self.include_hard_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete BEGINNERMAP on HARDMODE",
                        data={
                            "BEGINNERMAP": (self.beginner_maps, 1),
                            "HARDMODE": (self.included_hard_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    ),
                )
        
        if self.include_intermediate_maps:
            if self.include_easy_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete INTERMEDIATEMAP on EASYMODE",
                        data={
                            "INTERMEDIATEMAP": (self.intermediate_maps, 1),
                            "EASYMODE": (self.included_easy_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    ),
                )
            if self.include_medium_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete INTERMEDIATEMAP on MEDIUMMODE",
                        data={
                            "INTERMEDIATEMAP": (self.intermediate_maps, 1),
                            "MEDIUMMODE": (self.included_medium_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    ),
                )
            if self.include_hard_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete INTERMEDIATEMAP on HARDMODE",
                        data={
                            "INTERMEDIATEMAP": (self.intermediate_maps, 1),
                            "HARDMODE": (self.included_hard_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=1,
                    ),
                )
        
        if self.include_advanced_maps:
            if self.include_easy_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete ADVANCEDMAP on EASYMODE",
                        data={
                            "ADVANCEDMAP": (self.advanced_maps, 1),
                            "EASYMODE": (self.included_easy_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    ),
                )
            if self.include_medium_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete ADVANCEDMAP on MEDIUMMODE",
                        data={
                            "ADVANCEDMAP": (self.advanced_maps, 1),
                            "MEDIUMMODE": (self.included_medium_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=1,
                    ),
                )
            if self.include_hard_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete ADVANCEDMAP on HARDMODE",
                        data={
                            "ADVANCEDMAP": (self.advanced_maps, 1),
                            "HARDMODE": (self.included_hard_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=1,
                    ),
                )
        
        if self.include_expert_maps:
            if self.include_easy_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete EXPERTMAP on EASYMODE",
                        data={
                            "EXPERTMAP": (self.expert_maps, 1),
                            "EASYMODE": (self.included_easy_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    ),
                )
            if self.include_medium_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete EXPERTMAP on MEDIUMMODE",
                        data={
                            "EXPERTMAP": (self.expert_maps, 1),
                            "MEDIUMMODE": (self.included_medium_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=1,
                    ),
                )
            if self.include_hard_modes:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Complete EXPERTMAP on HARDMODE",
                        data={
                            "EXPERTMAP": (self.expert_maps, 1),
                            "HARDMODE": (self.included_hard_modes, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=1,
                    ),
                )
        
        if self.include_boss_bloons:
            if self.include_beginner_maps:
                objectives.extend([
                    GameObjectiveTemplate(
                        label="Beat EASIERTIER BOSS on BEGINNERMAP",
                        data={
                            "EASIERTIER": (self.easier_tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "BEGINNERMAP": (self.beginner_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Beat HARDERTIER BOSS on BEGINNERMAP",
                        data={
                            "HARDERTIER": (self.harder_tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "BEGINNERMAP": (self.beginner_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Beat TIER Elite BOSS on BEGINNERMAP",
                        data={
                            "TIER": (self.tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "BEGINNERMAP": (self.beginner_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                ])
            
            if self.include_intermediate_maps:
                objectives.extend([
                    GameObjectiveTemplate(
                        label="Beat TIER BOSS on INTERMEDIATEMAP",
                        data={
                            "TIER": (self.tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "INTERMEDIATEMAP": (self.intermediate_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Beat TIER Elite BOSS on INTERMEDIATEMAP",
                        data={
                            "TIER": (self.tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "INTERMEDIATEMAP": (self.intermediate_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                ])
            
            if self.include_advanced_maps:
                objectives.extend([
                    GameObjectiveTemplate(
                        label="Beat TIER BOSS on ADVANCEDMAP",
                        data={
                            "TIER": (self.tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "ADVANCEDMAP": (self.advanced_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Beat TIER Elite BOSS on ADVANCEDMAP",
                        data={
                            "TIER": (self.tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "ADVANCEDMAP": (self.advanced_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                ])
            
            if self.include_expert_maps:
                objectives.extend([
                    GameObjectiveTemplate(
                        label="Beat TIER BOSS on EXPERTMAP",
                        data={
                            "TIER": (self.tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "EXPERTMAP": (self.expert_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Beat TIER Elite BOSS on ADVANCEDMAP",
                        data={
                            "TIER": (self.tiers, 1),
                            "BOSS": (self.bosses, 1),
                            "EXPERTMAP": (self.expert_maps, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                ])
            
        return objectives

    @property
    def include_beginner_maps(self) -> bool:
        return bool(self.archipelago_options.bloons_td_6_include_beginner_maps.value)

    @staticmethod
    def beginner_maps() -> List[str]:
        return [
            "Monkey Meadow",
            "In The Loop",
            "Three Mines 'Round",
            "Spa Pits",
            "Tinkerton",
            "Tree Stump",
            
            "Town Center",
            "Middle Of The Road",
            "One Two Tree",
            "Scrapyard",
            "The Cabin",
            "Resort",
            
            "Skates",
            "Lotus Island",
            "Candy Falls",
            "Winter Park",
            "Carved",
            "Park Path",
            
            "Alpine Run",
            "Frozen Over",
            "Cubism",
            "Four Circles",
            "Hedge",
            "End Of The Road",
            
            "Logs",
        ]

    @property
    def include_intermediate_maps(self) -> bool:
        return bool(self.archipelago_options.bloons_td_6_include_intermediate_maps.value)

    @staticmethod
    def intermediate_maps() -> List[str]:
        return [
            "Lost Crevasse",
            "Luminous Cove",
            "Sulfur Springs",
            "Water Park",
            "Polyphemus",
            "Covered Garden",
            
            "Quarry",
            "Quiet Street",
            "Bloonarius Prime",
            "Balance",
            "Encrypted",
            "Bazaar",
            
            "Adora's Temple",
            "Spring Spring",
            "KartsNDarts"
            "Moon Landing",
            "Haunted",
            "Downstream",
            
            "Firing Range",
            "Cracked",
            "Streambed",
            "Chutes",
            "Rake",
            "Spice Islands",
        ]

    @property
    def include_advanced_maps(self) -> bool:
        return bool(self.archipelago_options.bloons_td_6_include_advanced_maps.value)

    @staticmethod
    def advanced_maps() -> List[str]:
        return [
            "Sunset Gulch",
            "Enchanted Glade",
            "Last Resort",
            "Ancient Portal",
            "Castle Revenge",
            "Dark Path",
            
            "Erosion",
            "Midnight Mansion",
            "Sunken Columns",
            "X Factor",
            "Mesa",
            "Geared",
            
            "Spillway",
            "Cargo",
            "Pat's Pond",
            "Peninsula",
            "High Finance",
            "Another Brick",
            
            "Off The Coast",
            "Cornfield",
            "Underground",
        ]

    @property
    def include_expert_maps(self) -> bool:
        return bool(self.archipelago_options.bloons_td_6_include_expert_maps.value)

    @staticmethod
    def expert_maps() -> List[str]:
        return [
            "Tricky Tracks",
            "Glacial Trail",
            "Dark Dungeons",
            "Sanctuary",
            "Ravine",
            "Flooded Valley",
            
            "Infernal",
            "Bloody Puddles",
            "Workshop",
            "Quad",
            "Dark Castle",
            "Muddy Puddles",
            
            "#Ouch",
        ]

    @property
    def include_easy_modes(self) -> bool:
        return bool(self.archipelago_options.bloons_td_6_include_easy_modes.value)

    @staticmethod
    def easy_modes() -> List[str]:
        return [
            "Standard Easy",
            "Primary Only",
            "Deflation",
        ]
    
    def included_easy_modes(self) -> List[str]:
        return sorted(self.archipelago_options.bloons_td_6_easy_modes_selection.value)
    
    @property
    def include_medium_modes(self) -> bool:
        return bool(self.archipelago_options.bloons_td_6_include_medium_modes.value)
    
    @staticmethod
    def medium_modes() -> List[str]:
        return [
            "Standard Medium",
            "Military Only",
            "Apopalypse",
            "Reverse",
        ]
    
    def included_medium_modes(self) -> List[str]:
        return sorted(self.archipelago_options.bloons_td_6_medium_modes_selection.value)
    
    @property
    def include_hard_modes(self) -> bool:
        return bool(self.archipelago_options.bloons_td_6_include_hard_modes.value)
    
    @staticmethod
    def hard_modes() -> List[str]:
        return [
            "Standard Hard",
            "Magic Monkeys Only",
            "Double HP MOABS",
            "Half Cash",
            "Alternate Bloons Rounds",
            "Impoppable",
            "CHIMPS",
        ]
    
    def included_hard_modes(self) -> List[str]:
        return sorted(self.archipelago_options.bloons_td_6_hard_modes_selection.value)

    @property
    def include_boss_bloons(self) -> bool:
        return bool(self.archipelago_options.bloons_td_6_include_boss_bloon_challenges.value)
    
    @staticmethod
    def bosses() -> List[str]:
        return [
            "Bloonarius",
            "Lych",
            "Vortex",
            "Dreadbloon",
            "Phayze",
            "Blastapopoulos",
        ]
    
    @staticmethod
    def easier_tiers() -> List[str]:
        return [
            "Tier 1",
            "Tier 2",
        ]
    
    @staticmethod
    def harder_tiers() -> List[str]:
        return [
            "Tier 3",
            "Tier 4",
            "Tier 5",
        ]
    
    @staticmethod
    def tiers() -> List[str]:
        return [
            "Tier 1",
            "Tier 2",
            "Tier 3",
            "Tier 4",
            "Tier 5",
        ]

class BloonsTD6IncludeBeginnerMaps(DefaultOnToggle):
    """
    Indicates whether to include Beginner maps when generating Bloons TD 6 objectives.
    
    Note: At least one map type needs to be included for the implementation to function.
    """

    display_name = "Bloons TD 6 Include Beginner Maps"

class BloonsTD6IncludeIntermediateMaps(DefaultOnToggle):
    """
    Indicates whether to include Intermediate maps when generating Bloons TD 6 objectives.
    
    Note: At least one map type needs to be included for the implementation to function.
    """

    display_name = "Bloons TD 6 Include Intermediate Maps"

class BloonsTD6IncludeAdvancedMaps(DefaultOnToggle):
    """
    Indicates whether to include Advanced maps when generating Bloons TD 6 objectives.
    
    Note: At least one map type needs to be included for the implementation to function.
    """

    display_name = "Bloons TD 6 Include Advanced Maps"

class BloonsTD6IncludeExpertMaps(Toggle):
    """
    Indicates whether to include Expert maps when generating Bloons TD 6 objectives.
    
    Note: At least one map type needs to be included for the implementation to function.
    """

    display_name = "Bloons TD 6 Include Expert Maps"

class BloonsTD6IncludeEasyModes(DefaultOnToggle):
    """
    Indicates whether to include the Easy difficulty modes when generating Bloons TD 6 objectives.
    
    Note: At least one set of modes need to be included for the implementation to function.
    """

    display_name = "Bloons TD 6 Include Easy Modes"

class BloonsTD6EasyModesSelection(OptionSet):
    """
    Which Easy modes to include when including the Easy difficulty modes.
    """
    
    display_name = "Bloons TD 6 Easy Modes Selection"
    valid_keys = BloonsTD6Game().easy_modes()

    default = valid_keys

class BloonsTD6IncludeMediumModes(DefaultOnToggle):
    """
    Indicates whether to include the Medium difficulty modes when generating Bloons TD 6 objectives.
    
    Note: At least one set of modes need to be included for the implementation to function.
    """

    display_name = "Bloons TD 6 Include Medium Modes"

class BloonsTD6MediumModesSelection(OptionSet):
    """
    Which Medium modes to include when including the Medium difficulty modes.
    """
    
    display_name = "Bloons TD 6 Medium Modes Selection"
    valid_keys = BloonsTD6Game().medium_modes()

    default = valid_keys

class BloonsTD6IncludeHardModes(DefaultOnToggle):
    """
    Indicates whether to include the Hard difficulty modes when generating Bloons TD 6 objectives.
    
    Note: At least one set of modes need to be included for the implementation to function.
    """

    display_name = "Bloons TD 6 Include Hard Modes"

class BloonsTD6HardModesSelection(OptionSet):
    """
    Which Hard modes to include when including the Hard difficulty modes.
    """
    
    display_name = "Bloons TD 6 Hard Modes Selection"
    valid_keys = BloonsTD6Game().hard_modes()

    default = valid_keys
    
class BloonsTD6IncludeBossBloonChallenges(Toggle):
    """
    Indicates whether to include Boss Bloon Challenges when generating Bloons TD 6 objectives.
    """
    
    display_name = "Bloons TD 6 Include Boss Bloon Challenges"
