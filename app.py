from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the chat interface (simple and inline)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>KV AFS Jorhat Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        #chat { border: 1px solid #ccc; height: 300px; overflow-y: scroll; padding: 10px; }
        input { width: 80%; padding: 10px; }
        button { padding: 10px; }
    </style>
</head>
<body>
    <h1>Welcome to the AI Chatbot for Pm Shri KV AFS Jorhat!</h1>
    <p>I can help with: Admission process, Classes offered, Fee structure, Required documents, School timings & contact, Facilities, Admission dates.</p>
    <div id="chat"></div>
    <input type="text" id="userInput" placeholder="Type your query here...">
    <button onclick="sendMessage()">Send</button>
    <script>
        function sendMessage() {
            const input = document.getElementById('userInput');
            const chat = document.getElementById('chat');
            const message = input.value.trim().toLowerCase();
            if (!message) return;
            
            chat.innerHTML += '<p><strong>You:</strong> ' + input.value + '</p>';
            input.value = '';
            
            fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                chat.innerHTML += '<p><strong>Bot:</strong> ' + data.response + '</p>';
                chat.scrollTop = chat.scrollHeight;
            });
        }
    </script>
</body>
</html>
"""

# Responses dictionary (same as before)
responses = {
    "admission process": """
    Admission Process for KV AFS Jorhat:
    - Admissions are handled through the Kendriya Vidyalaya Sangathan (KVS) online portal (admission.kvs.gov.in).
    - Priority is given to children of defense personnel, transferable central government employees, and others based on categories (e.g., RTE for Class 1).
    - For Classes 1-8: Based on distance from school and priority categories.
    - For Classes 9-12: Based on marks in previous class and availability.
    - Apply during the admission window (usually March-April). Check the official KVS website for exact steps.
    """,
    
    "classes offered": """
    Classes Offered at KV AFS Jorhat:
    - The school offers education from Class 1 to Class 12.
    - Curriculum follows CBSE (Central Board of Secondary Education) standards.
    - Streams in senior secondary: Science, Commerce, and Humanities.
    """,
    
    "fee structure": """
    Fee Structure for KV AFS Jorhat:
    - Kendriya Vidyalayas have subsidized fees as per KVS norms.
    - Approximate annual fees (may vary; confirm with school):
      - Class 1-8: ₹500-₹1,000 (including tuition, development, and other charges).
      - Class 9-12: ₹1,000-₹2,000.
    - Additional costs for uniforms, books, and extracurricular activities (around ₹5,000-₹10,000 annually).
    - Fees are low to ensure accessibility; no capitation fees. Check kvsangathan.nic.in for updates.
    """,
    
    "required documents": """
    Required Documents for Admission at KV AFS Jorhat:
    - Birth certificate.
    - Transfer certificate (for students from other schools).
    - Proof of residence (e.g., ration card, electricity bill).
    - Category certificate (if applicable, e.g., for defense personnel or SC/ST).
    - Medical certificate (if needed).
    - Passport-sized photos.
    - Aadhaar card (optional but recommended).
    - For online application: Scanned copies of these documents.
    """,
    
    "school timings & contact": """
    School Timings & Contact for KV AFS Jorhat:
    - Timings: Monday to Friday, 8:00 AM to 3:00 PM (may vary for summer/winter).
    - Saturdays: Half-day or as per schedule.
    - Contact:
      - Address: Air Force Station, Jorhat, Assam, India - 785005.
      - Phone: +91-376-XXXXXXX (Check official site for exact number; principal's office: approx. +91-376-230XXXX).
      - Email: kvafsjorhat@kvs.gov.in (or similar; verify on kvsangathan.nic.in).
      - Website: kvsangathan.nic.in or school-specific page.
    """,
    
    "facilities": """
    Facilities at KV AFS Jorhat:
    - Academic: Well-equipped classrooms, science/maths/computer labs, library with digital resources.
    - Sports: Playground, basketball court, gymnasium, swimming pool (if available at AFS).
    - Other: Hostel (for defense families), canteen, medical room, auditorium for events, smart classrooms, and extracurricular activities like NCC, Scouts, and arts.
    - The school emphasizes holistic development with focus on discipline and co-curriculars.
    """,
    
    "admission dates": """
    Admission Dates for KV AFS Jorhat:
    - Admissions are typically announced in March-April for the next academic year (starting June/July).
    - Online registration opens around March 1st and closes by April 15th (subject to KVS notifications).
    - Check admission.kvs.gov.in or the school's notice board for exact dates. Priority categories apply first.
    """
}

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip().lower()
    
    # Check for keywords
    for key in responses:
        if key in user_message:
            return {'response': responses[key]}
    
    return {'response': "Sorry, I can only answer queries about Admission process, Classes offered, Fee structure, Required documents, School timings & contact, Facilities, or Admission dates. Please rephrase!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)