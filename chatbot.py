def get_response(message):
    message = message.lower().strip()

    # Greetings
    if any(word in message for word in ["hello", "hi", "hey", "hii", "helo", "good morning", "good afternoon"]):
        return "Hello! 👋 I am your AI Student Support Assistant. How can I help you today?"

    # Courses
    if any(word in message for word in [
        "course", "courses", "program", "programs", "degree",
        "branch", "branches", "study program"
    ]):
        return "I can help with general course information. Please check your college website or academic department for the latest course details."

    # Subjects / syllabus
    if any(word in message for word in [
        "subject", "subjects", "syllabus", "curriculum",
        "what do i study", "academic"
    ]):
        return "For subjects and syllabus information, please check your latest department syllabus or contact your academic department."

    # College timings
    if any(word in message for word in [
        "college timing", "college timings", "college time",
        "college starts", "college start", "college hours",
        "working hours", "college open"
    ]):
        return "College timings may vary by department and day. Please check the latest college notice or timetable for accurate timings."

    # Attendance
    if any(word in message for word in [
        "attendance", "attend", "attendance percentage",
        "attendance status", "classes attended", "my presence",
        "attendance shortage", "short attendance"
    ]):
        return "You can check your attendance through your college/student portal or contact your class teacher or department for attendance-related queries."

    # Exams
    if any(word in message for word in [
        "exam", "exams", "examination", "test", "tests",
        "exam date", "exam dates", "exam schedule",
        "when is exam", "exam timetable"
    ]):
        return "For examination dates and schedules, please check the official college examination notice or contact the examination department."

    # Library
    if any(word in message for word in [
        "library", "book", "books", "issue book",
        "return book", "library timing", "library timings",
        "library hours"
    ]):
        return "The library is generally open during college working hours. Please check your college notice for the latest library timing and book-related information."

    # Assignments
    if any(word in message for word in [
        "assignment", "assignments", "homework",
        "assignment submission", "submit assignment",
        "assignment deadline", "submission date"
    ]):
        return "Please check the instructions given by your subject teacher for assignment submission, deadline, and format."

    # Fees
    if any(word in message for word in [
        "fee", "fees", "fee payment", "fees payment",
        "fee structure", "fees structure", "payment",
        "college fee", "tuition fee"
    ]):
        return "For fee-related information, please contact the college accounts or administration department."

    # Admission
    if any(word in message for word in [
        "admission", "admissions", "admission process",
        "admission requirements", "eligibility",
        "documents required", "apply for admission"
    ]):
        return "For admission-related queries, eligibility, required documents, and application details, please contact the college admission department."

    # Timetable
    if any(word in message for word in [
        "timetable", "time table", "time-table",
        "class schedule", "class timings", "lecture timing",
        "lecture timings", "daily schedule"
    ]):
        return "Please check your department's latest timetable notice or student portal for class schedules."

    # Student support / help
    if any(word in message for word in [
        "contact", "help", "support", "student support",
        "who can help", "where can i complain",
        "complaint", "problem", "issue"
    ]):
        return "Sure! Please contact the relevant college department, class teacher, or student support office for assistance."

    # Hostel
    if any(word in message for word in [
        "hostel", "hostel room", "hostel facility",
        "hostel fees", "hostel timing", "accommodation"
    ]):
        return "For hostel rooms, fees, rules, and facilities, please contact the college hostel administration."

    # Transport
    if any(word in message for word in [
        "bus", "transport", "college bus", "bus timing",
        "bus route", "transport facility"
    ]):
        return "For college transport routes, timings, and availability, please contact the transport department."

    # Canteen
    if any(word in message for word in [
        "canteen", "food", "cafeteria", "mess",
        "canteen timing", "mess timing"
    ]):
        return "For canteen or mess timings and facilities, please check the college notice or contact the concerned administration."

    # ID card
    if any(word in message for word in [
        "id card", "identity card", "student id",
        "college id", "lost id"
    ]):
        return "For student ID card issues, please contact the college administration or student office."

    # Scholarship
    if any(word in message for word in [
        "scholarship", "scholarships", "scholarship form",
        "scholarship status", "financial aid"
    ]):
        return "For scholarship information and application status, please contact the scholarship or student administration office."

    # Results
    if any(word in message for word in [
        "result", "results", "marks", "score",
        "exam result", "semester result"
    ]):
        return "For examination results and marks, please check the official student portal or contact the examination department."

    # Registration
    if any(word in message for word in [
        "registration", "register", "registration form",
        "course registration", "semester registration"
    ]):
        return "For registration-related information, please check the student portal or contact your academic department."

    # Leave
    if any(word in message for word in [
        "leave", "leave application", "absent",
        "absence", "holiday", "leave request"
    ]):
        return "For leave applications and attendance-related absence rules, please contact your class teacher or department."

    # Faculty / teacher
    if any(word in message for word in [
        "teacher", "teachers", "faculty", "professor",
        "faculty member", "class teacher"
    ]):
        return "For faculty-related information, please contact your department office or check the official college faculty information."

    # Lab
    if any(word in message for word in [
        "lab", "laboratory", "computer lab",
        "lab timing", "lab schedule"
    ]):
        return "For laboratory schedules and availability, please check your department timetable or contact the lab in-charge."

    # Placement
    if any(word in message for word in [
        "placement", "placements", "job", "jobs",
        "campus placement", "placement cell", "career"
    ]):
        return "For placement and career opportunities, please contact the college placement cell or training and placement department."

    # Internship
    if any(word in message for word in [
        "internship", "internships", "training",
        "industrial training", "internship opportunity"
    ]):
        return "For internship and training opportunities, please contact the placement or training department and check official notices."

    # Thank you
    if any(word in message for word in [
        "thank you", "thanks", "thank", "thx"
    ]):
        return "You're welcome! 😊 I'm happy to help."

    # Bye
    if any(word in message for word in [
        "bye", "goodbye", "see you"
    ]):
        return "Goodbye! 👋 Have a great day and good luck with your studies!"

    # General fallback
    return (
        "I'm here to help with student support services. "
        "You can ask me about courses, subjects, attendance, exams, "
        "library, assignments, fees, admission, timetable, hostel, "
        "transport, scholarships, results, placements, internships, "
        "or other college support services."
    )