s=input()
world=s[0]
stage=s[2]
stage=int(stage)
if stage==8:
    world=int(world)+1
    stage=1
else:
    stage+=1
print(str(world)+"-"+str(stage))