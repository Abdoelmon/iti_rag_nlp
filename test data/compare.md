# 🔎 Model & Infrastructure Comparison

This section explains why specific models and tools were selected by comparing them with strong alternatives.

---

# 🧠 1️⃣ LLM Comparison

## openai/gpt-oss-120b (via Groq) vs Mistral (Hugging Face)

| Criteria | openai/gpt-oss-120b (via Groq) | Mistral (Hugging Face) |
|-----------|--------------------------------|--------------------------|
| Parameter Size | 120B | 7B / 8x7B (Mixtral) |
| Reasoning Quality | Very strong long-context reasoning | Strong but smaller context reasoning |
| Inference Speed | ⚡ Extremely low latency (Groq hardware acceleration) | Depends on hosting (GPU required for speed) |
| Deployment | API-based (managed inference) | Self-hosted or HF Inference API |
| Cost Efficiency | Good performance per latency cost | Can be cheaper if self-hosted |
| Production Readiness | High (stable API + hardware acceleration) | Requires infrastructure setup |
| Multi-turn Chat | Excellent | Good |
| Scaling | Easily scalable via API | Requires infra scaling |

### Why openai/gpt-oss-120b was chosen:

- Superior reasoning for document-based QA
- Better summarization quality for large PDFs
- Ultra-low latency via Groq
- No infrastructure management needed
- More stable for production API use

### When Mistral would be preferred:

- Full local deployment requirement
- Budget-constrained environments
- GPU infrastructure already available
- Need for full model control

---

# 📦 2️⃣ Vector Store Comparison

## FAISS (L2 Distance) vs Chroma

| Criteria | FAISS | Chroma |
|------------|--------|----------|
| Performance | ⚡ Extremely fast similarity search | Fast, but slightly heavier |
| Persistence | Save/load locally | Built-in persistence |
| Scalability | Highly optimized | Good for small-medium projects |
| Metadata Filtering | Basic | Strong built-in metadata filtering |
| Deployment | Lightweight | Requires additional setup |
| Production Control | Full control | More abstraction layer |

### Why FAISS was chosen:

- Lightweight and efficient
- Ideal for local RAG systems
- Very fast L2 similarity search
- Mature and widely adopted
- Minimal overhead

### When Chroma would be preferred:

- Need advanced metadata filtering
- Rapid prototyping
- Developer-friendly API
- Built-in document management features

---

# 🔎 3️⃣ Embedding Model Comparison

## all-MiniLM-L6-v2 vs Larger Embedding Models (e.g., BGE / E5 / MPNet)

| Criteria | all-MiniLM-L6-v2 | Larger Embedding Models |
|------------|------------------|--------------------------|
| Model Size | ~80MB | 300MB+ |
| Speed | ⚡ Very fast | Slower |
| Semantic Accuracy | Strong for its size | Higher precision |
| Resource Usage | Low CPU usage | Requires more compute |
| RAG Suitability | Excellent for small-medium systems | Better for enterprise-scale retrieval |

### Why all-MiniLM-L6-v2 was chosen:

- Lightweight and fast
- Excellent semantic search performance
- Ideal for local deployment
- Low memory footprint
- Balanced accuracy vs efficiency

### When larger embedding models are preferred:

- Enterprise-scale document corpora
- High-precision semantic matching required
- GPU-based infrastructure available
- Large knowledge bases

---

# 🏗️ Final Architectural Decision

The selected stack:

- **LLM:** openai/gpt-oss-120b (via Groq)
- **Vector Store:** FAISS (L2)
- **Embedding:** all-MiniLM-L6-v2

### Why this combination?

- ⚡ High speed
- 🧠 Strong reasoning
- 💬 Reliable conversational performance
- 🖥 Efficient local retrieval
- 🚀 Production-ready API integration

The design prioritizes:

- Low latency
- Efficient resource usage
- High-quality summarization
- Scalable RAG architecture

---

# 🎯 Summary

This stack offers a strong balance between:

- Performance
- Cost
- Simplicity
- Production readiness

While alternatives like Mistral, Chroma, or larger embedding models are powerful, the selected configuration provides optimal performance for a scalable PDF-based RAG system.