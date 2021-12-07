from english_words import english_words_lower_alpha_set as words
import random
import time


class main():
    
    strict = False


    def mode_selector():
        
        print("Welcome to Terminal Typing Test!\n")
        
        choice = "y"

        while choice != "n":

            main.strict = False

            print("Please select the mode you would like to choose:\n")
            print('''
            1. Time test
            2. Word test
            3. Strict time test
            4. Strict word test
            5. Unlimited practice
            ''')
            mode = input("Enter choice (1,2,3,4 or 5): ")
            if mode == "1":
                main.time_test()
            elif mode == "2":
                main.word_test()
            elif mode == "3":
                main.strict = True
                main.time_test()
            elif mode == "4":
                main.strict = True
                main.word_test()    
            elif mode == "5":
                main.practice()
            else:
                print("\nPlease enter a valid choice")
            choice = input("Take the test again? (y or n): ").lower()
            print(choice)
        print("\nThank you!\n")
        


    def time_test():

        chars_typed = 0
        
        while True:
            
            test_time = input("Enter the test duration in seconds: ")
            digit_check = test_time.isdigit()
            if digit_check == True:
                print("Starting test...\n\n")
                break
            else:
                print("Invalid input. Try again and enter an integer value.")

        

        start = time.time() 


        while True:
            char = ""

            if time.time() - start >= int(test_time):
                print("\nTime over")
                break
            
            displayed_word = main.wordprinter()
            print(displayed_word)

            typed_word = input()

            for char in typed_word:
                chars_typed +=1


            if typed_word != displayed_word:
                chars_typed -= 6
                if main.strict == True:
                    break

            
        main.result(start, chars_typed)  


    def word_test():

        start = time.time()

        chars_typed = 0
        

        
        while True:
            
            count = input("Enter the target number of words (5, 10, 15, ....): ")
            digit_check = count.isdigit()
            if digit_check == True:
                print("Starting test...\n\n")
                break
            else:
                print("Invalid input. Try again and enter an integer value.")

        count = int(count)

        while count:
                
            char = ""
            displayed_word = main.wordprinter()
            print(displayed_word)
            typed_word = input()
            for char in typed_word:
                chars_typed +=1

            if typed_word != displayed_word:
                chars_typed -= 6
                if main.strict == True:
                    break


            count -= 5
            
        main.result(start, chars_typed)  


    def practice():

        start = time.time()
        chars_typed = 0
        print("Starting typing practice...")
        time.sleep(1)
        print("Type exit anytime to leave")
        time.sleep(1)
        while True:
            displayed_word = main.wordprinter()
            print(displayed_word)
            typed_word = input()
            if typed_word.lower() == "exit":
                break

            for char in typed_word:
                chars_typed +=1


            if typed_word != displayed_word:
                chars_typed -= 6      

        main.result(start, chars_typed)  


    def wordprinter():
        word_list = list(words)
        displayed_word = str(random.choice(word_list)).strip("['']") + " " + str(random.choice(word_list)).strip("['']") + " " + str(random.choice(word_list)).strip("['']") + " " + str(random.choice(word_list)).strip("['']") + " " + str(random.choice(word_list)).strip("['']")
        return displayed_word

    def result(start, chars_typed):
        end = time.time()
        total_time = round(end - start, 2)
        print("\nWell done!")
        print("\nTotal time taken: " + str(total_time))
        WPM = round(chars_typed*12/total_time, 2)
        if WPM < 0:
            WPM = 0
        print("WPM: " + str(WPM))
        print()   




main.mode_selector()
