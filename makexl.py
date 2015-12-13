import xlsxwriter as xl;

book = xl.Workbook ('cpp.xlsx');
sheet = book.add_worksheet ();
questions = open ('ans', 'r').readlines ();
#answers = open ('ans', 'r').readlines ();
sols = [];
q_num = 1;
opt_num = 1;

for i in range (len (questions)):
	if ('. ' in questions [i]):
		if (questions [i] [0].isnumeric ()):
			#QUESTION
			opt_num = 1;
			ques = questions [i] [questions [i].index ('. ')+2 : ];

			counter = i + 1;
			while ('. ' not in questions [counter]):
				ques += questions [counter];
				counter += 1;

			sheet.write ('A' + str (q_num), ques);
			print (q_num, ques)
			q_num += 1;
		else:
			#OPTION
			option = questions [i] [questions [i].index ('. ')+2 : ];
			counter = i + 1;
			while (counter < len (questions) and '. ' not in questions [counter]):
				option += questions [counter];
				counter += 1;

			sheet.write (chr (70 + opt_num) + str (q_num-1), option)
			print (opt_num, option);
			opt_num += 1;

'''
ques_num = 1;
for line in answers:
	print (ord (line [-2])-64);
#	ques_num += 1;
#	sheet.write ('L' + str (ques_num), ord (line [-2]) - 96);
			
'''
'''
ques_num = 1;
nenc = True;
for char in answers:
	if (char.isalpha ()):
		if (ques_num == 93 and nenc):
			nenc = False;
			continue;
		sols.append ( (ques_num, ord (char) - 96) );
		sheet.write ('L' + str (ques_num), ord (char) - 96);
		ques_num += 1;
'''

book.close ();
