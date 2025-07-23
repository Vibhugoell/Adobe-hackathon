# Adobe Hackathon – Round 1A: PDF Outline Extractor

## 🚀 Overview
This solution extracts hierarchical headings (H1, H2, H3) from a PDF document, including title and page numbers.

## 📦 Dependencies
- Python 3.10
- PyMuPDF 1.23.7

## 🛠️ Build Docker Image
```bash
docker build --platform linux/amd64 -t pdf-outliner:latest .
```

## ▶️ Run the Container
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-outliner:latest
```

## 📁 Sample Files
Refer to the `sample/` folder for example input and expected output.

## ✅ Constraints Met
- ✅ Runs offline
- ✅ Executes under 10 seconds
- ✅ No internet calls
- ✅ Model size = 0 (no ML model used)
