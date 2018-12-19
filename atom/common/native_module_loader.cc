// Copyright (c) 2018 GitHub, Inc.
// Use of this source code is governed by the MIT license that can be
// found in the LICENSE file.

#include "atom/common/native_module_loader.h"

namespace atom {

NativeModuleLoader::NativeModuleLoader() {
  LoadJavaScriptSource();
}

NativeModuleLoader::~NativeModuleLoader() = default;

v8::Local<v8::String> NativeModuleLoader::GetSource(v8::Isolate* isolate,
                                                    const char* id) const {
  const auto it = source_.find(id);
  CHECK_NE(it, source_.end());
  return it->second.ToStringChecked(isolate);
}

}  // namespace atom
