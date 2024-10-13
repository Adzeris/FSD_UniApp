# control/cli/__main__.py
try:
    from .cli_uni_app import main  # Relative import
except ImportError as e:
    print(f"ImportError: {e}")

if __name__ == "__main__":
    main()
