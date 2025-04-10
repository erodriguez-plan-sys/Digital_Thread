import sys
import os

try:
    import FreeCAD
    import Part

    print("📂 Current Directory:", os.getcwd())
    print("📄 Files in Directory:", os.listdir())

    file_path = "cdp_latest.STEP"
    if not os.path.exists(file_path):
        print(f"❌ STEP file not found: {file_path}")
        sys.exit(1)

    print("📥 Reading STEP file...")
    shape = Part.read(file_path)
    
    print("📦 Counting geometry...")
    solids = shape.Solids
    faces = shape.Faces
    shells = shape.Shells

    print(f"✅ Geometry Details:\n  Solids: {len(solids)}\n  Faces: {len(faces)}\n  Shells: {len(shells)}")

    if not shape.isValid():
        print("❌ Geometry is invalid or has topology issues")
        sys.exit(1)
    else:
        print("✅ Geometry is valid")
        sys.exit(0)

except Exception as e:
    print(f"🔥 Exception caught: {e}")
    sys.exit(1)

