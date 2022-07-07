from distutils.core import setup, Extension


module = Extension('_trace_skeleton',
                   sources=['trace_skeleton_wrap.c', 'trace_skeleton.c'],
                   )

setup (name = 'trace_skeleton',
       version = '0.1.0',
       author      = "Lingdong Huang",
       description = """A new algorithm for retrieving topological skeleton as a set of polylines from binary images.""",
       ext_modules = [module],
       py_modules = ["trace_skeleton"],
       )
