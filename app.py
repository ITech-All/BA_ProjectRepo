from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample investors data
investors = [
    {'name': 'Investor A', 'industry_interest': 'Technology'},
    {'name': 'Investor B', 'industry_interest': 'Education'},
    {'name': 'Investor C', 'industry_interest': 'Energy'},
    {'name': 'Investor D', 'industry_interest': 'Healthcare'},
    {'name': 'Investor E', 'industry_interest': 'Finance'},
    {'name': 'Investor F', 'industry_interest': 'Agriculture'},
    {'name': 'Investor G', 'industry_interest': 'Real Estate'},
    {'name': 'Investor H', 'industry_interest': 'Transportation'},
    {'name': 'Investor I', 'industry_interest': 'Manufacturing'},
    {'name': 'Investor J', 'industry_interest': 'Technology'},
    {'name': 'Investor K', 'industry_interest': 'Retail'},
    {'name': 'Investor L', 'industry_interest': 'Tourism'},
    {'name': 'Investor M', 'industry_interest': 'Education'},
    {'name': 'Investor N', 'industry_interest': 'Energy'},
    {'name': 'Investor O', 'industry_interest': 'Healthcare'}
]

@app.route('/', methods=['GET', 'POST'])
def submit_project():
    if request.method == 'POST':
        if 'chat_input' in request.form:
            # Handle chatbot message
            user_input = request.form['chat_input']
            bot_response = handle_chatbot_response(user_input)
            return bot_response  # Return the bot response directly to the chat

        # Capture form data for project submission
        name = request.form['name']
        project_title = request.form['project_title']
        project_description = request.form['project_description']
        industry = request.form['industry']
        
        # Redirect with the project data to the results page
        return redirect(url_for('show_results', name=name, project_title=project_title, industry=industry))

    return render_template('index.html')

@app.route('/results')
def show_results():
    # Capture the passed parameters
    name = request.args.get('name')
    project_title = request.args.get('project_title')
    industry = request.args.get('industry')

    # Find matching investors based on the industry
    matched_investors = [inv for inv in investors if inv['industry_interest'] == industry]

    return render_template('results.html', name=name, project_title=project_title, matched_investors=matched_investors)

def handle_chatbot_response(user_input):
    """A simple function to handle chatbot responses based on user input."""
    user_input = user_input.lower()

    if 'hello' in user_input or 'hellow' in user_input or 'hey' in user_input or 'hi' in user_input:
        return  ("Hello! How can I assist you today? \n " 
                 "1. With Investors \n "
                 "2. Industry of Interest")
    
    elif 'investors' in user_input or '1' in user_input:
        return "We have a range of investors interested in various industries. What industry are you interested in?"
    
    elif 'project' in user_input:
        return "Please tell me about your project, and I'll help you find the right investors."
    
    elif 'help' in user_input:
        return "You can ask me about investors, project submissions, or any other queries you have."
    elif 'education' in user_input:
        return "We have several investors interested in education. Are you looking for funding for a specific project in this sector?"
    elif 'technology' in user_input:
        return "Technology is a popular sector! We can connect you with investors who focus on innovative tech projects."
    elif 'healthcare' in user_input:
        return "Healthcare is crucial! We have investors keen on supporting new ideas in this field. What’s your project about?"
    elif 'finance' in user_input:
        return "Finance is always looking for innovative solutions. Can you share more about your project idea?"
    elif 'agriculture' in user_input:
        return "Agriculture investments are on the rise! What unique ideas do you have in this sector?"
    elif 'real estate' in user_input:
        return "Real estate has great potential! Are you working on a residential or commercial project?"
    elif 'transportation' in user_input:
        return "Transportation innovations are exciting! What aspect of transportation does your project focus on?"
    elif 'energy' in user_input:
        return "Energy projects are essential for sustainability. What type of energy solution are you proposing?"
    elif 'manufacturing' in user_input:
        return "Manufacturing is a key area for growth. What improvements or innovations are you working on?"
    elif 'retail' in user_input:
        return "Retail is evolving rapidly. How does your project aim to innovate in this space?"
    elif 'tourism' in user_input:
        return "Tourism is an exciting sector! What unique experience does your project offer?"
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome! If you have more questions, feel free to ask."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

if __name__ == '__main__':
    app.run(debug=True)
