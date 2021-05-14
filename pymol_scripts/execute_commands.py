
with open("pymol_commands.txt","r") as fi: 
	fi2 = fi.readlines()
for l in fi2:
	cmd.do(l)
