import csv
import sys
import re
import requests
from collections import Counter
import compago
app = compago.Application()
globvar = 0
globar = 1
filename = ''
else_count = 0
func_count = 0
local_count = 0
arr=[]
zipcode_array =[]

class HeaderPrint(object):
	def funky(self,header):
		# print "Header is",header
		r = csv.reader(open(header, "rU"), dialect=csv.excel_tab)
		line1=r.next()
		global filename
		filename = header			
		for element in line1:
			mylist = element.split(',')	
		print mylist		

class ColumnPrint(object):	
	def print_columns(self,filesname,alpha,beta):
		global globvar
		global globar
		global filename
		globvar = alpha
		globar = beta
		filename = filesname			
		with open(filesname,'rU') as data :			
			r = csv.reader(open(filesname, "rU"), dialect=csv.excel_tab)
			line1=r.next()	
			arrt = []
			for element in line1:
				mylist = element.split(',')				
			real_data = csv.DictReader(data)			
			for row in real_data :
				for i in range(int(alpha),int(beta)):					
					arrt.append(row[mylist[i]])								
			print arrt		

@app.command
def columns(filename="something"):
	x = HeaderPrint()
	x.funky(filename)

# @app.command
# def Column(filename = "fileName", begin="something",to="small"):
# 	y = ColumnPrint()
# 	y.print_columns(filename,begin,to)	

class ExecuteProgram(object):
	def fix_file(self,filesname,alpha,beta):
		global globvar
		global globar
		global filename
		globvar = alpha
		globar = beta
		filename = filesname
		count = 0
		counter = 0
		lower_states = []
		upper_states = []

		two_letter_lowercase_string_not_state_code = string_with_integer_spaces = email = website = string_with_space_no_integer = phone_no_with_alphabets = website_without_www = state_code = pure_uppercase_string = phone_no_two_hyphens = phone_no_with_parantheses = phone_no_without_hyphen_or_alphabets = valid_verified_zipcode_without_hyphen = empty = valid_verified_zipcode_with_two_hyphen = string_with_integer_without_spaces = pure_integer =  valid_verified_zipcode_with_one_hyphen = two_letter_uppercase_string_not_state_code = zipcode_with_two_not_successive_hyphens = string_without_integer_without_spaces = string_with_symbol_instead_of_at = string_first_line_address = integer_seperated_by_hyphen_not_zip_or_phone =  phone_no_one_hyphen = phone_no_with_only_open_parantheses = phone_no_with_only_close_parantheses = uncertain_entries = string_with_dots_not_email = mostly_zipcode_with_one_hyphen = mostly_zipcode_without_hyphen = mostly_zipcode_with_two_hyphen = mostly_zipcode_four_digits = requests_made = decimal_integer = string_with_integer_hyphen = 0
		states = [ "AK","Alaska","AL","Alabama","AR","Arkansas","AS","American Samoa","AZ","Arizona","CA","California","CO","Colorado","CT","Connecticut","DC","District of Columbia","DE","Delaware","FL","Florida","GA","Georgia","GU","Guam","HI","Hawaii","IA","Iowa","ID","Idaho","IL","Illinois","IN","Indiana","KS","Kansas","KY","Kentucky","LA","Louisiana","MA","Massachusetts","MD","Maryland","ME","Maine","MI","Michigan","MN","Minnesota","MO","Missouri","MS","Mississippi","MT","Montana","NC","North Carolina","ND","North Dakota","NE","Nebraska","NH","New Hampshire","NJ","New Jersey","NM","New Mexico","NV","Nevada","NY","New York","OH","Ohio","OK","Oklahoma","OR","Oregon","PA","Pennsylvania","PR","Puerto Rico","RI","Rhode Island","SC","South Carolina","SD","South Dakota","TN","Tennessee","TX","Texas","UT","Utah","VA","Virginia","VI","Virgin Islands","VT","Vermont","WA","Washington","WI","Wisconsin","WV","West Virginia","WY","Wyoming" ]
		state_code_array = ["AK","AL","AR","AS","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"]
		states_and_cities = ["Wyoming","Minnesota","California","Georgia","Kansas","Vermont","Indiana","Pennsylvania","Alabama","New York","Florida","Ohio","Texas","Maryland","Louisiana","Missouri","WY","MN","CA","GA","KS","VT","IN","PA","AL","NY","FL","OH","TX","MD","LA"]

		for t in range(0,len(states)-1):
			lower_states.append(states[t].lower())
		for t in range(0,len(states)-1):
			upper_states.append(states[t].upper())

		pattern_string = re.compile("[a-zA-Z]")
		pattern_caps = re.compile("[A-Z]")
		pattern_small = re.compile("[a-z]")
		pattern_integer = re.compile("[0-9]")
		pattern_email = re.compile("[\w+|\W+]@[\w+|\W+]")
		pattern_phone = re.compile("-")
		pattern_empty = re.compile("^(?![\s\S])")
		pattern_website = re.compile("www+|WWW+")
		pattern_dot = re.compile("[.]")
		pattern_word_after_dot = re.compile("[.][a-zA-Z]")
		pattern_http = re.compile("http")
		pattern_space = re.compile("[\w+|\W+]\s[\w+|\W+]")
		pattern_hashtag = re.compile("#")
		pattern_comma = re.compile(",")
		pattern_successive_hyphens = re.compile("--")
		patten_phone_parantheses = re.compile("\(\d+\)|\(\d+|\d+\)|\d+\(\d+\)")
		pattern_slash = re.compile("[\w+|\W+]/[\w+|\W+]")
		pattern_zipcode_one_hyphen = re.compile('^\d{5}-\d{4}$')
		pattern_zipcode_without_hyphen = re.compile('^\d{5}$')
		patter_zipcode_four_digits = re.compile('^\d{4}$')
		pattern_zipcode_two_hyphen = re.compile('^\d{5}--\d{4}$')

		def print_empty_entries():			
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :
					for i in range(int(globvar),int(globar)):
						find_empty = re.findall(pattern_empty,row[mylist[i]])
						row_no_in_original_file += 1							
						if find_empty :					
							with open('improperData.txt','a') as fp :
								defective_rows+=1
								if defective_rows == 1 : 
									global func_count
									func_count += 1							
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE THERE IS NO ENTRY IN COLUMN ") 
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		
		def print_string_entries():
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :
					for i in range(int(globvar),int(globar)):
						find_string = re.findall(pattern_string,row[mylist[i]])
						row_no_in_original_file += 1				
						if find_string :
							with open('improperData.txt','a') as fp :
								defective_rows+=1
								if defective_rows == 1 :
									global func_count
									func_count += 1	 							
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE A STRING IS PRESENT IN PLACE OF INTEGER IN COLUMN ") 
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")	

		def print_string_without_hyphen_entries():
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :
					for i in range(int(globvar),int(globar)):
						find_string = re.findall(pattern_string,row[mylist[i]])
						find_phone = re.findall(pattern_phone,row[mylist[i]])
						row_no_in_original_file += 1				
						if find_string and not find_phone :
							with open('improperData.txt','a') as fp :
								defective_rows+=1
								if defective_rows == 1 :
									global func_count
									func_count += 1	 							
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE A STRING (WITHOUT HYPHEN) IS PRESENT IN PLACE OF INTEGER IN COLUMN ") 
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")	

		def print_string_only_entries():
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :
					for i in range(int(globvar),int(globar)):
						find_string = re.findall(pattern_string,row[mylist[i]])
						row_no_in_original_file += 1				
						if find_string and len(find_string) == len(row[mylist[i]]) :
							with open('improperData.txt','a') as fp :
								defective_rows+=1
								if defective_rows == 1 : 
									global func_count
									func_count += 1								
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE A STRING (only string) IS PRESENT IN PLACE OF INTEGER IN COLUMN ") 
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_integer_entries():
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):				
						find_integer = re.findall(pattern_integer,row[mylist[i]])
						row_no_in_original_file += 1								
						if find_integer and len(find_integer)!=len(row[mylist[i]]):
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									global func_count
									func_count += 1										
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE AN INTEGER(BUT NOT ONLY INTEGER) IS PRESENT IN PLACE OF STRING IN COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_integer_only_entries():
			with open(filename,'rU') as data :		
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):				
						find_integer = re.findall(pattern_integer,row[mylist[i]])
						find_string = re.findall(pattern_string,row[mylist[i]])
						row_no_in_original_file += 1								
						if find_integer and not find_string and len(find_integer)==len(row[mylist[i]]) :
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									global func_count
									func_count += 1								
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE A PURE INTEGER IS PRESENT IN PLACE OF STRING IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")				

		def improper_integer_entries():
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):
						find_space = re.findall(pattern_space,row[mylist[i]])
						find_empty = re.findall(pattern_empty,row[mylist[i]])
						find_phone = re.findall(pattern_phone,row[mylist[i]])
						find_integer = re.findall(pattern_integer,row[mylist[i]])
						find_string = re.findall(pattern_string,row[mylist[i]])
						find_hashtag = re.findall(pattern_hashtag,row[mylist[i]])
						find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,row[mylist[i]])	
						find_slash = re.findall(pattern_slash,row[mylist[i]])	
						row_no_in_original_file += 1													
						if len(find_phone) == 1 and len(find_integer) != 10 and not find_string and not find_hashtag and not find_pattern_phone_parantheses and not find_slash :
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 :
									global func_count
									func_count += 1								
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE AN UNCERTAIN INTEGER ENTRY IS PRESENT  IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_email_entries():
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):				
						find_email = re.findall(pattern_email,row[mylist[i]])
						find_dot = re.findall(pattern_dot,row[mylist[i]])
						row_no_in_original_file += 1								
						if find_email and find_dot:
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									global func_count
									func_count += 1	
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE AN EMAIL IS PRESENT IN PLACE OF STRING IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_website_entries():
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):				
						find_website = re.findall(pattern_website,row[mylist[i]])
						find_dot = re.findall(pattern_dot,row[mylist[i]])
						row_no_in_original_file += 1								
						if find_website and find_dot:
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									global func_count
									func_count += 1	
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE A WEBSITE IS PRESENT IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_space_entries() :
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):				
						find_space = re.findall(pattern_space,row[mylist[i]])
						find_string = re.findall(pattern_string,row[mylist[i]])
						find_integer = re.findall(pattern_integer,row[mylist[i]])
						row_no_in_original_file += 1								
						if (find_string and find_space) or (find_integer and find_space):
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									global func_count
									func_count += 1	
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE SPACE IS PRESENT IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_no_dots() :
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):				
						find_string = re.findall(pattern_string,row[mylist[i]])
						find_dot = re.findall(pattern_dot,row[mylist[i]])
						row_no_in_original_file += 1								
						if (find_string and not find_dot) :
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									global func_count
									func_count += 1	
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE NO DOTS WERE PRESENT IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_integer_more_than_string() :
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):				
						find_integer = re.findall(pattern_integer,row[mylist[i]])
						find_string = re.findall(pattern_string,row[mylist[i]])					
						row_no_in_original_file += 1								
						if (len(find_integer) > len(find_string) and not find_website) :
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									global func_count
									func_count += 1	
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE INTEGERS DOMINATE STRING IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_string_more_than_integer() :
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):				
						find_integer = re.findall(pattern_integer,row[mylist[i]])
						find_string = re.findall(pattern_string,row[mylist[i]])					
						row_no_in_original_file += 1								
						if (len(find_string) > len(find_integer)) :
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									global func_count
									func_count += 1	
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE STRING DOMINATE INTEGER IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_not_state_code() :
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :
					for i in range(int(globvar),int(globar)):				
						row_no_in_original_file += 1										
						if (row[mylist[i]] in states) or (row[mylist[i]] in lower_states) or (row[mylist[i]] in upper_states)or (row[mylist[i]] == " ") :					
							pass					
						else :
							with open('improperData.txt','a') as fp :
								defective_rows+=1
								if defective_rows == 1 :
									# print "Defective",row[mylist[i]] 
									global func_count
									func_count += 1	
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE IS NOT A US STATE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

		def print_state_code() :
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :
					for i in range(int(globvar),int(globar)):				
						row_no_in_original_file += 1										
						if (row[mylist[i]] in state_code_array) and (row[mylist[i]] not in states_and_cities) :		
							with open('improperData.txt','a') as fp :
								defective_rows+=1
								if defective_rows == 1 : 
									global func_count
									func_count += 1	
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE IS A US STATE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
						else : 
							pass
			
		def print_zip_code() :
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :
					for i in range(int(globvar),int(globar)):				
						row_no_in_original_file += 1
						find_phone = re.findall(pattern_phone,row[mylist[i]])
						find_string = re.findall(pattern_string,row[mylist[i]])
						find_integer = re.findall(pattern_integer,row[mylist[i]])
						find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,row[mylist[i]])
						find_successive_hyphens =re.findall(pattern_successive_hyphens,row[mylist[i]])
						find_hashtag = re.findall(pattern_hashtag,row[mylist[i]])
						find_slash = re.findall(pattern_slash,row[mylist[i]])
						find_space = re.findall(pattern_space,row[mylist[i]])
						find_dot = re.findall(pattern_dot,row[mylist[i]])				

						if len(find_phone) == 1 and len(find_integer) < 10 and not find_string and not find_hashtag and not find_pattern_phone_parantheses and not find_slash and not find_space  :
							
							y = row[mylist[i]].split("-")[0]
							
							for j in range(0,len(zipcodes)-1):						
								if y == zipcodes[j] :
									if(len(y)>3):
										for k in range(0,len(mylist)-1):
											if zipcodes[j+3] == row[mylist[k]]:
												with open('improperData.txt','a') as fp :
													defective_rows+=1
													if defective_rows == 1 :
														global func_count
														func_count += 1	 								
														fp.write("***************************************************************************************\n")
														fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
														fp.write(mylist[a])
														fp.write(" OF THE CSV FILE IS POSSIBLY A ZIP CODE WITH A HYPHEN\n")
														fp.write("***************************************************************************************\n")
													fp.write(str(row)+ "\n" + "\n")
													fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
													fp.write("Zipcode ")
													fp.write(str(row[mylist[i]]) + " ")
													fp.write("belongs to ")
													fp.write(zipcodes[j+1])
													fp.write(" in the state of ")
													fp.write(zipcodes[j+2] + "\n")
													fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
													fp.write("Defective row No:")
													fp.write(str(defective_rows) + "\n")
													new_row_no_in_original_file=row_no_in_original_file + 1
													fp.write("Row no in original file is ")
													fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
								else :
									pass

						elif len(find_integer) == 5 and not find_phone and not find_hashtag and not find_dot and not find_string and not find_space :
							for j in range(0,len(zipcodes)-1):
								if row[mylist[i]] == zipcodes[j] :
									for k in range(0,len(mylist)-1):
										if zipcodes[j+3] == row[mylist[k]]:							
											defective_rows+=1
											with open('improperData.txt','a') as fp :
												if defective_rows == 1 :											
													func_count += 1										
													fp.write("***************************************************************************************\n")			
													fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
													fp.write(mylist[a])
													fp.write(" OF THE CSV FILE IS POSSIBLY A ZIP CODE \n")
													fp.write("***************************************************************************************\n")			
												fp.write(str(row)+ "\n" + "\n")
												fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
												fp.write("Zipcode ")
												fp.write(str(row[mylist[i]]) + " ")
												fp.write("belongs to ")
												fp.write(zipcodes[j+1])
												fp.write(" in the state of ")
												fp.write(zipcodes[j+2] + "\n")
												fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
												fp.write("Defective row No:")
												fp.write(str(defective_rows) + "\n")
												new_row_no_in_original_file = row_no_in_original_file + 1
												fp.write("Row no in original file is ")
												fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
								else :
									pass
						elif len(find_integer) == 4 and not find_phone and not find_hashtag and not find_dot and not find_string and not find_space :
							c = "0" + row[mylist[i]]
							for j in range(0,len(zipcodes)-1):
								if c == zipcodes[j] :
									for k in range(0,len(mylist)-1):
										if zipcodes[j+3] == row[mylist[k]]:											
											defective_rows+=1
											with open('improperData.txt','a') as fp :
												if defective_rows == 1 :											
													func_count += 1										
													fp.write("***************************************************************************************\n")			
													fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
													fp.write(mylist[a])
													fp.write(" OF THE CSV FILE IS POSSIBLY A ZIP CODE \n")
													fp.write("***************************************************************************************\n")			
												fp.write(str(row)+ "\n" + "\n")
												fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
												fp.write("Zipcode ")
												fp.write(str(row[mylist[i]]) + " ")
												fp.write("belongs to ")
												fp.write(zipcodes[j+1])
												fp.write(" in the state of ")
												fp.write(zipcodes[j+2] + "\n")
												fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
												fp.write("Defective row No:")
												fp.write(str(defective_rows) + "\n")
												new_row_no_in_original_file = row_no_in_original_file + 1
												fp.write("Row no in original file is ")
												fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
								else: 
									pass

						else : 
							pass										

		def print_improper_email_entries():
			with open(filename,'rU') as data :
				real_data = csv.DictReader(data)	
				defective_rows = 0
				row_no_in_original_file = 0	
				for row in real_data :			
					for i in range(int(globvar),int(globar)):	
						find_string = re.findall(pattern_string,row[mylist[i]])			
						find_space = re.findall(pattern_space,row[mylist[i]])
						find_dot = re.findall(pattern_dot,row[mylist[i]])
						find_email = re.findall(pattern_email,row[mylist[i]])
						row_no_in_original_file += 1								
						if find_string and find_space :
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 :
									global func_count
									func_count += 1								
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE AN EMPTY SPACE IS PRESENT IN PLACE OF EMAIL IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
							

						elif find_string and not find_dot :
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 : 
									
									func_count += 1								
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE DOT IS NOT PRESENT IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
							

						elif find_string and not find_email :
							with open('improperData.txt','a') as fp :
								defective_rows += 1
								if defective_rows == 1 :
									
									func_count += 1	 							
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE @ IS NOT PRESENT IN THE COLUMN ")
									fp.write(mylist[a])
									fp.write(" OF THE CSV FILE\n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")									

		#this loop checks for any extra commas which might cause an error prone data
		with open(filename,'rU') as data :
			r = csv.reader(open(filesname, "rU"), dialect=csv.excel_tab)
			line1=r.next()	
			arrt = []
			for element in line1:
				mylist = element.split(',')	
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0					
			for row in real_data :	
				row_no_in_original_file += 1	
				if (len(row) != len(mylist)) :
					open('improperData.txt', 'w').close()
					defective_rows += 1
					with open('improperData.txt','a') as fp :
						count+=1
						if count == 1:
							# pass
							fp.write("***************************************************************************************\n")
							fp.write("THESE ROWS ARE PRINTED BECAUSE THEY HAVE IMPERFECT COMMAS\n")
							fp.write("***************************************************************************************\n")
						fp.write(str(row)+ "\n")
						fp.write("Defective row No:")
						fp.write(str(defective_rows) + "\n")
						new_row_no_in_original_file = row_no_in_original_file + 1
						fp.write("Row no in original file is ")
						fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
					
				if (len(row) == len(mylist)) :
					open('improperData.txt', 'w').close()
					counter+=1									
					for i in range(int(globvar),int(globar)):
						a = i
						b = i+1				
						find_string = re.findall(pattern_string,row[mylist[i]])
						find_integer = re.findall(pattern_integer,row[mylist[i]])
						find_email = re.findall(pattern_email,row[mylist[i]])
						find_phone = re.findall(pattern_phone,row[mylist[i]])
						find_empty = re.findall(pattern_empty,row[mylist[i]])
						
						find_website = re.findall(pattern_website,row[mylist[i]])
						find_dot = re.findall(pattern_dot,row[mylist[i]])
						find_http = re.findall(pattern_http,row[mylist[i]])
						find_space = re.findall(pattern_space,row[mylist[i]])
						find_caps = re.findall(pattern_caps,row[mylist[i]])
						find_word_after_dot = re.findall(pattern_word_after_dot,row[mylist[i]])
						find_hashtag = re.findall(pattern_hashtag,row[mylist[i]])
						find_comma = re.findall(pattern_comma,row[mylist[i]])
						find_successive_hyphens =re.findall(pattern_successive_hyphens,row[mylist[i]])
						find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,row[mylist[i]])
						find_slash = re.findall(pattern_slash,row[mylist[i]])
						find_small = re.findall(pattern_small,row[mylist[i]])
						find_zipcode_one_hyphen=re.findall(pattern_zipcode_one_hyphen,row[mylist[i]])
						find_zipcode_without_hyphen= re.findall(pattern_zipcode_without_hyphen,row[mylist[i]])
						find_zipcode_two_hyphen=re.findall(pattern_zipcode_two_hyphen,row[mylist[i]])
						find_zipcode_four_digits=re.findall(patter_zipcode_four_digits,row[mylist[i]])

						if find_string :
							if find_string and find_integer and find_space:						
								#print "string with integer and spaces"
								string_with_integer_spaces+=1
							elif (find_string and find_http and find_slash and find_dot) or (find_string and find_http and find_slash and find_dot and find_integer):
								#print "possible website with http and slash"
								website+=1
							elif find_string and find_dot and find_integer and find_email and not find_empty :
								#print "possible email with integer"
								email+=1
							elif find_string and not find_space and find_integer and not find_email and not find_website and not find_dot and not find_phone:
								#print "string with integer without spaces"
								string_with_integer_without_spaces+=1
							elif find_string and not find_integer and not find_empty and not find_email and not find_http and not find_dot and not find_caps and row[mylist[i]] not in lower_states and row[mylist[i]] not in upper_states :
								#print "string without integer and without spaces"
								string_without_integer_without_spaces+=1
							elif find_string and find_email and find_dot and not find_empty and not find_integer:
								#print "possible email but without integer"
								email+=1
							elif find_string and find_email and not find_dot :
								#print "string with @ instead of at"
								string_with_symbol_instead_of_at+=1
							elif (find_string and find_website and find_dot and find_word_after_dot and not find_space) or (find_string and find_word_after_dot and find_http and find_dot and not find_space) :
								#print "possible website"
								website+=1
							elif find_space and find_string and not find_integer :
								#print "string with spaces but no integer"
								string_with_space_no_integer+=1
							elif find_string and find_phone and find_integer and not find_dot and len(find_integer) >= 6 :						
								#print "possible phone no but with alphabets"
								phone_no_with_alphabets+=1
							elif find_string and find_phone and find_integer and not find_dot and len(find_integer) < 6 :
								#print "Mixture of string integer and hyphen"
								string_with_integer_hyphen += 1

							if find_string and find_dot and not find_website and not find_email and  find_word_after_dot and not find_slash and not find_space and not find_hashtag and not find_comma and (len(find_string) > 5):								
								if len(find_dot) > 1 :
									x = [j for j,val in enumerate(row[mylist[i]]) if val=="."]
									if((x[len(x)-1]-x[0]) >= 3) :								
										#print "possible website but without www (2 dot) and without slashes"
										website_without_www+=1
									else :
										#print "string with more than one dot but not website."
										string_with_dots_not_email+=1

								elif len(find_dot) <= 1 :
									x = [j for j,val in enumerate(row[mylist[i]]) if val=="."]		
									if(len(row[mylist[i]])-x[0] > 4):
										#print "string with one dot but one website"
										string_with_dots_not_email+=1
									else :
										#print "possible website but without www (1 dot)."
										website_without_www+=1

								else :
									#print "possible website but without www (1 dot) and without slashes"
									website_without_www+=1 


							elif find_string and find_slash and find_dot and not find_website and find_word_after_dot and not find_space and not find_hashtag and not find_comma and (len(find_string) > 5):						
								x = [j for j,val in enumerate(row[mylist[i]]) if val=="."]
								if((x[len(x)-1]-x[0]) >= 3) :
									#print "possible website but without www and with slashes"
									website_without_www+=1

							else :						
								if len(find_caps) and len((find_string)) == 2 and not find_integer and not find_empty and not find_dot and not find_slash and not find_small:		
									matching = [s for s in states if row[mylist[i]] == s] 		
									if matching  :		
										#print "possible state code"
										state_code+=1
									else :
										#print "two lettered uppercase string not state code"
										two_letter_uppercase_string_not_state_code += 1


								if len(find_small) and len((find_string)) == 2 and not find_integer and not find_empty and not find_dot and not find_slash:			
									matching_lower = [s for s in lower_states if row[mylist[i]] == s]
									if matching_lower :		
										#print "possible state code in lowercase"
										state_code+=1
									else :
										#print "two lettered lowercase string not state code"
										two_letter_lowercase_string_not_state_code += 1

								if len(find_caps) == len(find_string) and len(find_string) > 2 and not find_integer and not find_empty and not find_dot and not find_slash:			
									matching_upper = [s for s in upper_states if row[mylist[i]] == s]

									if matching_upper :								
										#print "possible state name in capital letters"
										state_code+=1
									else :
										#print "uppercase string"
										two_letter_uppercase_string_not_state_code += 1

								elif (find_string and find_integer and not find_empty and find_dot and not find_email) or (find_string and not find_integer and not find_empty and find_dot and not find_email):
									#print "string with dot but not email"
									string_with_dots_not_email += 1
								elif len(find_caps) == 1 and not find_integer and not find_empty and not find_dot and not find_slash:
									#print "string with single caps with no integer or spaces."
									string_without_integer_without_spaces += 1
								elif len(find_string) > 2 and len(find_caps) == len(find_string) and not find_integer and not find_empty and not find_dot and not find_slash:
									#print "pure uppercase string with more than 2 characters"
									pure_uppercase_string+=1
								elif find_caps and len(find_caps) != len(find_string) and not find_integer and not find_empty and not find_dot and not find_slash and not find_space:
									#print "string with capital letters but not state code nor pure uppercase"
									string_without_integer_without_spaces += 1

						if find_integer :
							if find_phone :
								if(find_zipcode_one_hyphen):
									c = row[mylist[i]].split("-")
									if c[0] in zipcodes :
										#print row[mylist[i]], "is Most probably a zipcode with one hyphen"
										# zipcode_array.append(row[mylist[i]])
										mostly_zipcode_with_one_hyphen += 1	
									else :
										#print row[mylist[i]], "has one hyphen but is not a zipcode."
										pure_integer += 1

								if(find_zipcode_two_hyphen) :
									c = row[mylist[i]].split("--")
									if c[0] in zipcodes :
										#print row[mylist[i]], "is Most probably a zipcode with two hyphen"
										mostly_zipcode_with_two_hyphen += 1

								if len(find_phone) == 2 and len(find_integer) == 10 and not find_successive_hyphens and len(find_integer) > len(find_string):
										#print "possible phone no because of two hyphens"
										phone_no_two_hyphens+=1	
								if len(find_phone) == 1 and len(find_integer) == 10 and not find_successive_hyphens and len(find_integer) > len(find_string) and find_slash:
										#print "possible phone no but with slash instead of one of the hyphens"
										phone_no_one_hyphen+=1					

								if len(find_phone) == 1 and len(find_integer) != 10 and not find_successive_hyphens and len(find_integer) > len(find_string) and find_slash:
										#print "possible phone no without ten integers but with slash instead of one of the hyphens"
										phone_no_one_hyphen+=1
								if len(find_phone) == 2 and len(find_integer) != 10 and not find_successive_hyphens and not find_string :
									y = row[mylist[i]].split("-")
									if(len(y[0])>3):
										if row[mylist[i]] in zipcodes :
											#print row[mylist[i]] , "is possible zip codes but with two but not succesive hyphens"
											zipcode_with_two_not_successive_hyphens+=1
									else :
										#print "integers separated by hyphen but not zipcode or phone number"
										integer_seperated_by_hyphen_not_zip_or_phone+=1												
									
								if len(find_phone) == 1 and len(find_integer) != 10 and not find_string and not find_hashtag and find_pattern_phone_parantheses :
										open_brace = [phone for phone,val in enumerate(row[mylist[i]]) if val=="("]
										close_brace = [phone for phone,val in enumerate(row[mylist[i]]) if val==")"]
										if open_brace and close_brace :
											#print "phone no with parantheses"					
											phone_no_with_parantheses+=1
										if open_brace and not close_brace :
											#print "phone no with only open parantheses"				
											phone_no_with_only_open_parantheses+=1
										if close_brace and not open_brace :
											#print "phone no with only close parantheses"
											phone_no_with_only_close_parantheses+=1						

								if (len(find_phone) == 1 and len(find_integer) != 10 and not find_string and find_hashtag) or (find_string and find_integer and len(find_space) > 1 and len(find_string) > len(find_integer)):
									#print "possible line1 of address"
									string_first_line_address += 1
								if find_pattern_phone_parantheses and not find_website and not find_string and len(find_integer) == 10:
									#print "phone no with parantheses"							
									phone_no_with_parantheses+=1							

						if find_integer and not find_phone :
							if(find_zipcode_without_hyphen):
								if row[mylist[i]] in zipcodes :
									# for j in range(0,len(zipcodes)-1):
										# a = a.split("-")[0]
										# if row[mylist[i]] == zipcodes[j] :
									#print row[mylist[i]], "is most probably a zipcode (without hyphen)" 
											# zipcode_array.append(row[mylist[i]])
									mostly_zipcode_without_hyphen += 1
								else :
									#print row[mylist[i]], "is not a Zipcode"
									pure_integer += 1
									zipcode_array.append(row[mylist[i]])
							if(find_zipcode_four_digits):
								c = "0" + row[mylist[i]]
								if c in zipcodes :
									# for j in range(0,len(zipcodes)-1):
										# a = a.split("-")[0]
										# if c == zipcodes[j] :									
									#print row[mylist[i]], "is most probably a zipcode (four digits) " 
											# zipcode_array.append(row[mylist[i]])
									mostly_zipcode_four_digits += 1
								else :
									#print row[mylist[i]], "is a four digit integer"
									pure_integer += 1
							if not find_zipcode_without_hyphen and not find_zipcode_four_digits and not find_string and find_dot:
								#print "Integer with decimals"
								decimal_integer += 1
							if not find_zipcode_without_hyphen and not find_zipcode_four_digits and not find_string and not find_dot:
								#print "Pure integer"
								pure_integer += 1

						if find_integer and find_dot and find_phone and not find_string and row[mylist[i]][0] == "-" :
								#print "Negative integer with decimals"
								decimal_integer += 1

						if find_integer and not find_dot and find_phone and not find_string and row[mylist[i]][0] == "-" :
							#print "Negative integer without decimals"
							pure_integer += 1

						if find_empty :
							#print "empty entries"
							empty+=1
						#print row[mylist[i]]			
						# #print type(row[mylist[i]])
					# sys.stdout.write(".......................................\n")

			# print "\n!!!!!!!!!\n"
			# print  "\n", count, "rows have imperfect commas"
			if count > 0:
				print "***********************************************************"
				print "Your file has imperfect commas. Please open improperData.txt"
				print "*************************************************************"
			else:
				print "\nYour file is perfectly comma separated"
			if string_with_integer_spaces != 0 :
				print "No of string with integer and spaces", string_with_integer_spaces
			if string_with_integer_without_spaces != 0 :
				print "No of string with integer without spaces", string_with_integer_without_spaces	
			if string_without_integer_without_spaces != 0 :				
				print "No of string without integer and without spaces / string with single caps with no integer or spaces / string with capital letters but not state code nor pure uppercase", string_without_integer_without_spaces
			if string_with_dots_not_email != 0 :
				print "No of string with dot but not email", string_with_dots_not_email
			if two_letter_uppercase_string_not_state_code != 0 :
				print "No of two lettered uppercase string not state code", two_letter_uppercase_string_not_state_code
			if two_letter_lowercase_string_not_state_code != 0 :
				print "No of two lettered lowercase string not state code",two_letter_lowercase_string_not_state_code	
			if string_with_symbol_instead_of_at != 0 :
				print "No of string with @ instead of at", string_with_symbol_instead_of_at
			if string_with_integer_hyphen != 0 :
				print "No of string with integer and hyphen", string_with_integer_hyphen
			if email != 0 :
				print "No of possible email with integer / possible email without integer",  email
			if website != 0 :
				print "No of possible website with http and slash/ possible website", website
			if string_with_space_no_integer != 0 :
				print "No of string with spaces but no integer", string_with_space_no_integer
			if string_first_line_address != 0 :
				print "No of possible line1 of address" , string_first_line_address
			if phone_no_with_alphabets != 0 :
				print "No of possible phone no but with alphabets",phone_no_with_alphabets
			if website_without_www != 0 :
				print "No of possible website but without www and with slashes / possible website but without www (1 dot) and without slashes / possible website but without www (2 dot) and without slashes", website_without_www
			if state_code != 0 :
				print "No of possible state code", state_code
			if pure_uppercase_string != 0 :
				print "No of pure uppercase string with more than 2 characters", pure_uppercase_string
			if phone_no_two_hyphens != 0 :
				print "No of possible phone no because of two hyphens", phone_no_two_hyphens
			if phone_no_one_hyphen != 0 :
				print "No of possible phone no without ten integers but with slash instead of one of the hyphens / possible phone no but with slash instead of one of the hyphens", phone_no_one_hyphen
			if phone_no_with_parantheses != 0 :
				print "No of phone no with parantheses", phone_no_with_parantheses
			if phone_no_without_hyphen_or_alphabets != 0 :
				print "No of possible phone no but without hyphen or alphabets", phone_no_without_hyphen_or_alphabets
			if phone_no_with_only_open_parantheses != 0 :
				print "No of phone no with only open parantheses",phone_no_with_only_open_parantheses
			if phone_no_with_only_close_parantheses != 0 :
				print "No of phone no with only close parantheses", phone_no_with_only_close_parantheses
			# print "No of valid zipcode without hyphen as verified from unitedstateszipcodes.org", valid_verified_zipcode_without_hyphen
			# print "No of valid zipcode with one hyphen as verified from unitedstateszipcodes.org", valid_verified_zipcode_with_one_hyphen
			# print "No of valid zipcode with two hyphen as verified from unitedstateszipcodes.org", valid_verified_zipcode_with_two_hyphen
			if zipcode_with_two_not_successive_hyphens != 0 :
				print "No of possible zip codes but with two but not succesive hyphens", zipcode_with_two_not_successive_hyphens
			if empty != 0 :
				print "No of empty entries", empty
			if counter != 0 :
				print "Total no of lines", counter
			if decimal_integer != 0 :
				print "Total no of decimal integers", decimal_integer
			if pure_integer != 0 :
				print "No of PURE integer", pure_integer
			if integer_seperated_by_hyphen_not_zip_or_phone != 0 :
				print "No of integers separated by hyphen but not zipcode or phone number", integer_seperated_by_hyphen_not_zip_or_phone
			if uncertain_entries != 0 :
				print "No of Hard to say if it's a zip code or phone no.", uncertain_entries
			if mostly_zipcode_with_one_hyphen != 0 :
				print "No of Zipcode with one hyphen found by regular expression", mostly_zipcode_with_one_hyphen	
			if mostly_zipcode_without_hyphen != 0 :
				print "No of Zipcode without hyphen found by regular expression",mostly_zipcode_without_hyphen
			if mostly_zipcode_with_two_hyphen != 0 :
				print "No of zipcode with two hyphens found by regular expression", mostly_zipcode_with_two_hyphen
			if mostly_zipcode_four_digits != 0 :
				print "No of zipcode without hyphen but four digits", mostly_zipcode_four_digits

			total_zipcode =  valid_verified_zipcode_without_hyphen + valid_verified_zipcode_with_two_hyphen + zipcode_with_two_not_successive_hyphens + valid_verified_zipcode_with_one_hyphen + mostly_zipcode_with_one_hyphen + mostly_zipcode_without_hyphen + mostly_zipcode_with_two_hyphen + mostly_zipcode_four_digits
			total_phone = phone_no_two_hyphens + phone_no_without_hyphen_or_alphabets + phone_no_with_alphabets + phone_no_with_parantheses + phone_no_one_hyphen + phone_no_with_only_open_parantheses + phone_no_with_only_close_parantheses
			total_phone_only_integers = phone_no_two_hyphens + phone_no_without_hyphen_or_alphabets + phone_no_with_parantheses + phone_no_one_hyphen + phone_no_with_only_open_parantheses + phone_no_with_only_close_parantheses
			total_string = string_with_space_no_integer + string_with_integer_spaces + pure_uppercase_string + string_with_integer_hyphen + string_without_integer_without_spaces + string_with_symbol_instead_of_at + two_letter_uppercase_string_not_state_code + string_first_line_address + string_with_dots_not_email + two_letter_lowercase_string_not_state_code + string_with_integer_without_spaces
			total_website = website + website_without_www
			total_pure_string = string_without_integer_without_spaces + string_with_space_no_integer + pure_uppercase_string + two_letter_uppercase_string_not_state_code

			
			if total_zipcode != 0 :
				print "Total Zipcode",total_zipcode
			if total_phone != 0 :
				print "Total phone", total_phone
			if total_phone_only_integers != 0 :
				print "Total phone only integers",total_phone_only_integers
			if total_string != 0 :
				print "Total string", total_string
			if total_pure_string != 0 :
				print "Total pure string", total_pure_string
			if total_website != 0 :
				print "Total Website", total_website
			# print "Zipcode array with defective entries", zipcode_array
			
			
			print "\nOBSERVATIONS:"
			
			if((email) > (9*(counter - empty))/10):
				print "\tEmail dominates this column. Hence any other type of entries is considered a defective entry."
				print_improper_email_entries()		
				print_integer_only_entries()
				print_no_dots()
				print_integer_more_than_string()

			if(empty) < (counter/10) and empty > 0 :
				print "\tMore than 90 percent of this column is filled with entries. Hence any empty entry is considered defective."
				print_empty_entries()

			if(state_code > (6*(counter - empty))/10):
				print "\tThis column is dominated by state codes. Hence integer dataypes are considered defective"		
				print_not_state_code()

			if(decimal_integer > (5*counter)/10) :
				print "\tDecimal integers dominate this column."

			if(total_website > 5*(counter-empty)/10 ):
				print "\tWebsite entries dominate more than half of the column. Hence email entries and only integer entries are considered defective."		
				print_email_entries() 
				print_integer_only_entries()
				print_space_entries()
				print_no_dots()
				print_integer_more_than_string()
				print_string_only_entries()

			if((total_pure_string) > (9*(counter - empty))/10):
				print "\tThis column is dominated by pure string entries. Hence any other datatype is considered defective "
				if(state_code > (6*(counter - empty))/10):
					print_integer_entries()
					print_email_entries()			
				else :
					print_integer_entries()
					print_email_entries()
					print_state_code()

			# if(empty > (9.5*counter)/10):
			# 	print "\tThis column is predominantly empty. Hence any rows where data is present is considered defective."
			# 	print_integer_only_entries()
			# 	print_email_entries()
			# 	print_website_entries()
			# 	print_state_code()

			if(empty > (counter/3) ) :
				if(empty == counter):
					print "\tThis column is completely empty"
				else :
					print "\tMore than One third of this column is empty."
				if(website > (empty/2)) :
					print "\tHigh probability that this column represents website"
					if (email) :
						print "\tsome lines have email in the place of website."

			if(email > (counter/2)) :
				print "\tVery high probability that this column represents email"
				if(empty):
					print "\tThere are empty records in this column"

			if (total_zipcode > 0):
				if(total_zipcode <= (counter/10)):
					print "\tSome Zipcodes have been wrongly placed in this column"
					if ((string_with_integer_spaces > (7*(counter-empty))/10)) :
						print "Since this column seems to be dominated by one of the lines of address it is hard to distinguish between door no and zipcode. Hence such rows are not flaged here."
						pass
					else :	
						print_zip_code()

			if(total_phone_only_integers + pure_integer) > (5*counter)/10 :	
				print "\tPure integer occupy a large portion of this column. Hence any string integers are considered defective"
				print_string_without_hyphen_entries()

			if(total_phone) > (4*counter)/10 :	
				print "\tPhone numbers occupy a large portion of this column. Hence any string integers are considered defective"
				print_string_entries()

			if(total_zipcode > (counter/2)) :
				print "\tHigh probability that this column represents zipcode"
				print_string_entries()
				print_email_entries()

			if(total_phone > (counter/2)) :
				print "\tHigh probability that this column represents phone no"

			if (total_website > (counter/3)):
				print "\tThis column could be website "

			if(total_string > (9*counter)/10 or total_string > (counter - empty)/2 ) and (total_string > empty):
				print "\tThis column is definitely not email,website,zipcode or phone number"		
				global local_count
				local_count += 1
				if ((string_with_integer_spaces > (7*(counter-empty))/10)) :
					print "\tVery high probability that this is a line of address"				
					print_email_entries()
				if (pure_integer != 0):						
					print_integer_only_entries()
				if(email !=0) :
					print_email_entries()

			if (state_code > (9*counter)/10) :
				if(local_count == 0):
					print "\tHigh probability that this column represents state code"
				else :
					pass
			if(email == 0) :
				if(local_count == 0):
					print "\tThis column is definitely not email"
				else :
					pass	
			if(total_website == 0) :
				if(local_count == 0):
					print "\tThis column is definitely not website"
				else :
					pass
			if(total_phone == 0) :
				if(local_count == 0):
					print "\tThis column is definitely not phone"		
				else :
					pass
			if(total_zipcode == 0) :
				if(local_count == 0):
					print "\tThis column is definitely not zipcode"
				else :
					pass					
			if(two_letter_uppercase_string_not_state_code > (counter-empty)/10 ) :
				if(local_count == 0):
					print "\tThis column is definitely not state code"
				else :
					pass
			if(uncertain_entries):
				if(local_count == 0):
					print "\tThis column contains entries which seem anamalous."
				else :
					pass
				improper_integer_entries()

			if(func_count != 0):
				print "****************************"
				print "PLEASE OPEN improperData.txt"
				print "****************************"
			else:
				print "****************************"
				print "This column appears bug free"
				print "****************************"

# @app.command
# def execute(filename="filename",begin="something",to="small"):
# 	x = ExecuteProgram()
# 	x.fix_file(filename,begin,to)

class executerHeader(object):
	def work_header(self,filesname,columns) :
		global filename				
		filename = filesname
		global else_count 
		with open(filename,'rU') as data :
			r = csv.reader(open(filesname, "rU"), dialect=csv.excel_tab)
			line1=r.next()	
			arrt = []
			for element in line1:
				mylist = element.split(',')

		for i in range(0,len(mylist)):
			if columns in mylist[i]:				
				start = mylist.index(columns)
				end = mylist.index(columns)+1				
				x = ExecuteProgram()
				x.fix_file(filename,start,end)
				else_count += 1
		if else_count == 1:
			pass
		elif else_count == 0:
			print "header is not available"

@app.command
def executeColumns(filename="filename",columns="headerName"):
	x = executerHeader()
	x.work_header(filename,columns)


if __name__ == '__main__': 
	app.run()				