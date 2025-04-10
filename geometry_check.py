import sys
import os
import FreeCAD
import Part

# Check if the STEP file exists
file_path = "cdp_latest.STEP"
if not os.path.exists(file_path):
    print(f"❌ STEP file not found: {file_path}")
    sys.exit(1)

print("📥 Reading STEP file...")
try:
    shape = Part.read(file_path)
except Exception as e:
    print(f"🔥 Error reading STEP file: {e}")
    sys.exit(1)
