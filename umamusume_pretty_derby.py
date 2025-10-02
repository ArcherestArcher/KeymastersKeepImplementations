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
    umamusume_pretty_derby_include_g1: UmamusumePrettyDerbyIncludeG1
    umamusume_pretty_derby_include_g2: UmamusumePrettyDerbyIncludeG2
    umamusume_pretty_derby_include_g3: UmamusumePrettyDerbyIncludeG3
    umamusume_pretty_derby_include_ex: UmamusumePrettyDerbyIncludeEX

class UmamusumePrettyDerbyGame(Game):
    name = "Umamusume: Pretty Derby"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
    ]

    is_adult_only_or_unrated = False

    options_cls = UmamusumePrettyDerbyArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Use TRAINEE to complete these goals, if that is possible",
                data={
                    "TRAINEE": (self.trainees, 1),
                },
            ),
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

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
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
            "Hansin Juvenile Fillies",
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
            "Nakayama Kimapi",
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
    def include_ex(self) -> bool:
        return bool(self.archipelago_options.umamusume_pretty_derby_include_ex.value)

    @functools.cached_property
    def races_ex(self) -> List[str]:
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

        # Check if EX races are included, and include them if so
        if self.include_ex:
            races.extend(self.races_ex[:])

        return races

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

# Archipelago Options
class UmamusumePrettyDerbyTraineesOwned(OptionList):
    """
    Indicates which trainees the player owns in Umamusume: Pretty Derby.
    
    Note: Currently this is only used for generating optional restrictions, and not for any specific main objectives.
    """

    display_name = "Umamusume: Pretty Derby Trainees Owned"
    default  = [
        "Agnes Tachyon",
        "Air Groove (Normal)",
        "Air Groove (Wedding)",
        "Biwa Hayahide",
        "Curren Chan",
        "Daiwa Scarlet",
        "El Condor Pasa (Normal)",
        "El Condor Pasa (Fantasy)",
        "Fuji Kiseki",
        "Gold Ship",
        "Grass Wonder (Normal)",
        "Grass Wonder (Fantasy)",
        "Haru Urara",
        "Hishi Amazon",
        "King Halo",
        "Maruzensky",
        "Matikanefukukitaru",
        "Mayano Top Gun (Normal)",
        "Mayano Top Gun (Wedding)",
        "Mejiro McQueen (Normal)",
        "Mejiro McQueen (Anime Collab)",
        "Mejiro Ryan",
        "Mihono Bourbon",
        "Narita Brian",
        "Narita Taishin",
        "Nice Nature",
        "Oguri Cap",
        "Rice Shower",
        "Sakura Bakushin O",
        "Seiun Sky",
        "Silence Suzuka",
        "Smart Falcon",
        "Special Week",
        "Super Creek",
        "Symboli Rudolf",
        "Taiki Shuttle",
        "TM Opera O",
        "Tokai Teio (Normal)",
        "Tokai Teio (Anime Collab)",
        "Vodka",
        "Winning Ticket",
    ]

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

class UmamusumePrettyDerbyIncludeEX(Toggle):
    """
    Indicates whether to include EX Races when generating Umamusume: Pretty Derby objectives.
    
    Note: Currently, this means the five variations of the URA Finale Final.
    
    Since which variation you get is determined by what race type you raced the most in a run,
    with ties going to the shorter distance - please only include if you're willing to plan to
    both run and potentially have to win URA Finale (Long), since that one strictly requires planning.
    """

    display_name = "Umamusume: Pretty Derby Include EX Races"


