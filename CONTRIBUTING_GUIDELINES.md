# Contributing Guidelines

Thank you for contributing to the Multivariate KDE project. To ensure a professional and standardized workflow, please adhere to the following guidelines.

## 1. Branching Strategy
We follow a simplified **Feature Branch Workflow**.
* **`main`**: The protected production branch. **DO NOT push directly to main.**
* **Feature Branches**: Create a new branch for every task.
    * Format: `type/short-description`
    * Examples: `feat/gaussian-kernel`, `fix/numpy-shape-error`, `docs/update-readme`.

## 2. Commit Convention
We follow **Conventional Commits** to automate versioning and changelogs.
Structure: `<type>: <description>`

* `feat`: A new feature (e.g., `feat: implement epanechnikov kernel`).
* `fix`: A bug fix (e.g., `fix: handle singular matrix in bandwidth`).
* `docs`: Documentation only changes.
* `refactor`: A code change that neither fixes a bug nor adds a feature.
* `chore`: Maintenance tasks (e.g., `chore: update pixi.lock`).

## 3. Coding Standards (Strict)
Since we aim for a production-grade codebase, all PRs must meet these criteria:

* **Type Hinting:** All function arguments and return types must be typed.
    ```python
    # Good
    def calculate_density(self, data: np.ndarray) -> np.ndarray: ...
    ```
* **Docstrings:** Use Google-style or NumPy-style docstrings for all classes and public methods.
* **Clean Code:** Remove unused imports and commented-out code before pushing.

## 4. Pull Request (PR) Process
1.  Push your branch to GitHub.
2.  Open a Pull Request against `main`.
3.  **Self-Review:** Ensure your code passes local tests (`pytest`).
4.  Request a review from the **Lead Maintainer**.
5.  Once approved, squash and merge.

## 5. Environment
Please use `uv shell` to ensure you are using the shared development environment versions. Do not introduce new dependencies without updating `project.toml`.
