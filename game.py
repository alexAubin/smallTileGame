
from src import game, mapLayer, character


def main() :


    g = game.Game("test", 32);

    tileset = [ "assets/tileset.png", "assets/tileset_mask.csv" ]

    g.addMapLayer(mapLayer.MapLayer(tileset, 32, "map/map_bot.csv"))
    g.addMapLayer(mapLayer.MapLayer(tileset, 32, "map/map_top.csv"))

    g.setHero(character.Character("assets/sprites_trainers.png", 4, 32, 48, (10,15)))

    while True :
        g.mainLoop()

main()
