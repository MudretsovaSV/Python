dog_cal=140
bun_cal=120
ketchup_cal=80
mustard_cal=20
onion_cal=40

print "\t�������\t�������\t������\t�������\t���"
count=1
for dog in [0,1]:
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onion in [0,1]:
                    total_cal=bun*bun_cal+dog*dog_cal+\
                            ketchup*ketchup_cal+mustard*mustard_cal+\
                            onion*onion_cal                    
                    print "#", count, "\t",
                    print dog, "\t", bun, "\t", ketchup, "\t",
                    print mustard, "\t", onion,
                    print "\t", total_cal
                    count=count+1
