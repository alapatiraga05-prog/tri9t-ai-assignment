# AI Engineering Internship Assignment – Tri9T AI

## Overview

This project is a FastAPI-based backend application developed as part of the **Tri9T AI Engineering Internship Assignment**.

The system parses technical documents into a structured hierarchical tree, supports document versioning, compares different document versions, generates AI-powered QA test cases using an LLM, stores generated test cases in MongoDB, and tracks their traceability across document versions.

---

# Features

- Parse and ingest technical PDF documents
- Build a hierarchical document tree
- Store multiple versions of the same document
- Compare document versions
- Generate AI-powered QA test cases using OpenRouter LLM
- Store generated test cases in MongoDB
- Retrieve generated test cases by version
- Maintain traceability between document sections and generated test cases
- Detect stale test cases across document versions
- Interactive API documentation using Swagger UI

---

# Tech Stack

### Backend
- FastAPI
- Python

### Database
- SQLite
- MongoDB

### ORM
- SQLAlchemy

### AI
- OpenRouter API

### Validation
- Pydantic

### Server
- Uvicorn

---

# Project Structure

```text
tri9t-ai-assignment/
│
├── app/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── parser/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── generated/
├── tests/
├── requirements.txt
├── README.md
└── .env
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/alapatiraga05-prog/tri9t-ai-assignment.git

cd tri9t-ai-assignment
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_openrouter_api_key

MONGODB_URI=mongodb://localhost:27017
```

---

## 5. Run the Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Document APIs

### Upload Document

```
POST /documents/ingest
```

Uploads and parses a PDF document into a hierarchical structure.

---

### List Documents

```
GET /documents
```

Returns all available document versions.

---

## Test Case APIs

### Generate AI Test Cases

```
POST /testcases/generate/{old_document_id}/{new_document_id}
```

Compares two document versions and generates QA test cases using the OpenRouter LLM.

Example

```
POST /testcases/generate/3/4
```

---

### Retrieve Generated Test Cases

```
GET /testcases/{version}
```

Returns all generated test cases for a specific document version.

Example

```
GET /testcases/2
```

---

# Workflow

### Step 1

Upload the first version of the document

```
POST /documents/ingest
```

↓

### Step 2

Upload the updated version

```
POST /documents/ingest
```

↓

### Step 3

Generate QA Test Cases

```
POST /testcases/generate/{old_document_id}/{new_document_id}
```

↓

### Step 4

Retrieve Generated Test Cases

```
GET /testcases/{version}
```

---

# Database Design

## SQLite

Stores:

- Documents
- Document Versions
- Parsed Nodes
- Parent-Child Relationships

---

## MongoDB

Stores:

- Generated Test Cases
- Section Information
- Traceability Metadata
- Status (ACTIVE / STALE)

---

# AI Integration

The application uses the **OpenRouter API** to generate QA test cases from selected document sections.

Generated test cases are linked with:

- Document Version
- Section Name
- Traceability Information

---

# Traceability & Staleness

Each generated test case is associated with the document version from which it was generated.

The system maintains traceability between document content and generated test cases, enabling users to determine whether a test case still corresponds to the latest document version.

---

# Testing the Application

### 1. Upload a document

```
POST /documents/ingest
```

---

### 2. Upload another version

```
POST /documents/ingest
```

---

### 3. Generate AI Test Cases

```
POST /testcases/generate/{old_document_id}/{new_document_id}
```

---

### 4. Retrieve Generated Test Cases

```
GET /testcases/{version}
```

---

# Future Improvements

- Semantic document matching for version detection
- Advanced document diff visualization
- Automatic regeneration of stale test cases
- Improved search and filtering
- Authentication and authorization
- Docker deployment
- CI/CD pipeline

---

# Repository

GitHub Repository

https://github.com/alapatiraga05-prog/tri9t-ai-assignment

---

# Author

**Keerthi A**

Electronics and Communication Engineering

CMR Institute of Technology
