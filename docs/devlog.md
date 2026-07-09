# July 8, 2026

## Sprint 1 - Prompt Templates & LCEL

### What I Learned

- Difference between Chat Models and Prompt Templates.
- Learned how `ChatPromptTemplate` works.
- Understood dynamic placeholders using `{question}`.
- Learned the difference between `prompt.invoke()` and `model.invoke()`.
- Learned how LCEL connects runnables using the `|` operator.
- Built my first LangChain chain.

### What I Implemented

- Created `app/models/gemini_model.py`.
- Created `app/prompt/basic_prompt.py`.
- Moved Gemini configuration into a separate module.
- Created a reusable `ChatPromptTemplate`.
- Replaced manually created messages with a prompt template.
- Connected the prompt template to Gemini using LCEL.

### Problems Faced

- Python import errors (`ModuleNotFoundError`).
- Accidentally tried to commit the virtual environment.
- `.gitignore` was not ignoring `.newenv`.

### Solutions

- Added `.newenv/` to `.gitignore`.
- Removed the cached virtual environment from Git.
- Created `__init__.py` files.
- Fixed the import path.

### Git Commit

Commit 3

Summary:
Integrate ChatPromptTemplate and LCEL

### Key Takeaways

- Prompt Templates create messages.
- Chat Models generate responses.
- LCEL automatically connects multiple runnables.
- Every component should have a single responsibility.