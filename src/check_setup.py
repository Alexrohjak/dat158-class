"""Verify the ml-class environment is working.

Run with:  python src/check_setup.py
"""

import sys


def main() -> int:
    print(f"Python {sys.version.split()[0]}")
    print(f"Interpreter: {sys.executable}")

    if ".venv" not in sys.executable:
        print("\n  WARNING: this is not the project virtual environment.")
        print("  Run 'source .venv/bin/activate' first.\n")

    packages = ["numpy", "pandas", "sklearn", "matplotlib", "seaborn"]
    missing = []

    print()
    for name in packages:
        try:
            module = __import__(name)
            version = getattr(module, "__version__", "?")
            print(f"  ok    {name:<14} {version}")
        except ImportError:
            print(f"  MISSING  {name}")
            missing.append(name)

    if missing:
        print(f"\nMissing packages: {', '.join(missing)}")
        print("Fix with: pip install -r requirements.txt")
        return 1

    # A real end-to-end check: train a model and make sure it learns something.
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)

    print(f"\nTrained a decision tree on iris: {accuracy:.1%} test accuracy")

    if accuracy < 0.8:
        print("That is suspiciously low — something is wrong.")
        return 1

    print("Everything works. Go do some machine learning.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
