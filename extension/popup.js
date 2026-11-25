document.getElementById("checkBtn").addEventListener("click", function () {
  const text = (document.getElementById("sampleInput").value || "").toLowerCase();
  const triggers = [
    "urgent", "verify account", "wire", "crypto", "gift card",
    "blackmail", "leaked", "otp", "pin", "suspended"
  ];
  let score = 0;
  const matched = [];
  triggers.forEach((word) => {
    if (text.includes(word)) {
      score += 18;
      matched.push(word);
    }
  });
  if (text.includes("http://") || text.includes("bit.ly") || text.includes("tinyurl")) {
    score += 20;
    matched.push("short/unencrypted link");
  }
  score = Math.min(100, score);
  const level = score >= 50 ? "HIGH RISK" : score >= 25 ? "MODERATE RISK" : "LOW RISK";
  document.getElementById("resultBox").innerHTML =
    `<strong>${level} (${score}/100)</strong><br/>Signals: ${matched.length ? matched.join(", ") : "None detected"}`;
});
