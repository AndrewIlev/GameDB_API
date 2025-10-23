import importlib
import os

folder = "app/routers"
errors = []

for filename in os.listdir(folder):
    if filename.endswith(".py") and not filename.startswith("__"):
        module_name = f"app.routers.{filename[:-3]}"
        try:
            importlib.import_module(module_name)
            print(f"[OK] {module_name}")
        except Exception as e:
            print(f"[ERROR] {module_name} -> {e}")
            errors.append((module_name, e))

if errors:
    print("\nSummary of errors:")
    for mod, err in errors:
        print(mod, ":", err)
else:
    print("\nAll imports successful!")
