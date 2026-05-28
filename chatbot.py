data = {
    "courses": "B.Tech, B.Sc, B.Com, MBA",
    "fees": "Fees details will be updated by staff.",
    "admission": "Admission is based on entrance exam and merit.",
    "exam": "Exam notifications will be updated soon.",
    "results": "Results will be announced on portal.",
    "hostel": "Hostel facility is available.",
    "contact": "Contact: 9876543210",
    "holidays": "Holiday list will be updated.",
    "attendance": "Attendance details updated by staff.",
    "marks": "Marks will be uploaded after exams."
}

print("🤖 College Chatbot Login System\n")

while True:
    role = input("Login as (student/staff/exit): ").lower()

    if role == "exit":
        print("Bot: Thank you!")
        break

    # STUDENT LOGIN
    elif role == "student":
        print("✅ You are logged in as Student")
        print("Ask your questions (type 'back' to go back)\n")

        while True:
            user = input("You: ").lower()

            if user == "back":
                break

            elif "course" in user:
                print("Bot:", data["courses"])

            elif "fee" in user:
                print("Bot:", data["fees"])

            elif "admission" in user:
                print("Bot:", data["admission"])

            elif "exam" in user:
                print("Bot:", data["exam"])

            elif "result" in user:
                print("Bot:", data["results"])

            elif "hostel" in user:
                print("Bot:", data["hostel"])

            elif "contact" in user:
                print("Bot:", data["contact"])

            elif "holiday" in user:
                print("Bot:", data["holidays"])

            elif "attendance" in user:
                print("Bot:", data["attendance"])

            elif "marks" in user:
                print("Bot:", data["marks"])

            else:
                print("Bot: Sorry, I didn't understand.")

    # STAFF LOGIN
    elif role == "staff":
        password = input("Enter staff password: ")

        if password == "admin123":
            print("✅ You are logged in as Staff")
            print("You can update data (type 'back' to go back)\n")

            while True:
                key = input("What do you want to update? ").lower()

                if key == "back":
                    break

                elif key in data:
                    new_value = input("Enter new information: ")
                    data[key] = new_value
                    print("✅ Updated successfully!")

                else:
                    print("Invalid option")

        else:
            print("❌ Wrong password")

    else:
        print("Invalid option! Please type student or staff.")