#!/usr/bin/env python

import os
import subprocess
import sys

TEMPLATE = """
#include "atom/common/native_module_loader.h"
#include "node_internals.h"
#include "node_union_bytes.h"

using node::arraysize;
using node::UnionBytes;

namespace atom {{

{definitions}

void NativeModuleLoader::LoadJavaScriptSource() {{
  {initializers}
}}

}}  // namespace atom
"""

def main():
  node_path = os.path.abspath(sys.argv[1])
  natives = os.path.abspath(sys.argv[2])
  js_source_files = sys.argv[3:]

  js2c = os.path.join(node_path, 'tools', 'js2c.py')
  subprocess.check_call(
    [sys.executable, js2c, natives] +
    js_source_files +
    ['-t', TEMPLATE])


if __name__ == '__main__':
  sys.exit(main())
