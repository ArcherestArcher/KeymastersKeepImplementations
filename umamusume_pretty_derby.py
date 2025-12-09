"""
A Keymaster's Keep implementation of Umamusume: Pretty Derby, created by Archer (ArcherestArcher).
Depending on YAML Options, the following objective types can be included:

- Winning or getting certain placements in the Make Debut or in specific Graded Races
- Winning the URA Finale
- Winning or drawing against certain Unity Cup teams in the four preliminary rounds
- Winning against Team Zenith in the final Unity Cup round
- Winning against Little Cocon or Bitter Glasse in the URA Finale
- Getting the Good Ending with a specific trainee in a specific scenario
- Getting the Unique Epithet for a specific trainee
"""

from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, OptionList

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class UmamusumePrettyDerbyArchipelagoOptions:
    umamusume_pretty_derby_trainees_owned: UmamusumePrettyDerbyTraineesOwned
    umamusume_pretty_derby_include_trainee_challenges: UmamusumePrettyDerbyIncludeTraineeChallenges
    umamusume_pretty_derby_include_g1: UmamusumePrettyDerbyIncludeG1
    umamusume_pretty_derby_include_g2: UmamusumePrettyDerbyIncludeG2
    umamusume_pretty_derby_include_g3: UmamusumePrettyDerbyIncludeG3
    umamusume_pretty_derby_include_ura_finale: UmamusumePrettyDerbyIncludeURAFinale
    umamusume_pretty_derby_include_unity_cup: UmamusumePrettyDerbyIncludeUnityCup

class UmamusumePrettyDerbyGame(Game):
    """
    Umamusume: Pretty Derby is a Sports Simulation and Raising Simulation game, where you train horsegirls known as Umamusume to win races against other Umamusume.

    The multimedia series it is part of takes heavy inspiration from real life Japanese horse-racing.
    A majority of Umamusume are named after real horses, and have careers and stories heavily inspired by their namesakes.
    """
    
    name = "Umamusume: Pretty Derby"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
    ]

    is_adult_only_or_unrated = False

    options_cls = UmamusumePrettyDerbyArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Complete these goals whilst only training STAT, if that is possible",
                data={
                    "STAT": (self.stats, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Try to complete these goals in as few Career Runs as is possible",
                data={
                },
            ),
        ]
        
        if self.include_trainee_constraints:
            objectives.append(
                GameObjectiveTemplate(
                    label="Use TRAINEE to complete these goals, if that is possible",
                    data={
                        "TRAINEE": (self.trainees, 1),
                    },
                ),
            )
        
        return objectives

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Win 1st in RACE within Career Mode",
                data={
                    "RACE": (self.races, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get at least 2nd in RACE within Career Mode",
                data={
                    "RACE": (self.races, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get at least 3rd in RACE within Career Mode",
                data={
                    "RACE": (self.races, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get at least 4th in RACE within Career Mode",
                data={
                    "RACE": (self.races, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get at least 5th in RACE within Career Mode",
                data={
                    "RACE": (self.races, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]
        
        if self.include_ura_finale:
            objectives.append(
                GameObjectiveTemplate(
                    label="Win 1st in RACE within Career Mode",
                    data={
                        "RACE": (self.races_ura_finale,1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                )
            )
        
        if self.include_unity_cup:
            objectives.extend([
                GameObjectiveTemplate(
                    label="Win against the strongest team available in ROUND",
                    data={
                        "ROUND": (self.rounds_unity_cup,1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Win or Draw against the strongest team available in ROUND",
                    data={
                        "ROUND": (self.rounds_unity_cup,1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Win against the middle team available in ROUND",
                    data={
                        "ROUND": (self.rounds_unity_cup,1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Win or Draw against the middle team available in ROUND",
                    data={
                        "ROUND": (self.rounds_unity_cup,1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Win against the weakest team available in ROUND",
                    data={
                        "ROUND": (self.rounds_unity_cup,1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Win or Draw against the weakest team available in ROUND",
                    data={
                        "ROUND": (self.rounds_unity_cup,1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Win against Team Zenith at the end of the Unity Cup.",
                    data={
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
            ])
            
            if self.include_ura_finale:
                objectives.append(
                    GameObjectiveTemplate(
                        label="Win against Little Cocon or Bitter Glasse in the URA Finale",
                        data={
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    )
                )
        
        if self.include_trainee_challenges:
            objectives.extend([
                GameObjectiveTemplate(
                    label="Get the Good Ending in the SCENARIO scenario with TRAINEE",
                    data={
                        "SCENARIO": (self.scenarios,1),
                        "TRAINEE": (self.trainees,1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Get the unique epithet for TRAINEE",
                    data={
                        "SCENARIO": (self.scenarios,1),
                        "TRAINEE": (self.trainees,1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ])
        
        return objectives

    @functools.cached_property
    def races_base(self) -> List[str]:
        return [
            "Junior Make Debut",
        ]
    
    @property
    def include_g1(self) -> bool:
        return bool(self.archipelago_options.umamusume_pretty_derby_include_g1.value)

    @functools.cached_property
    def races_g1(self) -> List[str]:
        return [
            "Asahi Hai Futurity Stakes",
            "Hanshin Juvenile Fillies",
            "Hopeful Stakes",
            
            "Satsuki Sho",
            "NHK Mile Cup",
            "Tokyo Yushun (Japanese Derby)",
            "Yasuda Kinen",
            "Takarazuka Kinen",
            "Japan Dirt Derby",
            "Sprinters Stakes",
            "Kikuka Sho",
            "JBC Classic",
            "JBC Ladies' Classic",
            "JBC Sprint",
            "Queen Elizabeth II Cup",
            "Japan Cup",
            "Mile Championship",
            "Champions Cup",
            "Arima Kinen",
            "Tokyo Daishoten",

            "Februrary Stakes",
            "Tenno Sho (Spring)",
            "Victoria Mile",
            "Teio Sho",
            "Tenno Sho (Autumn)",
        ]

    @property
    def include_g2(self) -> bool:
        return bool(self.archipelago_options.umamusume_pretty_derby_include_g2.value)

    @functools.cached_property
    def races_g2(self) -> List[str]:
        return [
            "Daily Hai Junior Stakes",
            "Keio Hai Junior Stakes",

            "Fillies' Revue",
            "Tulip Sho",
            "Yayoi Sho",
            "Spring Stakes",
            "Aoba Sho",
            "Flora Stakes",
            "Kyoto Shimbun Hai",
            "Sapporo Kinen",
            "Centaur Stakes",
            "Rose Stakes",
            "All Comers",
            "Kobe Shimbun Hai",
            "St. Lite Kinen",
            "Fuchu Umamusume Stakes",
            "Kyoto Daishoten",
            "Mainichi Okan",
            "Copa Republica Argentina",
            "Stayers Stakes",
            "Hanshin Cup",

            "Nikkei Shinsun Hai",
            "American JCC",
            "Tokai Stakes",
            "Kyoto Kinen",
            "Nakayama Kinen",
            "Kinko Sho",
            "Nikkei Sho",
            "Hanshin Umamusume Stakes",
            "Keio Hai Spring Cup",
            "Meguro Kinen",
        ]

    @property
    def include_g3(self) -> bool:
        return bool(self.archipelago_options.umamusume_pretty_derby_include_g3.value)

    @functools.cached_property
    def races_g3(self) -> List[str]:
        return [
            "Hakodate Junior Stakes",
            "Niigata Junior Stakes",
            "Kokura Junior Stakes",
            "Sapporo Junior Stakes",
            "Saudi Arabia Royal Cup",
            "Artemis Stakes",
            "Fantasy Stakes",
            "Kyoto Junior Stakes",
            "Tokyo Sports Hai Junior Stakes",

            "Fairy Stakes",
            "Keisei Hai",
            "Shinzan Kinen",
            "Kisaragi Sho",
            "Kyodo News Hai",
            "Queen Cup",
            "Falcon Stakes",
            "Flower Cup",
            "Mainichi Hai",
            "Epsom Cup",
            "Mermaid Stakes",
            "Naruo Kinen",
            "Hakodate Sprint Stakes",
            "Unicorn Stakes",
            "CBC Sho",
            "Hakodate Kinen",
            "Procyon Stakes",
            "Radio Nikkei Sho",
            "Tanabata Sho",
            "Chukyo Kinen",
            "Ibis Summer Dash",
            "Queen Stakes",
            "Elm Stakes",
            "Kokura Kinen",
            "Leopard Stakes",
            "Sekiya Kinen",
            "Keeneland Cup",
            "Kitakyushu Kinen",
            "Shion Stakes",
            "Sirius Stakes",
            "Fukushima Kinen",
            "Miyako Stakes",
            "Musashino Stakes",
            "Keihan Hai",
            "Capella Stakes",
            "Challenge Cup",
            "Chunichi Shimbun Hai",
            "Turquoise Stakes",

            "Aichi Hai",
            "Kyoto Kimpai",
            "Nakayama Kimpai",
            "Negishi Stakes",
            "Silk Road Stakes",
            "Tokyo Shimbun Hai",
            "Diamond Stakes",
            "Hankyu Hai",
            "Kokura Daishoten",
            "Kyoto Umamusume Stakes",
            "Nakayama Umamusume Stakes",
            "Ocean Stakes",
            "Antares Stakes",
            "Lord Derby Challenge Trophy",
            "Niigata Daishoten",
            "Heian Stakes",
            "Keisai Hai Autumn Handicap",
            "Niigata Kinen",
        ]

    @property
    def include_ura_finale(self) -> bool:
        return bool(self.archipelago_options.umamusume_pretty_derby_include_ura_finale.value)

    @functools.cached_property
    def races_ura_finale(self) -> List[str]:
        return [
            "Ura Finals Final (Dirt)",
            "Ura Finals Final (Sprint)",
            "Ura Finals Final (Mile)",
            "Ura Finals Final (Medium)",
            "Ura Finals Final (Long)",
        ]

    def races(self) -> List[str]:
        races: List[str] = self.races_base[:]

        # Check if G1 races are included, and include them if so
        if self.include_g1:
            races.extend(self.races_g1[:])

        # Check if G2 races are included, and include them if so
        if self.include_g2:
            races.extend(self.races_g2[:])

        # Check if G3 races are included, and include them if so
        if self.include_g3:
            races.extend(self.races_g3[:])

        return races
    
    @property
    def include_unity_cup(self) -> bool:
        return bool(self.archipelago_options.umamusume_pretty_derby_include_unity_cup.value)
    
    @staticmethod
    def rounds_unity_cup() -> List[str]:
        return [
            "Unity Cup Round 1 (December Junior Year)",
            "Unity Cup Round 2 (June Classic Year)",
            "Unity Cup Round 3 (December Classic Year)",
            "Unity Cup Round 4 (June Senior Year)",
        ]

    @staticmethod
    def stats() -> List[str]:
        return [
            "Speed",
            "Stamina",
            "Power",
            "Guts",
            "Wit",
        ]

    def trainees(self) -> List[str]:
        trainees: List[str] = list(self.archipelago_options.umamusume_pretty_derby_trainees_owned.value)
        return sorted(trainees)

    @property
    def include_trainee_challenges(self) -> bool:
        return bool(self.archipelago_options.umamusume_pretty_derby_include_trainee_challenges.value)
    
    @property
    # I was paranoid about the "== False" working or not, so did this because it felt safer.
    def include_trainee_constraints(self) -> bool:
        if self.include_trainee_challenges:
            return False
        else:
            return True
    
    @staticmethod
    def scenarios() -> List[str]:
        return [
            "URA Finale",
            "Unity Cup",
        ]

# Archipelago Options
class UmamusumePrettyDerbyTraineesOwned(OptionList):
    """
    Indicates which trainees the player owns in Umamusume: Pretty Derby.
    
    If trainee challenges are on, these are the trainees that will be used for those objectives.
    If trainee challenges are off, these trainees instead will be used for one of the potential optional constraints.
    
    This list was made as an OptionList, meaning that you can add any text you want here without issue.
    As such, you can duplicate trainee names if you want to increase their odds of showing up,
    or if the current list isn't up to date, you can update it yourself with no game errors.
    """

    display_name = "Umamusume: Pretty Derby Trainees Owned"
    default  = [
        "Agnes Digital",
        "Agnes Tachyon",
        "Air Groove (Normal)",
        "Air Groove (Wedding)",
        "Biwa Hayahide",
        "Curren Chan",
        "Daiwa Scarlet",
        "Eishin Flash",
        "El Condor Pasa (Normal)",
        "El Condor Pasa (Fantasy)",
        "Fuji Kiseki",
        "Gold City",
        "Gold Ship",
        "Grass Wonder (Normal)",
        "Grass Wonder (Fantasy)",
        "Haru Urara",
        "Hishi Akebono",
        "Hishi Amazon",
        "Kawakami Princess",
        "King Halo",
        "Maruzensky (Normal)",
        "Maruzensky (Summer)",
        "Matikanefukukitaru (Normal)",
        "Matikanefukukitaru (Full Armour)",
        "Mayano Top Gun (Normal)",
        "Mayano Top Gun (Wedding)",
        "Meisho Doto",
        "Mejiro McQueen (Normal)",
        "Mejiro McQueen (Anime Collab)",
        "Mejiro Ryan",
        "Mihono Bourbon",
        "Narita Brian",
        "Narita Taishin",
        "Nice Nature",
        "Oguri Cap",
        "Rice Shower (Normal)",
        "Rice Shower (Halloween)",
        "Sakura Bakushin O",
        "Seiun Sky",
        "Silence Suzuka",
        "Smart Falcon",
        "Special Week (Normal)",
        "Special Week (Summer)",
        "Super Creek (Normal)",
        "Super Creek (Halloween)",
        "Symboli Rudolf",
        "Taiki Shuttle",
        "TM Opera O",
        "Tokai Teio (Normal)",
        "Tokai Teio (Anime Collab)",
        "Vodka",
        "Winning Ticket",
    ]

class UmamusumePrettyDerbyIncludeTraineeChallenges(DefaultOnToggle):
    """
    Indicates whether to include more Trainee focused challenges when generating Umamusume: Pretty Derby objectives.
    """

    display_name = "Umamusume: Pretty Derby Include Trainee Challenges"

class UmamusumePrettyDerbyIncludeG1(DefaultOnToggle):
    """
    Indicates whether to include G1 Races when generating Umamusume: Pretty Derby objectives.
    """

    display_name = "Umamusume: Pretty Derby Include G1 Races"

class UmamusumePrettyDerbyIncludeG2(DefaultOnToggle):
    """
    Indicates whether to include G2 Races when generating Umamusume: Pretty Derby objectives.
    """

    display_name = "Umamusume: Pretty Derby Include G2 Races"

class UmamusumePrettyDerbyIncludeG3(DefaultOnToggle):
    """
    Indicates whether to include G3 Races when generating Umamusume: Pretty Derby objectives.
    """

    display_name = "Umamusume: Pretty Derby Include G3 Races"

class UmamusumePrettyDerbyIncludeURAFinale(Toggle):
    """
    Indicates whether to include objectives to win any of the five variations of the URA Finale Final.
    
    Since which variation you get is determined by what race type you raced the most in a run,
    with ties going to the shorter distance - please only include if you're willing to plan to
    both run and win URA Finale (Long), since that one strictly requires planning.
    """

    display_name = "Umamusume: Pretty Derby Include URA Finale"

class UmamusumePrettyDerbyIncludeUnityCup(Toggle):
    """
    Indicates whether to include objectives involving the Unity Cup races from the Unity Cup scenario.
    
    Beating Team Zenith is one of the objectives.
    If URA Finale is also set to included, one of the possible objectives is beating Little Cocon or Bitter Glasse there.
    These are set as difficult challenges, and for good reason. Be warned.
    """
    
    display_name = "Umamusume: Pretty Derby Include Unity Cup"



