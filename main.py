def find_buzzwords(buzzwords, text):
    found_buzzwords = []
    for word in buzzwords:
        if word.lower() in text.lower():
            found_buzzwords.append(word)
    return found_buzzwords

def main():
    buzzwords = ["leadership", "teamwork", "communication", "problem-solving", "strategic planning","Specialized","Leadership","Experienced","Focused","Excellent","Generalist","Successful","Solutions","Great","Unique","Leading","Platform","Vision","Agile","Cloud-based","Collaborative","Creative","Customer-centric","Data-driven","Disruptive","Dynamic","Empowering","Engagement","Enthusiastic","Expert","Forward-thinking","Growth hacking","Highly motivated","Innovative","Influencer","Insightful","Lean","Leverage","Metricsdriven","Multitasking","Network","Ninja","Optimizing","Out-of-the-box","Passionate","Performance-driven","Pivot","Problem-solver","Proactive","Results-oriented","Scalable","Scrum","Self-motivated","Social media savvy","Strategic","Synergy","Team player","Thought leader","Thoughtful","Time management","Top performer","Transparent","Trendsetter","Value proposition","Visionary","Win-win situation","Workflow","Work-life balance"
]
    
    user_input = input("Enter a string: ")
    
    found = find_buzzwords(buzzwords, user_input)
    
    if found:
        print("Buzzwords found in the string:")
        for buzzword in found:
            print("-", buzzword)
    else:
        print("No buzzwords found in the string.")

if __name__ == "__main__":
    main()
  