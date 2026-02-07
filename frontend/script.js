console.log("✅ script.js loaded");

const btn = document.getElementById("summarizeBtn");
const fileInput = document.getElementById("pdfFile");
const output = document.getElementById("output");

btn.onclick = async () => {
  console.log("🔥 Button clicked");

  if (!fileInput.files.length) {
    alert("Please select a PDF");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  output.textContent = "⏳ Summarizing… please wait";

  try {
    const response = await fetch("http://127.0.0.1:8000/summarize", {
      method: "POST",
      body: formData
    });

    const text = await response.text();

    console.log("📨 Backend returned:");
    console.log(text);

    output.textContent = text || "⚠ Empty summary";

  } catch (err) {
    console.error(err);
    output.textContent = "❌ Backend connection failed";
  }
};
