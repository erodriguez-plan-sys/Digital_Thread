# geometry_check.py

import Part
import Import

doc = App.newDocument()

try:
    Import.open("cdp_latest.STEP")
    solids = []
    for obj in doc.Objects:
        if hasattr(obj, "Shape") and obj.Shape.Solids:
            solids.extend(obj.Shape.Solids)

    total_faces = sum(len(s.Faces) for s in solids)
    total_shells = sum(len(s.Shells) for s in solids)

    print(f"📦 Geometry Details:")
    print(f"  Solids: {len(solids)}")
    print(f"  Faces: {total_faces}")
    print(f"  Shells: {total_shells}")

    if not solids or any(s.isNull() or not s.isValid() for s in solids):
        print("❌ Geometry is invalid or has topology issues")
        exit(1)
    else:
        print("✅ Geometry is valid")
except Exception as e:
    print(f"❌ Error parsing STEP file: {e}")
    exit(1)
