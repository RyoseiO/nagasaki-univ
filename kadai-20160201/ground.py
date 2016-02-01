import mcpi.minecraft as minecraft
import mcpi.block as block
import math

mc = minecraft.Minecraft.create("cvcis01.progrape.jp")
#mc = minecraft.Minecraft.create("133.45.131.37")

pos = mc.player.getPos()

pos.x = 0
pos.y = 0
pos.z = 0

a = 55

for i in range(0, 253):
    for j in range(0, 95):
        if i<135:
            mc.setBlock(pos.x+i, pos.y-1, pos.z+j, block.SAND)
            #mc.setBlock(pos.x+i, pos.y, pos.z+j, block.AIR)
        else:
            mc.setBlock(pos.x+i, pos.y-1, pos.z+j, block.GRASS)
            #mc.setBlock(pos.x+i, pos.y, pos.z+j, block.AIR)

        if i==252:
            if j==94:
                for i in range(0, 90):
                    rad = i * math.pi /180
                    sin = a * math.sin(rad)
                    cos = a * math.cos(rad)

                    mc.setBlock(pos.x+cos, pos.y-1, pos.z+sin, block.STONE)


mc.postToChat("Run Python")

