
Wushangshu Decision Engine
A structured system for strategy modeling, evaluation, and adaptive decision-making — built as a composable, engineering-oriented framework.
This project translates classical strategic thinking into:


A programmable decision system




Overview
Wushangshu is designed as a multi-layer architecture:

Principle → Evaluation → Structure → Transition → Execution


Current progress:

✅ Relativity (Principle Layer)
✅ Ten Wins / Ten Losses (Evaluation Layer)
✅ Thirty-Six Strategies (Structure Layer)
🚧 Transition (State Change Engine)


Core Idea
Most strategy systems fail at one point:


They describe what to do, but not how to change dynamically.


Wushangshu focuses on solving:

How strategies are represented
How they are evaluated
And most importantly:
How they evolve over time


Architecture
1. Relativity (Principle Layer)
Defines a semantic coordinate system for interpreting situations.

No absolute perspective
Context-dependent meaning
Observer-relative evaluation
Comparable to:

Type systems
Semantic models
Context frameworks


2. Ten Wins / Ten Losses (Evaluation Layer)
A structured decision model for comparing competing states.

Enumerates advantage vs disadvantage
Converts qualitative judgment into structured evaluation
Enables consistent comparison
Comparable to:

Scoring functions
Heuristic evaluators


3. Thirty-Six Strategies (Structure Layer)
Defines a Strategy DSL (Domain-Specific Language).

Strategies as composable units
Reusable patterns
Abstract representations independent of context
Comparable to:

AST structures
Design patterns
Strategy libraries


🚧 4. Transition (Interval–Transformation Engine)
Currently under development
This is the core missing piece in most decision systems:


A formal mechanism for state transition


Concept Model

State Graph + Transition Function + Trigger Condition


Components
1. Interval (間)

The space between states
Represents the actionable difference from A → B
Not a static node, but a transformation field
2. Transformation (變)

Mapping rules between strategy structures
Similar to:AST transformations
Compiler passes
Rewrite systems
3. Trigger

Conditions that activate transitions
Internal or external signals
Defines when a strategy should change


Why Transition Matters
Without this layer:

The system is a static strategy library
Not a dynamic decision engine
With it:

Strategies become adaptive
Decisions become time-aware
The system becomes state-driven


Engineering Mapping

欄 1	欄 2
Wushangshu Layer	Engineering Equivalent
Relativity	Type System / Semantic Model
Ten Wins / Losses	Evaluation / Scoring Engine
Thirty-Six Strategies	Strategy DSL
Transition	Runtime / State Machine Engine



Current Focus

Defining strategy state space
Designing transformation grammar
Identifying reusable trigger patterns
Building a state transition model


Vision
Move from:


Strategy as description


To:


Strategy as execution + evolution




Repository Scope (WIP)
Planned components:

core/semantics → Relativity model
core/evaluation → Ten Wins / Losses engine
core/strategy → Strategy DSL
core/transition → State transition system
agents/ → decision agents built on top


Who This Is For
This project may be relevant if you're working on:

AI agents / agent architecture
Decision engines
Strategy modeling systems
DSL design & compilers
State machines & adaptive systems


Related

LinkedIn Post
https://www.linkedin.com/posts/meijia-yiyuanzi-7789b7404_wushangshu-system-progress-update-from-share-7472321502298693632-7jkv/
