import { useState } from "react";
import "./App.css";

function App() {

  const [transcript, setTranscript] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const detectBroll = async () => {

    if (!transcript.trim()) {
      alert("Please enter transcript");
      return;
    }

    setLoading(true);

    try {

      const response = await fetch("http://127.0.0.1:8000/detect", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          transcript: transcript,
        }),
      });

      const data = await response.json();

      setResults(data.placements || []);

    } catch (error) {
      console.error(error);
      alert("Backend connection failed");
    }

    setLoading(false);
  };

  return (
    <div className="App">

      <h1>Smart B-Roll Placement Detector</h1>

      <p className="subtitle">
        AI-powered transcript analysis system for detecting
        visually engaging moments and automatic B-roll suggestions.
      </p>

      <textarea
        placeholder="Paste transcript here..."
        value={transcript}
        onChange={(e) => setTranscript(e.target.value)}
      />

      <button onClick={detectBroll}>
        {loading ? "Analyzing..." : "Detect B-Roll"}
      </button>

      <div className="results">

        <h2>Suggested Placements</h2>

        {results.length === 0 ? (
          <p>No placements detected yet.</p>
        ) : (
          <ul>
            {results.map((item, index) => (
              <li key={index}>

                <strong>
                  {item.start} - {item.end}
                </strong>

                <p>{item.reason}</p>

                <p>
                  Confidence: {item.confidence}
                </p>

              </li>
            ))}
          </ul>
        )}

      </div>

    </div>
  );
}

export default App;