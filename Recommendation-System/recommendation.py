items = {
    "Iterstellar":["sci-fi","space","adventure","drama"],
    "The Matrix":["sci-fi","action","adventure"],
    "Avengers" :["action","superhero","adventure"],
    "The Notebook":["romance", "drama"],
    "Inception" : ["sci-fi", "action","thriller"],
    "Titanic":["romance","drama"],
    "Jurassic park":["sci-fi","adventure","thriller"],
}
print("welcome to the movie Recommendation System!")
user_input = input(
    "Enter your interest separated by commas "
    "(example:action, sci-fi,adventure):"
)
user_preferences =list(set(
    preference.strip().lower()
    for preference in user_input.split(",")
    if preference.strip()
))
if not user_preferences:
    print("Please enter at least one interest.")
    exit()
recommendation=[]
for items, preferences in items.items():
    score =0
    for preference in user_preferences:
        if preference in preferences:
            score += 1
    if score>0:
        recommendation.append((items,score)) 

recommendation.sort(key=lambda x: x[1], reverse=True)
print("\nRecommended for you:")
if recommendation:
    for item, score in recommendation:
        print(f"-{item}(Match score:{score})")
else: 
    print ("Sorry, no matching recommendation found.")