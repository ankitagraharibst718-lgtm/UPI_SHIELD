async function analyzeMessage() {

    const message = document.getElementById("message").value;

    if (!message.trim()) {
        alert("Please enter a message.");
        return;
    }

    const response = await fetch("/analyze", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    document.getElementById("level").innerText =
        data.level;

    document.getElementById("score").innerText =
        data.score;
        // Threat Meter
const threatBar = document.getElementById("threatBar");

if (threatBar) {
    threatBar.style.width = data.score + "%";
}
        // Risk color
const resultBox = document.getElementById("result");
const levelBox = document.getElementById("level");

resultBox.classList.remove("high", "medium", "low");
levelBox.classList.remove(
    "risk-high",
    "risk-medium",
    "risk-low"
);

if (data.score >= 70) {

    resultBox.classList.add("high");
    levelBox.classList.add("risk-high");

} else if (data.score >= 40) {

    resultBox.classList.add("medium");
    levelBox.classList.add("risk-medium");

} else {

    resultBox.classList.add("low");
    levelBox.classList.add("risk-low");
}

    document.getElementById("english").innerText =
        data.english_warning;

    document.getElementById("hindi").innerText =
        data.hindi_warning;


    const triggers =
        document.getElementById("triggers");

    triggers.innerHTML = "";

    data.detected.forEach(function(item) {

        const li = document.createElement("li");

        li.innerText = "⚠️ " + item;

        triggers.appendChild(li);
        

    });
    // Why is this risky?
const evidenceList = document.getElementById("evidenceList");

if (evidenceList) {

    evidenceList.innerHTML = "";

    data.detected.forEach(function(trigger) {

        const li = document.createElement("li");

        if (trigger.includes("Urgency")) {
            li.innerText =
                "The message creates pressure to act quickly.";
        }
        else if (trigger.includes("Payment")) {
            li.innerText =
                "The message requests money or a refund-related payment.";
        }
        else if (trigger.includes("Sensitive")) {
            li.innerText =
                "The message asks for sensitive information such as OTP or PIN.";
        }
        else {
            li.innerText =
                "This message contains a suspicious scam indicator.";
        }

        evidenceList.appendChild(li);
    });
}
}
function loadSample(type) {

    const messageBox = document.getElementById("message");

    if (type === "electricity") {

        messageBox.value =
            "URGENT! Your electricity connection will be disconnected today. Pay ₹20 immediately for verification refund. Send OTP to complete the process.";

    } else if (type === "refund") {

        messageBox.value =
            "URGENT! Your UPI refund is pending. Pay ₹10 immediately for verification. Send OTP to receive your refund.";

    } else if (type === "kyc") {

        messageBox.value =
            "Your KYC will expire today. Verify your account immediately or your UPI service will be blocked. Share OTP to complete verification.";

    } else if (type === "safe") {

        messageBox.value =
            "Hi, are you available for a meeting tomorrow at 10 AM?";
    }
}