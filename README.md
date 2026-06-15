# Wushangshu Decision Engine

> Early-stage decision system · Transition Engine v0.1

An executable strategy system that converts **uncertainty into a single decision**.

Most AI systems generate multiple options.  
Wushangshu does something different:

> It converges possibilities into action.

---

## Overview

Wushangshu is a layered decision architecture:

Principle → Evaluation → Structure → Transition → Execution

Current implementation:

- ✅ Relativity (semantic frame)
- ✅ Ten Wins / Ten Losses (evaluation model)
- ✅ Thirty-Six Strategies (structure abstraction)
- ✅ Transition Engine (v0.1)

---

## Core Idea

Most systems can:

- describe a situation  
- evaluate options  
- recommend strategies  

But they cannot answer:

> **How should a decision evolve over time?**

Wushangshu solves this by modeling:

- strategy as state  
- decisions as transitions  
- adaptation as an executable process  

---

## Transition Engine

The system models decision-making as:

State → Rule → New State

### Components

- **State**  
  Current situation + strategy  

- **Condition**  
  When a rule is applicable  

- **Trigger**  
  When change should occur  

- **Transformation**  
  How the strategy evolves  

---

## Quick Start
