#                              ============================================================
#                                             Library Managment System
#                              ============================================================

def Library():
    print("Welcome to the library")
    print("\n","TITLE OF BOOKS")
    print("  1.Train to Pakistan","\n"," 2.The God of Small Things","\n"," 3.The White Tiger","\n",
          " 4.Family Life","\n"," 5.Wings of Fire")
    n=int(input("Select number to read about book"))
    if n==1:
        print(" 1.[BOOK NAME]:-Train to Pakistan","\n","2.[AUTHOR NAME]:-Khushwant Singh","\n","3.[PUBLISEHED YEAR]:-1956","\n",
             '''4.[DESCRIPTION]:-Train to Pakistan is a novel by Khushwant Singh that tells the story of a peaceful village on the border of India and Pakistan,
                 that is torn apart by the partition of India in 1947.''')
    elif n==2:
        print(" 1.[BOOK NAME]:-The God of Small Things","\n","2.[AUTHOR NAME]:-Arundhati Roy","\n","3.[PUBLISEHED YEAR]:-1997","\n",
              '''4.[DESCRIPTION]:-The God of Small Things is a novel by Arundhati Roy that explores the lives of fraternal twins,
                  Estha and Rahel, in 1960s Kerala, India''')
    elif n==3:
        print(" 1.[BOOK NAME]:-The White Tiger","\n","2.[AUTHOR NAME]:-Aravind Adiga","\n","3.[PUBLISEHED YEAR]:-2008","\n",
              '''4.[DESCRIPTION]:-This novel highlights the socioeconomic discrimination in India's economic system,
                 which creates divisions in Indian society. It limits opportunity, social mobility, health, 
                 and other rights and pleasures that should be given to all.''')
    elif n==4:
        print(" 1.[BOOK NAME]:-Family Life","\n","2.[AUTHOR NAME]:-Akhil Sharma","\n","3.[PUBLISEHED YEAR]:-2014","\n",
              '''4.[DESCRIPTION]:- Growing up in Delhi in 1978, eight-year-old Ajay Mishra and his older brother Birju play cricket on the streets, 
                  eagerly waiting for the day they can join their father in America.''' )
    elif n==5:
        print(" 1.[BOOK NAME]:-Wings of Fire","\n","2.[AUTHOR NAME]:-A. P. J. Abdul Kalam and Arun Tiwari","\n","3.[PUBLISEHED YEAR]:-1999","\n",
              '''4.[DESCRIPTION]:-The book is about Kalam's journey from a young boy in Rameswaram to becoming a renowned scientist and president of India.
                It highlights the role of family, friends, society, and hard work in his success.''')
    else:
        print("please select serial number from TITLE BOOK")
        
    n1=input("Do you want to continue? (yes/no): ").strip().lower()
    if n1=='yes':
        Library()
    else:
         print("THANK YOU TO VISIT MY LIBRARY")
Library()
