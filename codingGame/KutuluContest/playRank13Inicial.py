import sys
import math
import random

# Survive the wrath of Kutulu
# Coded fearlessly by JohnnyYuge & nmahoude (ok we might have been a bit scared by the old god...but don't say anything)

width = int(input())
height = int(input())
for i in range(height):
    line = input()
    print(line, file=sys.stderr)

# sanity_loss_lonely: how much sanity you lose every turn when alone, always 3 until wood 1
# sanity_loss_group: how much sanity you lose every turn when near another player, always 1 until wood 1
# wanderer_spawn_time: how many turns the wanderer take to spawn, always 3 until wood 1
# wanderer_life_time: how many turns the wanderer is on map after spawning, always 40 until wood 1
sanity_loss_lonely, sanity_loss_group, wanderer_spawn_time, wanderer_life_time = [int(i) for i in input().split()]

# game loop
count=0
explorers={}
while True:
    
    entity_count = int(input())  # the first given entity corresponds to your explorer
    for i in range(entity_count):
        entity_type, id, x, y, param_0, param_1, param_2 = input().split()
        id = int(id)
        
        x = int(x)
        y = int(y)
        if i != 0 and entity_type == "EXPLORER":
            exporerPX= x
            exporerPY = y 
        param_0 = int(param_0)
        param_1 = int(param_1)
        param_2 = int(param_2)
    #if i==0:
    #print("MOVE " + str(exporerPX)+ " " + str(exporerPY)) ranking13
    print("MOVE 7 1")

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # MOVE <x> <y> | WAIT
