variables = {16 : ""}
# Function to allocate variables and modify them (starting address RAM[16])
def variable(name):
	for key, val in variables.items():
	    if val == name:
	        return key

	key = max(variables, key=int)

	if variables[key] == "":
		variables[key] = name
		return key
	else:
		variables[key+1] = name
		return key+1
