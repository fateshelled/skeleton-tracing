swig -python trace_skeleton.i
python3 setup.py build_ext --inplace
python3 setup.py bdist_wheel
