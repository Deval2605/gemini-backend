from flask import Flask, request, Response
import google.generativeai as genai

app = Flask(__name__)

API_KEY = "AIzaSyDkGEjnY8GtdxvuQpRAD_5tPDKshHKUgoc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

BASE_CONTEXT = """
You are a helpful AI assistant that gives clean, correctly formatted, and properly indented text or code output.
Do not include any markdown formatting like ``` or language names.
Always maintain indentation and spacing exactly as in your internal output.
"""

@app.route("/", methods=["GET"])
def home():
    return "✅ Gemini backend is running successfully!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        message = request.get_data(as_text=True).strip()
        if not message:
            return Response("No message provided", status=400, mimetype="text/plain")
        prompt = f"{BASE_CONTEXT}\n\nUser: {message}\nAI:"
        response = model.generate_content(prompt)
        text_reply = response.text.strip()
        return Response(text_reply, mimetype="text/plain")
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
