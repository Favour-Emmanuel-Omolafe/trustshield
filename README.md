# TrustShield

Real-time scam, impersonation, and extortion risk-scoring starter toolkit, featuring a Chrome extension (Manifest V3) and a Python signal-scoring module.

## Structure
* `extension/manifest.json`, `extension/popup.html`, `extension/popup.js`, `extension/background.js`: Browser extension UI and client-side heuristic scanner.
* `backend/detector.py`: Core Python risk-scoring module (`assess_content`) ready for API or test integration.
