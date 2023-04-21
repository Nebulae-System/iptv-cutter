from m3u_parser import M3uParser
pluto_us_url = "https://i.mjh.nz/PlutoTV/us.m3u8"
pluto_uk_url = "https://i.mjh.nz/PlutoTV/gb.m3u8"
stv_uk_url = "https://i.mjh.nz/SamsungTVPlus/gb.m3u8"
stv_us_url = "https://i.mjh.nz/SamsungTVPlus/us.m3u8"
stirr_url = "https://i.mjh.nz/Stirr/all.m3u8"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
pluto_us = M3uParser(timeout=5, useragent=user_agent)
pluto_us.parse_m3u(pluto_us_url)
pluto_removals = [
    "Degrassi", "America's Voice News", "CBS News Chicago", "OAN Plus", "WeatherNation Los Angeles",
    'Faith TV', 'TBN', 'GLORY Kickboxing', 'World Poker Tour', 'PokerGo', 'Golazo Network', 'Logo Pluto TV',
    'Baywatch', 'Star Trek', 'theGrio', '90210', "Bounce XL", 'Shades of Black', 'Heartland', 'Stargate',
    'More Star Trek', 'AspireTV Life', 'Johnny Carson TV', 'The Rifleman', 'Dark Shadows', 'The Carol Burnett Show',
    "Three's Company", 'Family Ties', 'Happy Days', 'The Love Boat', 'Beverly Hillbillies', 'Mission Impossible',
    'Wanted: Dead or Alive', 'The Andy Griffith Show', 'Matlock', 'Gunsmoke', 'Black Classics', 'Perry Mason',
    'The Ed Sullivan Show', 'I Love Lucy', 'Rawhide', 'The Dick Van Dyke Show', 'Gameplay: Roblox',
    'Gameplay: Call of Duty', 'Gameplay: Fortnite', 'Gameplay: Sports', 'Dallas Cowboys Cheerleaders', 'The Challenge',
    'Black Ink Crew', 'Survivor', 'Rescue 911', 'Jersey Shore', 'Bar Rescue', 'Teen Mom', 'Cheaters',
    'Best of Dr. Phil', 'This Old House', 'MinecrafTV', 'BET Pluto TV', 'BET Her', 'Ink Master', 'Black Throwbacks',
    'Julia Child', 'Best of The Drew Barrymore Show', 'MAVTV Select', 'CBS News Los Angeles', 'The Rachael Ray Show',
    'CBS News New York', 'PFL MMA', 'XITE Gospel', 'The First', 'Midsomer Murders', 'Inspector Gadget',
    'Sabrina Teenage Witch', 'Little Baby Bum', 'Morphle', 'Moonbug Kids', 'Arthur', 'Barney & Friends', 'Duck Dynasty',
    'Wicked Tuna', '16 & Pregnant', 'My Strange Addiction', 'Bridezillas', 'Hunter', 'Highway to Heaven',
    'Wild at Heart', 'CSI: New York', 'CSI: Miami', 'Hart to Hart', 'When Calls the Heart', 'Party of Five',
    'Rookie Blue'
]
samsung_removals = [
    'Project Runway', 'FailArmy', 'Catfish', 'TalkTV', 'GB News', 'Pluto TV Action', 'Pluto TV Romance',
    'Pluto TV Movies', 'Survivor', 'Are We There Yet?', 'Real Life', 'Bondi Vet', 'The Pet Collective',
    'Pluto TV Classic TV', 'LOL! Network', 'Bridezillas', 'Shades of Black', 'People Are Awesome', 'Baywatch',
    "McLeod's Daughters", 'The Wicked Tuna Channel', 'PBS America', 'Homicide Hunter', 'Pluto TV Crime',
    'Pluto TV Inside', 'Pluto TV Paranormal', 'Pluto TV Conspiracy', 'WaterBear', 'Pluto TV Animals', 'Fashion TV',
    'Pluto TV Food', 'World Poker Tour', 'Horse & Country', 'Strongman Champions League', 'MMA TV', 'CBS News',
    "Real America's Voice", 'TYT Network', 'NBC Bay Area News', 'ABC7 Bay Area', 'WN San Francisco', 'Stories by AMC',
    'TV Land Drama', 'BET Pluto TV', 'Bounce XL', 'Baywatch', 'The Walking Dead Universe', '21 Jump Street', 'Degrassi',
    'Lucky Dog', 'The Bob Ross Channel', 'Nosey', 'Divorce Court', 'Shades of Black', 'Dove Channel', 'Cowboy Way',
    'Fireplace 4K', 'Dr. G: Medical Examiner', 'Dateline 24/7', 'Midsomer Murders', 'CBS Sports HQ', 'beIN SPORTS XTRA',
    'Stadium', 'Origin Sports', 'IMPACT Wrestling', 'SURF NOW TV', 'People Are Awesome', 'Waypoint TV',
    'World Poker Tour', 'Top Gear', 'MAVTV Select', 'PowerNation', 'MotorTrend FAST TV', 'NHRA TV', 'MOTORVISION.TV',
    'Cars', 'Torque', 'Antiques Roadshow', 'This Old House', 'This Old House Makers', 'Home.Made.Nation', 'That Girl',
    'Family Ties', 'Portlandia', 'The Jack Hanna Channel'
]
stirr_removals = [
    'Buzzr', 'Nosey', 'Johnny Carson TV', 'The Carol Burnett Show', 'Shout Factory', 'The Tim Conway Show',
    'Dick Cavett', 'The Bob Ross Channel', 'Comedy Dynamics', 'Bloomberg TV', 'Filmrise Free Movies',
    'News 12 New York', 'The First', 'Cheddar', 'AFV', 'The Pet Collective', 'FailArmy', 'Horse Shopping Channel',
    'So...Real', 'People Are Awesome', 'Dove', 'HSN', 'The Country Network', 'ONTV4U', 'Shop LC', 'beIN Sports Xtra',
    'SportsGrid', 'Racing America', 'MavTv', 'QVC', 'Outdoor America', 'Stingray', 'World Poker Tour', 'Electric Now',

]
print(f"Pluto US: Loaded {len(pluto_us.get_list())} channels")
pluto_us.remove_by_category("En Español")
pluto_us.remove_by_category("Local News")
pluto_us.remove_by_category("Kids")
pluto_us.filter_by("name", pluto_removals, retrieve=False)
pluto_us.sort_by("category")
print(f"{len(pluto_us.get_list())} channels remaining")
print("")
pluto_us.to_file("pluto_us", "m3u")

pluto_uk = M3uParser(timeout=5, useragent=user_agent)
pluto_uk.parse_m3u(pluto_uk_url)
print(f"Pluto UK: Loaded {len(pluto_uk.get_list())} channels")
pluto_uk.filter_by("name", pluto_removals, retrieve=False)
pluto_uk.sort_by("category")
print(f"{len(pluto_uk.get_list())} channels remaining")
pluto_uk.to_file("pluto_uk", "m3u")

samsung_uk = M3uParser(timeout=5, useragent=user_agent)
samsung_uk.parse_m3u(stv_uk_url)
print(f"Samsung UK: Loaded {len(samsung_uk.get_list())} channels")
samsung_uk.filter_by("name", samsung_removals, retrieve=False)
samsung_uk.remove_by_category("Kids")
samsung_uk.remove_by_category("Motoring")
samsung_uk.sort_by("category")
print(f"{len(samsung_uk.get_list())} channels remaining")
samsung_uk.to_file("samsung_uk", "m3u")

samsung_us = M3uParser(timeout=5, useragent=user_agent)
samsung_us.parse_m3u(stv_us_url)
print(f"Samsung US: Loaded {len(samsung_us.get_list())} channels")
samsung_us.filter_by("name", samsung_removals, retrieve=False)
samsung_us.remove_by_category("Game Shows")
samsung_us.remove_by_category("Reality")
samsung_us.remove_by_category("Latino")
samsung_us.sort_by("category")
print(f"{len(samsung_us.get_list())} channels remaining")
samsung_us.to_file("samsung_us", "m3u")

stirr = M3uParser(timeout=5, useragent=user_agent)
stirr.parse_m3u(stirr_url)
print(f"Stirr: Loaded {len(stirr.get_list())} channels")
stirr.filter_by("name", stirr_removals, retrieve=False)
stirr.sort_by("category")
print(f"{len(stirr.get_list())} channels remaining")
stirr.to_file("stirr", "m3u")

