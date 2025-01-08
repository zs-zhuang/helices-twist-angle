#! /usr/bin/python

import os, sys, math, string

# write out twist angles
out_file = open("twist", 'w')

# get list of pdb file
in_list = open("mini_table", 'r')
list = in_list.readlines()

for x in range(0, len(list)):
#for x in range(0, 1):
	row = list[x].rstrip()
	pdb_id = row[0:4]
	#print pdb_id

	# get pdb file

	file_name = str(pdb_id) + ".pdb"
	#print file_name
	in_file = open(file_name, 'r')
	content = in_file.readlines()

	# get residues (res1 pairs with res2, res3 pairs with res4)
	res1 = row.split()[1] 
	res2 = row.split()[2]
	res3 = row.split()[3]
	res4 = row.split()[4]
	
	#print res1, res2, res3, res4

	# get the coordinates of C1* atom for each residue

	for i in range (0, len(content)):
		row = content[i].rstrip()
		if row != '':

			header = row[0:4]
			if header == "ATOM":
				current_res = str(row[22:26].strip())
                        	current_ATOM = str(row[12:16].strip())
				#print current_res 
				#print current_ATOM	
		        	if current_res == res1 and (current_ATOM == "C1\'" or current_ATOM == "C1*"):
                                	x1 = float(row[30:38].strip())
                                	y1 = float(row[38:46].strip())
                                	z1 = float(row[46:54].strip())
					#print "res1"
                                	#print current_res, current_ATOM, x1, y1, z1

				elif current_res == res2 and (current_ATOM == "C1\'" or current_ATOM == "C1*"):
                                	x2 = float(row[30:38].strip())
                                	y2 = float(row[38:46].strip())
                                	z2 = float(row[46:54].strip())
					#print "res2"
                                	#print current_res, current_ATOM, x2, y2, z2

				elif current_res == res3 and (current_ATOM == "C1\'" or current_ATOM == "C1*"):
                                	x3 = float(row[30:38].strip())
                                	y3 = float(row[38:46].strip())
                                	z3 = float(row[46:54].strip())
					#print "res3"
                                	#print current_res, current_ATOM, x3, y3, z3
			
				elif current_res == res4 and (current_ATOM == "C1\'" or current_ATOM == "C1*"):
                                	x4 = float(row[30:38].strip())
                                	y4 = float(row[38:46].strip())
                                	z4 = float(row[46:54].strip())
					#print "res4"
                                	#print current_res, current_ATOM, x4, y4, z4

	# Measure the twist angle using cosine rule
	a = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
	b = math.sqrt((x4-x3)**2+(y4-y3)**2+(z4-z3)**2)

	dx = x3 - x1 
	dy = y3 - y1
	dz = z3 - z1

	x3_t = x3 - dx  
	y3_t = y3 - dy
	z3_t = z3 - dz

	x4_t = x4 - dx
	y4_t = y4 - dy
	z4_t = z4 - dz

	c = math.sqrt((x2-x4_t)**2+(y2-y4_t)**2+(z2-z4_t)**2)

	#print a, b, c
	cos_twist = ( (a**2) + (b**2) - (c**2) ) / (2*a*b)
	#print cos_twist

	twist = math.degrees(math.acos(cos_twist))
	out_file.write(str(twist)+'\n')
