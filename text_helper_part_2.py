# Function go here...


# Offers users list of options, can be set to choose a random response
def text_helper(question, possible_answers, items_per_line, required=None):
    error = "This is a required field. Please choose an item from the list " \
            "or type in a word / phrase"

    print(question)

    valid = False
    while not valid:

        for item in possible_answers:
            print("{}. {}".format(possible_answers.index(item)+1, item))

        response = input("choose: ")

        # Checks that response has been given if required
        if required == "yes" and response == "":
            print(error)
            continue

        # Check if response is a number / choice, if it is, change
        # it to the option in the list

        try:
            response = int(response) - 1
            # Check that number is an option!
            if 0 <= int(response) < len(possible_answers):
                # response is a choice in the list, return word
                # that matches chosen number
                response = possible_answers[response]

        except ValueError:
            # User has typed in text, return it to the main routine
            return response


# Main Routine

# *** Set up genre list and sort it *****
genre_list = ["Action", "Adventure", "Detective", "Crime",
              "Fan-fiction", "Anthology"]
genre_list.sort()
print(genre_list)

# Make everything in list lowercase for comparison purposes
genre_list = [x.lower() for x in genre_list]

genre = text_helper("Please choose a genre", genre_list, 4, "yes")