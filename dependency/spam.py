#!/bin/python3

# Importing Important Modules
import smtplib
import webbrowser

from email.message import EmailMessage
from colorama import Fore, Style, Back
from os import system
from time import sleep

# Creating Loops
Info = True
Home = True



# Creating While Loop
while Home:
	system("clear")
	print(f"""{Fore.YELLOW}
 ______                    _  _                                
|  ____|                  (_)| |                               
| |__    _ __ ___    __ _  _ | |  ___  _ __    __ _  _ __ ___  
|  __|  | '_ ` _ \  / _` || || | / __|| '_ \  / _` || '_ ` _ \ 
| |____ | | | | | || (_| || || | \__ \| |_) || (_| || | | | | |
|______||_| |_| |_| \__,_||_||_| |___/| .__/  \__,_||_| |_| |_|
                                      | |                      
            {Fore.WHITE}{Back.RED}By - CodeWithSohel{Style.RESET_ALL}{Fore.YELLOW}        |_|                      
{Style.RESET_ALL}""")

	try:
		# Starter Page
		Options = "(1) Start\n(2) About\n(3) I have issue\n(0) Exit "
		user = int(input(Options + "\nSelect : "))
		
		# Option 1 - Start Tool
		if user == 1:
			Info = True
			while Info:
				system("clear")
				print(f"""
Target = {Fore.CYAN}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : 

Dear ,

Regards,

____________________________________________________________

SpamCount = 
""")
				
				Target = input(f"{Style.RESET_ALL}Enter Target Email(Without @gmail.com) :{Fore.CYAN} ")
				system("clear")
				print(f"""{Style.RESET_ALL}
Target = {Fore.CYAN}{Target}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : 

Dear ,

Regards,

____________________________________________________________

SpamCount = 
____________________________________________________________

""")
				
				Subject = input(f"{Style.RESET_ALL}Email Subject :{Fore.CYAN} ")
				system("clear")
				print(f"""{Style.RESET_ALL}
Target = {Fore.CYAN}{Target}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : {Fore.CYAN}{Subject}{Style.RESET_ALL}

Dear ,

Regards,

____________________________________________________________

SpamCount = 
____________________________________________________________

""")
				Salute = input(f"{Style.RESET_ALL}Target Name (Default = {Target}) :{Fore.CYAN} Dear ")
				system("clear")
				print(f"""{Style.RESET_ALL}
Target = {Fore.CYAN}{Target}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : {Fore.CYAN}{Subject}{Style.RESET_ALL}

Dear [{Fore.CYAN}Update Soon...{Style.RESET_ALL}],

Regards,

____________________________________________________________

SpamCount = 
____________________________________________________________

""")
				Introduction = input(f"{Style.RESET_ALL}Your Introduction(OPTIONAL) :{Fore.CYAN} ")
				system("clear")
				print(f"""{Style.RESET_ALL}
Target = {Fore.CYAN}{Target}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : {Fore.CYAN}{Subject}{Style.RESET_ALL}

Dear [{Fore.CYAN}Update Soon...{Style.RESET_ALL}],

{Fore.CYAN}{Introduction}{Style.RESET_ALL}

Regards,

____________________________________________________________

SpamCount = 
____________________________________________________________

""")
				Body = input(f"{Style.RESET_ALL}Main Content :{Fore.CYAN} ")
				system("clear")
				print(f"""{Style.RESET_ALL}
Target = {Fore.CYAN}{Target}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : {Fore.CYAN}{Subject}{Style.RESET_ALL}

Dear [{Fore.CYAN}Update Soon...{Style.RESET_ALL}],

{Fore.CYAN}{Introduction}{Style.RESET_ALL}

{Fore.CYAN}{Body}{Style.RESET_ALL}

Regards,

____________________________________________________________

SpamCount = 
____________________________________________________________

""")
				Ending = input(f"{Style.RESET_ALL}Ending (OPTIONAL):{Fore.CYAN} ")
				system("clear")
				print(f"""{Style.RESET_ALL}
Target = {Fore.CYAN}{Target}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : {Fore.CYAN}{Subject}{Style.RESET_ALL}

Dear [{Fore.CYAN}Update Soon...{Style.RESET_ALL}],

{Fore.CYAN}{Introduction}{Style.RESET_ALL}

{Fore.CYAN}{Body}{Style.RESET_ALL}

{Fore.CYAN}{Ending}{Style.RESET_ALL}

Regards,

____________________________________________________________

SpamCount = 
____________________________________________________________

""")
				Regards = input(f"""
{Style.RESET_ALL}Your Name(Default "Anonymous") :{Fore.CYAN}
Regards,
				
""")			
				try:
					system("clear")
					print(f"""{Style.RESET_ALL}
Target = {Fore.CYAN}{Target}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : {Fore.CYAN}{Subject}{Style.RESET_ALL}

Dear [{Fore.CYAN}Update Soon...{Style.RESET_ALL}],

{Fore.CYAN}{Introduction}{Style.RESET_ALL}

{Fore.CYAN}{Body}{Style.RESET_ALL}

{Fore.CYAN}{Ending}{Style.RESET_ALL}

Regards,

[{Fore.CYAN}Update Soon...{Style.RESET_ALL}]
____________________________________________________________

SpamCount = 
____________________________________________________________

""")
					SpamCount = int(input("How many Email do you want to send (0 - 50): "))
					
					# Checking Details
					test = 0
					system("clear")
					print(f"{Fore.GREEN}Checking details...{Style.RESET_ALL}")
					sleep(2)
					# Checking Target Email
					if "@" in Target or " " in Target:
						print(f"{Fore.GREEN}Email {Fore.RED}Error{Style.RESET_ALL}")
						sleep(1)
						print("REASON : {Fore.RED}Don't Use ({Fore.CYAN}@gmail.com{Style.RESET_ALL}) or {Fore.CYAN}Extra Spaces{Style.RESET_ALL}")
						sleep(2)
						
					elif Target == "" or Target == " ":
						print(f"{Fore.GREEN}Email {Fore.RED}Error{Style.RESET_ALL}")
						sleep(1)
						print(f"REASON : {Fore.RED}Email Is empty!{Style.RESET_ALL}")
						sleep(2)
					else:
						test += 1
						print(f"{Fore.GREEN}Email : {Fore.CYAN}Done{Style.RESET_ALL}")
						sleep(1)
					
					# Checking Email Subject
					if Subject == "":
						print(f"{Fore.GREEN}Subject {Fore.RED}Error{Style.RESET_ALL}")
						sleep(1)
						print(f"REASON : {Fore.RED}Subject is empty{Style.RESET_ALL}")
						sleep(2)
					else:
						test += 1
						print(f"{Fore.GREEN}Subject : {Fore.CYAN}Done{Style.RESET_ALL}")
						sleep(1)
					
					# Checking Salute
					if Salute == "" or Salute == " ":
						Salute = Target
						print(f"{Fore.GREEN}Target Name is empty so I used {Fore.CYAN}{Target}{Style.RESET_ALL}{Fore.GREEN} as a Target name{Style.RESET_ALL}")
						sleep(2)
					else:
						print(f"{Fore.GREEN}Target Name : {Fore.CYAN}Done{Style.RESET_ALL}")
						sleep(1)
					
					# Checking Body
					if Body == "" or Body == " ":
						print(f"{Fore.GREEN}Main Content {Fore.RED}Error{Style.RESET_ALL}")
						sleep(1)
						print(f"REASON : {Fore.RED}Main Content is Empty{Style.RESET_ALL}")
						sleep(2)
					else:
						test += 1
						print(f"{Fore.GREEN}Main Content : {Fore.CYAN}Done{Style.RESET_ALL}")
						sleep(1)
					
					# Checking User's name
					if Regards == "" or Regards == " ":
						Regards = "Anonymous"
						print(f"{Fore.GREEN}Your Name is empty so I used {Fore.CYAN}Anonymous{Style.RESET_ALL}{Fore.GREEN} as a your name")
						sleep(2)
					else:
						print(f"{Fore.GREEN}Your Name : {Fore.CYAN}Done{Style.RESET_ALL}")
						sleep(1)
					
					# Checking SpamCount
					if SpamCount < 1 or SpamCount > 50:
						print(f"{Fore.GREEN}Spam Count {Fore.RED}Error{Style.RESET_ALL}")
						sleep(1)
						print(f"{Fore.RED}Spam Count must be more than {Fore.CYAN}1{Style.RESET_ALL}{Fore.RED} or less then {Fore.CYAN}50{Style.RESET_ALL}")
						sleep(2)
					else:
						test += 1
						print(f"{Fore.GREEN}Spam Count : {Fore.CYAN}Done{Style.RESET_ALL}")
						sleep(1)
						
					if test == 4:
						print(f"{Fore.GREEN}Everything was {Fore.CYAN}Done{Style.RESET_ALL}")
						sleep(1)
						system("clear")
						for i in range(0,SpamCount):
							system("clear")
							print(f"""{Style.RESET_ALL}
Target = {Fore.CYAN}{Target}@gmail.com{Style.RESET_ALL}

                          Email
____________________________________________________________
Subject : {Fore.CYAN}{Subject}{Style.RESET_ALL}

Dear [{Fore.CYAN}Update Soon...{Style.RESET_ALL}],

{Fore.CYAN}{Introduction}{Style.RESET_ALL}

{Fore.CYAN}{Body}{Style.RESET_ALL}

{Fore.CYAN}{Ending}{Style.RESET_ALL}

Regards,

[{Fore.CYAN}Update Soon...{Style.RESET_ALL}]
____________________________________________________________

SpamCount = {SpamCount}

Email Sended = {i}
____________________________________________________________

""")
	
							# Creating Server
							server = smtplib.SMTP("smtp.gmail.com", 587)
							server.starttls()
							server.login("happybirthday7083@gmail.com", "ybqs vmut rgnw lhkp")
							
							# Creating Email
							msg = EmailMessage()
							msg.set_content(f"""Dear {Salute}
{Introduction}
		
{Body}

{Ending}

Regards,

{Regards}
""")
	
							msg['Subject'] = f"{Subject}"
							msg['From'] = f"happybirthday7083@gmail.com"
							msg['To'] = f"{Target}@gmail.com"
							
							# Sending Email To Target
							server.send_message(msg)
							
					else:
						print(f"{Fore.RED}Re-Enter Details Please{Style.RESET_ALL}")
						sleep(2)
					system("clear")
					print("All Done!")
					sleep(2)
					Info = False
				except ValueError:
					print(f"{Fore.RED}Enter Valid Number!{Style.RESET_ALL}")
					sleep(2)
					
		# Option 2 - About Tool
		elif user == 2:
			Statement = "Do you want to Redirect to our Official Github Repo?"
			YN = input(Statement+"(Y/n)")
			if YN == "" or YN == "y" or YN == "Y":
				url = "https://github.com/SohelHak/Pythagorean-Triples-Sum-Solver.git"
				system("clear")
				webbrowser.open(url)
			else:
				system("clear")
		
		# Option 3 - I have Issue
		elif user == 3:
			
			IssueSubject = input(f"{Style.RESET_ALL}Subject :{Fore.CYAN} ")
			Issue = input(f"{Style.RESET_ALL}Enter Your Issue:{Fore.CYAN} ")
			
			# Creating Server
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			server.login("happybirthday7083@gmail.com", "ybqs vmut rgnw lhkp")
			
			# Creating Email
			msg = EmailMessage()
			msg.set_content(f"{Issue}")
			
			msg['Subject'] = f"{IssueSubject}"
			msg['From'] = f"happybirthday7083@gmail.com"
			msg['To'] = f"codewithsohel9359@gmail.com"
			
			# Sending Email to owner
			server.send_message(msg)
			system("clear")
			print(f"""{Fore.GREEN}
Dear User,

We've received your issue regarding {IssueSubject}.

Our team will work to resolve this promptly.

Thank you for bringing it to our attention.

Regards,
CodeWithSohel{Style.RESET_ALL}""")
			input("\n\n\n\n\n\nPress ENTER to continue...")
		
		# Option 0 - Exit Tool
		elif user == 0:
			system("clear")
			print(f"{Fore.GREEN} THANK YOU FOR USING THIS TOOL{Style.RESET_ALL}")
			sleep(2)
			system("clear")
			exit()
			
		else:
			system("clear")
			print(f"{user} Option is not in list!")
			sleep(2)
			system("clear")
			
	except ValueError:
		print(f"{Fore.RED}Invalid Enter!{Style.RESET_ALL}")
		sleep(2)
		
