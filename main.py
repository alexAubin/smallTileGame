
from src import game, tileset, map, character     


def main() :


    g = game.Game("test", 32);

    t = tileset.Tileset(32, "assets/tileset.png", "assets/tileset_mask.csv")
    
    g.setMap(map.Map(t, "map/map_bot.csv", "map/map_top.csv"))
    g.setHero(character.Character("assets/sprites_trainers.png", 4, 32, 48, (10,15)))

    while True :
        g.mainLoop()

main()