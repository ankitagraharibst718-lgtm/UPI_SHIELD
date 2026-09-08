from flask import Flask, render_template, request, jsonify
from detector import detect_scam

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    message = data.get("message", "")

    result = detect_scam(message)

    if result["level"] == "HIGH RISK":

        english = (
            "Do not make the payment. "
            "Do not share OTP, PIN or banking information. "
            "Verify the message using the official organization."
        )

        hindi = (
            "भुगतान न करें। "
            "OTP, PIN या बैंकिंग जानकारी साझा न करें। "
            "संदेश की पुष्टि आधिकारिक संस्था से करें।"
        )

    elif result["level"] == "MEDIUM RISK":

        english = (
            "Be careful before making any payment. "
            "Verify the sender and request independently."
        )

        hindi = (
            "भुगतान करने से पहले सावधान रहें। "
            "भेजने वाले और अनुरोध की स्वतंत्र रूप से पुष्टि करें।"
        )

    else:

        english = (
            "No strong scam indicators were detected, "
            "but always verify unexpected payment requests."
        )

        hindi = (
            "कोई मजबूत धोखाधड़ी संकेत नहीं मिले, "
 -----           "फिर भी अनपेक्षित भुगतान अनुरोध की पुष्टि करें।"
        )

    result["english_warning"] = english
    result["hindi_warning"] = hindi

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)