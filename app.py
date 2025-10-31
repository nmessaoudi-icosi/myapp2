def greet(name: str = "world") -> str:
    return f"Hello from MyApp2 Dr Nabil Messaoudi, {name}!"

if __name__ == "__main__":
    # Entrée minimaliste : python app.py [nom]
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
