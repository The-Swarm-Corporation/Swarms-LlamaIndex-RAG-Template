
# 🚀 Swarms LlamaIndex RAG Template

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)


[![GitHub stars](https://img.shields.io/github/stars/The-Swarm-Corporation/Legal-Swarm-Template?style=social)](https://github.com/The-Swarm-Corporation/Legal-Swarm-Template)
[![Swarms Framework](https://img.shields.io/badge/Built%20with-Swarms-blue)](https://github.com/kyegomez/swarms)

A production-ready template for building RAG (Retrieval-Augmented Generation) applications using Swarms and LlamaIndex. This template provides everything you need to get started with document-based AI interactions.

## 🌟 Features

- 📚 Built-in RAG implementation with LlamaIndex
- 🤖 Advanced AI agent for healthcare data summarization
- 🔄 Interactive chat interface
- 📊 Sample data generator for testing
- 🛠️ Easy-to-customize architecture


## 🛠 Built With

- [Swarms Framework](https://github.com/kyegomez/swarms)
- Python 3.10+
- GROQ API Key or you can change it to use any model from [Swarm Models](https://github.com/The-Swarm-Corporation/swarm-models)

## 📬 Contact

Questions? Reach out:
- Twitter: [@kyegomez](https://twitter.com/kyegomez)
- Email: kye@swarms.world

---

## Want Real-Time Assistance?

[Book a call with here for real-time assistance:](https://cal.com/swarms/swarms-onboarding-session)

---

⭐ Star us on GitHub if this project helped you!

Built with ♥ using [Swarms Framework](https://github.com/kyegomez/swarms)










I'll help you create a professional README.md for the Swarms-LlamaIndex-RAG template repository. Here's the suggested update:

```markdown:README.md
# 🚀 Swarms LlamaIndex RAG Template

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)

## 🚀 Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/The-Swarm-Corporation/Swarms-LlamaIndex-RAG-Template.git
cd Swarms-LlamaIndex-RAG-Template
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your environment**
```bash
# Create a .env file and add your API keys and configurations
touch .env
# export OPENAI_API_KEY=<your-openai-api-key>
# export GROQ_API_KEY=<your-groq-api-key>
# export WORKSPACE_DIR=<your-workspace-directory>
```

4. **Generate sample data or add your own**
```bash
# To generate sample data:
python -m llamaindex_rag.fake_data_generator

# OR add your own documents to the 'docs' folder
```

5. **Run the application**
```bash
python main.py
```

## 📁 Project Structure

```
.
├── llamaindex_rag/
│   ├── agent.py          # Main RAG agent implementation
│   ├── memory.py         # LlamaIndex database integration
│   └── fake_data_generator.py  # Sample data generator
├── docs/                 # Document storage directory
├── requirements.txt      # Project dependencies
└── main.py              # Application entry point
```

## 🛠️ Built With

- [Swarms Framework](https://github.com/kyegomez/swarms) - AI agent framework
- [LlamaIndex](https://www.llamaindex.ai/) - Data framework for LLM applications
- Python 3.10+
- GROQ/OpenAI API

## 📖 Usage

1. **Add Your Documents**
   - Place your documents in the `docs` folder, or
   - Use the fake data generator for testing

2. **Interact with the Agent**
   - Run `main.py` to start the interactive session
   - Ask questions about your documents
   - Get AI-powered insights and summaries

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
