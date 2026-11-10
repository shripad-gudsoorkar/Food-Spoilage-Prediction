const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const result = document.getElementById("result");

imageInput.addEventListener("change", function () {
    const file = this.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
        result.innerHTML = "";
    }
});

async function predictFood() {
    const file = imageInput.files[0];

    if (!file) {
        alert("Please select an image first.");
        return;
    }

    result.innerHTML = "Analyzing image...";

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Prediction failed.");
        }

        const data = await response.json();

        result.innerHTML = `
            <h3>Prediction Results</h3>
            <p>Fruit: ${data.fruit}</p>
            <p>Freshness: ${data.freshness}</p>
            <p>Confidence: ${data.confidence}%</p>
        `;
    } catch (error) {
        result.innerHTML = "Error: " + error.message;
    }
}