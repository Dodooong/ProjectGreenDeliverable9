import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Page Configuration
st.set_page_config(
    page_title="Project GREEN - DevOps Knowledge Assistant",
    layout="wide"
)

# Styling
st.markdown("""
<style>

.block-container {
    max-width: 1000px;
    padding-top: 1rem;
}

h1 {
    color: #2E4053;
}

[data-testid="stChatInput"] {
    max-width: 500px;
    margin: auto;
}

</style>
""", unsafe_allow_html=True)

# Sidebar

with st.sidebar:

    st.title("Project GREEN")

    st.markdown("""

Agentic AI for DevOps-Related Queries

---

### Topics Covered

• Application Lifecycle Management

• Build Management

• Configuration Management

• Deployment Management

• Environment Management

• Continuous Integration

• Continuous Delivery

• Continuous Deployment

• Git & GitHub

• Jenkins

• Maven

• Gradle

• Docker

• Kubernetes

• SonarQube

• Nexus Repository

• Chef

• Shell Scripting

• Linux / Unix

• Python Automation

• AWS Cloud

• Infrastructure as Code

• DevSecOps

• Site Reliability Engineering

• Monitoring & Observability

• Agile & Scrum

""")

# Main Content

st.title("DevOps Knowledge Assistant")

st.write("""
Guidance, troubleshooting support, and learning assistance across the DevOps lifecycle.
""")

# System Prompt

SYSTEM_PROMPT = """
You are an Enterprise DevOps Knowledge Assistant.

You provide guidance about:

- Application Lifecycle Management
- Build Management
- Configuration Management
- Deployment Management
- Environment Management
- Continuous Integration
- Continuous Delivery
- Continuous Deployment
- Git
- GitHub
- Jenkins
- Maven
- Gradle
- Docker
- Kubernetes
- SonarQube
- Nexus Repository
- Chef
- Shell Scripting
- Linux
- Unix
- Python Automation
- AWS Cloud
- Infrastructure as Code
- Terraform
- DevSecOps
- Security Authentication
- Authorization
- Monitoring
- Logging
- Observability
- Site Reliability Engineering
- SLI
- SLO
- Error Budgets
- Agile
- Scrum

For conceptual questions provide:

1. Overview
2. Key Concepts
3. Benefits
4. Best Practices

For troubleshooting questions provide:

1. Possible Causes
2. Troubleshooting Steps
3. Recommended Fix

If outside the DevOps scope, respond:

"This topic is outside the supported DevOps knowledge base."
"""

# Chat History

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.markdown(message["content"])

    if message["role"] == "assistant":
        st.markdown("---")

# Chat Input

prompt = st.chat_input(
    "Ask a DevOps question..."
)

if prompt:

    try:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": f"**Question**\n\n{prompt}"
            }
        )

        conversation = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        conversation.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.spinner("Generating response..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=conversation,
                temperature=0.3,
                max_tokens=1500
            )

            answer = response.choices[0].message.content

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()

    except Exception as e:

        st.error("An error occurred.")
        st.code(str(e))