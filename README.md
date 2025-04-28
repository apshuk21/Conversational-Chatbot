# Conversational Chatbot

## Overview
The **Conversational Chatbot** is an intelligent AI-driven system designed to facilitate seamless and engaging interactions with users. Leveraging cutting-edge technologies like knowledge graphs, natural language processing (NLP), and advanced database integrations, this chatbot provides contextually relevant responses and dynamic conversational capabilities.

## Features
- **Two Memory Variants:**
  1. **Temporary Memory:** Uses an array data structure to store conversational context within a single session.
  2. **Persistent Memory:** Implements Neo4j and QDrantDB to retain context across sessions for richer, more informed conversations.
- **Knowledge Graph Integration:** Enables contextual reasoning and semantic search for enriched user interactions.
- **Database Connectivity:** Efficiently retrieves and stores data using advanced database technologies.
- **Scalable Architecture:** Designed for deployment in diverse environments using containerization tools like Docker.
- **Customizable Workflows:** Supports dynamic workflows tailored to specific use cases.

## Technologies Used
- **Mem0**: For modular and scalable AI workflows, particularly conversational and retrieval-augmented generation tasks.
- **Neo4j**: For graph database integration and relationship mapping in the persistent memory version.
- **QDrantDB**: For vector database storage and semantic search in the persistent memory version.
- **OpenAI API**: For generating conversational responses.
- **Docker**: For containerization and deployment.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/apshuk21/Conversational-Chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Conversational-Chatbot
   ```
3. Install dependencies using the `uv` package manager:
   ```bash
   uv install
   ```
   Dependencies are managed through the `pyproject.toml` file.

4. Run the application:
   ```bash
   uv run
   ```

## Usage
- **Switching Between Memory Versions:**
  - Use the **temporary memory version** for lightweight, session-based interactions.
  - Use the **persistent memory version** for conversations that require long-term context and reasoning.
- Customize the chatbot's knowledge graph and workflows by editing the configuration files.
- Integrate external APIs for enhanced functionality.
- Deploy the chatbot in your preferred environment using Docker.

## License
This project is licensed under the [MIT License].