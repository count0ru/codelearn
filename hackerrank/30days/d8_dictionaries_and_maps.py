
phonedb = {}
queries = int(input().strip())

for record in range(queries):
	name, phone	= input().split(" ")
	phonedb[name] = phone

for record in range(queries):
	sname = input().strip()
	if sname in phonedb:
		print("{}={}".format(sname,phonedb.get(sname)))
	else:
		print("Not found")

