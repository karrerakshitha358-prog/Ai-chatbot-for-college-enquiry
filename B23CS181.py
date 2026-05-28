def chatbot():
    print("🤖 College Enquiry Chatbot (type 'exit' to stop)\n")
    
    while True:
        user = input("You: ").lower()
        
        if user == "exit":
            print("Bot: Thank you! Have a great day 😊")
            break
        
        elif "course" in user or "courses" in user:
            print("Bot: We offer B.Tech, B.Sc, B.Com, MBA.")
        
        elif "fee" in user or "fees" in user:
            print("Bot: Fees vary by course. Please check the college website.")
        
        elif "admission" in user:
            print("Bot: Admissions are based on entrance exams and merit.")
        
        elif "hostel" in user:
            print("Bot: Yes, hostel facilities are available for students.")
        
        elif "timing" in user:
            print("Bot: College timings are from 9 AM to 4 PM.")
        
        elif "contact" in user:
            print("Bot: You can contact us at 9876543210.")
        
        else:
            print("Bot: Sorry, I didn't understand. Please try again.")

chatbot()