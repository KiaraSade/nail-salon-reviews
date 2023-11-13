# main.py

def view_reviews():
    with open('reviews.txt', 'r') as file:
        reviews = file.read()
        print(reviews)

def add_review():
    reviewer_name = input("Enter your name: ")
    rating = input("Enter your rating (out of 5): ")
    feedback = input("Enter your feedback: ")
    
    with open('reviews.txt', 'a') as file:
        file.write(f"\nReviewer: {reviewer_name}\n")
        file.write(f"Rating: {rating}/5\n")
        file.write(f"Feedback: {feedback}\n")

# Test the program
view_reviews()
add_review()
view_reviews()
