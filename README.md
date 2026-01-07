# Continuity Index (CI) v2.0

_A Python toolkit for measuring informational persistence and extinction risk in complex systems._

---

The **Continuity Index (CI) v2.0** is a quantitative framework based on **Information Continuity Theory (ICT)**.  
It helps you answer one core question:

> **Is this system on a path to persist, stay fragile, or collapse?**

You can apply CI to:

- AI ecosystems (agents, models, multi-agent systems)  
- Open-source/software projects  
- Institutions, organizations, and states  
- Cultural / knowledge systems  
- Synthetic and biological systems (with appropriate data)

---

## 🔍 Core Idea

CI v2.0 formalizes the balance between:

- **Reproduction** – can the system generate viable successors?  
- **Fidelity** – do successors preserve the essential information/structure?  
- **Deletion Hazard** – how likely is failure or loss?  
- **Volatility** – how turbulent is the environment?

Formally:

```text
CI = (R × f_I) / (λ × d_I)
log_CI = log10(CI)
