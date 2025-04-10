import sys

try:
    import FreeCAD
    import Part

    doc = FreeCAD.newDocument()
    shape = Part.read("cdp_latest.STEP")
    
    solids = shape.Solids
    faces = shape.Faces
    shells = shape.Shells

    print(f"📦 Geometry Details:\n  Solids: {len(solids)}\n  Faces: {len(faces)}\n  Shells: {len(shells)}")

    if not shape.isValid():
        print("❌ Geometry is invalid or has topology issues")
        sys.exit(1)
    else:
        print("✅ Geometry is valid")
        sys.exit(0)

except Exception as e:
    print(f"🔥 Exception during geometry check: {e}")
    sys.exit(1)

