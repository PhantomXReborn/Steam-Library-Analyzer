from steam_api import get_owned_games

data = get_owned_games()

games = data.get("response", {}).get("games", [])

print(f"Games found: {len(games)}")

for game in games[:10]:
    name = game.get("name", "Unknown")
    playtime = game.get("playtime_forever", 0)

    hours = playtime / 60

    print(f"{name} - {hours:.1f} hours")